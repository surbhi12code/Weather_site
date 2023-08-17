import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter the name of city \n")
url=f"https://api.weatherapi.com/v1/current.json?key=90279ea3b9aa4dc7ba8100412231708&q={city}"
r=requests.get(url)
wdic=json.loads(r.text)
print(wdic["current"] ["temp_c"])
w=wdic["current"] ["temp_c"]
text=f"the weather in {city} is{w}degrees"
speak.Speak(text)