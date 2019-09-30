from EXEMPLO1.View import ViewPessoa
from EXEMPLO1.Dao import GerenteBanco
from EXEMPLO1.Model import Pessoa

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

    def recuperaPessoas(self):
        lista = self._gerenteBanco_.retornaListaPessoas()
        for linha in lista:
            pessoa = Pessoa(linha[0],linha[1],linha[2])
            self._pessoaView_.adicionaFinanca(pessoa)
            self._listaCorrente_.append(pessoa)

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
