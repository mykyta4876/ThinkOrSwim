"""
When you run the code above, the code will open a Charles Schwab login screen in your browser. Here, you need to log in using your existing Charles Schwab portfolio credentials, not your Developer Portal credentials. From there, you will select the brokerage account(s) to which you elect to give the APIs access.

From there, you’ll be routed to an empty page, which contains a URL in the search bar with an access code embedded in it. You’ll need to copy the entire URL. The code will prompt you to paste it in terminal, and once you do so, the code will make a request for the first batch of authentication tokens, and logger will print the tokens out for you in terminal.

At this point, you have all of the tokens you need. The access token, however, expires after 30 minutes, and your application needs this access token every time it makes a request to the Trader APIs. To keep the access token refreshed, you need to exchange your current refresh token (included in the first batch) with Schwab, get a new refresh token (which comes with a new access token), etc. every 29 minutes to ensure you have a working access token at all times — or at least during market hours. The next step, then, is setting up a refresh token system.
"""


import os
import base64
import requests
import webbrowser
from logger import logger


def construct_init_auth_url() -> tuple[str, str, str]:
    
    app_key = "iVm16EvmauKNKwHjvLbocVjhiH5cbabA"
    app_secret = "wjMGYDHoMXCySAni"

    auth_url = f"https://api.schwabapi.com/v1/oauth/authorize?client_id={app_key}&redirect_uri=https://127.0.0.1"

    logger.info("Click to authenticate:")
    logger.info(auth_url)

    return app_key, app_secret, auth_url


def construct_headers_and_payload(returned_url, app_key, app_secret):
    response_code = f"{returned_url[returned_url.index('code=') + 5: returned_url.index('%40')]}@"

    credentials = f"{app_key}:{app_secret}"
    base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
        "utf-8"
    )

    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "grant_type": "authorization_code",
        "code": response_code,
        "redirect_uri": "https://127.0.0.1",
    }

    return headers, payload


def retrieve_tokens(headers, payload) -> dict:
    init_token_response = requests.post(
        url="https://api.schwabapi.com/v1/oauth/token",
        headers=headers,
        data=payload,
    )

    init_tokens_dict = init_token_response.json()

    return init_tokens_dict


def main():
    app_key, app_secret, cs_auth_url = construct_init_auth_url()
    webbrowser.open(cs_auth_url)

    logger.info("Paste Returned URL:")
    returned_url = input()

    init_token_headers, init_token_payload = construct_headers_and_payload(
        returned_url, app_key, app_secret
    )

    init_tokens_dict = retrieve_tokens(
        headers=init_token_headers, payload=init_token_payload
    )

    logger.debug(init_tokens_dict)

    return "Done!"


if __name__ == "__main__":
    main()