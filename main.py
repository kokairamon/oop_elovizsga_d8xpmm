from models import *

print("[Kölcsönző létrehozása]")

kolcsonzo = Kolcsonzo()
while(len(kolcsonzo.nev) == 0):
    kolcsonzo.nev = input("Kölcsönző neve: ")
kolcsonzo.cim = input("Kölcsönző címe: ")
kolcsonzo.telefonszam = input("Telefonszám: ")

print("\n")
print(f"[ A(z) '{kolcsonzo.nev}' kölcsönző megnyitott!]")
print(f"[Cím = {kolcsonzo.cim}] [Tel = {kolcsonzo.telefonszam}]")

kolcsonzo.print_fomenu()








