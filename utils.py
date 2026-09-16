import re

def format_phone(phone: str) -> str:
    cleaned = re.sub(r'\D', '', phone)
    if len(cleaned) == 11 and cleaned.startswith('8'):
        cleaned = '7' + cleaned[1:]
    return cleaned

def detect_search_type(query: str) -> str:
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', query):
        return "email"
    digits = re.sub(r'\D', '', query)
    if len(digits) >= 10 and len(digits) <= 15:
        return "phone"
    if query.startswith('@'):
        return "telegram"
    if query.startswith('#') or (query.isdigit() and len(query) >= 9):
        return "telegram"
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', query):
        return "domain"
    if re.match(r'^[\w\.-]+\.[a-z]{2,}$', query.lower()):
        return "domain"
    if re.match(r'^[A-HJ-NPR-Z0-9]{17}$', query.upper()):
        return "car"
    if re.match(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$', query.upper()):
        return "car"
    if query.isdigit() and len(digits) in (10, 12):
        return "company"
    return "fio"

def truncate_text(text: str, max_length: int = 4000) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."
