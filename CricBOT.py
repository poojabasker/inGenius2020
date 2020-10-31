import discord

bot=discord.Client() #add the bot

@bot.event

async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.lower() == '-awaken':
		await message.channel.send("Greetings, "+ str(message.author) +"! Your wish is my command :)")
	elif message.content.lower() == '-help':
		await message.channel.send("-predict team_1_name team_2_name  :  predicts the winner out of the two teams mentioned")

bot.run('NzcxNzEzNTAxMjE5NjUxNTg1.X5wINA.j20KROPEM7aJbasziCxJ_HYF_FE')