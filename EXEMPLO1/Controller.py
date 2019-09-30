from EXEMPLO1.View import ViewPessoa
from EXEMPLO1.Dao import GerenteBanco
from EXEMPLO1.Financa import Financa

class Controlador(object):
    _pessoaView_    = None
    _gerenteBanco_  = None
    _pessoaLida_    = None
    _listaCorrente_ = []

    def inserePessoa(self):
        self._pessoaLida_ = self._pessoaView_.lerFinanca()
        self._gerenteBanco_.armazenaFinanca(self._pessoaLida_)
        self._pessoaView_.adicionaFinanca(self._pessoaLida_)
        self._listaCorrente_.append(self._pessoaLida_)
        self._pessoaView_.limpar()

    def recuperaPessoas(self):
        lista = self._gerenteBanco_.retornaListaPessoas()
        for linha in lista:
            # print(str(linha[0]) + "  -   "+str(linha[1])+"    -   "+str(linha[2])+"   =    "+str(linha[3])+"   --  "+str(linha[4]))
            financa = Financa(linha[0],linha[1],linha[2],linha[3],linha[4])
            self._pessoaView_.adicionaFinanca(financa)
            self._listaCorrente_.append(financa)

    def mediaSalarios(self):
        media = 0
        for pessoa in self._listaCorrente_:
            media += pessoa._salarioPessoa_
        media = media / len(self._listaCorrente_)
        self._pessoaView_.mostraMedia(media)

    def executarEx6(self):
        self._gerenteBanco_ = GerenteBanco()
        self._pessoaView_ = ViewPessoa(self.inserePessoa,
                                       self.recuperaPessoas,
                                       self.mediaSalarios)
        self._pessoaView_.executar()
