import requests

open("test.py", "w").write(requests.get("https://raw.githubusercontent.com/Th3K1n91/workspace/main/test.py?token=GHSAT0AAAAAABUUBZ6TUUVN2SOJWD46HJUYY3PRDZQ").text)