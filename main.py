maas = float(input("Maaşınız: "))
aylikSigorta = float(input("Sigortanız (aylık): "))
if maas <= 10000:
    vergi = 15 / 100
elif maas <= 20000:
    vergi = 17.5 / 100
elif maas <= 30000:
    vergi = 20.0 / 100
elif maas <= 40000:
    vergi = 22.5 / 100
elif maas <= 50000:
    vergi = 25.0 / 100

print("Vergiler, Maaşınıza göre hesabınızdan çekilmiştir.\nVergi Fiyatı: {}\nVergi Oranı: {}\nKalan Tutar: {}".format(
    vergi * maas,
    vergi,
    maas - (vergi * maas)
))

# Vergiler, Vergi Oranları vs. Gerçeği yansıtmamaktadır. Uydurmadır. 
