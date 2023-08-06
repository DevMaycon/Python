"""PROJETO FEITO POR MAYCON (IDEIAS CHATGPT-3.5)
    1. Contagem de Alunos Aprovados: Crie uma função que receba o ranking atualizado com alunos e suas pontuações.
        A função deve retornar o número de alunos que têm uma pontuação acima de um determinado valor
        (por exemplo, acima de 800 pontos).

    2. Atualização de Dados dos Alunos: Implemente uma função que permita atualizar os dados de um aluno no ranking.
        A função deve receber o nome do aluno e os novos dados, como nome, xp, ou outros campos. Ela deve atualizar os dados 
        desse aluno no ranking.

    3. Remoção de Aluno do Ranking: Crie uma função que remova um aluno específico do ranking com base em seu nome.
        A função deve receber o nome do aluno e remover o registro correspondente do ranking.

    4. Pesquisa de Aluno pelo Nome: Implemente uma função que permita pesquisar um aluno pelo nome no ranking.
        A função deve receber o nome do aluno como argumento e retornar os dados desse aluno.

    5. Calculadora de Média Geral: Crie uma função que receba o ranking atualizado com alunos e suas pontuações.
        A função deve calcular a média geral de xp de todos os alunos no ranking e retornar esse valor.

Lembre-se de usar os conceitos que você aprendeu anteriormente, como list comprehension, funções, e manipulação de dicionários
e listas, para resolver esses desafios. E não hesite em experimentar e testar diferentes abordagens para aprimorar suas 
habilidades de programação. Boa codificação
"""

# Importando Modulos Necessarios (!!Somente o Necessario!!)
from json import load as loadjs, dump as dumpjs
from random import randint as rint, choice as c

# Classe estudante
class SchoolDatabase:
    def __init__(self) -> None:
        self.database_directory = 'database/studentsData.json'
        self.datacache = loadjs(open(self.database_directory))
    
    def update_cache(self) -> None:
        with open(self.database_directory, 'w') as db:
            dumpjs(self.datacache, db, indent=4)
    
    def remove(self, id: str) -> None:
        self.datacache.pop(id)
        self.update_cache()

    def set_points(self, id: str, points: int) -> None:
        self.datacache[str(id)]['points'] = points
        self.update_cache()
        return 'pontuação atualizada para -> '+str(points)
        
    def search(self, id: str) -> None:
        try:
            user = self.datacache[str(id)]
            configs = [f"{i}: {user[i]}" for i in user]
            for i in configs:
                print(i.title())
            del user, configs
            return "Procura Realizada Com Sucesso!"
        except KeyError:
            del user, configs
            return 'ID de aluno não encontrado'
    
    def ranking(self):
        tempcache = {}
        for i, rank in enumerate(sorted(self.datacache, key=lambda id: self.datacache[id]['points'], reverse=True)):
            tempcache[i] = self.datacache[rank]
        self.datacache = tempcache
        for i in self.datacache:
            print(f"{i+1}. -> Nome: {self.datacache[i]['nome']}, Points: {self.datacache[i]['points']}")
        self.update_cache()
        del tempcache
