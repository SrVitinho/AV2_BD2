from neo4j import GraphDatabase
from Database import Database
from query import Searches
# Configuração da conexão com o Neo4j
db=Database("bolt://34.205.69.38:7687", "neo4j", "sediments-gate-gunfire")

Search=Searches(db)

print(Search.get_renzo())
print(Search.get_teacher_with_m())
print(Search.get_cities())
print(Search.get_school())
print(Search.get_youngest_oldest())
print(Search.get_average_population())
print(Search.get_cep())
print(Search.get_an_weird_name())
