import requests
import logging
import os


logger = logging.getLogger(__name__)
RARIBLE_API = os.getenv('RARIBLE_API', 'http://rarible_sdk:8080')


class RaribleSdkException(Exception):
    pass


def transfer_through_rarible_sdk(receiver: str, contract: str, token: str, sender_private_key: str) -> str:
    data = {
        "user_receiver": receiver,
        "contract": contract,
        "token": token,
        "sender_private_ext": sender_private_key,
    }
    r = requests.post(RARIBLE_API, json=data)
    logger.info(f'requested rarible sdk with {data}, got response: {r.content}')

    j = r.json()
    if not j.get("status", "ERROR") == "OK" or not j.get('hash'):
        raise RaribleSdkException(j)

    return j['hash']
