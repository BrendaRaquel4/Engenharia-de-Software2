from triangle import Triangle, TriangleType

def test_scalene():
    # Todos os lados diferentes: 3, 4 e 5
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE