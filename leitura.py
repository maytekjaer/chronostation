import ast

from cliente import Cliente
from ast import literal_eval

def ler_arquivo(path):
    clientes = []
    with open(path, "r", encoding='utf-8') as f:
        for linha in f:

            partes = linha.split(";")

            id_, nome, idade, chrono, pais, ano_dest, anos_str, mald = partes[:8]

            anos_str = ast.literal_eval(anos_str)
            mald = ast.literal_eval(mald.strip())
            cliente = Cliente(id_ , nome, idade, chrono, pais, ano_dest, anos_str, mald)
            clientes.append(cliente)
    return clientes