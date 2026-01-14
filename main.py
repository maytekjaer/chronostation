import crud
import time

sections = [
    "1. Sobre a Chronostation\n\n"
    "A Chronostation é a autoridade central responsável pela fiscalização, regulamentação e auditoria de todas as atividades relacionadas a viagens temporais. Fundada com o propósito de garantir segurança operacional, estabilidade histórica e total rastreabilidade dos deslocamentos no tempo, a instituição atua como o principal órgão certificador de viajantes e tecnologias cronológicas.\n"
    "Seu trabalho inclui o registro padronizado de destinos, identidades, janelas temporais autorizadas e relatórios pós-viagem, assegurando que qualquer movimentação temporal atenda às normas internacionais de conservação de linha temporal. A Chronostation mantém ainda departamentos de compliance, monitoramento e atendimento ao viajante, garantindo transparência, controle e continuidade dos protocolos que preservam a integridade da malha temporal.",

    "2. Sobre o Chronojumper\n\n"
    "O Chronojumper é o dispositivo regulamentado pela Chronostation para realização de deslocamentos temporais. Projetado em formato de relógio de pulso, ele combina interface intuitiva com sistemas internos de estabilização temporal, permitindo ao usuário selecionar e executar viagens certificadas de forma segura.\n"
    "Existem diferentes versões do aparelho — como 1.0, 1.5, 2.3, entre outras — cada uma marcada por atualizações técnicas e estéticas. Versões superiores apresentam materiais mais refinados, maior precisão de salto e camadas adicionais de redundância, refletindo um padrão “premium” de navegação temporal. Independentemente da versão, todos os modelos passam por auditoria da Chronostation antes de serem liberados para uso.",

    "3. Sobre a Maldição do Tempo\n\n"
    "A chamada Maldição do Tempo é uma condição reconhecida pela Chronostation que acomete indivíduos submetidos a excesso de viagens temporais ao longo da vida. Embora não seja classificada oficialmente como patologia degenerativa, trata-se de um desgaste perceptível nos padrões cognitivos e de estabilidade temporal do viajante.\n"
    "Os sintomas variam, mas são frequentemente associados a episódios de desorientação cronológica, lapsos de memória ligados a diferentes linhas de viagem e dificuldade gradual de adaptação ao tempo nativo. A Chronostation mantém protocolos de acompanhamento desses indivíduos, reforçando políticas de limitação de viagens e fornecendo suporte técnico e administrativo quando necessário, a fim de reduzir impactos operacionais e garantir a segurança contínua do fluxo temporal.",

    "Programa de regulamentação — simplicidade intencional\n\n"
    "A Chronostation mantém um programa central de regulamentação de viagens temporais cuja principal diretriz é garantir clareza operacional entre diferentes eras, níveis tecnológicos e condições históricas. Por esse motivo, o sistema foi projetado de forma deliberadamente simples, priorizando estruturas lógicas universais que possam ser compreendidas por viajantes oriundos de múltiplas linhas do tempo.\n"
    "Essa simplicidade não representa limitação, mas sim um princípio estratégico: um programa leve, direto e padronizado reduz falhas de interpretação, facilita auditorias intertemporais e permite que cada civilização — independentemente do período em que se encontra — integre o protocolo com o mínimo de adaptação técnica. Assim, a Chronostation assegura que a gestão dos deslocamentos temporais permaneça acessível, estável e funcional através de séculos, realidades paralelas e diferentes estágios de desenvolvimento científico."
]


print(" $$$$$$\\  $$\\                                                $$$$$$\\    $$\\                $$\\     $$\\                     ")
print("$$  __$$\\ $$ |                                              $$  __$$\\   $$ |               $$ |    \\__|                    ")
print("$$ /  \\__|$$$$$$$\\   $$$$$$\\   $$$$$$\\  $$$$$$$\\   $$$$$$\\  $$ /  \\__|$$$$$$\\    $$$$$$\\ $$$$$$\\   $$\\  $$$$$$\\  $$$$$$$\\  ")
print("$$ |      $$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\ \\$$$$$$\\  \\_$$  _|   \\____$$\\\\_$$  _|  $$ |$$  __$$\\ $$  __$$\\ ")
print("$$ |      $$ |  $$ |$$ |  \\__|$$ /  $$ |$$ |  $$ |$$ /  $$ | \\____$$\\   $$ |     $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ |")
print("$$ |  $$\\ $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\\   $$ |  $$ |$$\\ $$  __$$ | $$ |$$\\ $$ |$$ |  $$ |$$ |  $$ |")
print("\\$$$$$$  |$$ |  $$ |$$ |      \\$$$$$$  |$$ |  $$ |\\$$$$$$  |\\$$$$$$  |  \\$$$$  |\\$$$$$$$ | \\$$$$  |$$ |\\$$$$$$  |$$ |  $$ |")
print(" \\______/ \\__|  \\__|\\__|       \\______/ \\__|  \\__| \\______/  \\______/    \\____/  \\_______|  \\____/ \\__| \\______/ \\__|  \\__|")
print("                                                                                                                            ")
print("                                                                                                                            ")
print("                                                                                                                            ")


print('Bem vindo(a) à ChronoStation')
arq = int(input('''Qual arquivo deseja manipular?
[1]Pqueno
[2]Médio
[3]Grande
[4]Gigante
R: '''))

if arq == 1:
    arquivo = 'database\pequeno.txt'
elif arq == 2:
    arquivo = 'database/medio.txt'
elif arq == 3:
    arquivo = 'database/grande.txt'
elif arq == 4:
    arquivo = 'database/gigante.txt'

#carrega o arquivo
inicio = time.time()
crud.carregar(arquivo)
fim = time.time()
tempo = fim - inicio
print(f'Tempo de carregamento do arquivo: {tempo:.4f}')


#loop principal
while True:
    print(
        '''
        ===Menu de Ações===
        [1]Listar Clientes
        [2]Buscar Cliente
        [3]Criar Cliente
        [4]Atualizar Cliente
        [5]Deletar Cliente
        [6]Sobre a ChronoStation
        [7]Sair
        '''
    )
    r = int(input('R: '))

    if r == 1:
        inicio = time.time()
        crud.lista_clientes()
        fim = time.time()
        tempo = fim - inicio
        print(f'Tempo de execução de listagem: {tempo:.4f}')

    elif r == 2:
        id_busca = int(input('Insira o ID do cliente que deseja buscar: '))
        inicio = time.time()
        c = crud.buscar_cliente(id_busca)
        fim = time.time()
        tempo = fim - inicio
        print(c)
        print(f'Tempo de execução da busca: {tempo:.4f}')

    elif r == 3:
        inicio = time.time()
        crud.criar_cliente()
        fim = time.time()
        tempo = fim - inicio
        print(f'Tempo de execução da criação: {tempo:.4f}')

    elif r == 4:
        inicio = time.time()
        crud.atualizar_cliente()
        fim = time.time()
        tempo = fim - inicio
        print(f'Tempo de execução da atualização: {tempo:.4f}')

    elif r == 5:
        inicio = time.time()
        crud.deletar_cliente()
        fim = time.time()
        tempo = fim - inicio
        print(f'Tempo de execução da exclusão: {tempo:.4f}')

    elif r == 6:
        for sec in sections:
            print(sec)
            print()
            time.sleep(1)

    elif r == 7:
        print('Obrigado por escolher a ChronoStation!')
        break


    inicio = time.time()
    crud.salvar()
    fim = time.time()
    tempo = fim - inicio
    print(f'Tempo de salvamento do arquivo: {tempo:.4f}')
