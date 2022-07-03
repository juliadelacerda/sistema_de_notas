aprovados = ['João', 'Maria', 'Pedro', 'Felipe']
na_recuperacao = ['Rafael', 'Maria', 'Lara']
reprovados = ['Igor', 'Henrique', 'Gabriela']


# Função que exibe as listas iniciais de alunos aprovados, de recuperação e reprovados
def mostrarResultados ():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Bem-vindo, professor!')
    print('Turma: 2° ano B')
    print('Turno: Manhã\n')


    print(f'Alunos aprovados: {aprovados}')
    print(f'Alunos que irão para a recuperação: {na_recuperacao}')
    print(f'Alunos reprovados: {reprovados}\n')
    
    print(f'Quantidade de alunos aprovados: {len(aprovados)}')
    print(f'Quantidade de alunos de recuperação: {len(na_recuperacao)}')
    print(f'Quantidade de alunos reprovados: {len(reprovados)}')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

aprovados[aprovados.index('Maria')] = 'Marina'


examesFinais = 0

# Função para, depois das provas de recuperação, saber se os alunos foram aprovados ou reprovados
def aprovarAlunos ():
    # Valida se as provas de recuperação já foram aplicadas pelo professor
    validacao = input('Os exames finais já foram aplicados? Responda "s" para "sim" ou "n" para "não": \n')
    if validacao == 's':
        examesFinais = True
    elif validacao == 'n':
        examesFinais = False
    else: 
        print('Digite "s" ou "n"!')


    
    if examesFinais == True: 
        # Lê a lista de alunos que ficaram de recuperação
        for i in na_recuperacao:
            notaFinal = float(input(f'\nQual foi a nota do(a) aluno(a) {i} no exame final?\n'))

            if notaFinal >= 6.5 and notaFinal <= 10:
                passou = True
            elif notaFinal >= 0:
                passou = False
            else: 
                print('Digite uma nota válida!')

            if passou == True:
                aprovados.append(i)
                print(f'\n{i} foi aprovado(a)!\n')
            
            else:
                reprovados.append(i)
                print(f'\n{i} foi reprovado(a)!\n')



        aprovados.sort()
        reprovados.sort()

        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'Alunos aprovados: {aprovados}\n')
        print(f'Alunos reprovados: {reprovados}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


aprovados.sort()
na_recuperacao.sort()
reprovados.sort()


mostrarResultados()
aprovarAlunos()