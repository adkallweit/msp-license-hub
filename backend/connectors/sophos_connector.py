import httpx
from backend.config import Config

class SophosConnector:

    def __init__(self):
        self.token = None

    async def authenticate(self):

        async with httpx.AsyncClient() as client:

            r = await client.post(
                "https://id.sophos.com/api/v2/oauth2/token",
                data={
                    "grant_type": "client_credentials",
                    "client_id": Config.SOPHOS_CLIENT_ID,
                    "client_secret": Config.SOPHOS_SECRET,
                    "scope": "token"
                }
            )

        self.token = r.json()["access_token"]

    async def tenants(self):

        async with httpx.AsyncClient() as client:

            r = await client.get(
                "https://api.central.sophos.com/partner/v1/tenants",
                headers={"Authorization": f"Bearer {self.token}"}
            )

        return r.json()["items"]
