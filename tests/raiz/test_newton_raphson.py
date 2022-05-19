#
# Cálculo Numérico (2022.1)
# https://github.com/rafaeljc/calculo_numerico
# 

import pytest
import numpy as np
from calculo_numerico import raiz


MSG_RAIZ = 'Valor da raiz diferente do esperado.'
MSG_NUM_ITERACOES = 'Número de iterações diferente do esperado'

f = lambda x: x*np.log10(x) - 1
x0 = 2.5
e = 1e-7

r = 2.5061841455904
num_iteracoes = 2


class TestNewtonRaphson:

    # 'max_iteracoes' negativo
    def test_max_iteracoes(self):
        with pytest.raises(ValueError):
            raiz.newton_raphson(f, x0, e, e, max_iteracoes=-1)

    # raiz
    def test_raiz(self):
        x = raiz.newton_raphson(f, x0, e, e)
        assert np.isclose(x, r), MSG_RAIZ

    # raiz e número de iterações
    def test_raiz_e_num_iteracoes(self):
        x, k = raiz.newton_raphson(f, x0, e, e, retorna_iteracoes=True)
        assert np.isclose(x, r), MSG_RAIZ
        assert k == num_iteracoes, MSG_NUM_ITERACOES
