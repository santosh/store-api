"""This is a adapter pattern practice. Mailgun can be replaced in future
with something else."""

import os
from typing import List

from dotenv import load_dotenv
import requests

load_dotenv()


class Mailgun:
    MAILGUN_DOMAIN = os.environ["MAILGUN_DOMAIN"]
    MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]
    FROM_EMAIL = f"mailgun@{MAILGUN_DOMAIN}"
    FROM_TITLE = "Excited User"

    @classmethod
    def send_email(
        cls, email: List[str], subject: str, text: str, html: str
    ) -> requests.Response:
        return requests.post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
            },
        )
