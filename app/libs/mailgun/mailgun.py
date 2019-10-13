"""This is a adapter pattern practice. Mailgun can be replaced in future
with something else."""

import os
from typing import List

from dotenv import load_dotenv
import requests

load_dotenv()

FAILED_LOAD_API_KEY = "Failed to load Mailgun API KEY."
FAILED_LOAD_DOMAIN = "Failed to load Mailgun domain."


class MailgunException(BaseException):
    """Mailgun specific Exception."""

    # Having libraries their own exception are beneficial in debugging
    def __init__(self, message: str):
        super().__init__(message)


class Mailgun:
    MAILGUN_DOMAIN = os.environ["MAILGUN_DOMAIN"]  # can return None
    MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]  # can return None
    FROM_EMAIL = f"mailgun@{MAILGUN_DOMAIN}"
    FROM_TITLE = "Excited User"

    @classmethod
    def send_email(
        cls, email: List[str], subject: str, text: str, html: str
    ) -> requests.Response:

        if cls.MAILGUN_API_KEY is None:
            raise MailgunException(FAILED_LOAD_API_KEY)

        if cls.MAILGUN_DOMAIN is None:
            raise MailgunException(FAILED_LOAD_DOMAIN)

        response = requests.post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
            },
        )

        if response.status_code != 200:
            raise MailgunException(
                "Error in sending confirmation email, user registration failed."
            )

        return response

