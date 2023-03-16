NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escalas
        tonalidade: Tonalidade da escala

    Raises:
        ValueError: Caso a tônica não seja uma nota válida
        KeyError: Caso a escala não exista ou não tenha sido implementada

    Returns:
        Um dicionários com as notas da escala e os graus.

    Examples:
        >>> escalas ('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()

    try:
        tonica_pos = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            f'Essa escala não existe, tente uma dessas {list(ESCALAS.keys())}'
        )

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
