import \
    traceback


class TracebackMiddleware(object):
    """
    打印错误详细信息
    """

    def __init__(self, do):
        self.do = do

    def __call__(self, request):
        response = self.do(request)
        traceback.format_exc()
        return response
