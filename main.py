import hikari
from config import *



bot = hikari.BotApp(TOKEN, intents=hikari.Intents.ALL)


@bot.listen()
async def voice_role(event: hikari.VoiceStateUpdateEvent):
    if event.old_state is None:
        await bot.rest.add_role_to_member(guild=DEFAULT_GUILD, user=event.state.member.id, role=VOICE_ROLE)

    if event.state is None:
        await bot.rest.remove_role_from_member(guild=DEFAULT_GUILD, user=event.state.member.id, role=VOICE_ROLE)

def main():
    bot.run(status=hikari.presences.Status.DO_NOT_DISTURB)


if __name__ == '__main__':
    main()
