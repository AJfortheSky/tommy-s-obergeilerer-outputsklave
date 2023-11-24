import tanjun
import hikari
from src.main import bot
from src.config import DEFAULT_GUILD
async def kick(ctx: tanjun.abc.SlashContext, user: hikari.Member.username,log: str):
    await bot.rest.kick_user(guild=DEFAULT_GUILD, user=user, reason=log)

slash_cmd = tanjun.SlashCommand(
    kick,
    "kick",
    "Kick a member",
)

slash_cmd.add_str_option('The user to be kicked')

component = tanjun.Component().load_from_scope().make_loader()