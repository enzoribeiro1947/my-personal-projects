alunos = []

while True:
    print("\n===== SISTEMA DE ALUNOS =====")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno")
    print("4. Remover aluno")
    print("5. Media geral")
    print("0. Sair")
        
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno (0 a 10): "))
        alunos.append({"nome": nome, "idade": idade, "nota": nota})
        print(f"Aluno {nome} cadastrado!")

    elif opcao == "2":
        if not alunos:
            print("Nao ha alunos no sistema")
        else:
            for a in alunos:
                print(f"Nome: {a['nome']} | Idade: {a['idade']} | Nota: {a['nota']}")

    elif opcao == "3":
        procura = input("Procure um aluno pelo nome: ")
        encontrado = False
        for a in alunos:
            if procura.lower() == a["nome"].lower():
                print(f"Nome: {a['nome']} | Idade: {a['idade']} | Nota: {a['nota']}")
                encontrado = True
        if not encontrado:
            print("Aluno nao encontrado")

    elif opcao == "4":
        qualnome = input("Qual o nome do aluno?: ")
        for a in alunos:
            if qualnome.lower() == a["nome"].lower():
                alunos.remove(a)
                print(f"Aluno {qualnome} removido!")
                break
        else:
            print("Aluno nao encontrado")

    elif opcao == "5":
        if not alunos:
            print("Nao ha alunos no sistema")
        else:
            media = sum(a["nota"] for a in alunos) / len(alunos)
            print(f"Media geral: {media:.2f}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Digite uma opcao valida!")