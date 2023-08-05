""" 
Estudando List Comprehension (Em funçoes ou não)
    1. Tente Apenas Retornar os valores e não armazenar
        variaveis desnecessarias.
    
    2. Manter o Codigo Limpo Para melhor entendimento da
        logica feita
        
    3. Adicionar Comentarios Sobre oque está sendo feito
        Em cada list comprehension
"""

def nota_media(medias: list):
    # Esta lista retornará à soma das notas
    # dividida pela quantidade de notas fornecidas
    return round((sum(medias) / len(medias)), 1) if medias else "nota não foi imformada".title()
    
# Teste a função com algumas notas

notas_aluno1 = [8, 7, 9, 6, 8]
notas_aluno2 = [6, 5, 7]
notas_aluno3 = []

print("Média do Aluno 1:", nota_media(notas_aluno1))
print("Média do Aluno 2:", nota_media(notas_aluno2))
print("Média do Aluno 3:", nota_media(notas_aluno3))
