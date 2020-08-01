from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    orm as orm,
    Boolean
)

from datetime import datetime
from .meta import Base
from ..utils.mapperDto import UserDTO, WalletDTO

#I know it's much space for string, but that's because i copied and pasted
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    document = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    creation_date = Column(DateTime,  default=datetime.utcnow)
    status = Column(Boolean, default=True)

    def __init__(self, document, name, last_name, email, password, status):
        self.document=document
        self.name=name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status

    def get_dic(self):
        userScheme = UserDTO()
        return userScheme.dump(self)


class Wallet(Base):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True)
    _hex = Column(String(256), unique=True, nullable=False)
    wif = Column(String(256), unique=True, nullable=False)
    wifc = Column(String(256), unique=True, nullable=False)
    pubkey = Column(String(256), unique=True, nullable=False)
    pubkeyc = Column(String(256), unique=True, nullable=False)
    pubaddr1 = Column(String(256), unique=True, nullable=False)
    pubaddr3 = Column(String(256), unique=True, nullable=False)
    pubaddrbc1_p2wsh = Column(String(256), unique=True, nullable=False)
    pubaddrbc1_p2wpkh = Column(String(256), unique=True, nullable=False)
    balances = Column(Float, default=1)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    creation_date = Column(DateTime,  default=datetime.utcnow)
    status = Column(Boolean, default=True)

    def __init__(self, _hex, wif, wifc, pubkey, pubkeyc, pubaddr1, pubaddr3, pubaddrbc1_p2wsh, pubaddrbc1_p2wpkh, user_id, status):
        self._hex=_hex
        self.wif=wif
        self.wifc=wifc
        self.pubkey=pubkey
        self.pubkeyc=pubkeyc
        self.pubaddr1=pubaddr1
        self.pubaddr3=pubaddr3
        self.pubaddrbc1_p2wsh=pubaddrbc1_p2wsh
        self.pubaddrbc1_p2wpkh=pubaddrbc1_p2wpkh
        self.user_id=user_id
        self.status=status

    def get_dic(self):
        walletScheme = WalletDTO(only=("pubaddr1", "pubaddr3", "pubaddrbc1_p2wsh", 'balances'))
        return walletScheme.dump(self)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    origin_address = Column(String(256), nullable=False)
    destination_address = Column(String(256), nullable=False)
    amount = Column(Float, nullable=False)
    fee = Column(Float, nullable=False)
    fee_percentil = Column(Float, nullable=False)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    creation_date = Column(DateTime,  default=datetime.utcnow)
    confirmation_date = Column(DateTime)
    
    def __init__(self, origin_address, destination_address, amount, fee, fee_percentil, wallet_id, confirmation_date):
        self.origin_address=origin_address
        self.destination_address=destination_address
        self.amount=amount
        self.fee=fee,
        self.fee_percentil=fee_percentil
        self.wallet_id=wallet_id
        self.confirmation_date=confirmation_date
        