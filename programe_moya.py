import requests

q = f"https://kidkodschool.github.io/welcome.html"

w = requests.get (q)

print(w.content)














