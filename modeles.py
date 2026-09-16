from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    username = Column(String(255), nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    queries = Column(Integer, default=0)
    role = Column(String(50), default="user")
    is_vip = Column(Boolean, default=False)
    vip_until = Column(DateTime, nullable=True)
    last_bonus = Column(DateTime, nullable=True)
    referral_balance = Column(Float, default=0.0)
    total_earned = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    amount = Column(Float)
    currency = Column(String(20))
    product = Column(String(100))
    status = Column(String(50), default="pending")
    telegram_payment_id = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    referral_id = Column(BigInteger)
    level = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

class PromoCode(Base):
    __tablename__ = "promocodes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(100), unique=True)
    max_activations = Column(Integer)
    current_activations = Column(Integer, default=0)
    queries_per_activation = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_by = Column(BigInteger)
    created_at = Column(DateTime, default=datetime.utcnow)

class DatabaseFile(Base):
    __tablename__ = "databases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    file_path = Column(String(500))
    records_count = Column(Integer, default=0)
    fields = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    added_by = Column(BigInteger)
    created_at = Column(DateTime, default
