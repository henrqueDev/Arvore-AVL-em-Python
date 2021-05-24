from musica import Musica
class Catalogo:

    def __init__(self):
          self.__root = None
          

    @property
    def root(self):
      return self.__root

      

    def search_id(self, chave ):
        if(self.__root != None):
          return self.__procurar_id(chave, self.__root)
        else:
          return None

    def __procurar_id(self, chave, node):
        if ( chave == node.id):
          return node
        elif ( chave < node.id and node.esq != None):
          return self.__procurar_id( chave, node.esq )
        elif ( chave > node.id and node.dir != None):
          return self.__procurar_id( chave, node.dir)
        else:
          return None    

    def search_ano(self, chave,vet):
        if( self.__root != None ):
          return self.__procurar_ano(chave, self.__root,vet)
        else:
          return None

    def __procurar_ano(self, chave, node,vet):
        if (chave == node.ano):
           vet.append(node)
        if (node.esq != None):
           self.__procurar_ano( chave, node.esq,vet)
        if (node.dir != None):
           self.__procurar_ano( chave, node.dir,vet)
        
        return vet
        
       
        



    def inserir(self, name,album,data,id):
      if self.search_id(id) == None and id > 0 :
          nome_cap = name.strip().capitalize()
          novo = Musica(nome_cap,data,album,id) 
          if self.__root == None:
               self.__root = novo
               self.__root.executaBalanco()
          else: 
               atual = self.__root
               while True:
                    anterior = atual
                    if id <= atual.id: 
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo                                               
                                self.__root.executaBalanco()
                                
                                return
                    
                    else: 
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo                       
                                 self.__root.executaBalanco()
                                 
                                 return
                    # fim da condição ir a direita
      else:
        print("ID inválido ou já existe!")


    def listar_ordem(self,node,vetor):
      if node != None:
        if node == self.__root:
          vetor.append(node.nome)
        if node.esq != None:
          vetor.append(node.esq.nome)
          self.listar_ordem(node.esq,vetor)
        if node.dir != None:
          vetor.append(node.dir.nome)
          self.listar_ordem(node.dir,vetor)  
        vetor.sort()
        return vetor
    
    def draw_arv_hor(self,node,dept,direita,path):
      if node == None:
        return
      dept += 1
      self.draw_arv_hor(node.dir,dept,1,path)
      path[dept - 2] = 0
      
      if direita:
        path[dept - 2] = 1
      if node.esq:
        path[dept-1] = 1
      print()
      for i in range(dept-1):
        if i == dept -2:
          print("+",end = "")
        elif path[i]:
          print("|",end = "")
        else:
          print(" ",end = "")
        for j in range(5):
          if i < (dept -2):  
            print(" ",end="")
          else:
            print("-",end="")
        
      print(node.id)
      for i in range(dept):
        
        if path[i]:
          print("|",end = "")
        else:
          print(" ",end = "")
        for j in range(5):
          print(" ",end ="")
      self.draw_arv_hor(node.esq,dept,0,path)


    def exibir_Arvore(self):
      if self.__root != None:
       p = list(range(255))
       return self.draw_arv_hor(self.__root,0,0,p)
    def altura(self,raiz):
     if raiz is None:
       return 0
     return max(self.altura(raiz.esq), self.altura(raiz.dir)) + 1
    
    def is_balanceada(self,raiz):
    # Uma árvore binária vazia é balanceada.
      if raiz is None:
          return True
      altura_esq = self.altura(raiz.esq)
      altura_dir = self.altura(raiz.dir)
      # Alturas diferem em mais de uma unidade.
      if abs(altura_esq - altura_dir) > 1:
        return False

      return self.balanceada(raiz.esq) and self.balanceada(raiz.dir)
    
    
    
    
    """
    def preorder(self, node, retlst = []):
        #if retlst is None:
        #    retlst = []
        retlst.append(node.id)
        if node.esq:
            retlst = self.preorder(node.esq, retlst) 
        if node.dir:
            retlst = self.preorder(node.dir, retlst)
        return retlst         
           
    def inorder(self, node, retlst = None):
        if retlst is None:
            retlst = [] 
        if node.esq:
            retlst = self.inorder(node.esq, retlst)
        retlst += [node.id] 
        if node.dir:
            retlst = self.inorder(node.dir, retlst)
        return retlst
        
    def postorder(self, node, retlst = None):
        if retlst is None:
            retlst = []
        if node.esq:
            retlst = self.postorder(node.esq, retlst) 
        if node.dir:
            retlst = self.postorder(node.dir, retlst)
        retlst += [node.id]
        return retlst
    


    def em_ordem(self, arvore):
        if arvore != None:
          self.em_ordem(arvore.esq)
          print(arvore.dado, end='')  #Visita a raiz
          self.em_ordem(arvore.dir)
    """