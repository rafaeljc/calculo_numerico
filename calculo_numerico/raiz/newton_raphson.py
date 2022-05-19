#
# Cálculo Numérico (2022.1)
# https://github.com/rafaeljc/calculo_numerico
# 

import numpy as np


def newton_raphson(
    f, 
    x0, 
    e1, 
    e2, 
    retorna_iteracoes = False,
    max_iteracoes=1_000,
):
    """Método de Newton-Raphson

    Args:
        f: Função f(x).
        x0: Ponto de aproximação inicial.
        e1: Precisão de |f(x)|.
        e2: Precisão de |x1 - x0|.
        retorna_iteracoes (optional = False): Passe 'True' caso deseje o retorno
            do número de iterações feitas.
        max_iteracoes (optional = 1_000): Número máximo de iterações.

    Return:
        Valor aproximado da raiz de f(x) mais próxima do ponto x0 e, caso
            'retorna_iteracoes' = True, o número de iterações.
        Caso o limite de iterações seja atingido, será retornado None e, caso
            'retorna_iteracoes' = True, o número de iterações.

    Raise:
        ValueError: max_iteracoes é negativo.
    """
    # validação
    if max_iteracoes < 0:
        raise ValueError('O argumento max_iteracoes não pode ser negativo.')

    def _prepara_retorno(raiz, num_iteracoes):
        if retorna_iteracoes:
            return raiz, num_iteracoes
        return raiz

    # se o valor de f(x0) for próximo o suficiente, o valor aproximado da 
    # raiz será x0
    if np.abs(f(x0)) < e1:
        return _prepara_retorno(x0, 0)

    dfdx = lambda x: (f(x + e2) - f(x - e2)) / (2*e2)
    for k in range(1, max_iteracoes + 1):
        # verificando o valor da derivada em x0
        # evitar uma divisão por zero
        dfdx_x0 = dfdx(x0)
        if np.abs(dfdx_x0) > e1:
            x1 = x0 - f(x0)/dfdx_x0
            x_w = x0
        else:
            x1 = x0 - f(x0)/dfdx(x_w)
        # se o valor de f(x1) ou |x1 - x0| forem pequenos o suficiente,
        # o valor aproximado da raiz será x1
        if (np.abs(f(x1)) < e1) or (np.abs(x1 - x0) < e2):
            return _prepara_retorno(x1, k)
        x0 = x1

    return _prepara_retorno(None, max_iteracoes)
