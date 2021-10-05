import logging

from web.models import Gift


logger = logging.getLogger(__name__)


def transfer_gift(gift: Gift, ethereum_address: str) -> bool:  # eht address check
    """Proceed transfering to eth address."""

    # ... # todo to kostil

    logger.info('Gift transfered, finally mark gift as received')
    # gift.received = True  # todo!
    gift.save()
    return True

