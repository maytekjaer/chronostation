class Cliente:
    def __init__(self, id_, nome, idade, chrono, pais, ano_destino, anos_visitados, maldicao):
        self.id = int(id_)
        self.nome = nome
        self.idade = int(idade)
        self.chrono = float(chrono)
        self.pais = pais
        self.ano_destino = int(ano_destino)
        # anos_visitados: lista de ints
        self.anos_visitados = anos_visitados
        # maldicao: bool
        self.maldicao = bool(maldicao)  #alterei aqui pra ficar no formato bool

    def para_linha(self):
        # Formato consistente com o gerador: id;nome;idade;chrono;pais;ano;[anos];maldicao
        return f"{self.id};{self.nome};{self.idade};{self.chrono};{self.pais};{self.ano_destino};{self.anos_visitados};{self.maldicao}\n"

    def __repr__(self):
        return f"{self.nome} ({self.idade}a) -> {self.pais} {self.ano_destino} | Chrono:{self.chrono} | Maldicao:{self.maldicao}"

    def __str__(self):
        return f"ID:{self.id:^6} | {self.nome:<22} ({self.idade}a) -> {self.pais:^15} {self.ano_destino} | Chrono:{self.chrono:.2f} | Maldicao:{self.maldicao}" #aqui eu só mudei pra tambem mostrar o ID e centralizar os clientes certinho
