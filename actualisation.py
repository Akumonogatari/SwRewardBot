from urllib.request import Request, urlopen

def actualisation():
    req = Request('https://swq.jp/_special/rest/Sw/Coupon?_csrf_token=0r_X6Mr_qpxIuYfbxaLx3M4BnPx_zeZ2PgcCMAD9QuuFTlvE9e-HbCTxt0SvYCvmvasDeS1Uea3NJq-bH769QRYfKCZ84Y4mWGHpztVtFULbDvBrS4Kr6qixxjiAvDqJs7DH85SJBh0&_ctx[b]=master&_ctx[c]=JPY&_ctx[l]=fr-FR&_ctx[t]=Europe%2FParis%3B%2B0200&results_per_page=50', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req,timeout=10).read()
    web = str(webpage)
    f= open("page3.json","w")
    f.write(web)
    f.close()

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
            q = web.find('Quantity',start-100)     #recherche de la quantité
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
            start = web.find('Quantity',b)
            rec.append((quant,recName))


        debut =  web.find('Created',b)
        dic[name] = rec
    return nb_validCode,dic
        
if __name__ == "__main__" :
    actualisation()