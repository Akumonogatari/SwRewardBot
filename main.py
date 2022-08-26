import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import os

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
    
    message = f"Il y a actuellement {nb_validCode} codes valides qui sont : \n"
    if nb_validCode == 1:
        message = f"Il y a actuellement {nb_validCode} code valide qui est : \n"

    for key in dic :
        message += f"{key} +  -> "
        for rec in dic[key]:
            message += f"x {rec[0]} {rec[1]}, "
        message += f"lien IOS : <http://withhive.me/313/{key}>\n"
    if nb_validCode == 0:
        message = "Il n'y malheureusement pas de code valide pour le moment essaie plus tard..."

    await ctx.send(message)


@bot.command()
async def actu(ctx):
    actualisation()
    await ctx.send("Le bot a actualisé sa liste. *code pour voir les codes coupons dispo !")


def actualisation():
    global nb_validCode
    global dic

    req = Request('https://swq.jp/_special/rest/Sw/Coupon?_csrf_token=0r_X6Mr_qpxIuYfbxaLx3M4BnPx_zeZ2PgcCMAD9QuuFTlvE9e-HbCTxt0SvYCvmvasDeS1Uea3NJq-bH769QRYfKCZ84Y4mWGHpztVtFULbDvBrS4Kr6qixxjiAvDqJs7DH85SJBh0&_ctx[b]=master&_ctx[c]=JPY&_ctx[l]=fr-FR&_ctx[t]=Europe%2FParis%3B%2B0200&results_per_page=50', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req,timeout=10).read()
    web = str(webpage)


    dic = {}

    nb_validCode = web.count('verified')    #nombres de codes valides

    debut = 0

    for i in range(nb_validCode):
        
        lab= web.find('Label',debut)                  #recherche du nom du code
        a= web.find('"',lab+8)              
        name=""                              
        for i in range(lab+8,a):
            name += web[i]

        rec=[]
        start=a
        while start < web.find("verified",a):   #recherche des récompenses
            q =  web.find('Quantity',start)     #recherche de la quantité
            b = web.find('"',q+11)
            quant=""                              
            for i in range(q+11,b):
                quant += web[i]
            start = q

            lab2 = web.find('"Label":',start)   #recherche du nom  
            b = web.find('"',lab2+11)              
            recName=""                              
            for i in range(lab2+9,b):
                recName += web[i]
            start = web.find('"Label":',b)
            rec.append((quant,recName))
        debut = start
        dic[name] = rec

actualisation()
bot.run(os.environ['TOKEN'])

