from EXEMPLO1.Financa import Financa
from tkinter import Tk,Label,Entry,Button, Listbox, END


class ViewPessoa(object):
    _janelaPrincipal_ = Tk()
    _janelaPrincipal_.title("Controle de finanças V1.0")
    _janelaPrincipal_.resizable(width=False, height=False)

    _nomeGastoLabel_    = None
    _numParcelaLabel_   = None
    _mesInicialLabel_   = None
    _mesAtualLabel_     = None
    _totalLabel_        = None
    _totalMesLabel_     = None

    _nomeGastoEntry_    = None
    _numPrestacaoEntry_ = None
    _mesInicialEntry_   = None
    _mesAtualEntry_     = None
    _totalEntry_        = None
    _totalDoMesEntry_   = None

    _inserirButton_     = None
    _carregarButton_    = None

    _financaListBox_    = None
    row_format = "{:<8}  {:>8}  {:<8}  {:8}  {:8}  {:8}"

    _mediaSalLabel_     = None
    _mediaButton_       = None
    def lerFinanca(self):
        nomeGasto   = self._nomeGastoEntry_.get()
        numParcela  = int(self._numPrestacaoEntry_.get())
        mesInicial  = int(self._mesInicialEntry_.get())
        mesAtual    = int(self._mesAtualEntry_.get())
        total = float(self._totalEntry_.get())

        financa  = Financa(nomeGasto,numParcela,mesInicial,mesAtual,total)
        return financa

    def adicionaFinanca(self,financa):
        # print(str(financa._nomeGasto_)+ "    "+str(financa._mesInicial_))
        sizeNome = len(financa._nomeGasto_)
        spaceNome = 30 - sizeNome

        sizeNumPrestacao = len(str(financa._numPrestacao_))
        spaceNumPrestacao = 33 - sizeNumPrestacao

        sizeMesInicial = len(str(financa._mesInicial_))
        spaceMesInicial = 26 - sizeMesInicial

        sizeMesAtual = len(str(financa._mesAtual_))
        spaceMesAtual = 26 - sizeMesAtual

        sizeTotal = len(str(financa._total_))
        spaceTotal = 28 - sizeTotal

        valorPorMes = float(float(financa._total_) / int(financa._numPrestacao_))

        self._financaListBox_.insert(END, financa._nomeGasto_+" "*spaceNome+ str(financa._numPrestacao_)+" "*spaceNumPrestacao+str(financa._mesInicial_)+" "*spaceMesInicial+str(financa._mesAtual_)+" "*spaceTotal+ str(valorPorMes) + " "*spaceMesAtual+str(financa._total_))

        # self._financaListBox_.insert(END,financa)

    def limpar(self):
        self._nomeGastoEntry_.delete(0, END)
        self._numPrestacaoEntry_.delete(0, END)
        self._mesInicialEntry_.delete(0, END)
        self._mesAtualEntry_.delete(0, END)
        self._totalEntry_.delete(0, END)
        print("Campos limpos")


    def __init__(self,comandoinserir,comandocarregar,relatorio):
        super().__init__()
        self._nomeGastoLabel_   = Label(master=self._janelaPrincipal_, text="Nome do gasto:")
        self._numParcelaLabel_  = Label(master=self._janelaPrincipal_, text="Nº de parcela:")
        self._mesInicialLabel_  = Label(master=self._janelaPrincipal_, text="Mês inícial:")
        self._mesAtualLabel_    = Label(master=self._janelaPrincipal_, text="Mês Atual:")
        self._totalLabel_       = Label(master=self._janelaPrincipal_, text="Total:")
        self._totalMesLabel_    = Label(master=self._janelaPrincipal_, text="total do mês:")

        self._nomeGastoEntry_       = Entry(master=self._janelaPrincipal_, width=60)
        self._numPrestacaoEntry_    = Entry(master=self._janelaPrincipal_, width=60)
        self._mesInicialEntry_      = Entry(master=self._janelaPrincipal_, width=60)
        self._mesAtualEntry_        = Entry(master=self._janelaPrincipal_, width=60)
        self._totalEntry_           = Entry(master=self._janelaPrincipal_, width=60)

        self._financaListBox_ = Listbox(master=self._janelaPrincipal_, width =90)
        headers = ["Gastos                        ", "Nº de Parcelas        ", "Mês Inicial        ", "Mês atual        ", "Total por mês        ", "Total"]
        self._financaListBox_.insert(0, self.row_format.format(*headers, sp=" " * 2))


        self._inserirButton_  = Button(master=self._janelaPrincipal_, text="Inserir", command=comandoinserir)
        self._carregarButton_ = Button(master=self._janelaPrincipal_, text="Listar finanças",command=comandocarregar)
        self._mediaButton_    = Button(master=self._janelaPrincipal_, text="Gerar relatório", command=relatorio)

        self._nomeGastoLabel_.grid(row=1,column=1)
        self._nomeGastoEntry_.grid(row=1,column=2)

        self._numParcelaLabel_.grid(row=2,column=1)
        self._numPrestacaoEntry_.grid(row=2,column=2)

        self._mesInicialLabel_.grid(row=3,column=1)
        self._mesInicialEntry_.grid(row=3,column=2)

        self._mesAtualLabel_.grid(row=4, column=1)
        self._mesAtualEntry_.grid(row=4, column=2)

        self._totalLabel_.grid(row=5, column=1)
        self._totalEntry_.grid(row=5, column=2)


        self._financaListBox_.grid(row=7, column=2)

        self._inserirButton_.grid(row=8,column=1)
        self._carregarButton_.grid(row=8,column=2)
        self._mediaButton_.grid(row=8, column=3)

    def executar(self):
        self._janelaPrincipal_.mainloop()