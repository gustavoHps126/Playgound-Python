PermissoesP = {"leitura", "escrita", "execução", "compartilhamento"}
PermissoesS = {"leitura", "escrita"}

if PermissoesS.issubset(PermissoesP):
        print("As permissões solicitadas fazem parte das permissões principais")
else:
        print("As permissões solicitadas NÃO fazem parte das permissões principais")