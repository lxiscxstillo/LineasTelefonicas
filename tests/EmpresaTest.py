from Empresa import Empresa

class TestEmpresa:

    def setup_method(self, method):
        self.empresa = Empresa()

    def setup_escenario1(self):
        self.empresa = Empresa()

    def setup_escenario2(self):
        self.empresa = Empresa()

        self.empresa.agregarLlamadaLocalLinea1(1)
        self.empresa.agregarLlamadaLargaDistanciaLinea1(2)
        self.empresa.agregarLlamadaCelularLinea1(3)

        self.empresa.agregarLlamadaLocalLinea2(10)
        self.empresa.agregarLlamadaLargaDistanciaLinea2(20)
        self.empresa.agregarLlamadaCelularLinea2(30)

        self.empresa.agregarLlamadaLocalLinea2(100)
        self.empresa.agregarLlamadaLargaDistanciaLinea2(200)
        self.empresa.agregarLlamadaCelularLinea2(300)

    def test_inicializacion(self):
        self.setup_escenario1()
        assert self.empresa.darLinea1() is not None
        assert self.empresa.darLinea2() is not None
        assert self.empresa.darLinea3() is not None

    def test_agregarLlamadaLocalLinea1(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLocalLinea1(10)
        assert self.empresa.darLinea1().darNumeroLlamadas() == 1

    def test_agregarLlamadaLocalLinea2(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLocalLinea2(10)
        assert self.empresa.darLinea2().darNumeroLlamadas() == 1

    def test_agregarLlamadaLocalLinea3(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLocalLinea3(10)
        assert self.empresa.darLinea3().darNumeroLlamadas() == 1

    def test_agregarLlamadaLargaDistanciaLinea1(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLargaDistanciaLinea1(10)
        assert self.empresa.darLinea1().darNumeroLlamadas() == 1

    def test_agregarLlamadaLargaDistanciaLinea2(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLargaDistanciaLinea2(10)
        assert self.empresa.darLinea2().darNumeroLlamadas() == 1

    def test_agregarLlamadaLargaDistanciaLinea3(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaLargaDistanciaLinea3(10)
        assert self.empresa.darLinea3().darNumeroLlamadas() == 1

    def test_agregarLlamadaCelularLinea1(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaCelularLinea1(10)
        assert self.empresa.darLinea1().darNumeroLlamadas() == 1

    def test_agregarLlamadaCelularLinea2(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaCelularLinea2(10)
        assert self.empresa.darLinea2().darNumeroLlamadas() == 1

    def test_agregarLlamadaCelularLinea3(self):
        self.setup_escenario1()
        self.empresa.agregarLlamadaCelularLinea3(10)
        assert self.empresa.darLinea3().darNumeroLlamadas() == 1

    def test_darTotalNumeroLlamadas(self):
        self.setup_escenario2()
        assert self.empresa.darTotalNumeroLlamadas() == 9

    def test_darTotalMinutos(self):
        self.setup_escenario2()
        assert self.empresa.darTotalMinutos() == 666

    def test_darTotalCosto(self):
        self.setup_escenario2()
        assert self.empresa.darTotalCostoLlamadas() == 420912

    def test_dar_costo_promedio(self):
        self.setup_escenario2()
        assert self.empresa.darCostoPromedioMinuto() == 632

    def test_reiniciar(self):
        self.setup_escenario2()
        self.empresa.reiniciar()
        assert self.empresa.darTotalNumeroLlamadas() == 0
        assert self.empresa.darTotalMinutos() == 0
        assert self.empresa.darTotalCostoLlamadas() == 0
