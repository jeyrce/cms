import \
    os.path

from django.contrib.auth.views import \
    PasswordResetView
from django.views import \
    View
from django.shortcuts import \
    render
from django.views.static import *
from django.utils.translation import \
    gettext as _

from cms.forms import \
    AsyncPasswordResetForm
from cms.settings import \
    ADMIN_SITE_URL


class AsyncPasswordResetView(PasswordResetView):
    """
    将原本同步发送邮件逻辑变更为异步
    """
    form_class = AsyncPasswordResetForm


class IndexView(View):
    """
    短暂延迟后定向至管理页面
    """

    def get(self, request, *args, **kwargs):
        return render(
            request, "index.html", {
                "ADMIN_SITE_URL": ADMIN_SITE_URL,
                "TITLE": "登录页"
            }
        )


# 固定文件响应
def file(request, document_root=None, content_type=None, encoding="utf8"):
    fullpath = Path(os.path.join(document_root, posixpath.normpath(request.path_info).lstrip("/")))
    if not fullpath.exists():
        raise Http404(
            _("“%(path)s” does not exist") % {
                "path": fullpath}
        )
    # Respect the If-Modified-Since header.
    statobj = fullpath.stat()
    if not was_modified_since(
            request.META.get("HTTP_IF_MODIFIED_SINCE"), statobj.st_mtime
    ):
        return HttpResponseNotModified()
    c, encode = mimetypes.guess_type(str(fullpath))
    if not content_type:
        content_type = c or "application/octet-stream"
    response = FileResponse(fullpath.open("rb"), content_type=content_type)
    response.headers["Last-Modified"] = http_date(statobj.st_mtime)
    response.headers["Content-Encoding"] = encode or encoding
    return response
