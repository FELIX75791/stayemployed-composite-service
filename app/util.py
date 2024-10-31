import httpx


# Asynchronous HTTP GET with Authorization
async def async_get(url, params=None, headers=None):
  async with httpx.AsyncClient() as client:
    response = await client.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()
  
def sync_get(url, params=None, headers=None):
  with httpx.Client() as client:
      response = client.get(url, params=params, headers=headers)
      response.raise_for_status()  # Raises an error for non-2xx responses
      return response.json()

# Asynchronous HTTP PATCH with Authorization
async def async_patch(url, json=None, headers=None):
    async with httpx.AsyncClient() as client:
      response = await client.patch(url, json=json, headers=headers)
      response.raise_for_status()  # Raises an error for non-2xx responses
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

# Asynchronous HTTP POST with Authorization
async def async_post(url, json=None, headers=None):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=json, headers=headers)
        response.raise_for_status()  # Raises an exception for 4xx/5xx responses
        return response.json()
