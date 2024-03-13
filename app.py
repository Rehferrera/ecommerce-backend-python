import os
restaurantes = [{'nome':'Dupão','categoria':'panificação','ativo':True},
                {'nome':'Pomodora','categoria':'italiana','ativo':True},
                {'nome':'Beiçola','categoria':'boteco','ativo':True}]


def exibir_nome_do_programa():
    
    print("""
            
█▀█ ▄▀█ █▄░█ █▀▀ █▀█   █▀▀ ▄▀█ █▀ ▀█▀
█▀▄ █▀█ █░▀█ █▄█ █▄█   █▀░ █▀█ ▄█ ░█░ 
""")

def exibir_opcoes():

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar restaurante')
    print('4. Sair\n')


def input_incorreto_menu_principal():
    print('Você digitou uma opção inválida!\n')
    input('Digite a tecla Enter para voltar ao menu\n')
    main()

def voltar_ao_menu_principal():
    input('\nDigite "Enter" para voltar ao menu\n')
    main()


def opcao_invalida():
    print('opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system ('cls')
    linha ='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    '''Essa função é responsável para alterar o estado do restaurante de ativo/inativo
    
    INPUT: 
    - Nome do restaurante

    OUTPUT: Altera estado de ativo/inativo do restaurante
    
    '''

    exibir_subtitulo('Alteranando estado do restaurante....')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] 
            else f'O restaurante {nome_restaurante} foi desativado com sucesso')
            print(mensagem)
            voltar_ao_menu_principal()

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')



def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    INPUT:
    - Nome do restaurante

    OUTPUT
    - Inclui o restaurante a lista
    

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados '''

    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()
        
       


def escolher_opcao():
    '''Essa função é responsável por escolher a opção do menu principal
    
    INPUT:
    - Opção de 1 a 4 

    OUTPUT:
    - Executa a função escolhida
    
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            input_incorreto_menu_principal()
    except: 
        input_incorreto_menu_principal()

def finalizar_app():
    '''Essa função é responsável por finalizar o aplicativo'''

    exibir_subtitulo('Finalizando o app')
    voltar_ao_menu_principal()
    

def main():
    '''Essa função é responsável em limpar os prompts das variáveis abaixo'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()