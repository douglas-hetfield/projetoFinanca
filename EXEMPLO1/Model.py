class Pessoa(object):
    _nomePessoa_    = None
    _idadePessoa_   = None
    _salarioPessoa_ = None
    def __init__(self,nome,idade,salario) -> None:
        super().__init__()
        self._nomePessoa_    = nome
        self._idadePessoa_   = idade
        self._salarioPessoa_ = salario
    def __str__(self) -> str:
        return self._nomePessoa_
    def linhaArquivo(self):
        linha = self._nomePessoa_ + ", " + str(self._idadePessoa_) + ", " + str(self._salarioPessoa_) + " \n"
        return linha
    def linhaArquivo2(self):
        linha = "{0},{1},{2:5.2f} \n".format(self._nomePessoa_,self._idadePessoa_,self._salarioPessoa_)
        return linha
