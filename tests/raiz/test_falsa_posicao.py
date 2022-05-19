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
i = (2., 3.)
e = 1e-7

np.random.seed(37508150)
r = 2.5061840264492
num_iteracoes = 5


class TestFalsaPosicao:    
    
    # f(a) e f(b) tem o mesmo sinal
    def test_fa_fb(self):
        novo_intervalo = (2., 2.1)
        with pytest.raises(ValueError):
            raiz.falsa_posicao(f, novo_intervalo, e, e)

    # 'max_iteracoes' negativo
    def test_max_iteracoes(self):
        with pytest.raises(ValueError):
            raiz.falsa_posicao(f, i, e, e, max_iteracoes=-1)

    # raiz
    def test_raiz(self):
        x = raiz.falsa_posicao(f, i, e, e)
        assert np.isclose(x, r), MSG_RAIZ

    # raiz e número de iterações
    def test_raiz_e_num_iteracoes(self):
        x, k = raiz.falsa_posicao(f, i, e, e, retorna_iteracoes=True)
        assert np.isclose(x, r), MSG_RAIZ
        assert k == num_iteracoes, MSG_NUM_ITERACOES
  