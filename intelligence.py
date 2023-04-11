import requests
import pprint 



url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url).json()

charachter_intelligence = []
for charachter in resp:
  if charachter["name"] == "Hulk":
    hulk_intelligence = {"Hulk": charachter["powerstats"]["intelligence"]}
    charachter_intelligence.append(hulk_intelligence)
  if charachter["name"] == "Captain America":
    captain_intelligence = {"Captain America": charachter["powerstats"]["intelligence"]}
    charachter_intelligence.append(captain_intelligence)
  if charachter["name"] == "Thanos":
    thanos_intelligence = {"Thanos": charachter["powerstats"]["intelligence"]}
    charachter_intelligence.append(thanos_intelligence)

max_intelligence = 0
for charachter in charachter_intelligence:
  for key, value in charachter.items():
    if max_intelligence< value:
      max_intelligence = value
    
for charachter in charachter_intelligence:
  for key, value in charachter.items():
    if value == max_intelligence:
      print(key)