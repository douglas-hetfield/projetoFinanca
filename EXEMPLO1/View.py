from EXEMPLO1.Financa import Financa
from tkinter import Tk,Label,Entry,Button, Listbox, END
class ViewPessoa(object):
    _janelaPrincipal_ = Tk()
    _nomeGastoLabel_    = None
    _numParcelaLabel_   = None
    _mesInicialLabel_ = None

    _nomeEntry_     = None
    _idadeEntry_    = None
    _salarioEntry_  = None

    _pessoaListBox_  = None

    _inserirButton_  = None
    _carregarButton_ = None

    _mediaSalLabel_  = None
    _mediaButton_    = None
    def lerFinanca(self):
        nomeGasto   = self._nomeEntry_.get()
        numParcela  = int(self._idadeEntry_.get())
        mesInicial  = int(self._salarioEntry_.get())
        mesAtual    = int(self._mesAtualEntry_.get())
        total = float(self._mesAtualEntry_.get())

        financa  = Financa(nomeGasto,numParcela,mesInicial,mesAtual,total)
        return financa

    def adicionaFinanca(self,financa):
        self._financaListBox_.insert(END,financa)

    def mostraMedia(self,media):
        self._mediaSalLabel_["text"] = "Media R$: " + str(media)

    def __init__(self,comandoinserir,comandocarregar,mediasalario):
        super().__init__()
        self._nomeGastoLabel_   = Label(master=self._janelaPrincipal_, text="Nome do gasto:")
        self._numParcelaLabel_  = Label(master=self._janelaPrincipal_, text="Nº de parcela:")
        self._mesInicialLabel_  = Label(master=self._janelaPrincipal_, text="Mês inícial:")
        self._mesAtualLabel_    = Label(master=self._janelaPrincipal_, text="Mês Atual:")
        self._totalLabel_       = Label(master=self._janelaPrincipal_, text="Total:")
        self._totalMesLabel_    = Label(master=self._janelaPrincipal_, text="total do mês:")

        self._nomeEntry_    = Entry(master=self._janelaPrincipal_, width=20)
        self._idadeEntry_   = Entry(master=self._janelaPrincipal_, width=5)
        self._salarioEntry_ = Entry(master=self._janelaPrincipal_, width=6)

        self._pessoaListBox_ = Listbox(master=self._janelaPrincipal_)


        self._inserirButton_  = Button(master=self._janelaPrincipal_, text="Inserir", command=comandoinserir)
        self._carregarButton_ = Button(master=self._janelaPrincipal_, text="Carregar",command=comandocarregar)
        self._mediaButton_    = Button(master=self._janelaPrincipal_, text="Media Salarios", command=mediasalario)

        self._nomeLabel_.grid(row=1,column=1)
        self._nomeEntry_.grid(row=1,column=2)

        self._idadeLabel_.grid(row=1,column=3)
        self._idadeEntry_.grid(row=1,column=4)

        self._salarioLabel_.grid(row=2,column=1)
        self._salarioEntry_.grid(row=2,column=2)

        self._mediaSalLabel_.grid(row=2, column=3)

        self._pessoaListBox_.grid(row=5, column=2)

        self._inserirButton_.grid(row=3,column=1)
        self._carregarButton_.grid(row=3,column=2)
        self._mediaButton_.grid(row=3, column=3)

    def executar(self):
        self._janelaPrincipal_.mainloop()