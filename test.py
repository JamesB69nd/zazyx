import requests

print("Updating Code..")
open("test.py", "w").write(requests.get("https://raw.githubusercontent.com/JamesB69nd/zazyx/main/test.py").text)
print("Update done")

print("yes")
