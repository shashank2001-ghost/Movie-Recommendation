import asyncio
import httpx
import requests

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": "42d064dfd224fb7e6c6553a611228791",
                "query": "avatar"
            }
        )
        print(r.status_code)
        print(r.text[:200])

asyncio.run(main())