def teskari_sozlar(satr):
    sozlar = satr.split()
    teskari_sozlar = [soz[::-1] for soz in sozlar]
    return ' '.join(teskari_sozlar)

satr = input("Istalgan satrni kiriting: ")
print(teskari_sozlar(satr))
```

Kodni ishlatish uchun quyidagicha amal qilishingiz mumkin:

1. Kodni yozuvchi faylga saqlang.
2. Faylni ochib, satrni kiriting.
3. Dastur satrni so'zlarga ajratib, har bir so'zni teskari yozadi va natijani ekranda chiqaradi.
