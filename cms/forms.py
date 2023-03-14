from django.contrib.auth.forms import \
    PasswordResetForm

from jobs import \
    async_send_mail


class AsyncPasswordResetForm(PasswordResetForm):
    """
    覆盖父类同步邮件发送方式，采用异步任务去实现
    """

    def send_mail(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        async_send_mail.delay(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)
