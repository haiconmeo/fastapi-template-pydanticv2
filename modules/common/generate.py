import random
import string
import re
from slugify import slugify as slug_convert


def generate_random_string(length=128):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_random_3(length=3):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string.upper()


def generate_account_id(length=22):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_chat_id(length=10):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_number(length=6):
    letters = string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def slugify(text):
    if not text:
        text = generate_account_id()
    text = slug_convert(text)
    random_string = ''.join(random.choice(string.ascii_letters)
                            for _ in range(4))
    slug = re.sub(r'[\W_]+', '-', text)
    return f'{slug}-{random_string}'


def slugify_title(text):
    text = slug_convert(text=text)
    random_string = ''.join(random.choice(string.ascii_letters)
                            for _ in range(3))
    slug = re.sub(r'[\W_]+', '-', text)
    return f'{random_string}-{slug}'


def generate_api_key(length=60):
    letters = list(string.ascii_letters + string.digits)
    random.shuffle(letters)
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return 'sk-'+random_string
