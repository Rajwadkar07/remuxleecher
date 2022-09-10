import feedparser
from time import sleep
from pyrogram import Client

app = Client("my_account")
key = ["remux", "1080p"]
print("Restarting")
old = []
while True:
    res = feedparser.parse("https://rss24h.torrentleech.org/98d5a4ce118834c42aad")
    new = []
    for i in res.entries:
        if all(x in i.title.lower() for x in key):
            command = "/mirror " + str(i.link)
            new += [command]
    for i in new:
        if i not in old:
            async def main():
                async with app:
                    await app.send_message(-1001618019889, i)
            app.run(main())
            print("Sent " + str(i)[8:])
            sleep(10)
    old = new
    print("Length of new: " + str(len(new)))
    print("Length of old: " + str(len(old)))
    print("Sleeping for 5 minutes.")
    sleep(300)
