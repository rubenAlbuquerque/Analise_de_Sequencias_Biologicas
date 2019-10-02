import Biological_Sequence



def escolha_sequencia():
    print("\n\t \033[0;34m Escoha uma opcão  \033[m ")
    print("***************************************************")
    print("**    1. Escrever a sequencia.                   **")
    print("**    2.-Retirar a sequencia de um ficheiro(.txt)**")
    print("***************************************************")
    opcao = input("\t->")
    if opcao == "1":
        seq = input("Escreva a sequencia:\n").upper()

        return seq
    elif opcao == "2":
        path_file = input("Escreva o caminho do ficheiro:")
        try:
            with open(path_file, "r") as file:
                seq = file.read()
                print(seq)
            return seq
        except:
            print("Tente novamente. Este caminho não existe.")
            escolha_sequencia()

    else:
        print("Não inseriu nenhum do numeros.")
        escolha_sequencia()

# menu 1
def menu1(seq):

    print("\n\t \033[0;34m ANALIZAR UMA SEQUENCIA . \033[m ")
    print("******************************************************************************************* ")
    print("****  Saber:                                     Operacoes:")
    print("****\t\t 1.- Nº de um determinado Nucleotideo.       8.-  Fazer Ungap.")
    print("****\t\t 2.- Frequencia do Nucleotideo.              9.-  Fazer a sequencia complementar.")
    print("****\t\t 3.- Como a sequencia termina.               10.-  Fazer a sequencia complementar reversa.")
    print("****\t\t 4.- Como a sequencia comeca.                11.- Fazer a transcrição")
    print("****\t\t 5.- A Massa Molecular                       12.- Fazer o clipping.")
    print("****\t\t 6.- Percentagem de GC.                      13.- Fazer a Tranlacao.")
    print("****\t\t 7.- Posicao de uma sub-sequencia            14.- Fazer o Splicing. ")
    print("****\t\t 1.- ")
    print("******************************************************************************************* \n")

    opcao1 = input(" \n Escolha a opcao que deseja fazer ? \n ")




if __name__ == '__main__':
    sequencia = escolha_sequencia()
    menu1(sequencia)
