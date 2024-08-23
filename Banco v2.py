# -*- coding: utf-8 -*-
"""
BANCO V2 - Created on Thu Aug 22 22:10:11 2024

@author: luca_

Esse programa foi feito para ser submetido como solução da aula "otimizando o sistema bancário com funções"

O programa não realiza as ações para uma dada conta, pois isso não foi especificado no exercício.
"""


from datetime import datetime, date

LIMITE_SAQUES = 3
limite = 500
extrato = ''
saques = 0 
saldo = 0.00
lista_usuario = []
lista_cc = []

def sacar(*,extrato=extrato, saldo=saldo, limite=limite, saques=saques):
    
        saque = float(input('Digite o valor do saque\nPor favor, utilize o fomrato XXX.XX\n'))
        saque = float("{:.2f}".format(saque))
    
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        if saque > limite: 
            print('Saque não realizado. Limite por saque é de R$500.00')
            extrato += dt_string + ' SAQUE NÃO EFETUADO: R$' + f'{saque:.2f}' + '\n'

        elif saque > saldo: 
            print(f'Saldo insuficiente. Seu saldo atual é R${saldo:.2f}\n')
            extrato += dt_string + ' SAQUE NÃO EFETUADO: R$' + f'{saque:.2f}' + '\n'

        else:
            saldo -= saque
            saques += 1

            extrato += dt_string + ' SAQUE: R$' + f'{saque:.2f}' + '\n'

        return extrato, saldo, saques

'''
procurando o motivo, satackoverflow me diz que argumentos posicionais não funcionam nas versões anteriores à 3.8, 
colocar o / nos argumentos da função gera erro de sintaxe.

def depositar(extrato, saldo, /): 

  File "<ipython-input-19-bec83d296d27>", line 38
    def depositar(extrato, saldo,/):
                                 ^
SyntaxError: invalid syntax
'''
    
def depositar(extrato, saldo): 

    deposito = float(input('Digite o valor do depósito\nPor favor, utilize o fomrato XXX.XX\n'))
    
    if deposito > 0:
        saldo += deposito

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        extrato += dt_string + ' DEPÓSITO: R$' + f'{deposito:.2f}' + '\n'
    else:
        print('Valor inválido para depósito.\n')
        
    return extrato, saldo


def mostrar_extrato(extrato,*,saldo=saldo):
    if extrato == '':
        print('Sem operações recentes\n')
    else:
        print('\nEXTRATO:\n\n'  + extrato + f'\nSALDO: R${saldo:.2f}' + '\n---------------\n')

def verifica_usuario(cpf, lista_usuario):
    for i in range(len(lista_usuario)):
        if lista_usuario[i]['cpf'] == cpf: 
            return usuario    
    return False

def verifica_cc(cpf, lista_cc):
    cc_usuario = []
    for i in range(len(lista_cc)):
        if lista_cc[i]['usuario']['cpf'] == cpf:
            cc_usuario.append(lista_cc[i]['nro_conta'])
            
    if cc_usuario == []:
        return False
    else:
        return cc_usuario

def formata_endereco():
    rua = input('informe a rua de residência:\n')
    nro = input('informe o número da residência:\n')
    bairro = input('informe o bairro da residência:\n')
    cidade = input('informe a cidade de residência:\n')
    estado = input('informe a sigla do estado de residência:\n')
    endereco = rua +','+nro+' - ' + bairro +' - '+cidade+'/'+estado
    return endereco
    
    
def formata_nascimento():
    ano = int(input('informe o ano do seu nascimento:\n'))
    mes = int(input('informe o número do mês do seu nascimento:\n'))
    dia = int(input('informe o número do dia do seu nascimento:\n'))
    nascimento = date(ano, mes, dia)
    return nascimento

def novo_usuario(lista_usuario):
    usuario={}
    usuario['nome'] = input('Digite o seu nome:\n')
    usuario['cpf'] = input('Digite o seu cpf (apenas números):\n')
    
    if verifica_usuario(usuario['cpf'], lista_usuario):
        print ('Usuario já existente---------------------\n')
        return None
    
    usuario['nascimento'] = formata_nascimento().strftime("%d/%m/%Y")
    usuario['endereço'] = formata_endereco()
    print('Usuário cadastrado!---------------------\n')
    return usuario
    
def nova_cc(lista_cc, lista_usuario):
    cc = {}
    cpf = input('Digite seu cpf (apenas números):\n')
    contas_criadas = verifica_cc(cpf, lista_cc)
    if contas_criadas:
        print('Contas já registradas nesse cpf:\n')
        for item in contas_criadas:
            print(item)
            
    cc['usuario'] = verifica_usuario(cpf, lista_usuario)
    
    if not cc['usuario']:
        print('Usuario não encontrado.---------------------\n')
        
    cc['agencia'] = '0001'
    cc['nro_conta'] = input('Digite o número da conta\n')
    print('Conta Cadastrada!---------------------\n')
    return cc
    
def todos_usuarios(lista_usuarios):
    print('\nLista de usuários:\n')
    if lista_usuarios != []:
        for item in lista_usuarios:
            for key,value in item.items():
                print(f'{key}: {value}')
            print('\n')
    else:
        print('Sem usuários cadastrados\n')
        
def todas_cc(lista_cc):
    print('\nLista de CC:\n')
    if lista_cc != []:
        for item in lista_cc:
            for key,value in item.items():
                print(f'{key}: {value}')
            print('\n')
    else:
        print('Sem CC cadastradas')
        
menu = '''
Escolha a operação desejada: ---------------------

Conta Existente:
[s] -> Saque
[d] -> Depósito
[e] -> Extrato

Criar Conta:
[u] -> Adicionar usuário
[c] -> Adicionar conta-corrente

Lista:
[lu] -> Lista Usuarios
[lc] -> Lista cc

[q] -> Sair ---------------------

'''

print('BEM VINDO!')

while True:

    print(menu)
    user = str(input())
    
    if user == 'u' or user == 'U':
        usuario = novo_usuario(lista_usuario)
        if usuario:
            lista_usuario.append(usuario)
            
    elif user == 'c' or user == 'C':
        cc = nova_cc(lista_cc, lista_usuario)
        lista_cc.append(cc)
        
    elif user == 'lu' or user == 'LU':
        todos_usuarios(lista_usuario)
        
    elif user == 'lc' or user == 'LC':
        todas_cc(lista_cc)

    elif user == 'd' or user == 'D':       
        extrato, saldo = depositar(extrato, saldo)

    elif user == 'e' or user == 'E':
        mostrar_extrato(extrato, saldo=saldo)

    elif user == 's' or user == 'S':        
        if saques >= LIMITE_SAQUES: 
            print('Limite de saques diários excedido.\n')
        else:            
            extrato, saldo, saques = sacar(extrato=extrato, saldo=saldo, saques=saques)
                
    elif user == 'q' or user == 'Q':
        print('Obrigado por utilizar o sistema\nEncerrando...')
        break
        
    else: 
        print('Opção inválida. Por favor, escolha uma das opções listadas no Menu:\n')