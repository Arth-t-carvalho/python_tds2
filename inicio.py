# from datetime import datetime
# ano_atual = datetime.now().year 
# clube = "SPFC"
# campeonato_mundial = 3
# ano_fundacao = 1930
# print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
# print(f"são {ano_atual - ano_fundacao} anos de existencia.")

# escola = 'senai'
# curso = 'tecnico em desenvovimneto de sistema'
# uc = 'logica de programação e algoritmo'
# print(
#     f"Escola: {escola} \n"
#     f"curso:  {curso} \n"
#     f"unidade curricular: {uc}"
# )
print(f"programa de emprestimos."
      f"responda: (0-não ou 1-sim)")

nome_negativado = int(input('Possui nome negativado'))
if nome_negativado == 1: #sim
    print("não pode realizar emprestimo")
else:
    carteira_assinada = int(input('possui carteira assinado'))
    if carteira_assinada == 0: #não
        print("não pode realizar emprestimos")
    else:
        possui_casa_propia = int(input("possui casa propia"))
        if possui_casa_propia == 0: #não
            print('não pode realizar emprestimo')
        else:
            print('conceder emprestimo')