import logging

from django.conf import settings

from utils.rarible import transfer_through_rarible_sdk
from web.models import Gift


logger = logging.getLogger(__name__)


def transfer_gift(gift: Gift, ethereum_address: str) -> bool:  # eht address check
    """Proceed transferring to eth address."""

    if gift.received or gift.obtaining_url == settings.URL_ONLY_FOR_DEMONSTRATION_DOGU:
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

    if settings.DEBUG and settings.DEBUG_DO_NOT_MARK_GIFT_AS_RECEIVED:
        gift.save()
        return True
        
    logger.info('Gift transferred successfully, thus, mark gift as received')
    gift.received = True
    gift.save()
    return True

