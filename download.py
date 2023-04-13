import asyncio

import aiohttp

proxies_urls = [

    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",

    "https://www.proxy-list.download/api/v1/get?type=socks4",

    "https://www.proxyscan.io/download?type=socks4",

    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",

    "https://www.socks-proxy.net/"

]

async def fetch_proxies(session, url):

    try:

        async with session.get(url) as response:

            if response.status == 200:

                proxies = await response.text()

                with open("socks4.txt", "a") as f:

                    f.write(proxies)

    except:

        pass

async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []

        for url in proxies_urls:

            task = asyncio.create_task(fetch_proxies(session, url))

            tasks.append(task)

        await asyncio.gather(*tasks)

print("> Downloading Proxy List...")

asyncio.run(main())

print("> Proxy List Downloaded as socks4.txt")

input("Press any key to exit...")

