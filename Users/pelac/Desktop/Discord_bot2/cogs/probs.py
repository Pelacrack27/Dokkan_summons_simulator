import discord
from discord.ext import commands

class Probs(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("probs online")

  #Comandos del bot
  @commands.command()
  async def probs(self, ctx):
    embed=discord.Embed(title="Probabilidades",  description="Probabilidades de los multisummons disponibles", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar_url)
    embed.add_field(name="Probabilidad de cada tirada:", value="20% SP | 35% HR | 45% EX", inline=False)
    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Probs(client))