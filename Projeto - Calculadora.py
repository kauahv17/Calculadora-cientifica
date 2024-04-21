import tkinter as tk

tela = tk.Tk()
tela.title('CALCULADORA')
tela.iconbitmap("icone_calculadora.ico")
def digitar_no_console(tecla):
    global console_calculadora, equacao_console
    global botao_expoente
    if "<ERRO>" in console_calculadora["text"]:
        console_calculadora["fg"] = 'black'
        console_resultado["fg"] = 'black'
        console_calculadora["text"] = ''
        equacao_console = ''
    tecla_normal = ""
    size_equacao = len(console_calculadora["text"])
    simbolos_matematicos = ['+','-','×','÷','^','√']
    mini_caracteres = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵', '6': '⁶','7': '⁷','8': '⁸','9': '⁹','+': '⁺','-': '⁻','×': 'ˣ','√': '√','÷': '÷','.': '.',',': ',','(': '⁽',')': '⁾'}

    if tecla == '^' and size_equacao != 0 and console_calculadora["text"][-1] != '-':
        botao_expoente["text"] = 'ᵛ'
    elif tecla == 'ᵛ':
        botao_expoente["text"] = '^'

    if tecla != '←' and tecla != 'clear' and tecla != 'ᵛ':
        if botao_expoente["text"] == 'ᵛ' and tecla != '^':
            tecla_normal = tecla
            tecla = mini_caracteres[tecla]
        else:
            tecla_normal = tecla
            tecla = tecla
        try:
            if tecla != console_calculadora["text"][-1]:
                if tecla in simbolos_matematicos and tecla != '-' and tecla != '√':
                    if console_calculadora["text"][-1] in simbolos_matematicos:
                        console_calculadora["text"] = console_calculadora["text"][:-1]
                        console_calculadora["text"] += tecla
                        equacao_console = equacao_console[:-1]
                        equacao_console += tecla_normal
                    else:
                        console_calculadora["text"] += tecla
                        equacao_console += tecla_normal
                else:
                    console_calculadora["text"] += tecla
                    equacao_console += tecla_normal

            else:
                if tecla in simbolos_matematicos:
                    if tecla == '√':
                        console_calculadora["text"] += tecla
                        equacao_console += tecla_normal
                    else:
                        pass
                else:
                    console_calculadora["text"] += tecla
                    equacao_console += tecla_normal
        except IndexError:
            if tecla in simbolos_matematicos:
                if tecla == '-' or tecla == '√':
                    console_calculadora["text"] += tecla
                    equacao_console += tecla_normal
                else:
                    pass
            else:
                console_calculadora["text"] += tecla
                equacao_console += tecla_normal
            
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

#-------------------------------------botão de igual-------------------------------------#
#--------funções do botão:
def mostrar_resultado():
    FUNC_CALCULO()
#--------botão IGUAL:
botao_igual = tk.Button(text='=',fg='white',bg='blue',font=("Arial",20),height=1,width=5,command=mostrar_resultado)
botao_igual.grid(row=6,column=2,columnspan=3,sticky='NSWE')
#-------------------------------------botão de igual-------------------------------------#

#----------------------------------------criar botões----------------------------------------#
#--------matriz dos BOTÕES:
matriz_botoes = [['1','2','3','+','←'],
                 ['4','5','6','-','clear'],
                 ['7','8','9','×',' '],
                 ['(','0',')','÷','√'],
                 ['.',',']]

simbolos_matematicos = ['+','-','×','÷','^','√']
linha = 2
coluna = 0
for X in range(linha,6+1):
    cor_letra = 'white'
    for Y in range(coluna,4+1):
        button = matriz_botoes[X-2][Y]
        if button in simbolos_matematicos:
            cor_fundo = 'blue'
        elif button == '←':
            cor_fundo = 'black'
            cor_letra = 'red'
        elif button == 'clear':
            cor_fundo = 'red'
            cor_letra = 'black'
        elif button == ' ':
            continue
        else:
            cor_fundo = 'black'
        tk.Button(tela,text=button,fg=cor_letra,bg=cor_fundo,font=("Arial",20),height=1,width=5,
                  command=lambda botao=button: digitar_no_console(botao)).grid(row=X,column=Y,sticky='NSWE')
        if button == ',':
            break
#----------------------------------------criar botões----------------------------------------#

#-------------------------------------botão de expoente-------------------------------------#
#--------funções do botão:
def digitar_expoente():
    botao = botao_expoente["text"]
    digitar_no_console(botao)
    
botao_expoente = tk.Button(text='^',bg='blue',fg='white',font=("Arial",20),height=1,width=5,command=digitar_expoente)    
botao_expoente.grid(row=4,column=4,sticky="NSWE")
#-------------------------------------botão de expoente-------------------------------------#

#-------------------------------------CALCULO MATEMÁTICO-------------------------------------#
#|-----------------funcão que resolve as equações-----------------|
def CALCULO_BASICO_RAIZ(main_equacao,simble):
    if '√' in simble:#--------resolve contas de radiciação:
        radicando = main_equacao.replace('√','')
        equation = float(radicando) ** 0.5
    return str(equation)
#|-----------------funcão que resolve as equações-----------------|

#|-----------------Arredondar Valores-----------------|
def arredondar(num):
    round_num = str(num)
    if "." in round_num:
        i = round_num.find(".")
        if len(round_num[i+1:]) > 7:
            round_num = str(round(num,7))
            round_num = f"{float(round_num):_}"
        elif len(round_num[i+1:]) == 1 and round_num[i+1] == "0":
            round_num = str(num)[:i]
            round_num = f"{int(round_num):_}"

    round_num = round_num.replace('.',',').replace('_','.')
    return round_num
#|-----------------Arredondar Valores-----------------|

#|-----------------converte o padrão numérico brasileiro para o padrão americano-----------------|
def FILTRO_EQUACAO(equation):
    equation = equation.replace('.','').replace(',','.')
    return equation
#|-----------------converte o padrão numérico brasileiro para o padrão americano-----------------|

#|---------------------------Resolve as Raizes---------------------------|
def RESOLVER_RAIZES(_equacao_):
    simbolos_matematicos_alg = ['+','-','*','/','√','(',')']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    while True:
        peso_simbolos_parents = []#vetor dos pesos dos simbolos na equação
        indices_simbolos_parents = []#vetor dos simbolos na equação
        dict_raizes = {'quantidade':0,'indices':[]}
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
        
        if dict_raizes['quantidade'] > 0:
            main_equacao = ''
            resto_esquerda_equacao = ''#monta a parte ESQUERDA da equação, supondo que não tenha
            resto_direita_equacao = ''#monta a parte DIREITA da equação, supondo que não tenha            
            primeira_raiz = dict_raizes['indices'][0]
            ind_raiz_ordem = 0
            for i,pref in enumerate(ordem_preferencial):
                peso,ind = pref
                if primeira_raiz == ind:
                    ind_raiz_ordem = i
                    
            if ind_raiz_ordem == 0:
                if size_ordem_preferencial == 1:
                    main_equation = _equacao_[primeira_raiz:]
                else:
                    ind_equacao_direita = ordem_preferencial[ind_raiz_ordem+1][1]
                    resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                    resto_direita_equacao = _equacao_[ind_equacao_direita:]#monta a parte DIREITA da equação
                    main_equation = _equacao_[primeira_raiz:ind_equacao_direita]

            elif ind_raiz_ordem == size_ordem_preferencial-1:
                resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                resto_direita_equacao = ''#monta a parte DIREITA da equação
                main_equation = _equacao_[primeira_raiz:]

            else:
                ind_equacao_direita = ordem_preferencial[ind_raiz_ordem+1][1]
                resto_esquerda_equacao = _equacao_[:primeira_raiz]#monta a parte ESQUERDA da equação
                resto_direita_equacao = _equacao_[ind_equacao_direita:]#monta a parte DIREITA da equação
                main_equation = _equacao_[primeira_raiz:ind_equacao_direita]

            _equation_ = CALCULO_BASICO_RAIZ(main_equation,simble='√')
            _equacao_ = resto_esquerda_equacao + _equation_ + resto_direita_equacao
        else:
            break
    
    return _equacao_
#|---------------------------Resolve as Raizes---------------------------|

#|-----------------filtra e separa as equações por ordem de preferência-----------------|
def FUNC_CALCULO():
    global console_calculadora
    global equacao_console
    equacao = equacao_console
    equacao = FILTRO_EQUACAO(equacao)
    resultado = ''
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos_matematicos = ['+','-','×','÷','^','√']
    simbolos_matematicos_alg = ['+','-','*','/','√','(',')']
    troca_simbolos_matematicos = [('+','+'),('-','-'),('×','*'),('÷','/'),('^','**'),('√','√')]
    
    _equation_ = ''
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
                _equation_ += posterior
                result = 'continue'
                break
            result = ''
        if result == 'continue':
            continue
        else:
            _equation_ += cr

    if qntd_simble > 0 or ')(' in equacao:#verifica se ainda tem equações a resolver
        try:
            if '(' in _equation_ or ')' in _equation_:#--------verifica se tem parenteses na equação:
                equacao = _equation_
                ordem_preferencial = []#matriz com os pesos e indices de cada conta
                size_ordem_preferencial = 0#tamanho da matriz

                qntd_parents_E = 0
                qntd_parents_D = 0
                if '(' in equacao:
                    qntd_parents_E = equacao.count('(')

                if ')' in equacao:
                    qntd_parents_D = equacao.count(')')
                if qntd_parents_E == qntd_parents_D:
                    pass
                else:
                    if qntd_parents_E > qntd_parents_D:
                        qntd = qntd_parents_E - qntd_parents_D
                        equacao += (')' * qntd)

                    elif qntd_parents_E < qntd_parents_D:
                        qntd = qntd_parents_D - qntd_parents_E
                        equacao = ('('* qntd) + equacao

                if ')(' in equacao:
                    equacao = equacao.replace(')(',')*(')

                for i,simble in enumerate(simbolos_matematicos_alg):
                    if f'){simble}(' in equacao:
                        equacao = '(' + equacao + ')'

                for N in numeros:
                    if f'{N}(' in equacao:
                        equacao = equacao.replace(f'{N}(',f'{N}*(')

                    if f'){N}' in equacao:
                        equacao = equacao.replace(f'){N}',f')*{N}')

                if ')√' in equacao:
                    equacao = equacao.replace(')√',')*√')

                equacao = RESOLVER_RAIZES(equacao)
                resultado = eval(equacao)

            else:
                equacao = _equation_
                if '√' in equacao:
                    equacao = RESOLVER_RAIZES(equacao)
                    resultado = eval(equacao)
                else:
                    resultado = eval(equacao)

        except:
            console_calculadora["fg"] = 'red'
            console_resultado["fg"] = 'red'
            console_calculadora["text"] = "<ERRO>"
            console_resultado["text"] = '='
        else:
            resultado = arredondar(resultado)
            console_resultado["text"] = f"= {resultado}"#--------exibe no console o resultado da equação
    else:#caso não tenha mais equações a resolver
        resultado = equacao
        console_resultado["text"] = f"= {resultado}"#--------exibe no console o resultado da equação

    #-----------------filtra e separa as equações por ordem de preferência-----------------#
#-------------------------------------CALCULO MATEMÁTICO-------------------------------------#
tela.mainloop()