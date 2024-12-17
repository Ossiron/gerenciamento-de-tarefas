tarefas = []
def adicionarTarefa():
    adicionar = input("digite uma tarefa ")
    gerenciar = {
            "tarefa": adicionar,
            "estado": False
        }
    tarefas.append(gerenciar)
    return 
def listarTarefas():
    if len(tarefas) == 0:
        print("não há tarefas")
    else:
        for i ,tarefa in enumerate(tarefas,1):
            print(i,tarefa)
    return

def tarefaConcluida():
    
    if len(tarefas) == 0:
        print("não há tarefas")
    else:
        posicao = int(input('digite oo numero da tarefa concluida'))
        tarefas[posicao-1]["estado"] = True
        print(f"a tarefa {tarefas[posicao-1]} foi comcluida")
    return
def removerTarefa():
    
    if len(tarefas) == 0:
        print("não há tarefas")
    else:
        posicao = int(input("digite o numero da tarefa a ser apagada"))
        print(f"a tarefa {tarefas[posicao-1]} foi removida")
        tarefas.pop(posicao-1)
    
    return
def selecionarOpcao():
        while True:
            try:
                opcao = int(input("escolha uma das das seguintes opções\n1- adicionar tarefa \n2- listar tarefas \n3- marcar tarefa como concluida \n4- remover tarefa da lista \n5- sair\n"))
                if opcao == 1:
                    try:
                        adicionarTarefa()
                    except:
                        print("alguma coisa deu errado, tente de novo")
                    continue
                elif opcao ==2:
                    try:
                        listarTarefas()
                    except:
                        print("alguma coisa deu errado, tente de novo")
                    continue
                elif opcao ==3:
                    try:
                        tarefaConcluida()
                    except:
                        print("alguma coisa deu errado, tente de novo")
                    continue
                elif opcao == 4:
                    try:
                        removerTarefa()
                    except:
                        print("alguma coisa deu errado, tente de novo")
                    continue
                elif opcao ==5:
                    break
                else:
                    print("opção invalida")
            except:
                print("alguma coisa deu errado, tente de novo")
selecionarOpcao()