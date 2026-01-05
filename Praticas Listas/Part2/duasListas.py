texto1 = ["cafe", "leite", "pão", "açúcar"]
texto2 = ["pão", "cafe", "biscoito", "chocolate"]

comum = list(set(texto1) & set(texto2))

texto1 = [i for i in texto1 if i not in comum]
texto2 = [i for i in texto2 if i not in comum]

print(f"Lista comum: {comum}")
print(f"Lista 1: {texto1}")
print(f"Lista 2: {texto2}")
