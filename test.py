import requests

update = requests.get("https://raw.githubusercontent.com/JamesB69nd/zazyx/main/test.py").text
print(len(update.strip()))
print(len(open("test.py").read().strip()))
if len(update.strip()) != len(open("test.py").read().strip()):
    print("Updating Code")
    open("test.py", "w").write(update.strip())
    print("Done")
    print("Restart Code")
    exit()
print("yes")
