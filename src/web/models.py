from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)


class EthereumWallet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ethereum_wallets')
    address = models.CharField(max_length=42)
    private_key = models.CharField(max_length=256, null=True, blank=True)  # todo: rehardcode should be deprecated, ofc


class Gift(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='gifts_sent')
    receiver = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='gifts_received')

    obtaining_url = models.URLField("Url that match receiver with a gift")  # todo: create generator
    rarible_url = models.URLField()
    text = models.TextField()

    received = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
