from django.urls import path

from .views import checking_page, index, receiving, GiftDetailView, EhtereumWalletView, SendAndCheckGiftView

app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
    path('gift/<slug:slug>', GiftDetailView.as_view(), name='gift_detail'),
    path('ethereum-wallet', EhtereumWalletView.as_view(), name='ethereum_wallet'),
    path('check-gift/<str:to_wallet>', SendAndCheckGiftView.as_view(), name='send_and_check'),

    path('receiving', receiving, name='receiving'),
    path('checking_page', checking_page, name='checking_page')
]
