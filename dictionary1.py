"""
22.03.2025

Python Basic(Python asoslari)

Mavzu:Dictionary(lug'atlar bilan ishlash)
                 
Muallif:Javohir Jumamurodov 
"""
# #Oila azolardan qisqa malumot
# akam = {'ismi':'jahongir', 'tug\'ilgan yili':'1993',\
#         'shahri':'Buxoro', 'ish joyi':'Toshkent'}
# ism = akam['ismi'].title()
# t_yili = akam['tug\'ilgan yili']
# joy = akam['shahri'].title()
# ishi = akam['ish joyi'].title()

# print(f"Akamning ismi {ism},{t_yili}-yilda,{joy}da tug'ilgan.Ish joyi {ishi}.")

# #Dostlarimizdan qanday taomni yaxshi ko'rishi
# taomlar = {
#     'oybek':'shashlik',
#     'jahongir':'sho\'rva',
#     'isoq':'manti',
#     'ozod':'palov',
#     'mehriddin':'tandir'
#     }

# print(f"Oybekning sevimli taomi {taomlar['oybek']}")
# print(f"Jahongirning sevimli taomi {taomlar['jahongir']}")
# print(f"Isoqning sevimli taomi {taomlar['isoq']}")

#Python izohli lug'ati
p_lugat = {
    'integer':'Butun son tipi',
    'float':'Haqiqiy son tipi',
    'string':'Matn tipi',
    'boolen':'mantiqiy',
    'title()':'So\'zlarni bosh harf bilan yozadi',
    'upper()':'Hamma harfni bosh harf bilan yozadi',
    'for':'Takrorlash operator',
    'if-else':'shart operatori',
    'dictionary':'lug\'atlar bilan ishlash',
    'list.append()':'listga malumot qo\'shish'
    }

# soz = input("Lugat kiriting:").lower()
# lugat =print( p_lugat.get(soz,'Bunday lugat yoq'))

kalit = input("Kalit soz kiriting:").lower()
tarjima = p_lugat.get(kalit)

if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} sozi {tarjima} deb tarjima qilinadi")








