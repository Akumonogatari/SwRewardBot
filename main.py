import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import os
from actualisation import *

intent = discord.Intents().all()
bot = commands.Bot(command_prefix= "*", description= "Bot for summoner's war rewards",intents=intent)


@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def code(ctx):
    global nb_validCode,dic
    nb_validCode,dic = actualisation()
    message = f"Il y a actuellement {nb_validCode} codes valides qui sont : \n"
    if nb_validCode == 1:
        message = f"Il y a actuellement {nb_validCode} code valide qui est : \n"

    for key in dic :
        message += f"{key}  -> "
        for rec in dic[key]:
            message += f"x {rec[0]} {rec[1]}, "
        message += f"lien IOS : <http://withhive.me/313/{key}>\n"
    if nb_validCode == 0:
        message = "Il n'y malheureusement pas de code valide pour le moment essaie plus tard..."

    await ctx.send(message)
  
@bot.command()
async def ncode(ctx):
    global nb_validCode,dic
    new_nb_validCode,new_dic = actualisation()
    temp,temp_nb = new_dic.copy(),new_nb_validCode

    for key in temp:
        if key in dic :
            new_dic.pop(key)
            new_nb_validCode -=1

    if new_nb_validCode == 0 :
        message = "Il n'y pas de nouveaux codes valides pour le moment essaie plus tard... (*code pour voir la liste des codes disponibles)"
    elif new_nb_validCode == 1:
        for i in new_dic :
            a = i
            b= new_dic[i]
        message = f"Il y a un nouveau code : {a} -> "

        for i in range(len(b)):
            message += f"x {b[i][0]} {b[i][1]},"

        message += f" lien IOS : <http://withhive.me/313/{a}>"
        await ctx.send(message)
    else :
        message = f"Il y a {new_nb_validCode} nouveaux codes valides qui sont : \n"        
        for key in new_dic :
            message += f"{key}  -> "
            for rec in new_dic[key]:
                message += f"x {rec[0]} {rec[1]}, "
            message += f"lien IOS : <http://withhive.me/313/{key}>\n"

    nb_validCode,dic = temp_nb,temp
    await ctx.send(message)

nb_validCode,dic = actualisation()
bot.run(os.environ["TOKEN"])

