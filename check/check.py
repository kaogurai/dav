from redbot.core import commands, checks

class Check(commands.Cog):
  """Check"""
  def __init__(self):
    pass
  
  @commands.command()
  async def check(self, ctx, *args):
    ctx.assume_yes = True
    clist=["userinfo","names"]

    for command_name in clist:
        command = ctx.bot.get_command(command_name)
        await ctx.invoke(command, *args)