# import jwt

# encoded_jwt = jwt.encode(
#         {"some": "payload"},
#         "secret",
#         algorithm="HS256"
#     )
# decoded  = jwt.decode(
#         encoded_jwt,
#         "secret",
#         algorithms=["HS256"]
#     )
# # {'some': 'payload'}

import jwt
key = "secret"

encoded_jwt = jwt.encode(
    {
        "key" : "value"
    },
    key,
    algorithm= "HS256"
)
decode = jwt.decode(
    encoded_jwt,
    key,
    algorithms= ["HS256"]
)
print(decode)