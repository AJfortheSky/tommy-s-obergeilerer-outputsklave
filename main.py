import hikari
import tanjun
from config import *
import plugins

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


def build_bot() -> hikari.GatewayBot:
    bot = hikari.GatewayBot(TOKEN, intents=hikari.Intents.ALL)

    make_client(bot)

    return bot





def main():
    build_bot().run(status=hikari.presences.Status.DO_NOT_DISTURB)


if __name__ == '__main__':
    main()
