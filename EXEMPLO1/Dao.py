import sqlite3
from EXEMPLO1.Model import Pessoa
class GerenteBanco(object):
    _nomeBanco_ = "pessoa.db"
    _conexao_ = None
    _sqlTabela1_          = "CREATE TABLE PESSOA(" \
                                         "NOME    TEXT, " \
                                         "SALARIO REAL, " \
                                         "IDADE   INTEGER)"

    _sqlInsereTabela1_    = "INSERT INTO PESSOA(NOME, SALARIO , IDADE) " \
                                         "VALUES(?,?,?)"

    _sqlConsultaTabela11_ = "SELECT NOME, SALARIO , IDADE " \
                            "FROM PESSOA"

    _sqlConsultaTabela12_ = "SELECT NOME, SALARIO , IDADE) " \
                            "FROM PESSOA" \
                            "WHERE NOME = ?"

    def __init__(self) -> None:
        super().__init__()
        self._conexao_ = sqlite3.connect(self._nomeBanco_)
        cursor = self._conexao_.cursor()
        try:
            cursor.execute(self._sqlTabela1_)
            self._conexao_.commit()
        except:
            print("Banco já criado - Criacao desconsiderada")
        cursor.close()
    def armazenaFinanca(self,pessoa):
        registro =(pessoa._nomePessoa_, pessoa._salarioPessoa_, pessoa._idadePessoa_)
        cursor = self._conexao_.cursor()
        cursor.execute(self._sqlInsereTabela1_,registro)
        self._conexao_.commit()
        cursor.close()
    def retornaListaPessoas(self):
        # OBS: a virgula vazia é necessaria para diferenciar o
        # () matematico do () de tupla
        cursor = self._conexao_.cursor()
        cursor.execute(self._sqlConsultaTabela11_)
        listaTuplas = cursor.fetchall()
        self._conexao_.commit()
        cursor.close()
        return listaTuplas
    def retornaListaPessoasNome(self,pessoa):
        # OBS: a virgula vazia é necessaria para diferenciar o
        # () matematico do () de tupla
        consulta = (pessoa._nomePessoa_,)
        cursor = self._conexao_.cursor()
        cursor.execute(self._sqlConsultaTabela12_, consulta)
        listaTuplas = cursor.fetchall()
        self._conexao_.commit()
        cursor.close()
        return listaTuplas
