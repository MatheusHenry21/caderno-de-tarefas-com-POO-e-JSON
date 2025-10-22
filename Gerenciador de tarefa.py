#REGRAS

#POO

#Adicionar tarefa
#Listar tarefas
#Concluir tarefa
#Remover tarefa
#Sair

import json
from os import system
system("cls")

class Tarefa:
    def __init__(self, nome, descricao):

        self.nome = nome
        self.descricao = descricao
        if self.descricao != "":
            self.descricao = descricao
        else: self.descricao = "NÃO INFORMADO" 
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def __str__(self):
        return f"{self.nome} - DESCRIÇÃO: {self.descricao} '{self.status}'"

class GerenciadorDeTarefa:

    def __init__(self):
        self.__tarefa = []
        self.resgatar_exterior()

    def salvar_exterior(self):
        dict_list = [vars(exterior) for exterior in self.__tarefa]
        with open("dados.json", "w", encoding="utf-8") as exterior:
            json.dump(dict_list, exterior, ensure_ascii=False)
    
    def resgatar_exterior(self):
        try:
            with open("dados.json", "r", encoding="utf-8") as exterior:
                dados = json.load(exterior)
            self.__tarefa = [Tarefa(t["nome"], t["descricao"]) for t in dados]
        except FileNotFoundError:
            self.__tarefa = []


    def add_tarefas(self):
        nome = input("\nDigite o nome da tarefa: ").capitalize().strip()
        descricao = input("Digite alguma descrição(Opcional): ").strip().capitalize()
        tarefa = Tarefa(nome, descricao)
        self.__tarefa.append(tarefa)
        self.salvar_exterior()

        print(f"\nA tarefa '{nome}' foi adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.__tarefa:
            print("\nNão há tarefa nesta lista.")
            return
        
        for i, tarefas in enumerate(self.__tarefa, start=1):
            print(f"\n{i} - {tarefas}")

    def concluir_tarefa(self):
        if not self.__tarefa:
            print("\nNão há tarefa nesta lista.")
            return
        
        self.listar_tarefas()
        local = Indice.local_tarefa()

        if 0 <= local < len(self.__tarefa):
            contato = self.__tarefa[local]
            contato.concluir()
            self.salvar_exterior()
            print(f"\nA tarefa '{contato.nome} foi alterar a sua situação!'")

        else:
            print("\nNão há essa tarefa no caderno.")

    def remover_tarefa(self):
        if not self.__tarefa:
            print("\nNão há tarefa nesta lista.")
            return
        
        self.listar_tarefas()
        
        indice = Indice.local_tarefa()

        if 0 <= indice < len(self.__tarefa):
            caderno = self.__tarefa[indice]
            self.__tarefa.pop(indice)
            print(f"\nO contato '{caderno.nome} removido com sucesso.'")
            self.salvar_exterior()
        else:
            print("\nNão há essa tarefa no caderno.")

class Indice:
    def local_tarefa():
        while True:  
            try:
                opcao = int(input("\nDigite o índice da tarefa que deseja alterar: "))
                return opcao - 1
            except ValueError:
                print("\nErro, digite apenas números.") 
                continue
    def opcao():
        while True: 
            try:
                opcao = int(input("\nDigite o numero da opção que deseja usar: "))
                return opcao
            except ValueError:
                print("\nErro, digite apenas números.")
                continue

class Menu:
    def menu():

        gerenciador = GerenciadorDeTarefa()

        while True:
            print("\n--- MENU ---")
            print("1 - Adicionar tarefas")
            print("2 - Listar tarefas")
            print("3 - Concluir tarefas")
            print("4 - Remover tarefas")
            print("5 - Sair")

            opcao = Indice.opcao()

            if opcao == 5:
                print("\nSaindo... até logo!")
                break

            elif opcao == 1:
                gerenciador.add_tarefas()

            elif opcao == 2:
                gerenciador.listar_tarefas()

            elif opcao == 3:
                gerenciador.concluir_tarefa()

            elif opcao == 4:
                gerenciador.remover_tarefa()

            else: print("Erro, não existe essa opção, tente novamente!")

    menu()