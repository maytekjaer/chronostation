from cliente import Cliente
from leitura import ler_arquivo

def salvar():
    with open(arq, 'w', encoding='utf-8') as f:
        for cliente in clientes:
            f.write(cliente.para_linha())

def carregar(arquivo):      #carrega um arquivo e define a lista dos clientes como global para que todas as funções acessem à ele
    global clientes, arq
    arq = arquivo
    clientes = ler_arquivo(arq)

clientes = []
arq = None

def criar_cliente():
    print('Insira os seguintes dados:')
    id = max([c.id for c in clientes], default=0)+1     #procura qual o maior ID existente e faz com que o novo cliente tenha esse maior +1
    nome = input('Nome e sobrenome: ')
    idade = int(input('Idade: '))
    lugar = input('Local de destino: ')
    ano = int(input('Ano de destino: '))
    chrono_jumper = float(input('Versão do ChronoJumper: '))
    maldicao = True if int(input('Possui a maldição do tempo?\n[1]Sim\n[0]Não\nR: ')) == 1 else False
    anos_visitados = list(map(int, input('Anos visitados(caso seja a primeira vez viajando digite 0): ').split()))
    cliente = Cliente(id, nome, idade, chrono_jumper, lugar, ano, anos_visitados, maldicao)
    clientes.append(cliente)
    print('Cliente criado com sucesso!')

def buscar_cliente(id):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    return None
        
def lista_clientes():
    for cliente in clientes:
        print(cliente)

def atualizar_cliente():
    lista_clientes()
    cliente = buscar_cliente(int(input('Digite o Index do cliente que deseja atualizar: '))) 
    if cliente == None:
        print('ID inválido.')
        return
    alteracoes = list(map(int, input('[0]Nome\n[1]Idade\n[2]Lugar de destino\n[3]Ano de destino\n[4]Versão do ChronoJumper\n[5]Maldição\n[6]Anos visitados\nDigite os campos que deseja alterar(separados por espaço): ').split()))
    for mudanca in alteracoes:
        if mudanca == 0:
            nome = input('Nome e sobrenome: ')
            cliente.nome = nome
        elif mudanca == 1:
            idade = int(input('Idade: '))
            cliente.idade = idade
        elif mudanca == 2:
            pais = input('Local de destino: ')
            cliente.pais = pais
        elif mudanca == 3:
            ano_destino = int(input('Ano de destino: '))
            cliente.ano_destino = ano_destino
        elif mudanca == 4:
            chrono = float(input('Versão do ChronoJumper: '))
            cliente.chrono = chrono
        elif mudanca == 5:
            maldicao = True if int(input('Possui a maldição do tempo?\n[1]Sim\n[0]Não\nR: ')) == 1 else False
            cliente.maldicao = maldicao
        elif mudanca == 6:
            anos_visitados = list(map(int, input('Anos visitados(caso seja a primeira vez viajando digite 0): ').split()))
            cliente.anos_visitados = anos_visitados
    print('Cliente Atualizado!')

def deletar_cliente():
    lista_clientes()
    id = int(input('Digite o ID do cliente que deseja excluir: '))
    cliente = buscar_cliente(id)
    if cliente == None:
        print('ID inválido')
    else:
        print(cliente)
        r = int(input(f'Tem certeza que deseja excluir esse cliente?[1]Sim[2]Não\nR: '))
        if r == 1:
            clientes.remove(cliente)
            print('Cliente Removido!')
        else:
            return