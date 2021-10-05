# todo: views should be rewritten to API for reactApp as frontend
import logging

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

        # if self.object.received:
        #     return HttpResponse(status=208)  # already reported

        if not to_wallet:  # todo: create eth field as in why-nft
            return HttpResponse(status=400)

        logger.info(
            f"Start sending gift {self.object.id} to {self.object.receiver.email} with wallet: {to_wallet}"
        )
        transfered = transfer_gift(gift=self.object, ethereum_address=to_wallet)
        if not transfered:
            return HttpResponse('can not transfer: rarible SDK', status=409)  # todo

        logger.info(f'Finally {self.object} transfered and response ready')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
