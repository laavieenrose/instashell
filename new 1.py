import trio
import httpx

from holehe.modules.social_media.snapchat import snapchat


async def main():
    email = "garciaabdullahadam@gmail.com"
    out = []
    client = httpx.AsyncClient()

    await snapchat(email, client, out)

    print(out)
    await client.aclose()

trio.run(main)