from values import initialise
channel_id, token, pfp, message_id = initialise()
# importing

import frenchcord
print('import')
# embed

embed = frenchcord.Embed(titre="Testing Embed", description="Testing description", couleur=0xad1457)
embed.set_footer('I\'m a footer', icon_url=pfp)
embed.set_image(pfp)
embed.set_thumbnail(pfp)
embed.add_field('Inline field title', 'inline field value')
embed.add_field('Non inline field title', 'Non inline field value', inline=False)
print('embed')
# send

frenchcord.send(channel_id=channel_id, contenu='Online', embeds=[embed], token=token, data=False)
print('send')
# client

client = frenchcord.Robot(token)
client.send(channel_id, contenu='Online', embeds=[embed], data=False)
print('client')
# message/channel

message = frenchcord.zaza.get_message(message_id, channel_id)
message.channel().send(contenu='Online', embeds=[embed], data=False)
print('message + channel')

guild = message.channel().guild()
print('guild')
@client.event('on_ready')
def ptonline():
  print('online')
print('event handler')
@client.event('message')
def cmd(message):
  if message.author.id == client.me.id: return
  client.process_commands(message)

@client.command()
def hi(ctx):
  ctx.send('WORKING')
print('command handler')
client.connexion(['?'], True)
