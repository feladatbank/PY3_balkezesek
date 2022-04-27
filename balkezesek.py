"""
név;első;utolsó;súly;magasság
Jim Abbott;1989-04-08;1999-07-21;200;75
Kyle Abbott;1991-09-10;1996-08-24;200;76
Joel Adamson;1996-04-10;1998-04-26;185;76
"""
#1-2 Feladat
class Balkez:
    def __init__(self,sor):
        nev,elso,utolso,suly,magassag = sor.strip().split(";")
        self.nev        = nev
        self.elso       = elso
        self.utolso     = utolso
        self.oktober    = utolso[0:7]
        self.suly       = suly
        self.magassag   = int(magassag)

with open("balkezesek.csv" , encoding="UTF-8")as f:
    r = f.readline()
    lista = [balkez(sor) for sor in f]
#3. Feladat
hosz = len([sor for sor in lista])
print(f"3. feladat: {hosz}")
#4. Feladat
print("4. feladat:")
cm = 2.54
oktober = [sor for sor in lista if sor.oktober == "1999-10"]

[print(f"        {sor.nev} {(sor.magassag * cm):.1f}") for sor in oktober]
#   
print("5. feladat:")
evszam = ""
while True:
    if evszam == "":
        evszam = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
    if 1990 <= evszam <=1999:
        break
    else:
        evszam = int(input("Hibás adat!Kérek egy 1990 és 1999 közötti évszámot!: "))



