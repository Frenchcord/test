import frenchcord
from os import environ
client = frenchcord.Robot(environ['token'])




@client.event('message')
def msg(message):
  message.send()
  if message.guild_id == 988248144213049364:
    client.process_commands(message)
    
@client.command
def help(ctx):
  ctx.send(embeds=[frenchcord.Embed(titre="hello", description="hi", color=frenchcord.color_random())])
