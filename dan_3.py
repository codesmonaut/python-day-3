# Funkcije

# def minimum_dva_broja (broj_a, broj_b):
    
#     if broj_a < broj_b:
#         return broj_a
#     else:
#         return broj_b

# a = 10
# b = 4

# manji_od_ta_dva = minimum_dva_broja(a, b)

# print(manji_od_ta_dva)

# Racunanje stepeni *F iz *C:

# def ctf (c_deg):
#     f_deg = c_deg * 1.8 + 32
#     return f_deg

# def ftc (f_deg):
#     return (f_deg - 32) / 1.8

# def prikazi_opcije ():
#     print("Opcije programa su:")
#     print(" 1) Konverzija iz *C u *F.")
#     print(" 2) Konverzija iz *F u *C.")
#     print(" 0) Prekid programa.")

# def trazi_izbor_od_korisnika ():
#     izbor = input("Vas izbor je: ")

#     if izbor in ["0", "1", "2"]:
#         return izbor
#     else:
#         print("Nepoznata opcija!")

# def C2F ():
#     tempC = float(input("Unesite temperaturu u *C: "))
#     tempF = ctf(tempC)
#     print(f"Ta temperatura u *F iznosi {tempF:.2f}")

# def F2C ():
#     tempF = float(input("Unesite temperaturu u *F: "))
#     tempC = ftc(tempF)
#     print(f"Ta temperatura u *C iznosi {tempC:.2f}")



# while True:
#     prikazi_opcije()

#     izbor = trazi_izbor_od_korisnika()

#     if izbor == "0":
#         print("Program se iskljucuje...")
#         break
#     elif izbor == "1":
#         C2F()
#     elif izbor == "2":
#         F2C()



# def f (n):
#     if n == 1:
#         return 1
#     return n * f(n - 1)

# # Bez pamcenja

# def fib (n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1

#     return fib(n - 1) + fib(n - 2)

# Sa pamcenjem

# upamcene_vrednosti = {
#     0: 0,
#     1: 1
# }

# def fib (n):
#     if n in upamcene_vrednosti.keys():
#         return upamcene_vrednosti[n]

#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     vrednost = fib(n - 1) + fib(n - 2)

#     upamcene_vrednosti[n] = vrednost

#     return vrednost

# def napravi_studenta (ime = "", prezime = "", indeks = 0):

#     return {
#         "ime": ime,
#         "prezime": prezime,
#         "indeks": indeks
#     }

# print(napravi_studenta(indeks = 2008213514))

def tacka (x, y, z = 0):
    broj_tacaka_jednakih_nuli = 0

    if x == 0:
        broj_tacaka_jednakih_nuli += 1
    
    if y == 0:
        broj_tacaka_jednakih_nuli += 1
    
    if z == 0:
        broj_tacaka_jednakih_nuli += 1
    
    t = {
        "x": x,
        "y": y,
        "z": z
    }

    return t, broj_tacaka_jednakih_nuli

tA, koliko_ih_je_nula = tacka(2, 5)

# print(tacka(2, -3, 1))
# print(tacka(z = 1, x = 2, y = -3))
# print(tacka(2, z = 1, y = -3))
print(tA)
print(koliko_ih_je_nula)