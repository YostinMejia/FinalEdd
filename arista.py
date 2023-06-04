class Arista:

    def __init__(self, valor, v1, v2) -> None:
        self.valor = valor
        self.v1 = v1
        self.v2 = v2
    
    def __repr__(self) -> str:
        return f"{self.v1}({self.valor})-->{self.v2}"
