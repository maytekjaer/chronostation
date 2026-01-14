import random
import time

NOMES = [
    "Luke", "Anakin", "Leia", "Han", "James", "Indiana", "Marty", "Emmett",
    "Tony", "Pepper", "Peter", "Gwen", "Bruce", "Clark", "Diana", "Jack",
    "Rose", "John", "Ellen", "Sarah", "Frodo", "Samwise", "Gandalf", "Bilbo"
]

SOBRENOMES = [
    "Skywalker", "Organa", "Solo", "Bond", "Jones", "McFly", "Brown", "Stark",
    "Potts", "Parker", "Stacy", "Wayne", "Kent", "Prince", "Dawson",
    "DeWitt Bukater", "Wick", "Ripley", "Connor", "Baggins", "Gamgee", "Grey"
]

PAISES = [
    "Brasil", "Japão", "Canadá", "Austrália", "Noruega", "Egito", "Índia",
    "México", "Itália", "França", "Alemanha", "Chile", "Argentina",
    "Coreia do Sul", "Espanha", "Portugal", "Nova Zelândia",
    "África do Sul", "Suécia", "Finlândia"
]


def gerar_viajante():
    nome = random.choice(NOMES)
    sobrenome = random.choice(SOBRENOMES)

    idade = random.randint(18, 80)

    qtd_viagens = random.randint(0, 10)
    anos_visitados = [random.randint(1000, 4000) for _ in range(qtd_viagens)]

    chrono_version = round(random.uniform(1.0, 5.0), 2)

    maldicao = qtd_viagens > 5

    pais_destino = random.choice(PAISES)
    ano_destino = random.randint(1000, 4000)

    return (
        nome + " " + sobrenome,
        idade,
        anos_visitados,
        chrono_version,
        maldicao,
        pais_destino,
        ano_destino
    )


def gerar_arquivo_viajantes(nome_arquivo, quantidade):
    inicio = time.time()

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for i in range(1, quantidade + 1):
            nome, idade, anos, chrono, mald, pais, ano_dest = gerar_viajante()

            linha = f"{i};{nome};{idade};{chrono};{pais};{ano_dest};{anos};{mald}\n"
            f.write(linha)

    fim = time.time()

    print(f"Arquivo '{nome_arquivo}' gerado com {quantidade} viajantes.")
    print(f"Tempo gasto: {fim - inicio:.3f} segundos\n")


TAMANHOS = {
    "database\pequeno.txt": 1_000,
    "database\medio.txt":   10_000,
    "database\grande.txt":  50_000,
    "database\gigante.txt": 200_000
}

tempos = {}

for arquivo, qtd in TAMANHOS.items():
    gerar_arquivo_viajantes(arquivo, qtd)