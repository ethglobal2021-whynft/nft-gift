# todo: hardcoded warming up
import logging
from django.conf import settings
from django.core.mail import send_mail

from web.models import Client, Gift, EthereumWallet

logger = logging.getLogger(__name__)


def warm_up_with_default_test_net_sender_and_gift(
        url="https://img.rarible.com/staging/image/upload/t_big/staging-itemImages/0x509fd4cdaa29be7b1fad251d8ea0fca2ca91eb60:111668/7584a2c3",
        obtaining_url='foo',
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
        rarible_image_url=url,
        rarible_title='TestTitle',  # todo: hardcoded
        rarible_description='TestDescription',
        obtaining_url=obtaining_url,
        text='Anya, I congratulate you on your birthday and present the asset to your collection. May your life be as incredible as this picture <3',
    )
    logger.info(f'warmed up with {gift=}')


def send_gift_email(gift: Gift):
    sender = gift.seder
    receiver = gift.receiver
    receiver_name = (receiver.name if receiver.name else receiver.email).capitalize()
    sender_name = (sender.name if sender.name else sender.email).capitalize()
    message = gift.text if gift.text else f"Dear, {receiver_name}!\n\n{sender_name} sent you the NFT Gift!"
    appendix = (
        '-' * 5 + '\n'
        f"{sender_name} has prepared an nft transfer for you.\n"
        f"To finally obtain the gift follow the link http://localhost/gift/{gift.obtaining_url}\n"
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



