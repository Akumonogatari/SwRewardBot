import os

def use_code(serveur,hiveid,code):

    curl = f"""curl 'https://event.withhive.com/ci/smon/evt_coupon/useCoupon'   -H 'Accept: application/json, text/javascript, */*; q=0.01'   -H 'Accept-Language: fr;q=0.9'   -H 'Connection: keep-alive'   -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'   -H 'Origin: https://event.withhive.com'   -H 'Referer: https://event.withhive.com/ci/smon/evt_coupon'   -H 'Sec-Fetch-Dest: empty'   -H 'Sec-Fetch-Mode: cors'   -H 'Sec-Fetch-Site: same-origin'   -H 'Sec-GPC: 1'   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'   -H 'X-Requested-With: XMLHttpRequest'   --data-raw 'country=FR&lang=fr&server={serveur}&hiveid={hiveid}&coupon={code}'   --compressed"""
    os.system(curl)

if __name__ == "__main__":
    serveur = "europe"
    hiveid = "OverEnder"
    code = "bestofbestsswc22"
    use_code(serveur,hiveid,code)
    