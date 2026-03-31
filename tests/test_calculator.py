from app.calculator import sum, resta

def test_sum() -> None:
    assert sum(2, 3) == 5       ## if true: la prueba pasó, completa y retorna None
                                ## if false: raise AssertionError

def test_resta() -> None:
    assert resta(5, 3) == 2