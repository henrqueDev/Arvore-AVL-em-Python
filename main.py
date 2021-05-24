import os
from arvore_avl import Catalogo
import time

cat = Catalogo()


while True:
  os.system('clear')
  print('#'*36)
  print('#'*36)
  print('#'*9 + "  MUSICAS AVL  " + '#'*12)
  print('#'*36)
  print('#'*9 + f"  EH O BOOOY   " + '#'*12)
  print('#'*36 + '\n'*3)


  opcao = input('#1- Inserir música  \n#2- Buscar música pelo ID \n#3- Buscar músicas pelo ano \n#4- Listar músicas pela ordem alfabetica \n#5- Altura da arvore  \n#6- Exibir a árvore\n#7- Sair\n\n-> ')



  if opcao == "1":
      
      try:
        
        nome = input("\nDigite o nome da música -> ")
        album = input("\nDigite o nome do album -> ")
        ano = int(input("\nDigite o ano de lançamento -> "))
        id = int(input("\nDigite o ID -> "))
        cat.inserir(nome,album,ano,id)
        """
        cat.inserir("Facarrao",2,2000,1)
        cat.inserir("    Manteiga           ",2,2000,4)  
        cat.inserir("Carne",2,2000,5)
        cat.inserir("Carn",2,2000,3)
        #cat.inserir("Carna",2,2000,4)
        cat.inserir("milhas",2,2002,2)
        cat.inserir("Duality",2,2000,6)
        print(cat.root)
        """
        time.sleep(5)
      except ValueError:
       print("Valor inválido! Digite Novamente!")
       time.sleep(1)
  elif opcao == "2":
    try:
      id = int(input("\nDigite o ID -> "))
      procura = cat.search_id(id)
      if procura != None: 
        print(f"{procura.nome}-{procura.album}-{procura.ano}")
        time.sleep(10)
      else:
        print("Música não encontrada!!")
        time.sleep(1)
    except ValueError:
      print("Valor inválido! Digite novamente!")
      time.sleep(1)
    
  elif opcao == "3":
    try:
      ano = int(input("\nDigite o ano da música -> "))
      vet = []
      vetor = cat.search_ano(ano,vet)
      if vetor != None:
        for mus in vetor:
          print(f"{mus.nome}-{mus.album}-{mus.ano}")
      
        time.sleep(10)
      else:
        print("Música não encontrada!!")
        time.sleep(1)
      vet = []
    except ValueError:
      print("Valor inválido! Digite novamente!")
      time.sleep(2)  
  
  
  elif opcao == "4":
    vetor = []
    vet = cat.listar_ordem(cat.root,vetor)
    if vet != None:
      for m in vet: 
        print(f"{m}")
      time.sleep(10)
    else:
      print("Musicas não encontradas!!")
      time.sleep(1)
    vetor = []
  
  elif opcao == "5":
    
    print(f"\n A altura da arvore é -> {cat.altura(cat.root)}")
    time.sleep(2)
    
  elif opcao == "6":
    try:
      
     cat.exibir_Arvore()
     print()
     time.sleep(10)
    except AttributeError:
      print("Arvore Vazia!!")
      time.sleep(2)
  
  elif opcao == "7":
    exit(0)
  else:
    print("Opção inválida! Digite Novamente!")
    time.sleep(1)
   
