"""
Mavzu:Nesting bo'yicha amaliyot

Muallif:
    
    
"""


# 1. Al-Xorazmiy haqida lug‘at
al_xorazmiy = {
    "ism": "Muhammad ibn Muso al-Xorazmiy",
    "tugilgan_yil": 780,
    "vafot_yil": 850,
    "kasb": "Matematik, astronom, geograf",
    "mashhur_asar": "Al-jabr va al-muqobala",
    "qisqacha": "Algebra asoschisi, algoritm atamasi uning nomidan kelib chiqqan."
}

# 2. Ibn Sino haqida lug‘at
ibn_sino = {
    "ism": "Abu Ali Ibn Sino",
    "tugilgan_yil": 980,
    "vafot_yil": 1037,
    "kasb": "Tabib, faylasuf, matematik",
    "mashhur_asar": "Tib qonunlari",
    "qisqacha": "Sharq tibbiyoti va falsafasining buyuk namoyandasi."
}

# 3. Mirzo Ulug‘bek haqida lug‘at
mirzo_ulugbek = {
    "ism": "Mirzo Ulug‘bek",
    "tugilgan_yil": 1394,
    "vafot_yil": 1449,
    "kasb": "Astronom, matematik, hukmdor",
    "mashhur_asar": "Zij jadvali",
    "qisqacha": "Dunyodagi eng aniq astronomik jadvallar muallifi."
}

# 4. Bobur haqida lug‘at
bobur = {
    "ism": "Zahiriddin Muhammad Bobur",
    "tugilgan_yil": 1483,
    "vafot_yil": 1530,
    "kasb": "Shoir, sarkarda, davlat arbobi",
    "mashhur_asar": "Boburnoma",
    "qisqacha": "Boburiylar sulolasiga asos solgan va Hindistonda Buyuk Mo‘g‘ullar davlatini barpo etgan."
}

# Lug‘atlarni ro‘yxatga joylash
buyuk_shaxslar = [al_xorazmiy, ibn_sino, mirzo_ulugbek, bobur]

# Har bir shaxs haqida ma'lumot chiqarish
for shaxs in buyuk_shaxslar:
    print(f"\n{shaxs['ism']} ({shaxs['tugilgan_yil']} - {shaxs['vafot_yil']})")
    print(f"Kasbi: {shaxs['kasb']}")
    print(f"Mashhur asari: {shaxs['mashhur_asar']}")
    print(f"Qisqacha: {shaxs['qisqacha']}")
