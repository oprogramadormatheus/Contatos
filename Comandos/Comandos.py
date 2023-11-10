import PySimpleGUI as sg

sg.theme('Black')
Cores = ('#FB181D', '#009400', '#4D4D4D')
SG01 = sg.Text('Contato', font=('Verdana', 10, 'bold'), pad=((5, 6), (1, 1)))
SG02 = sg.Text('Telefone', font=('Verdana', 10, 'bold'), pad=((5, 2), (1, 1)))
SG03 = sg.Input(enable_events=False, expand_x=True, expand_y=False, font=('Verdana', 10, 'bold'), key='SG03')
SG04 = sg.Input(enable_events=True, expand_x=True, expand_y=False, font=('Verdana', 10, 'bold'), key='SG04')
SG05 = sg.Input(enable_events=False, expand_x=True, expand_y=False, font=('Verdana', 10, 'bold'), key='SG05')
SG06 = sg.Button('Cadastrar', size=(25, 1), font=('Verdana', 10, 'bold'), key='SG06')
SG07 = sg.Button('Contatos', size=(25, 1),  font=('Verdana', 10, 'bold'), key='SG07')
SG08 = sg.Output(expand_x=True, expand_y=True, font=('Verdana', 10, 'bold'), key='SG08')
Integrantes = [[SG01, SG03], [SG02, SG04], [SG05], [SG06, SG07], [SG08]]
Quadro = sg.Frame('Cadastrar Contatos', Integrantes, expand_x=True, expand_y=True, font=('Verdana', 10, 'bold'))
Interface = [[sg.TabGroup([[sg.Tab('Contatos', [[Quadro]])]], expand_x=True, expand_y=True, font=('Verdana', 10, 'bold'))]]
Janela = sg.Window('Contatos', Interface, size=(500, 300), icon='Logo.ico')

def Encontrar(Base):
    try:
        with open(Base, 'rt'):
            pass
        return True
    except Exception:
        return False

def Gerar(Base):
    with open(Base, 'wt+'):
        pass

def Escrever(Base, Contato):
    with open(Base, 'at') as Contatos:
        Contatos.write('{}\n'.format(Contato))

Base_Contatos = 'Contatos.txt'
if not Encontrar(Base_Contatos):
    Gerar(Base_Contatos)

while True:
    
    def Retornar(Local, Cor, Texto=''):
        Janela[Local].update(background_color=Cor)
        Janela[Local].update(Texto)

    Eventos, Valores = Janela.read()    
    if Eventos == sg.WIN_CLOSED:
        break
    if Eventos == 'SG04':
        Valores_Inseridos = Valores['SG04']
        if not Valores_Inseridos.isnumeric() or len(Valores_Inseridos) > 11:
            Janela['SG04'].update(Valores_Inseridos[:-1])    
    if Eventos == 'SG06':
        Contato_Cadastrar = Valores['SG03']
        Telefone_Cadastrar = Valores['SG04']
        Janela['SG03'].update('')
        Janela['SG04'].update('')
        if len(Contato_Cadastrar) == 0 or len(Telefone_Cadastrar) != 11:
            Retornar('SG05', Cores[0], 'Dados Incorretos')
        else:
            Checar_Contato = Contato_Cadastrar.replace(' ', '')
            if not Checar_Contato.isalpha():
                Retornar('SG05', Cores[0], 'Dados Incorretos')
            else:
                Retornar('SG05', Cores[1], 'Cadastrado')
                Cadastrar_Contato = '{} ({}) {}'.format(Contato_Cadastrar, Telefone_Cadastrar[0:2], Telefone_Cadastrar[2:])
                Escrever(Base_Contatos, Cadastrar_Contato)
    if Eventos == 'SG07':
        Retornar('SG05', Cores[2])
        with open(Base_Contatos, 'rt') as Contatos:
            Mostrar_Cadastrados = Contatos.read()
            Janela['SG08'].update(Mostrar_Cadastrados)    
Janela.close()
