from src.pre_built.counter import count_ocurrences


def test_counter():
    'Recebendo uma string qualquer deve retornar o número de letras'
    assert count_ocurrences('data/jobs.csv', 'Time') == 7331
