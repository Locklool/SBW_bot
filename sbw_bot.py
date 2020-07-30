# -*- coding: utf8 -*-
import discord
from discord.ext import commands
<<<<<<< HEAD:SBW_bot.py
import sqlite3
import os
#Переменые sqlite3
connection = sqlite3.connect('server.db')
cursor = connection.cursor()


PR = '.' #Префикс
bad_words = open( 'bad_words.txt', 'r' ).readline()

client = commands.Bot(command_prefix = PR)

class DisId:
	ModLogID = 710579006533009460
	AdminID = 711267556937433149
	MainModerID = 724076828834136194
	ButowkaID = 704098951002980383
	MuteRoleID = 710578166413918220
	ModerChatID = 738443813067948083
	DontOficialRoleID = 704254142264377415
	AnketaChatID = 707672283732508673
	AnketaTesterChatID = 724222902182084688
	AlertsChatID = 738453663827361895
	TesterRoleID = 709336731916173382
	OficialRoleID = 707676867234103427


=======
import os
import sys


PR = '.' #Префикс
bad_words = ["Блять","Сука"]

client = commands.Bot(command_prefix = PR)

>>>>>>> origin/master:sbw_bot.py
@client.event
async def on_ready():
	print('Bot CONNECTED')
	channel = client.get_channel(704104096029868038)
<<<<<<< HEAD:SBW_bot.py
	await client.change_presence( status = discord.Status.online, activity = discord.Game('Create by Unlocklook: v0.9'))
	# await channel.send('@everyone Бот в онлайне, теперь все команды работают')
=======
	await client.change_presence( status = discord.Status.online, activity = discord.Game('обновление функцыонала!'))
	await channel.send('@everyone Бот в онлайне, теперь все команды работают')

>>>>>>> origin/master:sbw_bot.py

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
	channel = client.get_channel(DisId.Mod_logID)
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
async def бан(ctx, member: discord.Member,*, reason):
	channel = client.get_channel(DisId.Mod_logID)
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
<<<<<<< HEAD:SBW_bot.py
	channel = client.get_channel(DisId.ModLogID)
	# if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
	# 	if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
	# 		emb = discord.Embed( title = 'Размут',colour = discord.Color.green())
	# 		#Удаление сообщения
	# 		await ctx.channel.purge(limit = 1)
	# 		mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
	# 		await member.remove_roles(mute_role)
	# 		emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
	# 		emb.add_field(name = '''Был размучен''', value = member.mention)
	# 		await channel.send(embed = emb)
	# else:
	# 	await ctx.channel.purge(limit = 1)
	# 	await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
	#Команда для админов
	if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.ButowkaID in [y.id for y in ctx.author.roles] or DisId.MainModerID in [y.id for y in ctx.author.roles]:
=======
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
>>>>>>> origin/master:sbw_bot.py
		emb = discord.Embed( title = 'Размут',colour = discord.Color.green())
		#Удаление сообщения
		await ctx.channel.purge(limit = 1)
		mute_role = discord.utils.get(member.guild.roles, id = DisId.MuteRoleID)
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
<<<<<<< HEAD:SBW_bot.py
async def мут(ctx, member: discord.Member = None, *reason):
	channel = client.get_channel(DisId.ModLogID)
	if member is not None:
		# # Команда для инфо-модеров
		# if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
		# 	if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
		# 		emb = discord.Embed( title = 'Мут',colour = discord.Color.red())
		# 		#Удаление сообщения
		# 		await ctx.channel.purge(limit = 1)
		# 		mute_role = discord.utils.get(member.guild.roles, id = 710578166413918220)
		# 		await member.add_roles(mute_role)
			# 		emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
		# 		emb.add_field(name = f'Был замьючен по причине: {" ".join(reason)}', value = member.mention)
		# 		await channel.send(embed = emb)
		# 	else:
		# 		await ctx.channel.purge(limit = 1)
		# 		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
		# else:
		# 	await ctx.channel.purge(limit = 1)
		# 	await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')

		#Команда для админов
		if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.MainModerID in [y.id for y in ctx.author.roles] or DisId.ButowkaID in [y.id for y in ctx.author.roles]:
=======
async def мут(ctx, member: discord.Member, *reason):
	channel = client.get_channel(710579006533009460)
	# Команда для инфо-модеров
	if ctx.channel.id == 704108242493767800: #Вопрос где производиласть команда?
		if 709489069528186900 in [y.id for y in ctx.author.roles]: #Вопрос кто воизпроводил команду?
>>>>>>> origin/master:sbw_bot.py
			emb = discord.Embed( title = 'Мут',colour = discord.Color.red())
			#Удаление сообщения
			await ctx.channel.purge(limit = 1)
			mute_role = discord.utils.get(member.guild.roles, id = DisId.MuteRoleID)
			await member.add_roles(mute_role)
			emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
<<<<<<< HEAD:SBW_bot.py
			emb.add_field(name = f'''Был замьючен по причине: {" ".join(reason)}''', value = member.mention)
=======
			emb.add_field(name = f'Был замьючен по причине: {" ".join(reason)}', value = member.mention)
>>>>>>> origin/master:sbw_bot.py
			await channel.send(embed = emb)
		else:
			await ctx.channel.purge(limit = 1)
			await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
	else:
<<<<<<< HEAD:SBW_bot.py
		await ctx.send(f"{ctx.author.mention} Пожалуста напишите имя пользователя.")
=======
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

>>>>>>> origin/master:sbw_bot.py

#Жалоба
@client.command(pass_context = True )
<<<<<<< HEAD:SBW_bot.py
async def жалоба(ctx, member: discord.Member = None, *reason):
=======
async def жалоба(ctx, member: discord.Member, *reason):
>>>>>>> origin/master:sbw_bot.py
	#Канал для огласки нарушений
	channel = client.get_channel(DisId.ModerChatID)
	#Удаление сообщения
<<<<<<< HEAD:SBW_bot.py
	if member is None:
		await ctx.send(f"{ctx.author.mention} Напишите имя игрока, и причину. Жалоба без причины - мут на 10 мин")
	else:
		await ctx.send(f"{ctx.author.mention} Ваша жалоба была успешно отправлена на расмотрение.")
		await channel.send(f'Пользователь {ctx.author.mention} пожаловался на {member.mention}, по причине: {" ".join(reason)}. Сылка на сообщение (просто кликните): https://discordapp.com/channels/678327101031579735/{ctx.message.channel.id}/{ctx.message.id}')
=======
	await channel.send(f'Пользователь {ctx.author.mention} пожаловался на {member.mention}, по причине: {" ".join(reason)}. Сылка на сообщение (просто кликните): https://discordapp.com/channels/678327101031579735/{ctx.message.channel.id}/{ctx.message.id}')
>>>>>>> origin/master:sbw_bot.py
	


#Заявка
@client.command(pass_context = True )
async def заявка(ctx, *reason):
	#Чат для проверки
	channel = client.get_channel(DisId.AnketaTesterChatID)
	if ctx.channel.id == DisId.AnketaChatID:
		await ctx.channel.purge(limit = 1)
		await ctx.author.send(f'Твоя заявка в сообщество SBW была принита!')
		await channel.send(f'Пользователь {ctx.author.mention} подал заявку на вступление в клан. Эго контент: {" ".join(reason)}.')


#Тестирование
@client.command(pass_context = True )
async def проходит(ctx, member: discord.Member):
	channel = client.get_channel(DisId.AlertsChatID) #Канал для оповешений про учасников
	channel_test = client.get_channel(DisId.AnketaTesterChatID) #канал проверка
	if DisId.TesterRoleID in [y.id for y in ctx.author.roles]: #Если ето тестер
		await member.add_roles(discord.utils.get(member.guild.roles, id = DisId.OficialRoleID))
		await member.remove_roles(discord.utils.get(member.guild.roles, id = DisId.DontOficialRoleID))
		await ctx.channel.purge(limit = 1)
		await member.send('Поздравляю, ты прошол в наш клан!')
		await channel.send(f'{member.mention} проходит в клан. Поздравим его!')
		await channel_test.send(f'{member.mention} проходит.')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


@client.command(pass_context = True )
async def непроходит(ctx, member: discord.Member):
	channel = client.get_channel(DisId.AlertsChatID) #Канал для оповешений про учасников
	channel_test = client.get_channel(DisId.AnketaTesterChatID) #канал проверка
	if DisId.TesterRoleID in [y.id for y in ctx.author.roles]: #Если ето тестер
		await ctx.channel.purge(limit = 1)
		await member.send("Cожелею, но ты не прошол к нам в клан, завтра можешь еще раз подать заявку чтобы тебя протестили.")
		await channel_test.send(f'{member.mention} не прошол.')
	else:
		await ctx.channel.purge(limit = 1)
		await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')

@client.command(pass_context = True )
async def тестирую(ctx, member: discord.Member, *reason):
<<<<<<< HEAD:SBW_bot.py
	channel = client.get_channel(DisId.AnketaTesterChatID) #Чат проверка
	if DisId.TesterRoleID in [y.id for y in ctx.author.roles]: #Если ето тестер
=======
	channel = client.get_channel(709335990644506624) #Чат проверка
	if 709336731916173382 in [y.id for y in ctx.author.roles]: #Если ето тестер
>>>>>>> origin/master:sbw_bot.py
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
	channel = client.get_channel(DisId.ModLogID)

	role = discord.utils.get(member.guild.roles, id = DisId.DontOficialRoleID)
	await member.add_roles(role)
	await member.send(f'{member.name} Приветствуем тебя в нашей волчей стае, надеемся что тебе тут понравиться.\n Наши правила:\n 1. Оскорбление (пред) Не уважение. Ты (пред)\n 2. Провокация (мут)\n 3. Токсичность (бан)\n 4. любой СПАМ (мут)\n 5. 18+ контент, скример, шок (бан)\n 6. Символы в начале ника (пред)\n 7. Обмен и продажа (бан)\n 8. Реклама, пиар(бан)\n 9. Выпрашивание ролей у администрации (мут) или (пред)\n 10. Переусердствовать с матом (пред)\n 11. Обсуждение действий модерации (мут) или (пред)\n 12. Попрошайничество (мут)\n 13. Спор (мут) или (пред)\n Также тебе понадобиться написать заявку чтобы получить место в нашем клане. Подробней в чате для заявок.')

	await channel.send(f"Добро пожаловать в стаю - {member.name}")


@client.event
async def on_message( message ):
	await client.process_commands( message )

	channel = client.get_channel(713769252523475055)
<<<<<<< HEAD:SBW_bot.py
	# for word in message.content.split():
	# 	if word.lower() in bad_words:
	# 		await message.delete()
	# 		await message.author.send(f"{message.author.name} не надо так писать")
	# 	else:
	# 		pass
=======
	for word in message.content.split():
		if word.lower() in bad_words:
			await message.delete()
			await message.author.send(f"{message.author.name} не надо так писать")
		else:
			pass
>>>>>>> origin/master:sbw_bot.py

	#Удаление спама в заявках
	if message.channel.id == DisId.AnketaChatID: #Проверка канала
		if DisId.DontOficialRoleID in [y.id for y in message.author.roles]: #Проверка роли
			if '.заявка' in message.content:
				pass
			else:
				await message.channel.purge(limit = 1)
<<<<<<< HEAD:SBW_bot.py
=======
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
>>>>>>> origin/master:sbw_bot.py




# token = os.environ.get('BOT_TOKEN')
token = ("NzA5MTQ2MTUyMTI1MjAyNDMy.Xrhp0Q.5HjNOb4o9u7MZ6vi-hBUiCSdY_E")
client.run(token)