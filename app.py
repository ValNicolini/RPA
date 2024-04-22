import os

restaurantes = [{'Nome':'Pizza','Categoria':'Pizzaria', 'Ativo':False},
                {'Nome':'Tomate', 'Categoria':'Legumes', 'Ativo':True},
                {'Nome':'Arroz', 'Categoria':'Grãos', 'Ativo':False}]


def exibir_nome_do_programa():
    print("""NICOLINI
         LANCHES E SUCOS""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_menu_principal():
    input('\nDigite uma tecla pra voltar ao menu inicial: ')
    main()

def exibir_sub_menu(texto):
    print('Teste: ',texto)
def finalizar_app():
    #os.system('cls')
    # os.system('clear') 
    exibir_sub_menu('Finalizando o app')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
   exibir_sub_menu('Cadastro de novos restaurantes:')
   nome_restaurante = input('Nome do restaurante: ')
   nome_categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
   dados_restaurante = {'Nome': nome_restaurante, 'Categoria': nome_categoria, 'Ativo':False}
   restaurantes.append(dados_restaurante)
   print(f'O restaurante {nome_restaurante} foi add com sucesso!')
   voltar_menu_principal()

def listar_restaurantes():
    exibir_sub_menu('Listando os restaurantes:')
    for restaurante in restaurantes:
        print(restaurante)
        nome_restaurante = restaurante['Nome']
        nome_categoria = restaurante['Categoria']
        estado = restaurante['Ativo']
        print(f'{nome_restaurante}, {nome_categoria}, {estado}')
    voltar_menu_principal()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()