class Arista:

    def __init__(self, peso, v1, v2) -> None:
        self.peso = peso 
        self.v1 = v1
        self.v2 = v2
    
    def __repr__(self) -> str:
        return f"{self.v1}({self.peso})-->{self.v2}"
