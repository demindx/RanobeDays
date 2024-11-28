from django.urls import path, include

from .apis import GoogleLoginAPI, GoogleLoginRedirectAPI, TelegramLoginAPI, test


google_urlpatterns = [
    path("login/", GoogleLoginRedirectAPI.as_view(), name="login"),
    path("login/callback", GoogleLoginAPI.as_view(), name="callback"),
]

telegram_urlpatterns = [
    path("login/", test),
    path("login/callback/", TelegramLoginAPI.as_view(), name="callback"),
]

urlpatterns = [
    path("google/", include((google_urlpatterns, "google"), "google")),
    path("telegram/", include((telegram_urlpatterns, "telegram"), "telegram")),
]
