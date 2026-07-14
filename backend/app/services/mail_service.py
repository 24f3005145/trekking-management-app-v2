from flask_mail import Message

from app.extensions import mail


class MailService:

    @staticmethod
    def send_email(
        recipients,
        subject,
        body=None,
        html=None
    ):

        try:

            message = Message(
                subject=subject,
                recipients=recipients
            )

            if body:
                message.body = body

            if html:
                message.html = html

            mail.send(message)

            return True

        except Exception as e:

            print(f"Email sending failed: {e}")

            return False