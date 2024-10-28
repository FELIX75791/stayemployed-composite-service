import httpx


# Asynchronous HTTP GET with Authorization
async def async_get(url, params=None, headers=None):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()


# Synchronous HTTP PUT with Authorization
def sync_put(url, json=None, headers=None):
    response = httpx.put(url, json=json, headers=headers)
    response.raise_for_status()
    return response.json()


# Synchronous HTTP POST with Authorization
def sync_post(url, json=None, headers=None):
    response = httpx.post(url, json=json, headers=headers)
    response.raise_for_status()
    return response.json()
