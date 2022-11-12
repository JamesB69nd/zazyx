import requests

update = requests.get("https://raw.githubusercontent.com/JamesB69nd/zazyx/main/test.py").text
print(len(update))
print(len(open("test.py").read()))
if len(update) != len(open("test.py").read()):
    print("Updating Code")
    open("test.py", "w").write(update)
    print("Done")
    print("Restart Code")
    exit()
