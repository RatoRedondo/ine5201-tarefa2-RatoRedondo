# Calculadora GUI


Uma calculadora gráfica desenvolvida em Python utilizando `tkinter` e `ttk`. O programa permite realizar operações básicas, exibe os resultados no display e mantém um histórico das últimas operações realizadas.


## Funcionalidades


- Adição, subtração, multiplicação e divisão.
- Números decimais.
- Botão para apagar o último caractere.
- Botão para limpar o display e o histórico.
- Tratamento de expressões inválidas.
- Tratamento de divisão por zero.
- Histórico com até cinco operações.
- Interface gráfica simples e intuitiva.


## Requisitos


- Python 3 instalado.
- Biblioteca `tkinter`, geralmente incluída na instalação padrão do Python.


## Como executar


Salve o código em um arquivo chamado `calculadora_gui.py` e execute:


```bash
python calculadora_gui.py
```


No Windows, também pode ser necessário usar:


```bash
py calculadora_gui.py
```


## Como usar


1. Clique nos números para montar uma expressão.
2. Utilize os operadores `+`, `-`, `*` ou `/`.
3. Clique em `=` para calcular.
4. Use `←` para apagar o último caractere.
5. Use `C` para limpar o display e o histórico.


Exemplo:


```text
7 + 3 * 2 = 13
```


A multiplicação e a divisão são calculadas antes da adição e da subtração.


## Estrutura principal




































| Função | Descrição |
| --- | --- |
| `criar_layout()` | Cria a janela, o display, os botões e o histórico. |
| `atualizar_display(valor)` | Atualiza o valor exibido na calculadora. |
| `calcular(expressao)` | Processa a expressão matemática e calcula o resultado. |
| `tratar_erro(mensagem)` | Exibe mensagens de erro no display. |
| `adicionar_ao_historico(expressao, resultado)` | Adiciona uma operação ao histórico. |
| `main()` | Inicializa a aplicação e o loop de eventos. |



## Tratamento de erros


O programa identifica e informa situações como:


- Expressões inválidas.
- Operadores sem números.
- Expressões terminadas com operadores.
- Divisão por zero.
- Números decimais inválidos.


## Tecnologias utilizadas


- Python
- Tkinter
- ttk


## Observação


No arquivo Python real, confirme se os caracteres aparecem sem barras invertidas indevidas. Por exemplo:


```python
if __name__ == "__main__":
```


e:


```python
if operador == "*":
```
