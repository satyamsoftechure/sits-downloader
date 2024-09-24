from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.urls import reverse
import requests
from django.http import HttpResponse
from django.conf import settings


def fetch_video_info_from_api(request, url):
    api_url = request.build_absolute_uri(reverse("downloader:home_api"))
    headers = {"Authorization": settings.API_TOKEN, "Origin": request.get_host()}
    print("headers", headers)
    try:
        response = requests.post(api_url, json={"url": url}, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "index.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "index.html")


def Youtube(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "youtube.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "youtube.html")


def Instagram(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "instagram.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "instagram.html")


def Facebook(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "facebook.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "facebook.html")


def Twitter(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "twitter.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "twitter.html")


def Snapchat(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "snapchat.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "snapchat.html")


def LinkedIn(request):
    if request.method == "POST":
        url = request.POST.get("url")
        video_info = fetch_video_info_from_api(request, url)

        if "error" in video_info:
            return HttpResponse(f"An error occurred: {video_info['error']}")

        return render(
            request,
            "linkedin.html",
            {
                "formats": video_info.get("formats", []),
                "url": url,
                "banner_url": video_info.get("banner_url"),
                "title": video_info.get("title"),
                "duration": video_info.get("duration"),
            },
        )

    return render(request, "linkedin.html")
