import discord
from discord.ext import commands
import os


PR = '.' #Префикс
bad_words = open( 'bad_words.txt', 'r' ).readline()

client = commands.Bot(command_prefix = PR)

@client.event
async def on_ready():
	print('Bot CONNECTED')
	channel = client.get_channel(704104096029868038)
	await client.change_presence( status = discord.Status.online, activity = discord.Game('обновление функцыонала!'))
	await channel.send('@everyone Бот в онлайне, теперь все команды работают')


#Убрать сообщения
@client.command(pass_context = True )
async def очистка(ctx, amount = 100):
	#Очишение чата
	channel = client.get_channel(710579006533009460)
	#Команда для инфо-модеров
	if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
		if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
			await ctx.channel.purge(limit = amount)
	#Команда для админов
	if 704098951002980383 in [y.id for y in ctx.author.roles] or 718059665899913238 in [y.id for y in ctx.author.roles] or 704300807331250307 in [y.id for y in ctx.author.roles] or 711267556937433149 in [y.id for y in ctx.author.roles]: #1 - админ, 2 - разраб, 3 - можер, 4 - зам админ
		await ctx.channel.purge(limit = amount + 1)
	

#Кик
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)
async def кик(ctx, member: discord.Member, *, reason):
	print ('команда прописана')
	channel = client.get_channel(710579006533009460)
	emb = discord.Embed( title = 'Кик',colour = discord.Color.red())
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	# await member.kick(reason = reason)

	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	emb.add_field(name = f'Был кикнут по причине {reason}', value = member.mention)
	await channel.send(embed = emb)


#Бан
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)
async def бан(ctx, member: discord.Member,*, reason = ""):
	channel = client.get_channel(710579006533009460)
	emb = discord.Embed( title = 'Бан',colour = discord.Color.red())
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	# await member.ban(reason = reason)

	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	emb.add_field(name = f'Был забанен по причине {reason}', value = member.mention)
	await channel.send(embed = emb)

#Разбан
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)
async def разбан(ctx,*,member):
	channel = client.get_channel(710579006533009460)
	emb = discord.Embed( title = 'Разбан',colour = discord.Color.green())
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	ban_user = await ctx.guild.bans()
	#Unban
	for ban_entry in ban_user:
		user = ban_entry.user

		await ctx.guild.unban(user)
		emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
		emb.add_field(name = 'Был разбанен', value = member.mention)
		await channel.send(embed = emb)
		return


#Размут
@client.command(pass_context = True )
async def размут(ctx, member: discord.Member):
	channel = client.get_channel(710579006533009460)
	if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
		if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
			print('a')
			emb = discord.Embed( title = 'Размут',colour = discord.Color.green())
			#Удаление сообщения
			await ctx.channel.purge(limit = 1)
			mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
			await member.remove_roles(mute_role)
			emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
			emb.add_field(name = '''Был размучен''', value = member.mention)
			await channel.send(embed = emb)
	else:
		print('b')
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
	#Команда для админов
	if 704098951002980383 in [y.id for y in ctx.author.roles] or 718059665899913238 in [y.id for y in ctx.author.roles] or 704300807331250307 in [y.id for y in ctx.author.roles] or 711267556937433149 in [y.id for y in ctx.author.roles]: #1 - админ, 2 - разраб, 3 - можер, 4 - зам админ
		print('c')
		emb = discord.Embed( title = 'Размут',colour = discord.Color.green())
		#Удаление сообщения
		await ctx.channel.purge(limit = 1)
		mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
		await member.remove_roles(mute_role)
		emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
		emb.add_field(name = '''Был размучен''', value = member.mention)
		await channel.send(embed = emb)
		print('h')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')

# Мут
@client.command(pass_context = True )
async def мут(ctx, member: discord.Member, *reason):
	channel = client.get_channel(710579006533009460)
	# Команда для инфо-модеров
	if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
		if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
			emb = discord.Embed( title = 'Мут',colour = discord.Color.red())
			#Удаление сообщения
			await ctx.channel.purge(limit = 1)
			mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
			await member.add_roles(mute_role)
			emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
			emb.add_field(name = f'Был замьючен по причине: {" ".join(reason)}', value = member.mention)
			await channel.send(embed = emb)
		else:
			await ctx.channel.purge(limit = 1)
			await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')

	#Команда для админов
	if 704098951002980383 in [y.id for y in ctx.author.roles] or 718059665899913238 in [y.id for y in ctx.author.roles] or 704300807331250307 in [y.id for y in ctx.author.roles] or 711267556937433149 in [y.id for y in ctx.author.roles]: #1 - админ, 2 - разраб, 3 - можер, 4 - зам админ
		print('ее написал админ')
		emb = discord.Embed( title = 'Мут',colour = discord.Color.red())
		#Удаление сообщения
		await ctx.channel.purge(limit = 1)
		mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
		await member.add_roles(mute_role)
		emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
		emb.add_field(name = f'''Был замьючен по причине: {" ".join(reason)}''', value = member.mention)
		await channel.send(embed = emb)
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


#Жалоба
@client.command(pass_context = True )
async def жалоба(ctx, member: discord.Member, *reason):
	#Канал для огласки нарушений
	channel = client.get_channel(718195637627125962)
	#Удаление сообщения
	await channel.send(f'Пользователь {ctx.author.mention} пожаловался на {member.mention}, по причине: {" ".join(reason)}. Сылка на сообщение (просто кликните): https://discordapp.com/channels/678327101031579735/{ctx.message.channel.id}/{ctx.message.id}')
	


#Заявка
@client.command(pass_context = True )
async def заявка(ctx, *reason):
	#Чат для проверки
	channel = client.get_channel(709335990644506624)
	if ctx.channel.id == 707672283732508673:
		await ctx.channel.purge(limit = 1)
		await ctx.author.send(f'Твоя заявка в сообщество SBW была принита!')
		await channel.send(f'Пользователь {ctx.author.mention} подал заявку на вступление в клан. Эго контент: {" ".join(reason)}.')


#Тестирование
@client.command(pass_context = True )
async def проходит(ctx, member: discord.Member):
	channel = client.get_channel(709368859542421504) #Канал для оповешений про учасников
	channel_test = client.get_channel(709335990644506624) #канал проверка
	if 709336731916173382 in [y.id for y in ctx.author.roles]: #Если ето тестер
		await member.add_roles(discord.utils.get(member.guild.roles, id = 707676867234103427))
		await member.remove_roles(discord.utils.get(member.guild.roles, id = 704254142264377415))
		await ctx.channel.purge(limit = 1)
		await member.send('Поздравляю, ты прошол в наш клан!')
		await channel.send(f'{member.mention} проходит в клан. Поздравим его!')
		await channel_test.send(f'{member.mention} проходит')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду') 

@client.command(pass_context = True )
async def непроходит(ctx, member: discord.Member):
	channel_test = client.get_channel(709335990644506624)
	if 709336731916173382 in [y.id for y in ctx.author.roles]: #Если ето тестер
		await ctx.channel.purge(limit = 1)
		await member.send('К сожелению, ты не прошол етап тестирования')
		await channel_test.send(f'{member.mention} непроходит')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.senddd(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')

@client.command(pass_context = True )
async def тестирую(ctx, member: discord.Member, *reason):
	channel = client.get_channel(709335990644506624) #Чат проверка
	if 709336731916173382 in [y.id for y in ctx.author.roles]: #Если ето тестер
		await ctx.channel.purge(limit = 1)
		#Кидает сообщение в лс проверечнику
		await member.send(f"""Поздравляю! Твою завку в сообщество SBW принял тестер {ctx.author.mention}, пожалуста проверь в фортнайте заявку в друзья от: {" ".join(reason)} . Тестер сыграет с тобой в 10 раундов бокс файтов(из низ 4 разминочных) и 6 билд файтов(из низ 2 разминочных). Если тестер во время проверки будет както токсить(обзывать и т.д) напиши на него жалобу.""")
		await channel.send(f'{ctx.author.mention} Проверяет {member.mention}')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду') 
	




@client.command(pass_context = True )
async def ютуб(ctx):
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	emb = discord.Embed( title = 'Нажми на меня для перехода на наш офицальный ютуб канал', description = 'Это наш офицальный канал где мы будем выставлять инфу и вашы топ моменты, нашего клана',colour = discord.Color.green(), url = 'https://www.youtube.com/channel/UC1S3iEfqkZeXNA3FI1mPUKw')
	#Аватар бота
	#emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)

	#Аватар пользователя
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)

	#Фотка под всем текстом
	#emb.set_image(url = 'https://image.freepik.com/free-vector/_56473-306.jpg')

	#Сылка на канал с тексте 'title'
	emb.set_thumbnail(url = 'https://yt3.ggpht.com/a/AATXAJxmcKQKHfTUCmPOxcKmKE8rUq_vxvq4BUDcXA=s100-c-k-c0xffffffff-no-rj-mo')

	await ctx.send(embed = emb)

@client.command(pass_context = True )
async def патреон(ctx):
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	emb = discord.Embed( title = 'Нажми на меня для перехода на наш патреон(платформа для спонсорства)', description = 'Это наш патреон. Здесь вы можете пожертвовать деньгу, чтобы стать спонсорм, или же просто помочь нам в развитии',colour = discord.Color.green(), url = 'https://www.patreon.com/SBWp')
	#Аватар пользователя
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)

	#Фотка под всем текстом
	#emb.set_image(url = 'https://image.freepik.com/free-vector/_56473-306.jpg')

	#Сылка на канал с тексте 'title'
	emb.set_thumbnail(url = 'https://yt3.ggpht.com/a/AATXAJxmcKQKHfTUCmPOxcKmKE8rUq_vxvq4BUDcXA=s100-c-k-c0xffffffff-no-rj-mo')

	await ctx.send(embed = emb)




#Авто роль
@client.event
async def on_member_join(member):
	channel = client.get_channel(710579006533009460)

	role = discord.utils.get(member.guild.roles, id = 704254142264377415)
	await member.add_roles(role)
	await member.send(f'{member.name} привет зашёл в наш клан SBW (Squad Black Wolves). Но ты еще не являешься полноценным участником клана. Чтобы стать им, тебе потребуется: зайди на наш дискорд канал -> зайти в раздел "Чат для не официалов" -> зайти в чат "заявки в клан" -> написать заявку. Вид заявки: .заявка(ето команда) количество своего птс ник в фортнайт (Все пробелы кроме первого: .заявка слово, надо заменять на .. иначе твое сообщение будет неполное). Пример: .заявка 9999..NikFortnite' )


@client.event
async def on_message( message ):
	await client.process_commands( message )

	channel = client.get_channel(713769252523475055)
	for word in message.content.split():
		if word.lower() in bad_words:
			await message.delete()
			await message.author.send(f"{message.author.name} не надо так писать")
		else:
			pass

	#Удаление спама в заявках
	if message.channel.id == 707672283732508673: #Проверка канала
		if 704254142264377415 in [y.id for y in message.author.roles]: #Проверка роли
			if '.заявка' in message.content:
				print('была написана заявка')
				
			else:
				await message.channel.purge(limit = 1)
	#Удаление спама в заявках на сбв турнир
	if message.channel.id == 718473326867251211: #Проверка канала 

		if 'заявка' in message.content:
			pass
				
		else:
			await message.channel.purge(limit = 1)


#Команда для выдачи роли инфо-модера
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def give_mod(ctx, member: discord.Member):
	channel = client.get_channel(709368859542421504)
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	info_moder = discord.utils.get(member.guild.roles, id = 709488247419568129)

	await member.add_roles(info_moder)

	await channel.send((f'{member.mention} Становиться инфо-модером на обучении'))

#Команда для выдачи роли тестера
@client.command(pass_context = True )
@commands.has_permissions(administrator = True)
async def give_test(ctx, member: discord.Member):
	channel = client.get_channel(709368859542421504)
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	tester = discord.utils.get(member.guild.roles, id = 710080851517636678)

	await member.add_roles(tester)

	await channel.send((f'{member.mention} Становиться тестером на обучении'))

#Пример ембти с сылкой на ютуб
@client.command(pass_context = True )
async def embmaket(ctx):
	#Удаление сообщения
	await ctx.channel.purge(limit = 1)

	emb = discord.Embed( title = 'Гыг', description = 'Описание гыг',colour = discord.Color.green(), url = 'https://discordpy.readthedocs.io/en/latest/api.html#clientuser')

	emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url)
	#emb.set_image(url = 'https://image.freepik.com/free-vector/_56473-306.jpg')
	emb.set_thumbnail(url = 'https://yt3.ggpht.com/a/AATXAJxmcKQKHfTUCmPOxcKmKE8rUq_vxvq4BUDcXA=s100-c-k-c0xffffffff-no-rj-mo')

	await ctx.send(embed = emb)


token = os.environ.get('BOT_TOKEN')
#token = open( 'token.txt', 'r' ).readline()
client.run(token)
