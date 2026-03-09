import asyncio

from backend.connectors.sophos_connector import SophosConnector
from backend.connectors.veeam_connector import VeeamConnector

async def run_sync():

    sophos = SophosConnector()
    veeam = VeeamConnector()

    await sophos.authenticate()

    tenants = await sophos.tenants()
    companies = await veeam.companies()

    print("Sophos tenants:", len(tenants))
    print("Veeam companies:", len(companies))

if __name__ == "__main__":

    asyncio.run(run_sync())
