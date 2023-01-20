class Ordinal:

    numero: int = 0
    apocopado: bool = False

    unidades: list[str] = ["", "primero", "segundo", "tercero", "cuarto",
                           "quinto", "sexto", "séptimo", "octavo", "noveno"]
    decenas: list[str] = ["", "décimo", "vigésimo", "trigésimo", "cuadragésimo",
                          "quincuagésimo", "sexagésimo", "septuagésimo", "octogésimo", "nonagésimo"]
    centenas: list[str] = ["", "centésimo", "ducentésimo", "tricentésimo", "cuadringentésimo",
                           "quingentésimo", "sexcentésimo", "septingentésimo", "octingentésimo", "noningentésimo"]

    def __init__(self, numero: int, apocopado: bool = False) -> None:
        if numero == 0:
            raise ValueError("El número debe ser mayor a 0")
        if numero > 999:
            raise ValueError("El número debe ser menor a 1000")
        self.numero: int = numero
        self.apocopado: bool = apocopado

        if self.apocopado:
            self.unidades[1] = "primer"
            self.unidades[3] = "tercer"

    def __repr__(self) -> str:
        unidades = self.numero % 10
        decenas = (self.numero // 10) % 10
        centenas = (self.numero // 100) % 10

        if decenas == 0:
            repr = f"{self.unidades[unidades]}"
        elif centenas == 0:
            repr = f"{self.decenas[decenas]} {self.unidades[unidades]}"
        else:
            repr = f"{self.centenas[centenas]} {self.decenas[decenas]} {self.unidades[unidades]}"
        return repr
