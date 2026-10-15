import time


def dibujar_torres(torres, cantidad_discos):
    """Dibuja las torres y los discos en la terminal."""
    ancho = cantidad_discos * 2 + 1
    base = "-" * (ancho + 2)

    print("\nEjemplo visual de las torres:")
    for nivel in range(cantidad_discos - 1, -1, -1):
        fila = []
        for torre in torres:
            if nivel < len(torre):
                disco = torre[nivel]
                dibujo = "=" * (disco * 2 - 1)
                fila.append(dibujo.center(ancho))
            else:
                fila.append("|".center(ancho))
        print("   ".join(fila))
    print("   ".join([base.center(ancho)] * 3))
    print("   ".join(["A".center(ancho), "B".center(ancho), "C".center(ancho)]))


def mover_discos(n, origen, auxiliar, destino, movimientos):
    """Resuelve recursivamente y guarda cada movimiento; usar con pocos discos."""
    if n == 1:
        movimientos.append((origen, destino))
        return
    mover_discos(n - 1, origen, destino, auxiliar, movimientos)
    movimientos.append((origen, destino))
    mover_discos(n - 1, auxiliar, origen, destino, movimientos)


def resolver_hanoi(n):
    """Calcula el numero minimo de movimientos y mide ese calculo."""
    inicio = time.perf_counter()
    movimientos = 2 ** n - 1
    fin = time.perf_counter()
    return movimientos, fin - inicio


def main():
    print("=" * 62)
    print("                 TORRES DE HANOI EN PYTHON")
    print("=" * 62)

    ejemplo = 3
    torres = [list(range(ejemplo, 0, -1)), [], []]
    dibujar_torres(torres, ejemplo)

    movimientos_ejemplo = []
    mover_discos(ejemplo, "A", "B", "C", movimientos_ejemplo)
    print("\nMovimientos del ejemplo de 3 discos:")
    for numero, (origen, destino) in enumerate(movimientos_ejemplo, start=1):
        print(f"{numero}. {origen} -> {destino}")

    print("\nPruebas de rendimiento:")
    print("Se mide el calculo de 2^n - 1, no la ejecucion de cada movimiento.")
    print("Resolver fisicamente todos los movimientos de 30 o 64 discos")
    print("requiere una cantidad impracticable de operaciones.")
    print("\n{:<10} {:<28} {}".format("Discos", "Movimientos minimos", "Tiempo (s)"))
    print("-" * 62)

    for discos in [5, 10, 30, 64]:
        cantidad, duracion = resolver_hanoi(discos)
        print(f"{discos:<10} {cantidad:<28,} {duracion:.10f}")


if __name__ == "__main__":
    main()
