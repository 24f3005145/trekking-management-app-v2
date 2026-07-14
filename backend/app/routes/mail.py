from flask import Blueprint, jsonify

from app.services.mail_service import MailService

mail_bp = Blueprint("mail", __name__)


@mail_bp.route("/test-email", methods=["GET"])
def test_email():

    MailService.send_email(

        recipients=["classysassy2105@gmail.com"],

        subject="Trekking App Test",

        body="Congratulations! Flask-Mail is working."

    )

    return jsonify({

        "message": "Email sent."

    })