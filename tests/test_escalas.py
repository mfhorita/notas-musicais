"""
AAA / A3 / 3A

Arranger - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escalas


def test_escala_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Agir
    result = escalas(tonica, tonalidade)

    # Garantir
    assert result


def test_escala_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escalas(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]

    # assert False
    # print(error)


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = (
        f'Essa escala não existe, tente uma dessas {list(ESCALAS.keys())}'
    )

    with raises(KeyError) as error:
        escalas(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escalas(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'

    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escalas(tonica, tonalidade)

    assert resultado['graus'] == esperado
