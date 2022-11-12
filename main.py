from curses import use_default_colors
from discord.ext import tasks
import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import os
from actualisation import *
from usecode import *
import time
 

class MyClient(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.ncode.start()

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def ncode(self):
        channel = self.get_channel(739595329434943630)  # channel ID goes here
        global nb_validCode,dic
        new_nb_validCode,new_dic = actualisation()
        global used

        temp,temp_nb = new_dic.copy(),new_nb_validCode
        for key in temp:
            if key in dic :
                new_dic.pop(key)
                new_nb_validCode -=1

        for i in new_dic :
            if i in used :
                new_dic.pop(i)
                new_nb_validCode -=1
            else :
                used.append[i]
                while len(used) > 50:
                    used.pop(0)



        if new_nb_validCode == 1:
            for i in new_dic :
                a = i
                b= new_dic[i]
            message = f"<@&739594402967715981>\nIl y a un nouveau code : {a} -> "

            for i in range(len(b)):
                message += f"x {b[i][0]} {b[i][1]},"

            message += f" lien IOS : <http://withhive.me/313/{a}>"
            await channel.send(message)
            use_code("europe","OverEnder",a)
            
        elif new_nb_validCode > 1:
            message = f"<@&739594402967715981>\nIl y a {new_nb_validCode} nouveaux codes valides qui sont : \n"        
            for key in new_dic :
                message += f"{key}  -> "
                for rec in new_dic[key]:
                    message += f"x {rec[0]} {rec[1]}, "
                message += f"lien IOS : <http://withhive.me/313/{key}>\n"
                use_code("europe","OverEnder",key)
            await channel.send(message)

        nb_validCode,dic = temp_nb,temp

    @ncode.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in



client = MyClient(command_prefix= "*", description= "Bot for summoner's war rewards using swq.jp",intents=discord.Intents.all())

@client.command()
async def ping(ctx):    
    await ctx.send("pong")

@client.command()
async def ncode(ctx):    
    await ctx.send("La commande ncode n'existe plus le bot s'actualise tout seul maintenant !")

@client.command()
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

used = []

nb_validCode,dic = actualisation()
client.run(os.environ["TOKEN"])
