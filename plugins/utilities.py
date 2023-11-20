import tanjun

nl = '\n'

component = tanjun.Component()
@component.with_slash_command
@tanjun.as_slash_command('Test command', 'This does absolutely nothing', default_to_ephemeral=True)
async def test_command(ctx: tanjun.abc.Context):
    await ctx.respond(content=f'Penis')


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())