"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import \
    os, \
    re

from django.contrib import \
    admin
from django.urls import \
    path, \
    re_path
from django.contrib.auth import \
    views
from django.views.static import \
    serve

from cms.settings import \
    ADMIN_SITE_URL, \
    PASSWORD_URL, \
    MEDIA_ROOT, \
    MEDIA_URL, \
    STATIC_ROOT, \
    STATIC_URL, \
    BASE_DIR
from cms.views import \
    AsyncPasswordResetView, \
    IndexView, \
    file

urlpatterns = [
    path("", IndexView.as_view()),
    path(ADMIN_SITE_URL, admin.site.urls, name="admin_site"),
    path(os.path.join(PASSWORD_URL, 'admin/password_reset/'), AsyncPasswordResetView.as_view(), name='password_reset'),
    path(os.path.join(PASSWORD_URL, 'admin/password_reset_done/'), views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(os.path.join(PASSWORD_URL, 'reset/<uidb64>/<token>/'), views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(os.path.join(PASSWORD_URL, 'reset/done/'), views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(MEDIA_URL.lstrip("/")), serve, {
            "document_root": MEDIA_ROOT}
    ),
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(STATIC_URL.lstrip("/")), serve, {
            "document_root": STATIC_ROOT}
    ),
    path(
        "robots.txt", file, {
            "document_root": BASE_DIR / "static",
            "content_type": "text/plain",
        }, name="robots"
    ),
    path(
        "LICENSE", file, {
            "document_root": BASE_DIR,
            "content_type": "text/plain",
        }, name="license"
    ),
]
