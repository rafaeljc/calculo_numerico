#
# Cálculo Numérico (2022.1)
# https://github.com/rafaeljc/calculo_numerico
# 

import numpy as np


def secante(
    f, 
    x0, 
    x1, 
    e1, 
    e2, 
    retorna_iteracoes = False,
    max_iteracoes=1_000,
):
    """Método da Secante

    Args:
        f: Função f(x).
        x0: Primeiro ponto de aproximação inicial.
        x1: Segundo ponto de aproximação inicial.
        e1: Precisão de |f(x)|.
        e2: Precisão de |x1 - x0|.
        retorna_iteracoes (optional = False): Passe 'True' caso deseje o retorno
            do número de iterações feitas.
        max_iteracoes (optional = 1_000): Número máximo de iterações.

    Return:
        Valor aproximado da raiz de f(x) e, caso 'retorna_iteracoes' = True, o 
            número de iterações.
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
    # se o valor de f(x1) ou |x1 - x0| forem pequenos o suficiente,
    # o valor aproximado da raiz será x1        
    if (np.abs(f(x1)) < e1) or (np.abs(x1 - x0) < e2):
        return _prepara_retorno(x1, 0)

    for k in range(1, max_iteracoes + 1):
        x2 = x1 - (f(x1)/(f(x1) - f(x0)) * (x1 - x0))
        # se o valor de f(x2) ou |x2 - x1| forem pequenos o suficiente,
        # o valor aproximado da raiz será x2
        if (np.abs(f(x2)) < e1) or (np.abs(x2 - x1) < e2):
            return _prepara_retorno(x2, k)
        x0 = x1
        x1 = x2
        
    return _prepara_retorno(None, max_iteracoes)
