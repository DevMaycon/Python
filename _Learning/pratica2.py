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
squares = lambda x: [i**2 for i in range(1, x)] if x > 0 else "Numero Abaixo de 0. Não está permitido!"

root1 = 10
root2 = 3
root3 = 0

print(f'Os quadrados de 1 ate {root1} é', squares(root1))
print(f'Os quadrados de 1 ate {root2} é', squares(root2))
print(f'Os quadrados de 1 ate {root3} é', squares(root3))


# Criação de Rank Basico

rank = [
    {'nome': 'zoão',
        'xp': 600
    },
    {'nome': 'alice',
        'xp': 700
    },
    {'nome': 'Pedro',
        'xp': 1200
    }
    ]
# Ordenando o rank
ordened_rank = sorted(rank, key=lambda x:  (-(x['xp'] * 120), x['nome']))

# Mostrando o rank
print([(int(x['pontos'] * 120)) for x in ordened_rank])