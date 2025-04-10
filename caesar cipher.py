"""
Bu yerda shirflangan matnni kiritib deshifrlangan matn 
olindi
"""




def sezar_desifr(sifr_text, shift):
    desifr_text=""
    for char in sifr_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            desifr_text += chr((ord(char)-offset-shift)%26+offset)
        else:
            desifr_text += char
    return desifr_text

def brute_force(sifr_text):
    print("Barcha mumkin bo'lagn desifrlashlar:")
    for key in range(1,26):
        desifr = sezar_desifr(sifr_text, key)
        print(f"Kalit {key:2}: {desifr}")

sifr_text = input("Sifr matnni kiriting:")
brute_force(sifr_text)