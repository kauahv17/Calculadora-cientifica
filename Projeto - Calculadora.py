import tkinter as tk

tela = tk.Tk()
tela.title('CALCULADORA')

#-------------------------------------digitar no console-------------------------------------#
def digitar_no_console(tecla):
    global console_calculadora
    global equacao_console
    global botao_expoente
    if "<ERRO>" in console_calculadora["text"]:
        console_calculadora["fg"] = 'black'
        console_calculadora["text"] = ''
        equacao_console = ''
    sit = ""
    size_equacao = len(console_calculadora["text"])
    simbolos_matematicos = ['+','-','×','÷','^','√']
    mini_caracteres = {'0': '⁰',
                       '1': '¹',
                       '2': '²',
                       '3': '³',
                       '4': '⁴',
                       '5': '⁵',
                       '6': '⁶',
                       '7': '⁷',
                       '8': '⁸',
                       '9': '⁹',
                       '+': '⁺',
                       '-': '⁻',
                       '×': 'ˣ',
                       '√': '√',
                       '÷': '÷',
                       '.': '.',
                       ',': ',',
                       '(': '⁽',
                       ')': '⁾'}

    if tecla == '^' and size_equacao != 0 and console_calculadora["text"][-1] != '-':
        console_calculadora["text"] += tecla
        botao_expoente["text"] = 'ᵛ'
    elif tecla == 'ᵛ':
        botao_expoente["text"] = '^'

    if tecla != '←' and tecla != 'clear' and tecla != 'ᵛ':
        try:
            if tecla != console_calculadora["text"][-1]:
                if tecla == '-' or tecla == '√':
                    console_calculadora["text"] += tecla
                    sit = "pass"
                else:
                    sit = ""
                if botao_expoente["text"] == 'ᵛ':
                    for mini_cr in mini_caracteres:
                        if tecla == mini_cr:
                            console_calculadora["text"] += mini_caracteres[mini_cr]
                else:
                    if sit == "pass" or console_calculadora["text"][-1] == '-':
                        if tecla in simbolos_matematicos:
                            if console_calculadora["text"][-1] != '-':
                                pass
                            pass
                        else:
                            console_calculadora["text"] += tecla
                    else:
                        console_calculadora["text"] += tecla
                equacao_console += tecla
            else:
                if tecla in simbolos_matematicos:
                    if tecla == console_calculadora["text"][-2] and tecla != '√':
                        console_calculadora["text"] = console_calculadora["text"][:-2] + tecla
                        equacao_console = equacao_console[:-2] + tecla
                    elif tecla != '^':
                        console_calculadora["text"] += tecla
                else:
                    console_calculadora["text"] += tecla
                equacao_console += tecla
                
        except IndexError:
            if tecla in simbolos_matematicos:
                if tecla == '-' or tecla == '√':
                    console_calculadora["text"] += tecla
                    equacao_console += tecla
                else:  
                    pass
            else:
                console_calculadora["text"] += tecla
                equacao_console += tecla
            
    elif tecla == '←':
        console_calculadora["text"] = console_calculadora["text"][:-1]
        equacao_console = equacao_console[:-1]
    elif tecla == 'clear':
        console_calculadora["text"] = ""
        equacao_console = ""

console_calculadora = tk.Label(text='',fg='black',bg='gray',font=("Arial",34),height=2,width=18,anchor='e')
console_calculadora.grid(row=0,column=0,columnspan=5,sticky='NSWE')

equacao_console = ''

console_resultado = tk.Label(text='',fg='black',bg='gray',font=("Arial",22),height=1,width=18,anchor='ne')
console_resultado.grid(row=1,column=0,columnspan=5,sticky='NSWE')
#-------------------------------------digitar no console-------------------------------------#

#-------------------------------------botões dos números-------------------------------------#
#--------funções dos botões:
def digitar_1():
    botao = '1'
    digitar_no_console(botao)
def digitar_2():
    botao = '2'
    digitar_no_console(botao)
def digitar_3():
    botao = '3'
    digitar_no_console(botao)
def digitar_4():
    botao = '4'
    digitar_no_console(botao)
def digitar_5():
    botao = '5'
    digitar_no_console(botao)
def digitar_6():
    botao = '6'
    digitar_no_console(botao)
def digitar_7():
    botao = '7'
    digitar_no_console(botao)
def digitar_8():
    botao = '8'
    digitar_no_console(botao)
def digitar_9():
    botao = '9'
    digitar_no_console(botao)
def digitar_0():
    botao = '0'
    digitar_no_console(botao)


#--------botão 1:
botao_1 = tk.Button(text='1',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_1)
botao_1.grid(row=2,column=0,sticky='NSWE')
#--------botão 2:
botao_2 = tk.Button(text='2',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_2)
botao_2.grid(row=2,column=1,sticky='NSWE')
#--------botão 3:
botao_3 = tk.Button(text='3',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_3)
botao_3.grid(row=2,column=2,sticky='NSWE')

#--------botão 4:
botao_4 = tk.Button(text='4',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_4)
botao_4.grid(row=3,column=0,sticky='NSWE')
#--------botão 5:
botao_5 = tk.Button(text='5',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_5)
botao_5.grid(row=3,column=1,sticky='NSWE')
#--------botão 6:
botao_6 = tk.Button(text='6',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_6)
botao_6.grid(row=3,column=2,sticky='NSWE')


#--------botão 7:
botao_7 = tk.Button(text='7',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_7)
botao_7.grid(row=4,column=0,sticky='NSWE')
#--------botão 8:
botao_8 = tk.Button(text='8',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_8)
botao_8.grid(row=4,column=1,sticky='NSWE')
#--------botão 9:
botao_9 = tk.Button(text='9',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_9)
botao_9.grid(row=4,column=2,sticky='NSWE')

#--------botão 0:
botao_0 = tk.Button(text='0',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_0)
botao_0.grid(row=5,column=1,sticky='NSWE')
#-------------------------------------botões dos números-------------------------------------#

#--------------------------------botões dos caracteres especiais--------------------------------#
#--------funções dos botões:
def digitar_parents_D():
    botao = ')'
    digitar_no_console(botao)
def digitar_parents_E():
    botao = '('
    digitar_no_console(botao)
def digitar_ponto():
    botao = '.'
    digitar_no_console(botao)
def digitar_virgula():
    botao = ','
    digitar_no_console(botao)

#--------botão " ) ":
botao_parents_D = tk.Button(text=')',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_parents_D)
botao_parents_D.grid(row=5,column=2,sticky='NSWE')
#--------botão " ( ":
botao_parents_E = tk.Button(text='(',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_parents_E)
botao_parents_E.grid(row=5,column=0,sticky='NSWE')

#--------botão do ponto:
botao_ponto = tk.Button(text='.',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_ponto)
botao_ponto.grid(row=6,column=0,sticky='NSWE')
#--------botão da vígula:
botao_virgula = tk.Button(text=',',fg='white',bg='black',font=("Arial",20),height=1,width=5,command=digitar_virgula)
botao_virgula.grid(row=6,column=1,sticky='NSWE')
#--------------------------------botões dos caracteres especiais--------------------------------#

#-------------------------------------botões matemáticos-------------------------------------#
#--------funções dos botões:
def digitar_MAIS():
    botao = '+'
    digitar_no_console(botao)
def digitar_MENOS():
    botao = '-'
    digitar_no_console(botao)
def digitar_VEZES():
    botao = '×'
    digitar_no_console(botao)
def digitar_DIVISAO():
    botao = '÷'
    digitar_no_console(botao)
def digitar_EXPOENTE():
    botao = botao_expoente["text"]
    digitar_no_console(botao)
def digitar_RAIZ():
    botao = '√'
    digitar_no_console(botao)

#--------botão MAIS:
botao_mais = tk.Button(text='+',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_MAIS)
botao_mais.grid(row=2,column=3,sticky='NSWE')
#--------botão MENOS:
botao_menos = tk.Button(text='-',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_MENOS)
botao_menos.grid(row=3,column=3,sticky='NSWE')
#--------botão VEZES:
botao_vezes = tk.Button(text='×',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_VEZES)
botao_vezes.grid(row=4,column=3,sticky='NSWE')
#--------botão DIVISÃO:
botao_div = tk.Button(text='÷',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_DIVISAO)
botao_div.grid(row=5,column=3,sticky='NSWE')

#--------botão EXPOENTE:
botao_expoente = tk.Button(text='^',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_EXPOENTE)
botao_expoente.grid(row=4,column=4,sticky='NSWE')
#--------botão RAIZ QUADRADA:
botao_raiz = tk.Button(text='√',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=digitar_RAIZ)
botao_raiz.grid(row=5,column=4,sticky='NSWE')
#-------------------------------------botões matemáticos-------------------------------------#

#-------------------------------------botões de limpeza-------------------------------------#
#--------funções dos botões:
def exluir_UM():
    botao = '←'
    digitar_no_console(botao)
def exluir_TUDO():
    botao = 'clear'
    digitar_no_console(botao)

#--------botão EXCLUIR:
botao_excluir = tk.Button(text='←',fg='red',bg='black',font=("Arial",20),height=1,width=5,command=exluir_UM)
botao_excluir.grid(row=2,column=4,sticky='NSWE')
#--------botão LIMPAR TUDO:
botao_clear = tk.Button(text='clear',fg='black',bg='red',font=("Arial",20),height=1,width=5,command=exluir_TUDO)
botao_clear.grid(row=3,column=4,sticky='NSWE')
#-------------------------------------botões de limpeza-------------------------------------#

#-------------------------------------CALCULO MATEMÁTICO-------------------------------------#
#|-----------------funcão que resolve as equações-----------------|
def calculo_basico(main_equacao,simble):
    if '^' in simble:#--------resolve contas de exponenciação:
        numerador,denominador = main_equacao.split('^')
        equation = float(numerador) ** float(denominador)
        if '-' in main_equacao:#converte o numerador para negativo se ele for negativo
            equation = -equation
        print(f'potenciação = {equation}')

    if '√' in simble:#--------resolve contas de radiciação:
        radicando = main_equacao.replace('√','')
        equation = float(radicando) ** 0.5
        print(f'radiciação = {equation}')

    if '×' in simble:#--------resolve contas de multiplicação:
        numerador,denominador = main_equacao.split('×')
        equation = float(numerador) * float(denominador)
        print(f'multiplicação = {equation}')

    if '÷' in simble:#--------resolve contas de divisão:
        numerador,denominador = main_equacao.split('÷')
        equation = float(numerador) / float(denominador)
        print(f'divisão = {equation}')

    if '+' in simble:#--------resolve contas de adição:
        numerador,denominador = main_equacao.split('+')
        equation = float(numerador) + float(denominador)
        print(f'adição = {equation}')

    if '-' in simble:#--------resolve contas de subtração:
        valores = main_equacao.split('-')
        ind_menos = main_equacao.rfind('-')
        if main_equacao.count('-') >= 2:#verifica se existem 2 números negativos na equação
            vazio,numerador,denominador = valores
            if main_equacao[ind_menos] == main_equacao[ind_menos-1]:
                main_equacao = main_equacao.replace('--','+')
                equation = calculo_basico(main_equacao,simble = '+')
            else:
              equation = -float(numerador) - float(denominador)
        else:
            numerador,denominador = valores
            equation = float(numerador) - float(denominador)
        print(f'subtração = {equation}')

    #--------converte para string e arrendonda para no máximo 7 casas decimais:
    round_equation = str(equation)
    if '.' in round_equation:
        ind_float = round_equation.find('.')
        if len(round_equation[ind_float+1:]) > 7:
            round_equation = str(round(equation,7))

    return round_equation
#|-----------------funcão que resolve as equações-----------------|

#|-----------------converte o padrão numérico brasileiro para o padrão americano-----------------|
def filtro_equacao(equation):
    equation = equation.replace('.','').replace(',','.')
    return equation
#|-----------------converte o padrão numérico brasileiro para o padrão americano-----------------|

#|-----------------filtra e separa as equações por ordem de preferência-----------------|
def func_CALCULO():
    global console_calculadora
    global equacao_console
    equacao = equacao_console
    equacao = filtro_equacao(equacao)
    #equacao = "12÷2)+√81×3+5√25"
    #equacao = "5^2)÷(5×2)+(3+5-(3)"
    resultado = ''
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos_matematicos = ['+','-','×','÷','^','√']
    simbolos_matematicos_alg = ['+','-','*','/','√','(',')']
    troca_simbolos_matematicos = [('+','+'),
                                  ('-','-'),
                                  ('×','*'),
                                  ('÷','/'),
                                  ('^','**'),
                                  ('√','√')]
    indices_simbolos = []#vetor dos simbolos na equação
    peso_simbolos = []#vetor dos pesos dos simbolos na equação
    
    indices_simbolos_parents = []#vetor dos simbolos na equação
    peso_simbolos_parents = []#vetor dos pesos dos simbolos na equação
    
    while True:#--------loop que roda até rosolver a equação inteira:
        _equation_ = ''
        dict_raizes = {'quantidade':0,'indices':[]}

        indices_simbolos = []#zera o vetor dos simbolos na equação
        peso_simbolos = []#zera o vetor dos pesos dos simbolos na equação

        resto_esquerda_equacao = ''#monta a parte ESQUERDA da equação, supondo que não tenha
        resto_direita_equacao = ''#monta a parte DIREITA da equação, supondo que não tenha

        qntd_simble = 0#supondo que não tenha simbolos na equação

        for ind,cr in enumerate(equacao):#--------loop que conta quantas equações existem para fazer:
            for simbles in troca_simbolos_matematicos:
                antecessor,posterior = simbles
                if cr in antecessor:
                    if cr == '-' and ind == 0:#verifica se o primeiro número é negativo:
                        pass
                    elif cr == '-' and equacao[ind-1] in simbolos_matematicos:#verifica se tem número é negativo no meio da equação:
                        pass
                    else:
                        qntd_simble +=1#conta todas as contas existentes na equação
                        if antecessor == '^':
                            peso_simbolos.append(3)#peso da exponenciação
                        if antecessor == '√':
                            if equacao[ind-1] == '√':
                                peso_simbolos.append(3.5)#peso da radiciação
                            else:
                                peso_simbolos.append(3)#peso da radiciação
                        if antecessor == '×':
                            peso_simbolos.append(2)#peso da multiplicação
                        if antecessor == '÷':
                            peso_simbolos.append(2)#peso da divisão
                        if antecessor == '+':
                            peso_simbolos.append(1)#peso da adição
                        if antecessor == '-':
                            peso_simbolos.append(1)#peso da subtração

                        indices_simbolos.append(ind)#indice do simbolo na STRING equação
                    _equation_ += posterior
                    result = 'continue'
                    break
                result = ''
            if result == 'continue':
                continue
            else:
                _equation_ += cr


        ordem_preferencial = list(zip(peso_simbolos,indices_simbolos))#matriz com os pesos e indices de cada conta
        size_ordem_preferencial = len(ordem_preferencial)#tamanho da matriz

        print('quantidade de equações:',qntd_simble)

        if qntd_simble > 0 or ')(' in equacao:#verifica se ainda tem equações a resolver
            try:
                if '(' in _equation_ or ')' in _equation_:#--------verifica se tem parenteses na equação:
                    _equacao_ = _equation_
                    print(f"antes: {_equacao_}")
                    ordem_preferencial = []#matriz com os pesos e indices de cada conta
                    size_ordem_preferencial = 0#tamanho da matriz

                    qntd_parents_E = 0
                    qntd_parents_D = 0
                    if '(' in _equacao_:
                        qntd_parents_E = _equacao_.count('(')

                    if ')' in equacao:
                        qntd_parents_D = _equacao_.count(')')
                    if qntd_parents_E == qntd_parents_D:
                        pass
                    else:
                        if qntd_parents_E > qntd_parents_D:
                            qntd = qntd_parents_E - qntd_parents_D
                            _equacao_ += (')' * qntd)

                        elif qntd_parents_E < qntd_parents_D:
                            qntd = qntd_parents_D - qntd_parents_E
                            _equacao_ = ('('* qntd) + _equacao_

                    if ')(' in _equacao_:
                        _equacao_ = _equacao_.replace(')(',')*(')

                    for i,simble in enumerate(simbolos_matematicos_alg):
                        if f'){simble}(' in _equacao_:
                            _equacao_ = '(' + _equacao_ + ')'

                    for N in numeros:
                        if f'{N}(' in _equacao_:
                            _equacao_ = _equacao_.replace(f'{N}(',f'{N}*(')

                        if f'){N}' in _equacao_:
                            _equacao_ = _equacao_.replace(f'){N}',f')*{N}')

                    if ')√' in _equacao_:
                        _equacao_ = _equacao_.replace(')√',')*√')

                    print(f"depois: {_equacao_}")

                    for indi,cr in enumerate(_equacao_):#--------loop que conta quantas equações existem para fazer:
                        for simbles in simbolos_matematicos_alg:
                            if cr in simbles:
                                if cr == '-' and indi == 0:#verifica se o primeiro número é negativo:
                                    pass
                                elif cr == '-' and _equacao_[indi-1] in simbolos_matematicos_alg:#verifica se tem número é negativo no meio da equação:
                                    pass
                                else:
                                    indices_simbolos_parents.append(indi)
                                    if simbles == '√':
                                        if _equacao_[indi-1] == '√':
                                            peso_simbolos_parents.append(3.5)#peso da radiciação
                                        else:
                                            peso_simbolos_parents.append(3)#peso da radiciação
                                        vet = dict_raizes['indices']
                                        vet.append(indi)
                                        dict_raizes['quantidade'] += 1
                                    if simbles == '*':
                                        peso_simbolos_parents.append(2)#peso da multiplicação
                                    if simbles == '/':
                                        peso_simbolos_parents.append(2)#peso da divisão
                                    if simbles == '+':
                                        peso_simbolos_parents.append(1)#peso da adição
                                    if simbles == '-':
                                        peso_simbolos_parents.append(1)#peso da subtração
                                    if simbles == '(':
                                        peso_simbolos_parents.append(4)#peso do parenteses esquerdo
                                    if simbles == ')':
                                        peso_simbolos_parents.append(4)#peso do parenteses direito

                    ordem_preferencial = list(zip(peso_simbolos_parents,indices_simbolos_parents))#matriz com os pesos e indices de cada conta
                    size_ordem_preferencial = len(ordem_preferencial)#tamanho da matriz

                    print('ordem preferencial:',ordem_preferencial)
                    print(dict_raizes)

                    if dict_raizes['quantidade'] > 0:
                        for raizes in dict_raizes['indices']:
                            main_equacao = ''
                            resto_esquerda_equacao = ''#monta a parte ESQUERDA da equação, supondo que não tenha
                            resto_direita_equacao = ''#monta a parte DIREITA da equação, supondo que não tenha
                            primeira_raiz = dict_raizes['indices'][0]
                            for i,pref in enumerate(ordem_preferencial):
                                peso,ind = pref
                                if raizes == ind:
                                    primeira_raiz = ind
                                    if i == 0:
                                        ind_equacao_direita = ordem_preferencial[i+1][1]
                                        resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                                        resto_direita_equacao = _equacao_[ind_equacao_direita:]#monta a parte DIREITA da equação

                                        main_equation = _equacao_[primeira_raiz:ind_equacao_direita]

                                    elif i == size_ordem_preferencial-1:
                                        resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                                        resto_direita_equacao = ''#monta a parte DIREITA da equação

                                        main_equation = _equacao_[primeira_raiz:]

                                    else:
                                        ind_equacao_direita = ordem_preferencial[i+1][1]
                                        resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                                        resto_direita_equacao = _equacao_[ind_equacao_direita:]#monta a parte DIREITA da equação

                                        main_equation = _equacao_[primeira_raiz:ind_equacao_direita]

                                    print('resto da esquerda:',resto_esquerda_equacao)
                                    print('main:',main_equation)
                                    print('resto da direita:',resto_direita_equacao)

                                    _equation_ = calculo_basico(main_equation,simble='√')
                                    _equacao_ = resto_esquerda_equacao + _equation_ + resto_direita_equacao

                    else:
                        pass

                    print(f"equação: {_equacao_}")
                    equacao = eval(_equacao_)
                    break

                else:#--------caso não tenha parenteses na equação:
                    primeira_equacao = ordem_preferencial[0]#supondo que a conta principal seja primeira

                    for peso,ind in ordem_preferencial:#escolhendo a conta principal com maior peso
                        if peso > primeira_equacao[0]:
                            primeira_equacao = (peso,ind)

                    ind_primeira_equacao = primeira_equacao[1]#indice da conta principal com maior peso
                    simbolo = equacao[ind_primeira_equacao]#simbolo da conta principal com maior peso
                    ind_esquerda_equacao = 0#supondo que não tenha o INDICE conta da esquerda
                    ind_direita_equacao = 0#supondo que não tenha o INDICE conta da direita
                    print(ordem_preferencial)
                    print(primeira_equacao)

                    if qntd_simble > 1:#supondo que a conta principal seja primeira
                        if primeira_equacao == ordem_preferencial[0]:
                            ind_direita_equacao = ordem_preferencial[1][1]
                            resto_direita_equacao = equacao[ind_direita_equacao:]#monta a parte DIREITA da equação

                            if simbolo == '√':#verifica se tem raiz na conta principal
                                resto_esquerda_equacao = equacao[:ind_primeira_equacao]#monta a parte ESQUERDA da equação
                                main_equacao = equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:ind_direita_equacao]#monta a conta principal para resolver
                            else:
                                main_equacao = equacao[:ind_primeira_equacao] + equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:ind_direita_equacao]#monta a conta principal para resolver

                        elif primeira_equacao == ordem_preferencial[size_ordem_preferencial-1]:
                            ind_esquerda_equacao = ordem_preferencial[size_ordem_preferencial-1-1][1]
                            resto_esquerda_equacao = equacao[:ind_esquerda_equacao+1]#monta a parte ESQUERDA da equação

                            if simbolo == '√':#verifica se tem raiz na conta principal
                                main_equacao = equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:]#monta a conta principal para resolver
                            else:
                                main_equacao = equacao[ind_esquerda_equacao+1:ind_primeira_equacao] + equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:]#monta a conta principal para resolver

                        else:
                            ind_main_equacao = ordem_preferencial.index(primeira_equacao)
                            ind_esquerda_equacao = ordem_preferencial[ind_main_equacao-1][1]
                            ind_direita_equacao = ordem_preferencial[ind_main_equacao+1][1]
                            resto_esquerda_equacao = equacao[:ind_esquerda_equacao+1]#monta a parte ESQUERDA da equação
                            resto_direita_equacao = equacao[ind_direita_equacao:]#monta a parte DIREITA da equação

                            if simbolo == '√':#verifica se tem raiz na conta principal
                                main_equacao = equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:ind_direita_equacao]
                            else:
                                main_equacao = equacao[ind_esquerda_equacao+1:ind_primeira_equacao] + equacao[ind_primeira_equacao] + equacao[ind_primeira_equacao+1:ind_direita_equacao]

                        print('resto da esquerda:',resto_esquerda_equacao)
                        print('main:',main_equacao)
                        print('resto da direita:',resto_direita_equacao)

                        equation = calculo_basico(main_equacao,simbolo)#manda para a função resolver o calculo
                        equacao = resto_esquerda_equacao + equation + resto_direita_equacao#monta de volta a equação com o resultado

                        print(f"equação: {equacao}")
                        print('')
                    else:
                        if simbolo == '√':#verifica se tem raiz na conta principal
                            resto_esquerda_equacao = equacao[:ind_primeira_equacao]#monta a parte ESQUERDA da equação
                            main_equacao = equacao[ind_primeira_equacao:]#monta a conta principal para resolver
                        else:
                            main_equacao = equacao#monta a conta principal para resolver

                        equation = calculo_basico(main_equacao,simbolo)#manda para a função resolver o calculo
                        equacao = resto_esquerda_equacao + equation + resto_direita_equacao#monta de volta a equação com o resultado

                        print('resto da esquerda:',resto_esquerda_equacao)
                        print('main:',main_equacao)
                        print('resto da direita:',resto_direita_equacao)
                        print(f"equação: {equacao}")
                        print('')
            except:
                console_calculadora["fg"] = 'red'
                console_calculadora["text"] = "<ERRO>"
        else:#caso não tenha mais equações a resolver
            break
            
    equacao = f"{float(equacao):_}"
    resultado = equacao.replace('.',',').replace('_','.')
    print('resultado:',resultado)
    print('')

    console_resultado["text"] = f"={resultado}"#--------exibe no console o resultado da equação

    #-----------------filtra e separa as equações por ordem de preferência-----------------#
#-------------------------------------CALCULO MATEMÁTICO-------------------------------------#

#-------------------------------------botão de igual-------------------------------------#
#--------funções dos botões:
def mostrar_resultado():
    func_CALCULO()
#--------botão IGUAL:
botao_igual = tk.Button(text='=',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=mostrar_resultado)
botao_igual.grid(row=6,column=2,columnspan=3,sticky='NSWE')
#-------------------------------------botão de igual-------------------------------------#

tela.mainloop()