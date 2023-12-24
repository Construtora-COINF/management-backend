import base64
import hashlib
import re

from bs4 import BeautifulSoup


def md5(value: str):
    hash_value = hashlib.md5(value.encode()).hexdigest()
    return hash_value


def sha1(value: str):
    hash_value = hashlib.sha1(value.encode()).hexdigest()
    return hash_value


def base64_encode(value: str):
    encode_value = base64.b64encode(value.encode()).decode()
    return encode_value


def generate_token(mac_address: str) -> str:
    hash_generated = base64_encode(sha1(md5(mac_address.upper())))
    return hash_generated


def is_valid_ip_address(ip_address: str) -> bool:
    regex = re.compile(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    return regex.match(ip_address) is not None


def valid_format_email(email: str):
    regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(regex, email):
        return False
    return True


async def remove_html_text(text: str):
    soup = BeautifulSoup(text, "html.parser")
    body_text = soup.get_text()
    cleaned_text = re.sub(r"\n{3,}", "\n\n", body_text)
    return cleaned_text
