from marshmallow import Schema

class UserDTO(Schema):
    class Meta:
        fields = ("id", "document", "name", "last_name", "email", "password", "creation_date", "status")

class WalletDTO(Schema):
    class Meta:
        fields = ("_hex", "wif", "wifc", "pubkey", "pubkeyc", "pubaddr1", "pubaddr3", "pubaddrbc1_p2wsh", "pubaddrbc1_p2wpkh", "balances", "user_id", "status")