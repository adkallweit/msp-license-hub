import httpx
from backend.config import Config

class VeeamConnector:

    async def companies(self):

        async with httpx.AsyncClient() as client:

            r = await client.get(
                f"{Config.VEEAM_URL}/v3/organizations",
                headers={
                    "Authorization": f"Bearer {Config.VEEAM_TOKEN}"
                }
            )

        return r.json()["data"]
