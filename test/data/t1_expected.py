from proto_parser.proto_parser import ScopedSection, WORD_ROOT, WORD_PROTO_FILE, WORD_SERVICE, Service, RPC, Message, HttpMethod, \
    WORD_MESSAGE, MessageField, WORD_FIELD

T1_BASKET_SERVICE_CONTENT = [
    "rpc Update(UpdateBasketReq) returns (UpdateBasketResp) {",
    "option (google.api.http) = {",
    "post: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
    "rpc Get(GetBasketReq) returns (Basket) {",
    "option (google.api.http) = {",
    "get: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
]

T1_BASKET_SERVICE = [
    "service BasketService {",
    "rpc Update(UpdateBasketReq) returns (UpdateBasketResp) {",
    "option (google.api.http) = {",
    "post: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
    "rpc Get(GetBasketReq) returns (Basket) {",
    "option (google.api.http) = {",
    "get: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
    "}",
]

T1_MESSAGE_UPDATEBASKETREQ = [
    "message UpdateBasketReq {",
    "Basket basket = 1;",
    "}",
]

T1_MESSAGE_UPDATEBASKETRESP = [
    "message UpdateBasketResp {",
    "double subtotal = 1;",
    "double total = 2;",
    "repeated api.gen.Promotion applied_promotions = 3;",
    "}",
]

T1_MESSAGE_UPDATEBASKET = [
    "message Basket {",
    "string id = 1;",
    "string user_id = 2;",
    "repeated string product_ids = 3;",
    "}",
]

T1_LINES = [
    str.join("\n", T1_BASKET_SERVICE) + "\n",
    str.join("\n", T1_MESSAGE_UPDATEBASKETREQ) + "\n",
    str.join("\n", T1_MESSAGE_UPDATEBASKETRESP) + "\n",
    str.join("\n", T1_MESSAGE_UPDATEBASKET) + "\n"
]

T1_BASKET_SERVICE_RPC_GET = [
    "rpc Get(GetBasketReq) returns (Basket) {",
    "option (google.api.http) = {",
    "get: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
]

T1_BASKET_SERVICE_RPC_POST = [
    "rpc Update(UpdateBasketReq) returns (UpdateBasketResp) {",
    "option (google.api.http) = {",
    "post: \"/user/{basket.user_id}/basket\"",
    "body: \"*\"",
    "};",
    "}",
]

T1_BASKET_SERVICE_WRAPPED = [
    str.join("\n", T1_BASKET_SERVICE_RPC_GET) + "\n",
    str.join("\n", T1_BASKET_SERVICE_RPC_POST) + "\n",
]

T1_SCOPED_SECTION_EXPECTED = ScopedSection()
T1_SCOPED_SECTION_EXPECTED.name = WORD_ROOT
T1_SCOPED_SECTION_EXPECTED.data_type = WORD_PROTO_FILE
T1_SCOPED_SECTION_EXPECTED.declaration_dict = {
    WORD_SERVICE: [
        Service(name="BasketService", rpc_list=[
            RPC(
                name="Update",
                req="UpdateBasketReq",
                resp="UpdateBasketResp",
                endpoint="/user/{basket.user_id}/basket",
                http_method=HttpMethod.POST,
            ),
            RPC(
                name="Get",
                req="GetBasketReq",
                resp="Basket",
                endpoint="/user/{basket.user_id}/basket",
                http_method=HttpMethod.GET,
            ),
        ])
    ],
    WORD_MESSAGE: [
        Message(
            name="UpdateBasketReq",
            declaration_dict={
                WORD_FIELD: [
                    MessageField(name="basket", data_type="Basket"),
                ]
            }
        ),
        Message(
            name="UpdateBasketResp",
            declaration_dict={
                WORD_FIELD: [
                    MessageField(name="subtotal", data_type="double"),
                    MessageField(name="total", data_type="double"),
                    MessageField(name="applied_promotions", data_type="api.gen.Promotion", is_array=True),
                ],
            },
        ),
        Message(
            name="Basket",
            declaration_dict={
                WORD_FIELD: [
                    MessageField(name="id", data_type="string"),
                    MessageField(name="user_id", data_type="string"),
                    MessageField(name="product_ids", data_type="string", is_array=True),
                ],
            },
        )
    ],
}
