link = "https://monitorrenan."

def verificar(link):
    if link.startswith("https://") and link.endswith(".com"):
        print("É um link valido")
    else:
        print("Não é um link valido")
    return

verificar(link)