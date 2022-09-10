import feedparser
from time import sleep
from pyrogram import Client
app = Client("my_account")
filter = ["remux", "1080p"]
old = []
while True:
  res = feedparser.parse("https://rss24h.torrentleech.org/98d5a4ce118834c42aad")
  new = []
  with open('links.txt', 'w+') as f:
    for i in res.entries:
      if all(x in i.title.lower() for x in filter):
        command = "/mirror "+i.link
        if command not in old:
          new += [command]
          async def main():
            async with app:
              await app.send_message(-1001618019889, command)
          f.write(command+"\n")
          app.run(main())
          print("Sent "+i.title)
          sleep(60)
  old = new
  print("Sleeping")
  sleep(10)
