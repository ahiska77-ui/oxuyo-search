import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "YourBot")
OWNER_ID = int(os.getenv("OWNER_ID", "5295393159"))

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///ahiska.db")

HUNTER_API_KEY = os.getenv("HUNTER_API_KEY", "c750a854258bf1a9c264f6166ca7e34f0a3c783d")
LEAKCHECK_API_KEY = os.getenv("LEAKCHECK_API_KEY", "4344cd645b6e6cc2559c1a92017d9bfa12e4e4b1")
HIBP_API_KEY = os.getenv("HIBP_API_KEY", "0123456789abcdef0123456789abcdef")
NUMLOOKUP_API_KEY = os.getenv("NUMLOOKUP_API_KEY", "num_live_sL8EgCimFaiqCAxcd8peRCkInxUWX2Zg1h1ceMIf")
SMSC_LOGIN = os.getenv("SMSC_LOGIN", "kirahacker333")
SMSC_PASSWORD = os.getenv("SMSC_PASSWORD", "Zangar5050!")
SMSC_API_KEY1 = os.getenv("SMSC_API_KEY1", "9fcd3e6622f96a780f0908ce414bb16360d3779d8253f484f319e02cc5c25065")
SMSC_API_KEY2 = os.getenv("SMSC_API_KEY2", "dbbc251dda62fb51321132d79b070d00cad48acec4c660f7f0b313eb09056e9b")
SMSC_API_KEY3 = os.getenv("SMSC_API_KEY3", "58878ed65228db88eddfda4983bce5d19d425ddf81f427857b3f59f11aecc34f127862a1cc7d4581")

CRYPTOBOT_TOKEN = os.getenv("CRYPTOBOT_TOKEN", "")
TON_WALLET = os.getenv("TON_WALLET", "")

WEB_HOST = os.getenv("WEB_HOST", "0.0.0.0")
WEB_PORT = int(os.getenv("WEB_PORT", "8080"))
WEB_SECRET = os.getenv("WEB_SECRET", "admin123")

TARIFFS = {
    "10_queries": {"stars": 75, "ton": 0.75, "queries": 10},
    "25_queries": {"stars": 170, "ton": 1.7, "queries": 25},
    "50_queries": {"stars": 300, "ton": 3, "queries": 50},
    "100_queries": {"stars": 550, "ton": 5.5, "queries": 100},
    "250_queries": {"stars": 1200, "ton": 12, "queries": 250},
    "500_queries": {"stars": 2000, "ton": 20, "queries": 500},
}

SUBSCRIPTIONS = {
    "start_7d": {"days": 7, "queries": 50, "stars": 250, "ton": 2.5},
    "standart_30d": {"days": 30, "queries": 200, "stars": 800, "ton": 8},
    "premium_30d": {"days": 30, "queries": 500, "stars": 1500, "ton": 15},
    "ultra_90d": {"days": 90, "queries": 2000, "stars": 3500, "ton": 35},
}

VIP_TARIFFS = {
    "vip_30d": {"days": 30, "stars": 1200, "ton": 12},
    "vip_90d": {"days": 90, "stars": 3000, "ton": 30},
    "vip_forever": {"days": 9999, "stars": 7500, "ton": 75},
}

SPECIAL = {
    "novice": {"stars": 50, "ton": 0.5, "queries": 5},
    "1000_queries": {"stars": 3500, "ton": 35, "queries": 1000},
    "5000_queries": {"stars": 14000, "ton": 140, "queries": 5000},
    "unlimited_30d": {"days": 30, "stars": 5000, "ton": 50},
}
