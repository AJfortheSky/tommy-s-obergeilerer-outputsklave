import hikari
import tanjun
from config import *

bot = hikari.GatewayBot(token=TOKEN, intents=hikari.Intents.ALL)

def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = (
        tanjun.Client.from_gateway_bot(
            bot,
            mention_prefix=True,
            set_global_commands=DEFAULT_GUILD
        )
    ).add_prefix("!")

    client.load_modules('plugins.utilities')

    return client

def main():
    bot.run(status=hikari.presences.Status.DO_NOT_DISTURB)

if __name__ == '__main__':
    main()