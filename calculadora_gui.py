import tkinter as tk
from tkinter import ttk

# calculadora_gui.py
# ├── Importações
# ├── Classe ou funções principais:
# │   ├── criar_layout()
# │   ├── atualizar_display(valor)
# │   ├── calcular(expressao)
# │   ├── tratar_erro(mensagem)
# │   ├── adicionar_ao_historico(expressao, resultado)
# │   └── main()
# └── Loop de eventos da GUI

_root = None
_display = None
_historico = None
_novo_numero = False
_LIMITE_DISPLAY = 18


def criar_layout():
    global _display, _historico

    _root.title("Calculadora")
    teclado = ttk.Frame(_root, padding=10)
    teclado.grid(row=0, column=0)
    painel_historico = ttk.LabelFrame(_root, text="Histórico", padding=10)
    painel_historico.grid(row=0, column=1, sticky="ns", padx=(0, 10), pady=10)

    _display = tk.StringVar(value="0")
    ttk.Entry(
        teclado, textvariable=_display, justify="right", state="readonly", width=18
    ).grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 8))

    def clicar_botao(event):
        global _novo_numero
        valor = event.widget["text"]
        atual = _display.get()

        if valor == "=":
            calcular(atual)
        elif valor == "C":
            atualizar_display("0")
            _historico.delete(0, tk.END)
            _novo_numero = False
        elif valor == "←":
            atualizar_display(atual[:-1] or "0")
            _novo_numero = False
        else:
            if atual.startswith("Erro:"):
                atual = "0"
            if _novo_numero and (valor.isdigit() or valor == "."):
                atual = "0"
            if atual == "0" and valor.isdigit():
                atual = ""
            atualizar_display(atual + valor)
            _novo_numero = False

    botoes = (
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("0", ".", "←", "+"),
    )
    for linha, valores in enumerate(botoes, start=1):
        for coluna, valor in enumerate(valores):
            botao = ttk.Button(teclado, text=valor)
            botao.bind("<Button-1>", clicar_botao)
            botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

    for coluna, valor in ((0, "C"), (2, "=")):
        botao = ttk.Button(teclado, text=valor)
        botao.bind("<Button-1>", clicar_botao)
        botao.grid(row=5, column=coluna, columnspan=2, sticky="nsew", padx=2, pady=2)

    _historico = tk.Listbox(painel_historico, height=10, width=24)
    _historico.grid(row=0, column=0)


def atualizar_display(valor):
    texto = str(valor)
    if not texto.startswith("Erro:"):
        texto = texto[:_LIMITE_DISPLAY]
    _display.set(texto)


def calcular(expressao):
    global _novo_numero

    numeros = []
    operadores = []
    numero = ""

    for caractere in expressao:
        if caractere in "+-*/":
            if not numero:
                tratar_erro("Expressão inválida")
                return
            numeros.append(numero)
            operadores.append(caractere)
            numero = ""
        elif caractere.isdigit() or caractere == ".":
            numero += caractere
        else:
            tratar_erro("Expressão inválida")
            return

    if not numero:
        tratar_erro("Expressão inválida")
        return
    numeros.append(numero)

    try:
        numeros = [float(valor) for valor in numeros]
    except ValueError:
        tratar_erro("Expressão inválida")
        return

    for indice, operador in enumerate(operadores):
        if operador == "/" and numeros[indice + 1] == 0:
            tratar_erro("Divisão por zero")
            return

    indice = 0
    while indice < len(operadores):
        if operadores[indice] in "*/":
            esquerda = numeros[indice]
            direita = numeros[indice + 1]
            if operadores[indice] == "*":
                numeros[indice] = esquerda * direita
            else:
                numeros[indice] = esquerda / direita
            del numeros[indice + 1]
            del operadores[indice]
        else:
            indice += 1

    resultado = numeros[0]
    for indice, operador in enumerate(operadores):
        if operador == "+":
            resultado += numeros[indice + 1]
        else:
            resultado -= numeros[indice + 1]

    adicionar_ao_historico(expressao, resultado)
    atualizar_display(resultado)
    _novo_numero = True


def tratar_erro(mensagem):
    atualizar_display(f"Erro: {mensagem}")


def adicionar_ao_historico(expressao, resultado):
    _historico.insert(0, f"{expressao} = {resultado}")
    if _historico.size() > 5:
        _historico.delete(5, tk.END)


def main():
    global _root
    _root = tk.Tk()
    criar_layout()
    _root.mainloop()


if __name__ == "__main__":
    main()
