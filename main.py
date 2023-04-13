import httpx

import random

import string

import colorama

from colorama import *

import os

import time

s = httpx.AsyncClient()

proxylist = []

with open("proxies.txt", "r") as f:

    proxylist = [line.strip() for line in f.readlines()]

errmessage = "Unknown Sara"

valid_codes = []

valid_count = 0

invalid_count = 0

checked_count = 0

rate_limited_count = 0

bad_proxy_count = 0

while True:

    proxy = random.choice(proxylist)

    set_title(f"Sara Cracker - Valid: {valid_count} | Invalid: {invalid_count} | Checked: {checked_count} | Rate Limited: {rate_limited_count} | Bad Proxy: {bad_proxy_count}")

    code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

    try:

        response = s.get(f'https://discordapp.com/api/invite/{code}', proxies={proxy}, timeout=30)

        if response.status_code != 429:

            json = response.json()

            if json.get('message') == errmessage:

                print(f"{Fore.RED}[-] {response.status_code} | Invalid Sara Code: {code}")

                invalid_count += 1

            else:

                print(f"{Fore.GREEN}[+] {response.status_code} | Valid Code: {code}")

                valid_codes.append(code)

                valid_count += 1

        else:

            print(f"{Fore.YELLOW}Rate Limited!")

            rate_limited_count += 1

    except httpx.exceptions.ProxyError:

        proxylist.remove(proxy)

        bad_proxy_count += 1

    except Exception as e:

        print(f"{Fore.RED}Error: {e}")

    finally:

        checked_count += 1

