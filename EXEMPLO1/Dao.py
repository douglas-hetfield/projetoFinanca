import sqlite3
from EXEMPLO1.Model import Pessoa
class GerenteBanco(object):
    _nomeBanco_ = "pessoa.db"
    _conexao_ = None
    _sqlTabela1_          = "CREATE TABLE FINANCA(" \
                                         "NOMEGASTO    TEXT, " \
                                         "NUMPARCELA INTEGER, " \
                                         "MESINICIAL INTEGER, " \
                                         "MESATUAL INTEGER, " \
                                         "TOTAL REAL) " \

    _sqlInsereTabela1_    = "INSERT INTO FINANCA(NOMEGASTO, NUMPARCELA , MESINICIAL, MESATUAL, TOTAL) " \
                                         "VALUES(?,?,?,?,?)"

    _sqlConsultaTabela11_ = "SELECT NOMEGASTO, NUMPARCELA , MESINICIAL, MESATUAL, TOTAL " \
                            "FROM FINANCA"

    _sqlConsultaTabela12_ = "SELECT NOMEGASTO, NUMPARCELA , MESINICIAL, MESATUAL, TOTAL " \
                            "FROM FINANCA" \
                            "WHERE NOMEGASTO = ?"

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

    def armazenaFinanca(self,financa):
        registro =(financa._nomeGasto_, financa._numPrestacao_, financa._mesInicial_, financa._mesAtual_, financa._total_)
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
