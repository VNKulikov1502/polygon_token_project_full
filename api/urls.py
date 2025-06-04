from django.urls import path
from .views import (
    GetBalanceView,
    GetBalanceBatchView,
    GetTokenInfoView,
    GetTopHoldersView,
    GetTopWithLastTxView
)

urlpatterns = [
    path('get_balance/', GetBalanceView.as_view()),
    path('get_balance_batch/', GetBalanceBatchView.as_view()),
    path('get_token_info/', GetTokenInfoView.as_view()),
    path('get_top/', GetTopHoldersView.as_view()),
    path('get_top_with_transactions/', GetTopWithLastTxView.as_view()),
]
