""" 
Estudando Lambda
    1. Manter o Codigo Limpo Para melhor entendimento da
        logica feita.
        
    2. Adicionar Comentarios Sobre oque está sendo feito
        Em cada função anonima ou lambda.
"""

# Retornar numero de quadrados perfeitos
squares = lambda x: [i**2 for i in range(1, x)]
print(squares(11))
