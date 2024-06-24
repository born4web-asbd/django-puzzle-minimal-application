"""
Module parameters not
"""

# Pri zakladani domu, se automaticky vytvori nejstarsi zaznam v tabulce UzaverkyAutorizace
# tento parametr urcuje mesic aktualniho roku od ktereho se jiz zapise posledni zaznam
# na 31.12 predchoziho roku. Tedy nebude jiz mozno delat uzaverku predchoziho roku
# protoze by mela byt jiz davno hotova
# Napr. nastaveno na 5 (kveten) => dum vytvorim v cervnu 2018 a posledni zaznam tedy bude 31.12.2017
# => dum vytvorim v breznu 2018 a posledni zaznam tedy bude 31.12.2016 (jeste delam zaverku predchoziho roku)
NEJSTARSI_ZAZNAM_UZAVERKY_AUTORIZACE_PRELOMOVY_MESIC = 5


# Kam presmeruji uzivatele v ramci aplikace po uspesnem prihlaseni a po jake dobe v milisekundach
AFTER_LOGIN_CONFIRMATION_APPLICATION_REDIRECT_PATERN = "accounts:account-listing"
AFTER_LOGIN_CONFIRMATION_APPLICATION_REDIRECT_TIMEOUT = 2000


# Povolit v aplikaci tzv. verejne kontakty tedy kontakty, ktere nemusi patrit do zadne skupiny kontaktu
ALLOW_PUBLIC_CONTACTS = False
