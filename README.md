# Cálculo Numérico (2022.1)
### Exemplo de Uso
```python
from calculo_numerico import raiz

f = lambda x: x**3 - x - 1
i = (1., 2.)
e = 1e-6

raiz.bissecao(f, i, e)
```
