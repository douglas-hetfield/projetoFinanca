from EXEMPLO1.View import ViewPessoa
from EXEMPLO1.Dao import GerenteBanco
from EXEMPLO1.Financa import Financa
from tkinter import messagebox

class Controlador(object):
    _pessoaView_    = None
    _gerenteBanco_  = None
    _pessoaLida_    = None
    _listaCorrente_ = []
    row_format = "{:<8}  {:>8}  {:<8}  {:8}  {:8}  {:8}"

    def inserePessoa(self):
        self._pessoaLida_ = self._pessoaView_.lerFinanca()
        self._gerenteBanco_.armazenaFinanca(self._pessoaLida_)
        self._pessoaView_.adicionaFinanca(self._pessoaLida_)
        self._listaCorrente_.append(self._pessoaLida_)
        self._pessoaView_.limpar()

    def recuperaPessoas(self):
        totMes = 0
        porMes = 0

        self._pessoaView_._financaListBox_.delete(0, 'end')

        headers = ["Gastos                        ", "Nº de Parcelas        ", "Mês Inicial        ",
                   "Mês atual        ", "Total por mês        ", "Total"]
        self._pessoaView_._financaListBox_.insert(0, self.row_format.format(*headers, sp=" " * 2))

        lista = self._gerenteBanco_.retornaListaPessoas()
        for linha in lista:
            financa = Financa(linha[0],linha[1],linha[2],linha[3],linha[4])
            porMes = linha[4] / linha[1]
            totMes = totMes + porMes
            self._pessoaView_.adicionaFinanca(financa)
            self._listaCorrente_.append(financa)
        self._pessoaView_._totMesLabel_['text'] = "Total do mês: " + str(round(totMes, 2))

    def relatorio(self):
        arquivo = open('relatorio.txt', 'w')
        lista = self._gerenteBanco_.retornaListaPessoas()
        for linha in lista:
            # print(str(linha[0]) + "  -   "+str(linha[1])+"    -   "+str(linha[2])+"   =    "+str(linha[3])+"   --  "+str(linha[4]))
            arquivo.write("Nome do gasto: "+str(linha[0])+ "   -    Nº de parcelas: " +str(linha[1])+"   -    Mês Inicial: " +str(linha[2])+"   -    Mês Atual: " +str(linha[3])+"   -    Total: " +str(linha[4])+ "\n")
        arquivo.close()
        messagebox.showinfo("Alerta", "Relatório gerado com sucesso.")


    def executarEx6(self):
        self._gerenteBanco_ = GerenteBanco()
        self._pessoaView_ = ViewPessoa(self.inserePessoa,
                                       self.recuperaPessoas,
                                       self.relatorio)
        self._pessoaView_.executar()
