import random

slovnik = [
    "a", "aby", "aj", "ale", "anebo", "ani", "ano", "asi", "aspoň",
    "džuzna", "během", "bez", "beze", "blízko", "bohužel", "brzo", 
    "bude", "budeme", "humna", "budeš", "budete", "budou", "budu",
    "byl", "byla", "byli", "bylo", "byly", "být", "čau", "chce", 
    "chceme", "chceš", "chcete", "chci", "chtít", "chtějí", "chut'", 
    "chuti", "co", "dál", "dále", "bo", "daleko","děkovat", "děkujeme",
    "děkuji", "den", "deset", "devatenáct", "do", "dobrý", "docela",
    "dvě", "hodně", "já", "jak", "jde", "je", "jeden","jedna", "jednou",
    "jedou", "jeho", "jehož", "jej", "její", "jejich", "jemu", "jen",
    "kobzole", "jenom", "ještě", "jestli", "jestliže", "jí", "jich", "jím",
    "jimi", "jinak", "jsem", "jsi", "jsme", "jsou", "jste", "kam", "kde",
    "kdo", "kdy", "když", "ke", "kolik", "cip", "kromě", "která", "které", 
    "který", "kvůli", "má", "mají", "málo", "mám", "máme", "máš", "šnuptychl",
    "máte", "mé", "pizděc", "mě", "mezi", "mí", "mít", "mně", "mnou", "moc",
    "mohl", "mohou", "moje", "moji", "možná", "můj", "musí", "může", "my",
    "na", "nad", "nade", "nám", "včil", "námi", "naproti", "nás", "náš",
    "naše", "naši", "ne", "ně", "nebo", "nebyl", "nebyla", "nebyli","nebyly",
    "něco", "nedělá", "nedělají", "nedělám", "ludra", "neděláme", "neděláš", 
    "neděláte", "nějak", "nejsi", "někde", "někdo", "nemají", "nemáme", "nemáte",
    "neměl", "němu", "není", "paštěka", "nestačí", "nevadí", "než", "nic",
    "nich", "ním", "nimi", "nové", "nový", "nula", "od", "ode", "on", "ona",
    "oni", "ono", "ony", "osmnáct", "pak", "haluz", "patnáct", "pět", "po", "pod", 
    "podle", "pokud", "potom", "pouze", "pozdě", "před", "přes","přese",
    "pro", "proč", "prosím", "prostě", "proti", "protože", "rovně", "se", "sedm",
    "šest", "šestnáct", "skoro", "smějí", "smí", "čagan", "snad", "spolu",
    "sta","sté", "ta", "tady", "tak", "takhle", "taky", "tamhle", "tebe", 
    "tebou", "ted'","tedy", "ten", "tě", "ti", "to", "tobě", "tohle", "toto",
    "třeba", "tři", "třináct", "trošku", "tvá", "tvé", "tvoje", "tvůj", "ty",
    "určitě", "už","vám", "vámi", "vás", "váš", "vaše","vaši", "ve", "večer",
    "vlastně", "vy", "vždy", "za","zač", "či", "zatímco", "ze", "že"
]

pocet_vet = int(input("Zadejte počet vět v odstavci: "))
pocet_odstavcu = int(input("Zadejte počet odstavců: "))
text = ""
for _ in range(pocet_odstavcu):
    for _ in range(pocet_vet):
        predchozi_slovo = None
        veta = []
        for i in range(5):
            while True:
                slovo = random.choice(slovnik)
                if slovo != predchozi_slovo:
                    break
            veta.append(slovo.capitalize() if i == 0 else slovo)
            predchozi_slovo = slovo
        text += ' '.join(veta) + random.choice(['.', '!', '?']) + ' '
    text += "\n\n"

print(text)
