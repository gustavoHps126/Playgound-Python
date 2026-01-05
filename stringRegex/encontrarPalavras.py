import re

livro = "As Aventuras de Alice no País das Maravilhas"
inicial = "A"

def pesquisa(livro, inicial):
    #A regex \b{letra}[a-zà-ÿ]* captura todas palavras,
    #  incluindo aquelas com caracteres acentuados e o parâmetro re.IGNORECASE permite que o programa funcione tanto com maiúscula quanto minúscula.
    x = re.findall(rf"\b{inicial}[a-zà-ÿ]*", livro, re.IGNORECASE)
    print(x)
    return

pesquisa(livro, inicial)