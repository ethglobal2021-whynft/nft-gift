# todo: views should be rewritten to API for reactApp as frontend
import logging
from eth_account import Account
import secrets
import requests

from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, HttpResponse, get_object_or_404

from utils.authorizations import session_authorization_check
from utils.gift_transfer import transfer_gift
from web.models import Gift

logger = logging.getLogger(__name__)


class GiftDetailView(DetailView):  # todo: on no object
    """1st step
    We also store special cookie, so it is kinda auth.
    """

    context_object_name = 'gift'
    model = Gift
    slug_field = 'obtaining_url'
    template_name = 'web/open_gift.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        logger.debug(f"set gift id {self.object.id} to session...")
        request.session['gift'] = self.object.id

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class EhtereumWalletView(TemplateView):
    """2nd step."""

    template_name = 'web/enter_ethereum_wallet.html'

    @session_authorization_check
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class SendAndCheckGiftView(DetailView):  # todo: view is really synced
    """3d step.
    Call the view with wallet for gift.

    Return:
        - 200: and DetailView;
        - 208: if already sent.
        - 409: transfer is not suceeded
    """

    template_name = 'web/check_gift.html'
    context_object_name = 'gift'
    model = Gift

    @session_authorization_check
    def get(self, request, to_wallet, *args, **kwargs):
        self.object = get_object_or_404(Gift, pk=request.session['gift'])

        if self.object.received:
            return HttpResponse(status=208)  # already reported

        if not to_wallet:  # todo: create eth field as in why-nft
            return HttpResponse(status=400)

        logger.info(
            f"Start sending gift {self.object.id} to {self.object.receiver.email} with wallet: {to_wallet}"
        )
        transfered = transfer_gift(gift=self.object, ethereum_address=to_wallet)
        if not transfered:
            return HttpResponse(status=409)  # todo

        logger.info(f'Finally {self.object} transfered and response ready')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# class EhtereumWalletView(View):  # TODO
#     # 2nd step
#
#     def get(self, request):
#         return render(request, 'receiving.html', {'private_key': private_key, 'public_key': addr})


# class IndexView(View):
#     def get(self, request, *args):
#         target_view = 'web:web' if request.user.is_authenticated else 'web:web'
#         return redirect(reverse(target_view))


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
        r = requests.post('http://rarible_sdk_1:8080', json=data)
        print(r.content)
    except Exception as e:
        print(f'Exception: {e}')
        pass

    return render(request, 'receiving.html', {'private_key': private_key, 'public_key': addr})


def checking_page(request):
    return render(request, 'checking-page.html')
