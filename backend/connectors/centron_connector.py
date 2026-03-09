import requests
from backend.config import Config

class CentronConnector:

    def __init__(self):

        self.ticket = None

    def login(self):

        payload = {
            "Ticket": "",
            "Data": {
                "Username": Config.CENTRON_USER,
                "Password": Config.CENTRON_PASS
            }
        }

        r = requests.post(
            Config.CENTRON_URL + "/Login",
            json=payload
        )

        self.ticket = r.json()["Result"][0]

    def update_article(self, customer_id, article_id, qty):

        payload = {
            "Ticket": self.ticket,
            "Data": {
                "CustomerId": customer_id,
                "ArticleId": article_id,
                "Quantity": qty
            }
        }

        requests.post(
            Config.CENTRON_URL + "/UpdateCustomerArticle",
            json=payload
        )
