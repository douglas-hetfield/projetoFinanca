from EXEMPLO1.Financa import Financa
from tkinter import Tk,Label,Entry,Button, Listbox, END
class ViewPessoa(object):
    _janelaPrincipal_ = Tk()
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
        print(financa)
        self._financaListBox_.insert(END,financa)

    def __init__(self,comandoinserir,comandocarregar,mediasalario):
        super().__init__()
        self._nomeGastoLabel_   = Label(master=self._janelaPrincipal_, text="Nome do gasto:")
        self._numParcelaLabel_  = Label(master=self._janelaPrincipal_, text="Nº de parcela:")
        self._mesInicialLabel_  = Label(master=self._janelaPrincipal_, text="Mês inícial:")
        self._mesAtualLabel_    = Label(master=self._janelaPrincipal_, text="Mês Atual:")
        self._totalLabel_       = Label(master=self._janelaPrincipal_, text="Total:")
        self._totalMesLabel_    = Label(master=self._janelaPrincipal_, text="total do mês:")

        self._nomeGastoEntry_       = Entry(master=self._janelaPrincipal_, width=20)
        self._numPrestacaoEntry_    = Entry(master=self._janelaPrincipal_, width=20)
        self._mesInicialEntry_      = Entry(master=self._janelaPrincipal_, width=20)
        self._mesAtualEntry_        = Entry(master=self._janelaPrincipal_, width=20)
        self._totalEntry_           = Entry(master=self._janelaPrincipal_, width=20)

        self._financaListBox_ = Listbox(master=self._janelaPrincipal_, width =40)


        self._inserirButton_  = Button(master=self._janelaPrincipal_, text="Inserir", command=comandoinserir)
        self._carregarButton_ = Button(master=self._janelaPrincipal_, text="Carregar",command=comandocarregar)
        self._mediaButton_    = Button(master=self._janelaPrincipal_, text="Media Salarios", command=mediasalario)

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