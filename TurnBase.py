import random
import time

class Karakter:
    def __init__ (self, name, hp, atk, spd):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.spd=spd
    def hidup(self):
        return self.hp>0
    def serang(self, target):
        damage = self.atk+random.randint(-2,2)
        target.hp-=damage
        print(f"{self.name} menyerang {target.name} sebesar {damage} HP")
tim_player=[
    Karakter("Castorice", 8000, 2500, 110),
    Karakter("Yannz", 3000, 2100, 120),
    Karakter("Lingsha", 3600, 1900, 115),
    Karakter("Cipher", 3800, 2400, 130)
]
tim_musuh=[
    Karakter("Borisin", 5000, 3400, 120),
    Karakter("Nanook", 6000, 4000, 145)
]

semua_karakter=tim_player+tim_musuh
semua_karakter.sort(key=lambda c: c.spd, reverse=True)

giliran=1
while any(c.hidup() for c in tim_player) and any(c.hidup() for c in tim_musuh):
    print(f"\n=== Giliran {giliran} ===")
    for karakter in semua_karakter:
        if not karakter.hidup():
            continue
        if karakter in tim_player:
            musuh_hidup=[e for e in tim_musuh if e.hidup()]
            if musuh_hidup:
                target=random.choice(musuh_hidup)
                karakter.serang(target)
        else:
            player_hidup=[p for p in tim_player if p.hidup()]
            if player_hidup:
                target=random.choice(player_hidup)
                karakter.serang(target)
        time.sleep(0.5)

        if not any(e.hidup() for e in tim_musuh):
            print("\n=== Kamu Menang! ===")
            exit()
        if not any(p.hidup() for p in tim_player):
            print("\n=== Kamu Kalah! ===")
            exit()
    giliran+=1