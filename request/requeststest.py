import requests

params = {"q": "pizza"}
r = requests.get("http://www.google.com/search", params=params)
print("Status: ", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
