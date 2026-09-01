tarefas = []

while True:
    print("")
    print("=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Remover tafera")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    escolher = int(input("Digite qual opção deseja: "))
    
    match escolher:
        case 1:
            add = input("Digite qual tarefa quer adicionar: ")
            tarefas.append(add)
            
        case 2:
            rem = input("Digite qual tarefa quer remover: ")
            tarefas.remove(rem)
            
        case 3:
            for tarefa in tarefas:
                print(f"- {tarefa}")
                
        case 0:
            break