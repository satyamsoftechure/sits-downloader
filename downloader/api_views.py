from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import yt_dlp
import os
import uuid
from .serializers import URLSerializer, DownloadSerializer
from django.conf import settings
from django.http import HttpResponse
import urllib.parse
from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlencode
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.permissions import BasePermission
from django.views.decorators.http import require_GET


class TokenDomainPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get("Authorization")
        print("token", token)
        if not token:
            return False

        if token != settings.API_TOKEN:
            return False

        origin = request.headers.get("Origin")
        if not origin:
            return False

        allowed_domains = settings.ALLOWED_DOMAINS
        print("allowed_domains", allowed_domains)
        if origin not in allowed_domains:
            return False

        return True


@require_GET
def proxy_instagram_thumbnail(request):
    url = request.GET.get("url")
    if not url:
        return HttpResponseBadRequest("Missing URL parameter")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return HttpResponse(
                response.content, content_type=response.headers["Content-Type"]
            )
        else:
            return HttpResponseBadRequest(
                f"Failed to fetch image: HTTP {response.status_code}"
            )
    except requests.RequestException as e:
        return HttpResponseBadRequest(f"Error fetching image: {str(e)}")


class HomeAPIView(APIView):
    # permission_classes = [TokenDomainPermission]

    def post(self, request):
        serializer = URLSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data["url"]

            formats, banner_url, title, error = self.extract_video_info(url)

            if error:
                return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

            response_data = {
                "url": url,
                "banner_url": banner_url,
                "title": title,
                "formats": formats,
            }

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def extract_video_info(self, url):
        ydl_opts = {"format": "best"}
        formats = []
        best_audio_found = False
        banner_url = None
        title = None
        error = None

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)

                banner_url = info_dict.get("thumbnail")
                title = info_dict.get("title")

                if "instagram.com" in url and banner_url:
                    proxy_url = (
                        reverse("downloader:proxy_thumbnail")
                        + "?"
                        + urlencode({"url": banner_url})
                    )
                    banner_url = proxy_url

                for format in info_dict["formats"]:
                    format_id = format.get("format_id")
                    resolution = format.get("resolution", "audio only")
                    ext = format.get("ext", "unknown")
                    download_url = format.get("url", "No URL available")
                    if ".m3u8" not in download_url and ext != "mhtml":
                        if (
                            format.get("acodec") != "none"
                            and format.get("vcodec") == "none"
                        ):
                            if best_audio_found:
                                continue
                            else:
                                best_audio_found = True
                        formats.append(
                            {
                                "format_id": format_id,
                                "title": title,
                                "resolution": resolution,
                                "ext": ext,
                                "download_url": download_url,
                            }
                        )
        except Exception as e:
            error = str(e)

        return formats, banner_url, title, error


class DownloadAPIView(APIView):

    def post(self, request):
        serializer = DownloadSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data["url"]
            format_id = serializer.validated_data["format_id"]
            audio_only = serializer.validated_data.get("audio_only", False)
            video_only = serializer.validated_data.get("video_only", False)

            unique_id = uuid.uuid4().hex[:8]

            ydl_opts = {
                "format": (
                    f"{format_id}+bestaudio/b"
                    if not audio_only and not video_only
                    else format_id
                ),
                "outtmpl": f"/tmp/{unique_id}_%(title)s.%(ext)s",
                "cookiefile": "/tmp/youtube_cookies.txt",

            if "mp4" in format_id:
                ydl_opts["merge_output_format"] = "mp4"

            if audio_only:
                ydl_opts["format"] = f"{format_id}/bestaudio"
                ydl_opts["postprocessors"] = [
                    {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}
                ]

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    result = ydl.extract_info(url, download=True)

                output_file = ydl.prepare_filename(result)

                with open(output_file, "rb") as f:
                    file_data = f.read()

                response = HttpResponse(
                    file_data, content_type="application/octet-stream"
                )

                encoded_filename = urllib.parse.quote(os.path.basename(output_file))
                print("encoded_filename", encoded_filename)
                response["Content-Disposition"] = (
                    f'attachment; filename="{encoded_filename}"; filename*="UTF-8\'\'{encoded_filename}"'
                )
                print(
                    "response['Content-Disposition']", response["Content-Disposition"]
                )

                os.remove(output_file)

                return response

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
