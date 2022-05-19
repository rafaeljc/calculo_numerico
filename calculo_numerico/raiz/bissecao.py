#
# Cálculo Numérico (2022.1)
# https://github.com/rafaeljc/calculo_numerico
# 

import numpy as np


def bissecao(
    f,
    intervalo_inicial,
    e,
    retorna_iteracoes = False,
    max_iteracoes = 1_000,
):
    """Método da Bisseção

    Args:
        f: Função f(x).
        intervalo_inicial: Intervalo [a, b].
        e: Precisão de |b - a|.
        retorna_iteracoes (optional = False): Passe 'True' caso deseje o retorno
            do número de iterações feitas.
        max_iteracoes: Número máximo de iterações.

    Return:
        Valor aproximado da raiz de f(x) no intervalo [a, b] e, caso
            'retorna_iteracoes' = True, o número de iterações.
        Caso o limite de iterações seja atingido, será retornado None e, caso
            'retorna_iteracoes' = True, o número de iterações.

    Raise:
        ValueError: f(a) e f(b) tem o mesmo sinal.
        ValueError: max_iteracoes é negativo.
    """
    a, b = intervalo_inicial

    # validações
    if not (f(a)*f(b) < 0.):
        raise ValueError('f(a) e f(b) precisam ter sinais opostos para garantir'
            + ' a existência de pelo menos uma raiz no intervalo [a, b].')
    if max_iteracoes < 0:
        raise ValueError('O argumento max_iteracoes não pode ser negativo.')

    def _prepara_retorno(raiz, num_iteracoes):
        if retorna_iteracoes:
            return raiz, num_iteracoes
        return raiz

    # (1)
    # se o intervalo [a, b] for pequeno o suficiente, o valor aproximado da raiz
    # será qualquer número pertencente a este intervalo
    if (b - a) < e:
        raiz = np.random.uniform(a, b)
        return _prepara_retorno(raiz, 0)

    m = f(a)
    for k in range(1, max_iteracoes + 1):
        x = (a + b) / 2
        # reduzindo o intervalo [a, b]
        if m*f(x) > 0:
            a = x
        else:
            b = x
        # vide comentário (1)
        if (b - a) < e:
            raiz = np.random.uniform(a, b)
            return _prepara_retorno(raiz, k)
            
    return _prepara_retorno(None, max_iteracoes)
