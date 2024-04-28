import re
import tkinter as tk

class CALCULADORA:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title('CALCULADORA')
        #self.tela.iconbitmap("icone_calculadora.ico")
        self.digitar_minicaracteres = False
        self.mini_caracteres = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵', '6': '⁶','7': '⁷','8': '⁸','9': '⁹','+': '⁺','-': '⁻','×': 'ˣ','√': '√','÷': '÷','.': '.',',': ',','(': '⁽',')': '⁾'}
        
        self.matriz_botoes = [['1','2','3','+','←'], ['4','5','6','-','clear'],['7','8','9','×',' '],['(','0',')','÷','√'],['.',',',' ',' ',' ']]
        self.console_calculadora = None
        self.console_resultado = None
        self.equacao_console = ""

        self.simbolos_matematicos = ['+','-','×','÷','^','√']
        self.cor_tecla, self.cor_botao = ("white","black")
        self.cor_buttons = {"simbles":("white","#305496"),"clear":("black","red"),"←":("red","black"),}
        
        self.botao_igual = tk.Button(text='=',fg='white',bg='#305496',font=("Arial",20),height=1,width=5,command=self.funcionalidade("enviar equacao", None))
        self.botao_igual.grid(row=6,column=2,columnspan=3,sticky='NSWE')

        self.botao_expoente = tk.Button(text='^',bg='#305496',fg='white',font=("Arial",20),height=1,width=5,command=self.funcionalidade("digitar", "^"))
        self.botao_expoente.grid(row=4,column=4,sticky="NSWE")
    
    def encontrar_raizes(self, equacao):
        # Encontrando todas as ocorrências de '√' seguidas por um ou mais dígitos
        potencias_raiz = ""
        padrao = r'(√+)(\d+)'
        ocorrencias = re.findall(padrao, equacao)

        for ocorrencia in ocorrencias:
            raizes, numero = ocorrencia
            for i in range(len(raizes)):
                potencias_raiz += '**0.5' + ')'
            substituicao = '(' * len(raizes) + numero + potencias_raiz
            equacao = equacao.replace(raizes + numero, substituicao)

        return equacao
    
    def converter(self, equacao, padrao):
        if padrao == "eua":
            equacao = equacao.replace(",","_").replace(".",",").replace("_",".")
        
        elif padrao == "br":
            equacao = f"{equacao:_}".replace(".",",").replace("_",".")

        return equacao
    #|-----------------Arredondar Valores-----------------|
    def arredondar(self, num):
        around_num = str(num)
        if "," in around_num:
            i = around_num.find(",")
            if len(around_num[i+1:]) > 7:
                around_num = around_num[:i+1+7]
            elif int(around_num[i+1:]) == 0:
                around_num = around_num[:i]
        return around_num
    #|-----------------Arredondar Valores-----------------|
    def CALCULO(self, conta):
        equacao = self.converter(conta, "eua")
        troca_simbolos_matematicos = {'+':'+','-':'-','×':'*','÷':'/','^':'**','√':'√'}
        simbolos_matematicos = ['+','-','×','÷','^','√']
        simbolos_matematicos_alg = troca_simbolos_matematicos.values()

        #troca os simbolos aritiméticos da matemática por simbolos matemáticos em programação:
        if "√" in equacao:
            equacao = self.encontrar_raizes(equacao)
        _equation_ = "".join(troca_simbolos_matematicos[cr] if cr in simbolos_matematicos else cr for cr in equacao)
        
        if '(' in _equation_ or ')' in _equation_:#--------verifica se tem parenteses na equação:
            qntd = 0
            qntd_parents_E = _equation_.count('(')
            qntd_parents_D = _equation_.count(')')

            if qntd_parents_E != qntd_parents_D:
                if qntd_parents_E > qntd_parents_D:
                    qntd = qntd_parents_E - qntd_parents_D
                    _equation_ += (')' * qntd)

                elif qntd_parents_E < qntd_parents_D:
                    qntd = qntd_parents_D - qntd_parents_E
                    _equation_ = ('('* qntd) + _equation_

            _equation_ = _equation_.replace(')(',')*(').replace(')√',')*√')

            for simble in simbolos_matematicos_alg:
                if f'){simble}(' in _equation_:
                    _equation_ = '(' + _equation_ + ')'

            for N in range(10):
                _equation_ = _equation_.replace(f'{N}(',f'{N}*(').replace(f'){N}',f')*{N}')

        try:
            resultado = eval(_equation_)
            resultado = self.converter(resultado, "br")
            resultado = self.arredondar(resultado)
        except:
            self.ERRO()
        else:
            return self.arredondar(resultado)

    def funcionalidade(self, tipo, tecla):
        if tipo == "digitar":
            return lambda: self.digitar(tecla)
        elif tipo == "apagar um":
            return lambda: self.apagar_um()
        elif tipo == "apagar tudo":
            return lambda: self.apagar_tudo()

        elif tipo == "enviar equacao":
            return lambda: self.enviar_equacao()
        
        return lambda: None
    
    def digitar(self, tecla):
        tecla_normal = tecla
        # Inicializando o texto do console e da equação se estiver em erro
        if "<ERROR>" in self.console_calculadora["text"]:
            self.apagar_tudo()
        texto_atual = self.console_calculadora["text"]

        if tecla == "^":
            self.exponenciacao()
            return

        if self.digitar_minicaracteres:
            tecla = self.mini_caracteres.get(tecla, tecla)

        # Regra 1: não permitir símbolos matemáticos no início, exceto '-' e '√'
        if not texto_atual and tecla in self.simbolos_matematicos and tecla not in ['-', '√']:
            return texto_atual

        if texto_atual:
            ultimo_caractere = texto_atual[-1]

            # Regra 5: "." e "," não podem ser inseridos após símbolos matemáticos ou após "(" e ")"
            if tecla in ['.', ','] and (ultimo_caractere in self.simbolos_matematicos + ['(', ')']):
                return texto_atual

            # Tratando inserção de símbolos matemáticos
            if tecla in self.simbolos_matematicos:
                # Regra 6: Se o último e o atual caracteres são símbolos matemáticos, substitua o último pelo atual
                if ultimo_caractere in self.simbolos_matematicos:
                    if tecla not in ['-', '√']:
                        if not (ultimo_caractere == '√' and tecla == '+'):  # Permitir "√" seguido por "+"
                            texto_atual = texto_atual[:-1]  # Remova o último caractere
                    else:
                        # Permite inserção direta apenas para "-" e "√" após outro símbolo matemático
                        if tecla == "-":
                            if ultimo_caractere != "-":
                                pass
                            else:
                                texto_atual = texto_atual[:-1]

                # Regra 4: "√" pode ser inserido após "√"
                if tecla == '√' and ultimo_caractere == '√':
                    pass  # Permitir múltiplos '√'

        # Adicionando o caractere digitado ao texto do console e atualizando a equação
        self.console_calculadora["text"] = texto_atual + tecla
        self.equacao_console = self.equacao_console + tecla_normal

    def apagar_um(self):
        self.console_calculadora["text"] = self.console_calculadora["text"][:-1]
        self.equacao_console = self.equacao_console[:-1]

    def apagar_tudo(self):
        self.console_calculadora["text"] = ""
        self.console_calculadora["fg"] = 'black'
        self.console_resultado["fg"] = 'black'
        self.equacao_console = ""

    def exponenciacao(self):
        if self.botao_expoente["text"] == "^" and len(self.equacao_console) != 0 and self.console_calculadora["text"][-1] != '-':
            self.console_calculadora["text"] += "^"
            self.equacao_console += "^"
            self.botao_expoente["text"] = "ᵛ"
            self.digitar_minicaracteres = True
        else:
            self.botao_expoente["text"] = "^"
            self.digitar_minicaracteres = False

    def enviar_equacao(self):
        resultado = self.CALCULO(self.equacao_console)
        self.console_resultado["text"] = resultado

    def ERRO(self):
        self.console_calculadora["text"] = "<ERROR>"
        self.console_resultado["text"] = "="
        self.console_resultado["fg"] = "red"
        self.console_calculadora["fg"] = "red"

    def desenhar_tela(self):
        comando = None

        self.console_calculadora = tk.Label(text='',fg='black',bg='gray',font=("Arial",34),height=2,width=18,anchor='e')
        self.console_calculadora.grid(row=0,column=0,columnspan=5,sticky='NSWE')

        self.console_resultado = tk.Label(text='',fg='black',bg='gray',font=("Arial",22),height=1,width=18,anchor='ne')
        self.console_resultado.grid(row=1,column=0,columnspan=5,sticky='NSWE')

        for x in range(len(self.matriz_botoes)):
            for y in range(len(self.matriz_botoes[0])):
                tecla = self.matriz_botoes[x][y]
                if " " in tecla:
                    continue

                if tecla in self.simbolos_matematicos:
                    self.cor_tecla, self.cor_botao = self.cor_buttons["simbles"]
                    comando = "digitar"
                elif tecla == "←":
                    self.cor_tecla, self.cor_botao = self.cor_buttons["←"]
                    comando = "apagar um"
                elif tecla == "clear":
                    self.cor_tecla, self.cor_botao = self.cor_buttons["clear"]
                    comando = "apagar tudo"
                else:
                    self.cor_tecla, self.cor_botao = ("white","black")
                    comando = "digitar"
                
                tk.Button(self.tela,text=tecla,fg=self.cor_tecla,bg=self.cor_botao,font=("Arial",20),height=1,width=5,
                        command=self.funcionalidade(comando, tecla)).grid(row=x+2,column=y,sticky='NSWE')

def main():
    Calculadora = CALCULADORA()
    Calculadora.desenhar_tela()
    Calculadora.tela.mainloop()

if __name__ == "__main__":
    main()