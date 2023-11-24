import tanjun
from hikari import Embed

nl = "\n"

component = tanjun.Component()

@component.with_slash_command
@tanjun.as_slash_command("whats-my-id",
                         "Find out what your User ID is!",
                         default_to_ephemeral=False)
async def whats_my_id(ctx: tanjun.abc.Context) -> None:
    await ctx.respond(f"Hi {ctx.author.mention}! {nl} Your User ID is: ```{ctx.author.id}```")

@component.with_slash_command
@tanjun.as_slash_command("help",
                         "Get information about the bot.",
                         default_to_ephemeral=False)
async def whats_my_id(ctx: tanjun.abc.Context) -> None:
    embed = Embed(title=f"Hello, {ctx.member.nickname or ctx.member.username}!",
                  description='There is not much to discover, YET! '
                              f'We are (and by we I mean myself) working on new features to be delivered.{nl}'
                              f'Stay Tuned!')
    await ctx.respond()


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
