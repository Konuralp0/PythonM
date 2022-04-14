


def rakam_topla(x):
    toplam = 0
    a = str(x)
    lt = list(a)
    if a.isnumeric():
        print(lt)
        for numbers in lt:
            toplam = toplam + int(numbers)
        return toplam
    else:
        return "not numeric"

def karakter_say(a):
    harf_sum = 0
    rakam_sum = 0
    karakter_sum = 0
    l = list(a)
    for char in l:
        if (ord(char) <= 90 and ord(char) >= 65) or (ord(char) <=122 and ord(char) >=97):
            harf_sum+=1
        elif ord(char) >= 48 and ord(char) <= 57:
            rakam_sum+=1
        else:
            karakter_sum +=1
    return f"Bu Stringde toplamm {harf_sum} harf, {rakam_sum} rakam ve {karakter_sum} karakter vardir"



class Bisiklet():
    def __init__(self, jant, model, marka, is_heltmet):
        self.__jant =jant
        self.__model = model
        self.__is_helmet = is_heltmet
    def getJant(self):
        return self.__jant
    def setJant(self, jant):
        self.__jant = jant

    def __str__(self):
        return self.__jant , self.__model

b1 = Bisiklet(23,"sport", "bianchi", True)

print(b1.getJant())
b1.setJant(45)
print(b1.getJant())
print(b1.__str__())

boola = False
while boola == False:
    sifre = input("Sifre: ")
    sifre_bas = sifre[0:1]
    sifre_son = sifre[len(sifre) - 1]
    a = not sifre.__contains__(" ")
    uzunluk = len(sifre) >= 8
    sifreBuyuk = ord(sifre_bas) >= 65 and ord(sifre_bas) <= 90
    sifreKucujk = ord(sifre_son) >= 97 and ord(sifre_son) <= 122

    if a and uzunluk and sifreBuyuk and sifreKucujk:
        print("Sifre basariyla kaydoldu")
        boola = True
    else:
        print("Lutfen sifreyi tekrar olusturun")