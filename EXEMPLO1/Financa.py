class Financa(object):
    _nomeGasto_     = None
    _numPrestacao_  = None
    _mesInicial_    = None
    _mesAtual_      = None
    _total_         = None
    _totalDoMes_    = None
    def __init__(self,nomeGasto,numPretacao,mesInicial,mesAtual,total) -> None:
        super().__init__()
        self._nomeGasto_    = nomeGasto
        self._numPrestacao_ = numPretacao
        self._mesInicial_   = mesInicial
        self._mesAtual_     = mesAtual
        self._total_        = total

    def __str__(self) -> str:
        return self._nomeGasto__

    def linhaArquivo(self):
        linha = "Nome do gasto: " + self._nomeGasto__ + " | Nº de prestação: " + str(self._numPrestacao__) + " | Mês inícial: " + str(self._mesInicial__) + " | Mês atual: " + str(self._mesAtual_) + "Total do mês: " + str(self._totalDoMes_) + " | Total: " + str(self._total_) + "\n"
        return linha

    def linhaArquivo2(self):
        linha = "{0},{1},{2:5.2f} \n".format(self._nomeGasto__,self._numPrestacao__,self._total__)
        return linha
