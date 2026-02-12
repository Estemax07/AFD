import sys

# Estados
Q1, Q2, Q3 = 1, 2, 3

def delta(state: int, symbol: str) -> int:
    
    if state == Q1:
        return Q2 if symbol == "0" else Q3  
    if state == Q2:
        return Q2 
    return Q3    

def acepta(linea: str) -> bool:
    w = linea.strip()

    #Cadena vacia
    if w == "":
        return False

    #Validacion de solo 0 y 1
    for ch in w:
        if ch not in ("0", "1"):
            return False

    estado = Q1
    for ch in w:
        estado = delta(estado, ch)

    return estado == Q2


def main() -> int:
    #"solo imprimir ACEPTA o NO ACEPTA"
    if len(sys.argv) != 2:
        return 1

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            for linea in f:
                print("ACEPTA" if acepta(linea) else "NO ACEPTA")
    except Exception:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
