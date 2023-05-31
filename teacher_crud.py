from neo4j import GraphDatabase


class TeacherCRUD:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_teacher(self, name, ano_nasc, cpf):
        with self.driver.session() as session:
            session.run("CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf}) RETURN t.id as id", name=name, ano_nasc=ano_nasc, cpf=cpf)

    def update_teacher(self, name, newCpf):
        with self.driver.session() as session:
            session.run("MATCH (t:Teacher) WHERE (t.name = $name) SET t.cpf = $cpf", name=name, cpf=newCpf)

    def delete_teacher(self, name):
        with self.driver.session() as session:
            session.run("MATCH (t:Teacher) WHERE t.name = $name DETACH DELETE t", name=name)

    def get_teacher(self, name):
        with self.driver.session() as session:
            result = session.run("MATCH (t:Teacher) WHERE (t.name = $name) RETURN t.name as name, t.cpf as cpf, t.ano_nasc as ano", name=name)
            return [{"Name": record["name"], "cpf": record["cpf"], "Ano_nasc": record["ano"]} for record in result]