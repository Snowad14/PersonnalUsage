from requests_html import HTMLSession

s = HTMLSession()


url = "https://serveur-prive.net/template/ajax/vote.php"

test = {
    "referer": "https://serveur-prive.net/minecraft/storycraft-meilleur-serveur-survie-1-18-1-nouvelles-grottes-6911/vote",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
} 


response = s.get("https://serveur-prive.net/minecraft/storycraft-meilleur-serveur-survie-1-18-1-nouvelles-grottes-6911/vote")

res = s.post(url, data=test)


print(res)
print(res.content)
print(res.text)

