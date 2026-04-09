from triangle import Triangle, TriangleType

def test_isosceles():
    # Dois lados iguais (7) e um diferente (10)
    t = Triangle(7, 7, 10)
    
    # O assert verifica se o código classificou corretamente
    assert t.type == TriangleType.ISOSCELES