from LineaTelefonica import LineaTelefonica

class TestLineaTelefonica:

    def setup_method(self, method):
        self.linea = LineaTelefonica() 

    def test_agregarLlamadaCelular(self):
        
        self.linea.agregarLlamadaCelular(10)
        assert self.linea.darNumeroLlamadas() == 1
        assert self.linea.darNumeroMinutos() == 10
        assert self.linea.darCostoLlamadas() == 9990

    def test_agregarLlamadaLocal(self):
        self.linea.agregarLlamadaLocal(5)
        assert self.linea.darNumeroLlamadas() == 1
        assert self.linea.darNumeroMinutos() == 5
        assert self.linea.darCostoLlamadas() == 175

    def test_agregarLlamadaLargaDistancia(self):
        self.linea.agregarLlamadaLargaDistancia(7)
        assert self.linea.darNumeroLlamadas() == 1
        assert self.linea.darNumeroMinutos() == 7
        assert self.linea.darCostoLlamadas() == 2660

    def test_reiniciar(self):
        self.linea.agregarLlamadaLargaDistancia(7)
        self.linea.Reiniciar()
        assert self.linea.darNumeroLlamadas() == 0
        assert self.linea.darNumeroMinutos() == 0
        assert self.linea.darCostoLlamadas() == 0
