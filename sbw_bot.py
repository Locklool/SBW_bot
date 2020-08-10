# -*- coding: utf8 -*-
import discord
from discord.ext import commands
import sqlite3
import random
from random import randint
import os

# Переменые sqlite3
connection = sqlite3.connect('server.db')
cursor = connection.cursor()

PR = '.'  # Префикс
bad_words = open('bad_words.txt', 'r').readline()

client = commands.Bot(command_prefix=PR)


def give_exp_users(exp_count, user_id):
    cursor.execute(f"""UPDATE users SET exp = exp + "{exp_count}" WHERE id = {user_id.id}""")
    connection.commit()


def check_lvl(user_id):
    if cursor.execute(f"""SELECT exp FROM users WHERE id = {user_id.id}""").fetchone()[0] >= 2000:
        print(f"ранг 1 у {cursor.execute(f'SELECT name FROM users WHERE id = {user_id.id}').fetchone()[0]}")
    else:
        print("все ще ранг 1")


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


def RangsEMJ():
    NOranked = client.get_emoji(740152519497613393)
    Rang1 = client.get_emoji(740152519845478481)
    Rang2 = client.get_emoji(740152519996604476)
    Rang3 = client.get_emoji(740152520223096914)
    return NOranked, Rang1, Rang2, Rang3


@client.event
async def on_ready():
    print('Bot CONNECTED')
    channel = client.get_channel(704104096029868038)
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Create by Unlocklook: v0.9'))
    # await channel.send('Бот в онлайне, теперь все команды работают')

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
		name TEXT,
		id INT,
		FUsername TEXT,
		mute INT,
		exp BIGINT,
		warns INT,
		rangs INT
	)""")
    for guild in client.guilds:
        for member in guild.members:
            if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                cursor.execute(f"INSERT INTO users VALUES ('{member.name}','{member.id}', 'Не указано',0,0,0,0) ")

    connection.commit()


@client.command(pass_context=True)
async def info(ctx, member: discord.Member):
    await ctx.send(f"""
Имя {cursor.execute(f" SELECT name FROM users WHERE id = {member.id}").fetchone()[0]}, 
id {cursor.execute(f" SELECT id FROM users WHERE id = {member.id}").fetchone()[0]}, 
Фортнайт ник {cursor.execute(f" SELECT FUsername FROM users WHERE id = {member.id}").fetchone()[0]}, 
Мут? {cursor.execute(f" SELECT mute FROM users WHERE id = {member.id}").fetchone()[0]}, 
Опыт {cursor.execute(f" SELECT exp FROM users WHERE id = {member.id}").fetchone()[0]},
Варны {cursor.execute(f" SELECT warns FROM users WHERE id = {member.id}").fetchone()[0]},
Ранг {cursor.execute(f" SELECT rangs FROM users WHERE id = {member.id}").fetchone()[0]}""")


# Убрать сообщения
@client.command(aliases=["очитска", "cle", "clear"])
async def __clear(ctx, amount=100):
    # Команда для админов
    if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.ButowkaID in [y.id for y in
                                                                                ctx.author.roles] or DisId.MainModerID in [
        y.id for y in ctx.author.roles]:
        await ctx.channel.purge(limit=amount + 1)


# Кик
@client.command(aliases=["kik", "кик"])
@commands.has_permissions(administrator=True)
async def __kik(ctx, member: discord.Member, *, reason):
    print('команда прописана')
    channel = client.get_channel(DisId.Mod_logID)
    emb = discord.Embed(title='Кик', colour=discord.Color.red())
    # Удаление сообщения
    await ctx.channel.purge(limit=1)

    # await member.kick(reason = reason)

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.add_field(name=f'Был кикнут по причине {reason}', value=member.mention)
    await channel.send(embed=emb)


# Бан
@client.command(aliases=["бан", "ban", "забанить"])
@commands.has_permissions(administrator=True)
async def __ban(ctx, member: discord.Member, *, reason):
    channel = client.get_channel(DisId.Mod_logID)
    emb = discord.Embed(title='Бан', colour=discord.Color.red())
    # Удаление сообщения
    await ctx.channel.purge(limit=1)

    # await member.ban(reason = reason)

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.add_field(name=f'Был забанен по причине {reason}', value=member.mention)
    await channel.send(embed=emb)


# Разбан
@client.command(aliases=["разбан", "разбанить", "unban"])
@commands.has_permissions(administrator=True)
async def __unban(ctx, *, member):
    channel = client.get_channel(710579006533009460)
    emb = discord.Embed(title='Разбан', colour=discord.Color.green())
    # Удаление сообщения
    await ctx.channel.purge(limit=1)

    ban_user = await ctx.guild.bans()
    # Unban
    for ban_entry in ban_user:
        user = ban_entry.user

        await ctx.guild.unban(user)
        emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        emb.add_field(name='Был разбанен', value=member.mention)
        await channel.send(embed=emb)
        return


# Размут
@client.command(aliases=["размут", "unmute"])
async def __unmute(ctx, member: discord.Member):
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
    # Команда для админов
    if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.ButowkaID in [y.id for y in
                                                                                ctx.author.roles] or DisId.MainModerID in [
        y.id for y in ctx.author.roles]:
        emb = discord.Embed(title='Размут', colour=discord.Color.green())
        # Удаление сообщения
        await ctx.channel.purge(limit=1)
        mute_role = discord.utils.get(member.guild.roles, id=DisId.MuteRoleID)
        await member.remove_roles(mute_role)
        emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        emb.add_field(name='''Был размучен''', value=member.mention)
        await channel.send(embed=emb)
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


# Мут
@client.command(aliases=["мут", "mute"])
async def __mute(ctx, member: discord.Member = None, *reason):
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

        # Команда для админов
        if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.MainModerID in [y.id for y in
                                                                                      ctx.author.roles] or DisId.ButowkaID in [
            y.id for y in ctx.author.roles]:
            emb = discord.Embed(title='Мут', colour=discord.Color.red())
            # Удаление сообщения
            await ctx.channel.purge(limit=1)
            mute_role = discord.utils.get(member.guild.roles, id=DisId.MuteRoleID)
            await member.add_roles(mute_role)
            emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
            emb.add_field(name=f'''Был замьючен по причине: {" ".join(reason)}''', value=member.mention)
            await channel.send(embed=emb)
        else:
            await ctx.channel.purge(limit=1)
            await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')
    else:
        await ctx.send(f"{ctx.author.mention} Пожалуста напишите имя пользователя.")


# Жалоба
@client.command(aliases=["жалоба", "complaint"])
async def __complaint(ctx, member: discord.Member = None, *reason):
    # Канал для огласки нарушений
    channel = client.get_channel(DisId.ModerChatID)
    # Удаление сообщения
    if member is None:
        await ctx.send(f"{ctx.author.mention} Напишите имя игрока, и причину. Жалоба без причины - мут на 10 мин")
    else:
        await ctx.send(f"{ctx.author.mention} Ваша жалоба была успешно отправлена на расмотрение.")
        await channel.send(
            f'Пользователь {ctx.author.mention} пожаловался на {member.mention}, по причине: {" ".join(reason)}. Сылка на сообщение (просто кликните): https://discordapp.com/channels/678327101031579735/{ctx.message.channel.id}/{ctx.message.id}')


# Заявка
@client.command(aliases=["заявка", "request"])
async def __request(ctx, *reason):
    # Чат для проверки
    channel = client.get_channel(DisId.AnketaTesterChatID)
    if ctx.channel.id == DisId.AnketaChatID:
        await ctx.channel.purge(limit=1)
        await ctx.author.send(f'Твоя заявка в сообщество SBW была принита!')
        await channel.send(
            f'Пользователь {ctx.author.mention} подал заявку на вступление в клан. Эго контент: {" ".join(reason)}.')


# Тестирование
@client.command(aliases=["проходит", "passes"])
async def __passes(ctx, member: discord.Member):
    channel = client.get_channel(DisId.AlertsChatID)  # Канал для оповешений про учасников
    channel_test = client.get_channel(DisId.AnketaTesterChatID)  # канал проверка
    if DisId.TesterRoleID in [y.id for y in ctx.author.roles]:  # Если ето тестер
        await member.add_roles(discord.utils.get(member.guild.roles, id=DisId.OficialRoleID))
        await member.remove_roles(discord.utils.get(member.guild.roles, id=DisId.DontOficialRoleID))
        await ctx.channel.purge(limit=1)
        await member.send('Поздравляю, ты прошол в наш клан!')
        await channel.send(f'{member.mention} проходит в клан. Поздравим его!')
        await channel_test.send(f'{member.mention} проходит.')
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


@client.command(aliases=["непроходит", "notpasses"])
async def __dontpasses(ctx, member: discord.Member):
    channel = client.get_channel(DisId.AlertsChatID)  # Канал для оповешений про учасников
    channel_test = client.get_channel(DisId.AnketaTesterChatID)  # канал проверка
    if DisId.TesterRoleID in [y.id for y in ctx.author.roles]:  # Если ето тестер
        await ctx.channel.purge(limit=1)
        await member.send(
            "Cожелею, но ты не прошол к нам в клан, завтра можешь еще раз подать заявку чтобы тебя протестили.")
        await channel_test.send(f'{member.mention} не прошол.')
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


@client.command(aliases=["тестурую", "test"])
async def __test(ctx, member: discord.Member, *reason):
    channel = client.get_channel(DisId.AnketaTesterChatID)  # Чат проверка
    if DisId.TesterRoleID in [y.id for y in ctx.author.roles]:  # Если ето тестер
        await ctx.channel.purge(limit=1)
        # Кидает сообщение в лс проверечнику
        await member.send(
            f"""Поздравляю! Твою завку в сообщество SBW принял тестер {ctx.author.mention}, пожалуста проверь в фортнайте заявку в друзья от: {" ".join(reason)} . Тестер сыграет с тобой в 10 раундов бокс файтов(из низ 4 разминочных) и 6 билд файтов(из низ 2 разминочных). Если тестер во время проверки будет както токсить(обзывать и т.д) напиши на него жалобу.""")
        await channel.send(f'{ctx.author.mention} Проверяет {member.mention}')
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{ctx.author.mention} Вы не имеете право изпользовать эту команду')


@client.command(pass_context=True)
async def rexp(ctx, member: discord.Member, count, type="+", type_var="exp"):
    if DisId.AdminID in [y.id for y in ctx.author.roles]:
        print("hhh")
        if "exp" in type_var:
            print("ffsfefefew")
            if type is "+":
                give_exp_users(count, member)
                await ctx.send(f"Вы успешно дали {''.join(count)} опыта")
            elif type is "-":
                cursor.execute(f"""UPDATE users SET exp = exp - "{count}" WHERE id = {member.id}""")
                await ctx.send(f"Вы успешно отняли {''.join(count)} опыта")
        elif "rangs" in type_var:
            print("c")
            if type is "+":
                print("b")
                cursor.execute(f"""UPDATE users SET rangs = rangs + "{count}" WHERE id = {member.id}""")
                await ctx.send(f"Вы успешно дали ранг {''.join(count)}")
            elif type is "-":
                print("x")
                cursor.execute(f"""UPDATE users SET rangs = rangs - "{count}" WHERE id = {member.id}""")
                await ctx.send(f"Вы успешно отняли ранг {''.join(count)}")

    else:
        await ctx.send("мам родная")


@client.command(aliases=["ютуб", "youtube"])
async def __youtube(ctx):
    # Удаление сообщения
    await ctx.channel.purge(limit=1)

    emb = discord.Embed(title='Нажми на меня для перехода на наш офицальный ютуб канал',
                        description='Это наш офицальный канал где мы будем выставлять инфу и вашы топ моменты, нашего клана',
                        colour=discord.Color.green(), url='https://www.youtube.com/channel/UC1S3iEfqkZeXNA3FI1mPUKw')
    # Аватар бота
    # emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)

    # Аватар пользователя
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

    # Фотка под всем текстом
    # emb.set_image(url = 'https://image.freepik.com/free-vector/_56473-306.jpg')

    # Сылка на канал с тексте 'title'
    emb.set_thumbnail(
        url='https://yt3.ggpht.com/a/AATXAJxmcKQKHfTUCmPOxcKmKE8rUq_vxvq4BUDcXA=s100-c-k-c0xffffffff-no-rj-mo')

    await ctx.send(embed=emb)


@client.command(aliases=["патреон", "patreon"])
async def __patreon(ctx):
    # Удаление сообщения
    await ctx.channel.purge(limit=1)

    emb = discord.Embed(title='Нажми на меня для перехода на наш патреон(платформа для спонсорства)',
                        description='Это наш патреон. Здесь вы можете пожертвовать деньгу, чтобы стать спонсорм, или же просто помочь нам в развитии',
                        colour=discord.Color.green(), url='https://www.patreon.com/SBWp')
    # Аватар пользователя
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

    # Фотка под всем текстом
    # emb.set_image(url = 'https://image.freepik.com/free-vector/_56473-306.jpg')

    # Сылка на канал с тексте 'title'
    emb.set_thumbnail(
        url='https://yt3.ggpht.com/a/AATXAJxmcKQKHfTUCmPOxcKmKE8rUq_vxvq4BUDcXA=s100-c-k-c0xffffffff-no-rj-mo')

    await ctx.send(embed=emb)


# Авто роль
@client.event
async def on_member_join(member):
    channel = client.get_channel(DisId.ModLogID)

    role = discord.utils.get(member.guild.roles, id=DisId.DontOficialRoleID)
    await member.add_roles(role)
    await member.send(
        f'{member.name} Приветствуем тебя в нашей волчей стае, надеемся что тебе тут понравиться.\n Наши правила:\n 1. Оскорбление (пред) Не уважение. Ты (пред)\n 2. Провокация (мут)\n 3. Токсичность (бан)\n 4. любой СПАМ (мут)\n 5. 18+ контент, скример, шок (бан)\n 6. Символы в начале ника (пред)\n 7. Обмен и продажа (бан)\n 8. Реклама, пиар(бан)\n 9. Выпрашивание ролей у администрации (мут) или (пред)\n 10. Переусердствовать с матом (пред)\n 11. Обсуждение действий модерации (мут) или (пред)\n 12. Попрошайничество (мут)\n 13. Спор (мут) или (пред)\n Также тебе понадобиться написать заявку чтобы получить место в нашем клане. Подробней в чате для заявок.')

    await channel.send(f"Добро пожаловать в стаю - {member.name}")


@client.event
async def on_message(message):
    await client.process_commands(message)

    NOrankedEM, Rang1EM, Rang2EM, Rang3EM = RangsEMJ()
    message_conx = message.content.split()

    channel = client.get_channel(713769252523475055)
    # for word in message.content.split():
    # 	if word.lower() in bad_words:
    # 		await message.delete()
    # 		await message.author.send(f"{message.author.name} не надо так писать")
    # 	else:
    # 		pass

    # print(message_conx)

    # Давайние опыта за слово
    for word in message_conx:
        exp_give = randint(1, 3)
        give_exp_users(exp_give, message.author)

    check_lvl(message.author)

    # Проверка уровня
    if cursor.execute(f"""SELECT rangs FROM users WHERE id = {message.author.id}""").fetchone()[0] == 0 and \
            cursor.execute(f"""SELECT exp FROM users WHERE id = {message.author.id}""").fetchone()[0] == 0:
        await message.channel.send(f"{message.author.mention} Сейчас ты без ранга. {NOrankedEM}")
        print(NOrankedEM)
    if cursor.execute(f"""SELECT rangs FROM users WHERE id = {message.author.id}""").fetchone()[0] == 0 and \
            cursor.execute(f"""SELECT exp FROM users WHERE id = {message.author.id}""").fetchone()[0] >= 3000:
        cursor.execute(f"""UPDATE users SET rangs = 1 WHERE id = {message.author.id}""")
        cursor.execute(f"""UPDATE users SET exp = 0 WHERE id = {message.author.id}""")
        await message.channel.send(f"{message.author.mention} Вы перейшли на **ЖЕЛЕЗО 1** {Rang1EM}")
    # else:
    # 	print(f"все ще ранг 0 у {cursor.execute(f'SELECT name FROM users WHERE id = {message.author.id}').fetchone()[0]}")
    if cursor.execute(f"""SELECT rangs FROM users WHERE id = {message.author.id}""").fetchone()[0] == 1 and \
            cursor.execute(f"""SELECT exp FROM users WHERE id = {message.author.id}""").fetchone()[0] >= 5000:
        print(f"ранг 2 у {cursor.execute(f'SELECT name FROM users WHERE id = {message.author.id}').fetchone()[0]}")
        cursor.execute(f"""UPDATE users SET rangs = '2' WHERE id = {message.author.id}""")
        cursor.execute(f"""UPDATE users SET exp = 0 WHERE id = {message.author.id}""")
        await message.channel.send(f"{message.author.mention} Вы перейшли на **ЖЕЛЕЗО 2** {Rang2EM}")
    if cursor.execute(f"""SELECT rangs FROM users WHERE id = {message.author.id}""").fetchone()[0] == 2 and \
            cursor.execute(f"""SELECT exp FROM users WHERE id = {message.author.id}""").fetchone()[0] >= 10000:
        print(f"ранг 3 у {cursor.execute(f'SELECT name FROM users WHERE id = {message.author.id}').fetchone()[0]}")
        cursor.execute(f"""UPDATE users SET rangs = '3' WHERE id = {message.author.id}""")
        cursor.execute(f"""UPDATE users SET exp = 0 WHERE id = {message.author.id}""")
        await message.channel.send(f"{message.author.mention} Вы перейшли на **ЖЕЛЕЗО 3** {Rang3EM}")
    if cursor.execute(f"""SELECT rangs FROM users WHERE id = {message.author.id}""").fetchone()[0] == 3 and \
            cursor.execute(f"""SELECT exp FROM users WHERE id = {message.author.id}""").fetchone()[0] >= 15000:
        print(f"Все ранги у {cursor.execute(f'SELECT name FROM users WHERE id = {message.author.id}').fetchone()[0]}")
        cursor.execute(f"""UPDATE users SET rangs = '4' WHERE id = {message.author.id}""")
        cursor.execute(f"""UPDATE users SET exp = 0 WHERE id = {message.author.id}""")
        await message.channel.send(f"{message.author.mention} Вы перейшли на **ХЗ КАК ТЫ ВООБЩЕ СЮДА ДОШОЛ**")

    connection.commit()

    # Удаление спама в заявках
    if message.channel.id == DisId.AnketaChatID:  # Проверка канала
        if DisId.DontOficialRoleID in [y.id for y in message.author.roles]:  # Проверка роли
            if '.заявка' in message.content:
                pass
            else:
                await message.channel.purge(limit=1)


@client.command(aliases=["rename"])
async def __revork_my_acc(ctx, member: discord.Member = None, *name):
    if member is None:
        await ctx.send(f"{ctx.author.mention} На пишите свое имя, в дискорде!")
    elif member is not ctx.author.mention:
        if DisId.AdminID in [y.id for y in ctx.author.roles] or DisId.ButowkaID in [y.id for y in
                                                                                    ctx.author.roles] or DisId.MainModerID in [
            y.id for y in ctx.author.roles]:
            print(name)
            cursor.execute(f"""UPDATE users SET FUsername = "{"".join(name)}" WHERE id = {member.id}""")
            await ctx.send(f"{ctx.author.mention} Вы успешно изменили никнейм игрока {member.mention}")
        else:
            cursor.execute(f"""UPDATE users SET FUsername = "{"".join(name)}" WHERE id = {ctx.author.id}""")
            await ctx.send(f"{ctx.author.mention} Вы успешно изменили свой никнейм.")
    # else:
    # 	await ctx.send(f"{ctx.author.mention} Вы не имете право изменять чужие никнеймы")

    connection.commit()


# token = os.environ.get('BOT_TOKEN')
token = ("NzA5MTQ2MTUyMTI1MjAyNDMy.Xrhp0Q.ZnOoe5PlH0KuLf86YKFCszbcznY")
client.run(token)
