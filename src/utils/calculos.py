def calcular_tempo_entrega(total):
    if total <= 50:
        return 1, 3
    elif total <= 100:
        return 2, 5
    elif total <= 150:
        return 3, 6
    elif total <= 200:
        return 5, 8
    else:
        return 6, 10
