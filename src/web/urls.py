from django.urls import path

from .views import GiftDetailView, EhtereumWalletView, SendAndCheckGiftView

app_name = 'web'

urlpatterns = [
    path('gift/<slug:slug>', GiftDetailView.as_view(), name='gift_detail'),
    path('ethereum-wallet', EhtereumWalletView.as_view(), name='ethereum_wallet'),
    path('check-gift/<str:to_wallet>', SendAndCheckGiftView.as_view(), name='send_and_check'),
]
