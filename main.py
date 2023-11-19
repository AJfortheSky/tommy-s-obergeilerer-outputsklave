import hikari
from config import *

bot = hikari.GatewayBot(token=TOKEN, intents=hikari.Intents.ALL)


def main():
    bot.run(status=hikari.presences.Status.IDLE)

if __name__ == '__main__':
    main()