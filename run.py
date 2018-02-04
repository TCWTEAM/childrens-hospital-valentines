import requests
import json
from bs4 import BeautifulSoup as bs
from random import *
def main(email, num, firstname):
    #made by xo be a good guy
    scount = 0
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'giving.cincinnatichildrens.org',
    'Origin':'https://giving.cincinnatichildrens.org',
    'Referer':'https://giving.cincinnatichildrens.org/send-a-valentine',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    for i in range(int(num)):
        url = "https://giving.cincinnatichildrens.org/send-a-valentine"
        s = requests.session()
        k = s.post(url, headers)

        soup0 = bs(k.content, "html.parser")
        viewstate = soup0.find('input', {'name': '__VIEWSTATE'})
        viewstate = str(viewstate)
        viewstate = viewstate.split('value="')[1]
        viewstate = viewstate.split('"/>')[0]

        lastnamel = ['Ryans', 'Markson', 'Reynolds', 'Halpert', 'Velluci', 'Carnado', 'Smith', 'Parkins', 'Santana', 'Vargas', 'C']
        namenum = randint(0, len(lastnamel) - 1)
        lastname = lastnamel[namenum]

        cardtypel = ['Oh So Sweet (Cupcake)', 'Gold Star (Girl with Book)', 'Beary Happy (Bear)']
        cnum = randint(0, len(cardtypel) - 1)
        cardtype = cardtypel[cnum]

        data = {
        'ScriptManager1_HiddenField': '',
        '__EVENTTARGET': 'PC15569$formWizard$formWizard$finishWizardButton',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR': '8CAEDFE0',
        '__VIEWSTATEENCRYPTED': '',
        'PC15569$formWizard$formWizard$96dee683_1cbf_406b_b28e_0c14c6121ec4':firstname,
        'PC15569$formWizard$formWizard$f1afad0e_a0d7_422e_9321_151a89727b25':lastname,
        'PC15569$formWizard$formWizard$8d9a3a8e_d2d4_4813_b88a_b336861a14dd':email,
        'PC15569$formWizard$formWizard$9dc94955_61b3_4200_9e65_ece612eb4a1f':cardtype
        }

        j = s.post(url, headers=headers)
        if j.status_code == 200:
            scount = scount + 1
            print("Sent Card {}/{}".format(scount, num))
        else:
            print("Error :(")
    print("Sent {}/{} Cards")
    print("Thank You :) -XO")



if __name__ == '__main__':
    print("Childrens Hospital Script By XO")
    print("twitter: xodev0x1010")
    print("-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    email = input("email:" )
    firstname = input("firstname: ")
    num = input("# to send: ")
    main(email, num, firstname)
