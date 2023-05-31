from neo4j import GraphDatabase
from Database import Database
from query import Searches
from teacher_crud import TeacherCRUD

# Configuração da conexão com o Neo4j
db = Database("bolt://34.205.69.38:7687", "neo4j", "sediments-gate-gunfire")
cli = TeacherCRUD("bolt://34.205.69.38:7687", "neo4j", "sediments-gate-gunfire")

Search = Searches(db)
# 1 e 2
print(Search.get_renzo())
print(Search.get_teacher_with_m())
print(Search.get_cities())
print(Search.get_school())
print(Search.get_youngest_oldest())
print(Search.get_average_population())
print(Search.get_cep())
print(Search.get_an_weird_name())

# 3
cli.create_teacher('Cris Lima', 1956, '189.052.396-66')
print('--------------------')
print(cli.get_teacher('Cris Lima'))
print('--------------------')
cli.update_teacher('Cris Lima', "162.052.777-77")
print(cli.get_teacher('Cris Lima'))
print('--------------------')
cli.delete_teacher('Cris Lima')  # eu adicionei pra que possa ser rodado multiplas vezes
