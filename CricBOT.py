import discord 
from pycricbuzz import Cricbuzz

bot=discord.Client() #add the bot

c = Cricbuzz()
matches = c.matches()

@bot.event 

async def on_message(message):

	message.content=message.content.lower()

	if message.author == bot.user:   #checking if bot is talking to itself
		return

	#bit commands
	if message.content == '-awaken':
		await message.channel.send("Greetings, "+ str(message.author) +"! Your wish is my command :)")
	
	elif message.content == '-help':
		await message.channel.send("-predict team_1_name team_2_name   :   predicts the winner out of the two teams mentioned\n-livescore  :  detailed scoreboard of the ongoing match\n-commentary  :  shows the live commentary of the ongoing match")
	
	elif message.content.startswith('-pred'):
		cmd = list(str(message.content).split(' '))
		#await message.channel.send(cmd)
		if len(cmd) != 3:
			await message.channel.send("Wrong syntax, use -help for command documentation")
		#else: call predict function from jupyter notebook

	elif message.content == '-livescore':	
		score = c.livescore(matches[0]['id'])
		await message.channel.send("Live Score\n")
		for a in score:
			await message.channel.send(str(a))
			for b in score[a]:
				await message.channel.send(str(b)+' : '+str(score[a][b]))
	
	elif message.content.startswith('-comm'):
		com = c.commentary(matches[0]['id'])
		for a in com:
			await message.channel.send(str(a))
			for b in com[a]:
				await message.channel.send(str(b))

bot.run('NzcxNzEzNTAxMjE5NjUxNTg1.X5wINA.j20KROPEM7aJbasziCxJ_HYF_FE')