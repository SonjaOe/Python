with open("tiedosto.txt") as tiedosto:
    sanalista = []
    try:
        for sana in tiedosto:
            sanalista.append(sana)
    except NameError:
        print("Something is not defined!")
#print(sanalista)
sanalista.sort()
sanalista.sort(key=len)
print(sanalista)

sanajono = ""
for sana in sanalista:
    sanajono += sana

with open("uusitiedosto.txt", "a") as uusi_tiedosto:
    uusi_tiedosto.write(sanajono)
