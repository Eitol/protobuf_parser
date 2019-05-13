from proto_parser.proto_parser import ProtoEnum, Service, RPC, HttpMethod

EXPECTED_SIMPLE_ENUM = ProtoEnum()
EXPECTED_SIMPLE_ENUM.name = "Color"
EXPECTED_SIMPLE_ENUM.values = [
    "INVALID",
    "RED",
    "BLUE",
]

RPC_GET = RPC()
RPC_GET.endpoint = "/user/{basket.user_id}/basket"
RPC_GET.http_method = HttpMethod.GET
RPC_GET.request = "GetBasketReq"
RPC_GET.response = "Basket"
RPC_GET.name = 'Get'

RPC_UPDATE = RPC()
RPC_UPDATE.endpoint = "/user/{basket.user_id}/basket"
RPC_UPDATE.http_method = HttpMethod.POST
RPC_UPDATE.request = "UpdateBasketReq"
RPC_UPDATE.response = "UpdateBasketResp"
RPC_UPDATE.name = 'Update'


EXPECTED_SIMPLE_SERVICE = Service()
EXPECTED_SIMPLE_SERVICE.rpc_list = [RPC_UPDATE, RPC_GET]
EXPECTED_SIMPLE_SERVICE.name = "BasketService"
