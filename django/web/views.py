import logging
from eth_account import Account
import secrets

import requests

from django.shortcuts import render, HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def receiving(request):
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    addr = acct.address

    print(addr)

    data = {
        "user": addr,
        "contract": "0x60f80121c31a0d46b5279700f9df786054aa5ee5",
        "token": "1375655",

        "debug": "---",
        "private_ext": "bf991944c7de84b69be8c3e5523bf1b1d7f92b96f5cc9e98949962d814a72a83"
    }

    try:
        r = requests.post('http://nft_gifts_node_kostil_1:8080', json=data)
        print(r.content)
    except Exception as e:
        print(f'Exception: {e}')
        pass

    return render(request, 'receiving.html', {'private_key': private_key, 'public_key': addr})


def checking_page(request):
    return render(request, 'checking-page.html')
