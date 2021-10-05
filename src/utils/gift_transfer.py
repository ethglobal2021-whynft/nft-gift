import logging

from django.conf import settings

from utils.rarible import transfer_through_rarible_sdk
from web.models import Gift


logger = logging.getLogger(__name__)


def transfer_gift(gift: Gift, ethereum_address: str) -> bool:  # eht address check
    """Proceed transfering to eth address."""

    if gift.received:
        return True

    contract, token = gift.url_to_contract_and_token
    try:
        transfer_through_rarible_sdk(
            receiver=ethereum_address,
            contract=contract,
            token=token,
            sender_private_key=settings.DEFAULT_SENDER_PRIVATE_KEY,
        )
    except Exception:
        logger.exception('Can not transfer due to SDK')
        return False

    logger.info('Gift transfered, finally mark gift as received')
    gift.received = True
    gift.save()
    return True

