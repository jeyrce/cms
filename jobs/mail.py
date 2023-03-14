from celery import \
    shared_task
from django.core.mail import \
    send_mail, \
    send_mass_mail


@shared_task
def async_send_mail(
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
):
    send_mail(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)
