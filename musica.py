class BinaryTreeException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)


class Musica:
  def __init__(self,nome,ano,album,id):
    self.__nome = nome
    self.__ano = ano
    self.__album = album
    self.__id = id # Hashing????
    self.__esq = None
    self.__dir = None

  #Metodos de Setar atributos  ******NAO OLHE NÃO RECOMENDO*******  

  def setter_esq_dir(self, esquerda, direita): #Metodo de setar os apontadores self.__esq e self.__dir
    self.__esq = esquerda
    self.__dir = direita
  



  def set_atr_dir(self): #Metodo para setar/trocar os valores durante uma rotação para a esquerda
    self.__nome,self.__ano,self.__album,self.__id, self.__dir.__nome, self.__dir.__ano,self.__dir.__album,self.__dir.__id = self.__dir.__nome,self.__dir.__ano,self.__dir.__album,self.__dir.__id , self.__nome,self.__ano, self.__album,self.__id


  def set_atr_esq(self):#Metodo para setar/trocar os valores durante uma rotação para a direita
    self.__nome,self.__ano,self.__album,self.__id, self.__esq.__nome, self.__esq.__ano,self.__esq.__album,self.__esq.__id = self.__esq.__nome,self.__esq.__ano,self.__esq.__album,self.__esq.__id , self.__nome,self.__ano, self.__album,self.__id

   
  # GETTERS E SETTERS
  @property
  def ano(self):
    return self.__ano
  @ano.setter
  def ano(self,novo):
    self.__ano = novo

  @property
  def nome(self):
    return self.__nome
  
  # set
  @nome.setter
  def nome(self,new_nome):
    self.__nome = new_nome
  # get
  @property
  def esq(self):
    return self.__esq
  
  # set
  @esq.setter
  def esq(self, novo):
    if self.__esq != None:
      raise BinaryTreeException('O nó esquerdo já existe')
    else:
      self.__esq = novo
  @property
  def album(self):
    return self.__album
  @album.setter
  def album(self,novo):
    self.__album = novo
  # get
  @property
  def dir(self):
    return self.__dir
  
  # set
  @dir.setter
  def dir(self, novo):
    if self.dir != None:
      raise BinaryTreeException('O nó direito já existe')
    else:
      self.__dir = novo

  @property
  def id(self):
    return self.__id
  @id.setter
  def id(self,novo):
    self.__id = novo

#METODOS PARA BALANCEAMENTO

  def balanco(self):
        prof_esq = 0
        if self.esq:
            prof_esq = self.esq.profundidade()
        prof_dir = 0
        if self.dir:
            prof_dir = self.dir.profundidade()
        return prof_esq - prof_dir

  def profundidade(self):
        prof_esq = 0
        if self.__esq:
            prof_esq = self.__esq.profundidade()
        prof_dir = 0
        if self.__dir:
            prof_dir = self.__dir.profundidade()
        return 1 + max(prof_esq, prof_dir)

  def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.__esq.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.__dir.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()



#METODOS DE ROTAÇÃO



  def rotacaoEsquerda(self): #Troca os valores dos atributos do objeto com o objeto da sua direita
        
        self.set_atr_dir()
        
        old_esq = self.__esq  #Armazena o objeto da esquerda na variavel
        self.setter_esq_dir(self.dir, self.dir.dir)#Seta os objetos do nó atual (self.dir.dir na direita e self.dir na esquerda)
        self.__esq.setter_esq_dir(old_esq, self.__esq.__esq)#Seta os objetos da esquerda do nó atual (old_esq na esquerda e self.esq.esq na direita)

  def rotacaoDireita(self): #Troca os valores dos atributos do objeto com o objeto da sua esquerda
        
        self.set_atr_esq()
        old_dir = self.__dir  #Armazena o objeto da direita na variavel
        self.setter_esq_dir(self.__esq.__esq, self.__esq) #Seta os objetos do nó atual (self.esq.esq na esqueda e self.esq na direita) 
        self.__dir.setter_esq_dir(self.__dir.__dir, old_dir)#Seta os objetos da direita do nó atual (self.dir.dir na esquerda da direita  e old_dir na direita )

  def rotacaoEsquerdaDireita(self):
        self.__esq.rotacaoEsquerda()
        self.rotacaoDireita()

  def rotacaoDireitaEsquerda(self):
        self.__dir.rotacaoDireita()
        self.rotacaoEsquerda()

 
  """
  def max_height(self):
        if self.__esq and self.__dir:
            return max(self.__esq.__height, self.__dir.__height)
        elif self.__esq and not self.__dir:
            return self.__esq.__height
        elif not self.__esq and  self.__dir:
            return self.__dir.__height
        else:
            return -1
  """  

  def __str__(self):
    return f"{self.__id}"
