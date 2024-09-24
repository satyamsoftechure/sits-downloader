from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import api_views
from .api_views import HomeAPIView, DownloadAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("youtube/", views.Youtube, name="youtube"),
    path("youtube-mp4/", views.Youtube, name="youtube"),
    path("youtube-shorts/", views.Youtube, name="youtube"),
    path("youtube-mp3/", views.Youtube, name="youtube"),
    path("instagram/", views.Instagram, name="instagram"),
    path("instagram-Reels/", views.Instagram, name="instagram"),
    path("instagram-Viewers/", views.Instagram, name="instagram"),
    path("facebook/", views.Facebook, name="facebook"),
    path("twitter/", views.Twitter, name="twitter"),
    path("snapchat/", views.Snapchat, name="snapchat"),
    path("linkedin/", views.LinkedIn, name="linkedin"),
    path("api/get-media-format/", HomeAPIView.as_view(), name="home_api"),
    path("api/get-media-file/", DownloadAPIView.as_view(), name="download_api"),
    path(
        "proxy-thumbnail/", api_views.proxy_instagram_thumbnail, name="proxy_thumbnail"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
