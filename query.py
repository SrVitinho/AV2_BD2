class Searches:
    def __init__(self, database):
        self.db = database

    def get_renzo(self):
        query = "match (t:Teacher {name: 'Renzo'}) return t.ano_nasc as nasc, t.cpf as CPF"
        results = self.db.execute_query(query)
        nascimento = [result["nasc"] for result in results]
        cpf_renzo = [result["CPF"] for result in results]
        return cpf_renzo, nascimento

    def get_teacher_with_m(self):
        query = "match (t:Teacher) where (t.name starts with 'M' ) return t.cpf as CPF, t.name as nome"
        results = self.db.execute_query(query)
        cpf = [result["CPF"] for result in results]
        nomes = [result["nome"] for result in results]
        return cpf, nomes

    def get_cities(self):
        query = "match (c:City) return c.name as nome"
        results = self.db.execute_query(query)
        cidades = [result["nome"] for result in results]
        return cidades

    def get_school(self):
        query = "match (s:School) where (s.number >= 150 AND s.number <= 550) return s.address as end, s.name as nome, s.number as num"
        results = self.db.execute_query(query)
        endereco = [result["end"] for result in results]
        nomes = [result["nome"] for result in results]
        numero = [result["num"] for result in results]
        return endereco, nomes, numero

    def get_youngest_oldest(self):
        query = "match (t:Teacher) return t.ano_nasc as ano_min order by t.ano_nasc limit 1"
        results = self.db.execute_query(query)
        anos_min = [result["ano_min"] for result in results]
        query = "match (t:Teacher) return t.ano_nasc as ano_max order by t.ano_nasc desc limit 1"
        results = self.db.execute_query(query)
        anos_max = [result["ano_max"] for result in results]
        string_anos_min = f"menor ano {anos_min}"
        string_anos_max = f"maior ano {anos_max}"
        return string_anos_min, string_anos_max

    def get_average_population(self):
        query = "match (c:City) return avg(c.population) as population"
        results = self.db.execute_query(query)
        return [result["population"] for result in results]

    def get_cep(self):
        query = "match (c:City {cep: '37540-000'}) return c.name as name"
        results = self.db.execute_query(query)
        nome_raw = [result["name"] for result in results]
        nome = nome_raw[0].replace("a", "A")
        return nome

    def get_an_weird_name(self):
        query = "match (t:Teacher) return t.name as nome"
        results = self.db.execute_query(query)
        nome_raw = [result["nome"] for result in results]
        nomes = []
        for nome in nome_raw:
            nomes.append(nome[3])
        return nomes