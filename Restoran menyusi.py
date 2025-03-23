# Restoran menyusi lug'ati
menyu = {
    "osh": 50000,
    "shashlik": 25000,
    "mastava": 30000,
    "somsa": 10000,
    "lag'mon": 45000,
    "manti": 35000,
    "chuchvara": 40000,
    "shorva": 38000,
    "norin": 42000,
    "dimlama": 48000
}

# Foydalanuvchidan 3 ta taom buyurtma qilishni so'raymiz
print("Buyurtmangizni kiriting:")
buyurtmalar = []
for i in range(3):
    taom = input(f"{i+1}-taomni kiriting: ").lower()
    buyurtmalar.append(taom)

# Buyurtmalarni tekshiramiz
for taom in buyurtmalar:
    if taom in menyu:
        print(f"{taom.title()} narxi {menyu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q.")


