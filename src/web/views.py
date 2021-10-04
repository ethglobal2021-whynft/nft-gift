import logging
from eth_account import Account
import secrets

from django.views.generic import TemplateView, View
from django.shortcuts import render, HttpResponse

import requests


logger = logging.getLogger(__name__)


class IndexView(View):
    def get(self, request):
        target_view = 'panel:leads' if request.user.is_authenticated else 'panel:login'
        return redirect(reverse(target_view))





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
