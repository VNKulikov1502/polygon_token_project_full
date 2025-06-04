from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import (
    get_balance,
    get_balance_batch,
    get_token_info,
    get_top_holders,
    get_top_with_last_tx
)

class GetBalanceView(APIView):
    def get(self, request):
        address = request.query_params.get('address')
        if not address:
            return Response({"error": "Missing address"}, status=400)
        balance = get_balance(address)
        return Response({"balance": balance})

class GetBalanceBatchView(APIView):
    def post(self, request):
        addresses = request.data.get("addresses", [])
        if not isinstance(addresses, list):
            return Response({"error": "Invalid addresses format"}, status=400)
        balances = get_balance_batch(addresses)
        return Response({"balances": balances})

class GetTokenInfoView(APIView):
    def get(self, request):
        info = get_token_info()
        return Response(info)

class GetTopHoldersView(APIView):
    def get(self, request):
        top_n = int(request.query_params.get("n", 10))
        top = get_top_holders(top_n)
        formatted_top = [(addr, bal / 1e18) for addr, bal in top]  # Optional: format to decimals
        return Response({"top_holders": formatted_top})

class GetTopWithLastTxView(APIView):
    def get(self, request):
        top_n = int(request.query_params.get("n", 10))
        top = get_top_with_last_tx(top_n)
        formatted_top = [(addr, bal / 1e18, last_tx) for addr, bal, last_tx in top]  # Optional
        return Response({"top_with_last_tx": formatted_top})
