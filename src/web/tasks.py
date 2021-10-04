# todo: hardcoded warming up
import logging
from django.conf import settings
from django.core.mail import send_mail

from web.models import Client, Gift, EthereumWallet

logger = logging.getLogger(__name__)


def warm_up_with_default_test_net_sender_and_gift(
        url="https://rinkeby.rarible.com/token/0x509fd4cdaa29be7b1fad251d8ea0fca2ca91eb60:111442?tab=details",
        obtaining_url='http://localhost:8000/receive',
):
    """De facto it is our workflow.

    !a lot of hardcoded values. todo
    """

    test_net_address = settings.DEFAULT_TESTNET_SENDER_ADDRESS
    test_net_private = settings.DEFAULT_TESTNET_SENDER_PRIVATE_KEY

    client, created = Client.objects.get_or_create(name='sender', email='sender@google.com')
    logger.info(f'warmed up with {client=}')

    wallet, created = EthereumWallet.objects.get_or_create(
        client=client,
        address=test_net_address,
        private_key=test_net_private,
    )
    logger.info(f'warmed up with {wallet=}')

    receiver, created = Client.objects.get_or_create(name='receiver', email='receiver@google.com')

    gift, created = Gift.objects.get_or_create(
        sender=client,
        receiver=receiver,
        rarible_url=url,
        obtaining_url=obtaining_url,
        text='Hi, this is 4 u, bro!',
    )
    logger.info(f'warmed up with {gift=}')


def send_gift_email(sender: Client, receiver: Client, gift: Gift):
    receiver_name = (receiver.name if receiver.name else receiver.email).capitalize()
    sender_name = (sender.name if sender.name else sender.email).capitalize()
    message = gift.text if gift.text else f"Dear, {receiver_name}!\n\n{sender_name} sent you the NFT Gift!"
    appendix = (
        '-' * 5 + '\n'
        f"{sender_name} has prepared an nft transfer for you.\n"
        f"To finally obtain the gift follow the link {gift.obtaining_url}\n"
        '-' * 5 + '\n'
        'Sincerely Yours Why-NFT-Team\n'
        'why-nft.com'
    )
    send_mail(
        subject=f'{sender_name} Sent You an NFT Gift!',
        message=message + appendix,
        from_email='nft-gift@why-nft.com',  # todo: research if there can be used sender email
        recipient_list=[receiver.email],
        fail_silently=False,
    )


