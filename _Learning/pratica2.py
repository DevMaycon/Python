""" 
Estudando Lambda
    0. (IMPORTANTE)
        Tente usar list comprehension em todas as funções

    1. Manter o Codigo Limpo Para melhor entendimento da
        logica feita.
        
    2. Adicionar Comentarios Sobre oque está sendo feito
        Em cada função anonima ou lambda.
"""

# Retornar numero de quadrados perfeitos
squares = lambda x: [i**2 for i in range(1, x)] if x > 0 else "Error"

root1 = 10
root2 = 3
root3 = 0

print(f'Os quadrados de 1 ate {root1} são', squares(root1))
print(f'Os quadrados de 1 ate {root2} são', squares(root2))
print(f'Os quadrados de 1 ate {root3} são', squares(root3))