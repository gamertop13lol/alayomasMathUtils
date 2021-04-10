from calculadora import *
from guizero import App, Picture, TextBox, Text, PushButton, Drawing
from math import prod

app = App(title="a'mu v1.0", width=720, height=550) # App dimensions and title

listaOperacao = [] # Set the variable's initial value

def drawer(resultado): # Draw the result into the window
    drawingres.clear()
    drawingres.image(0, 0, ".\why not.png")
    drawingres.text(20, 20, str(resultado), font="Cascadia Code", color="#A0A0A0", size=15)

def numberAppend(): # Append a number to the calculation list
    numberToAppend = float(numinsert.value)
    global listaOperacao
    listaOperacao.append(numberToAppend)

def clearlist(): # Clear the calculation list
    global listaOperacao
    listaOperacao = []

def flist():
    app.info("Function list:", 
    "divisores, multiplos, listavertices,\nmmc, mdc, potencia,\nsubtracao, divisao, reverso,\nelementor, maximo, somaacu,\nsoma and multiplicacao.")

def calcular(): # Calculate a result based on the operation
    global resultado
    global listaOperacao
    operation = operacao.value
    if operation == "divisores":
        resultado = divisores(listaOperacao[0])
    elif operation == "multiplos":
        resultado = multiplos(listaOperacao[0], listaOperacao[1])
    elif operation == "listavertices":
        resultado = listavertices(listaOperacao[0], listaOperacao[1])
    elif operation == "mmc":
        resultado = mmc(listaOperacao[0], listaOperacao[1], 256)
    elif operation == "mdc":
        resultado = mdc(listaOperacao[0], listaOperacao[1])
    elif operation == "potencia":
        resultado = potencia(listaOperacao[0], listaOperacao[1])
    elif operation == "subtracao":
        resultado = subtracao(listaOperacao)
    elif operation == "divisao":
        resultado = divisao(listaOperacao)
    elif operation == "reverso":
        resultado = reverso(listaOperacao)
    elif operation == "elementor":
        resultado = elementor(listaOperacao[0], listaOperacao[1:])
    elif operation == "maximo":
        resultado = maximo(listaOperacao)
    elif operation == "somaacu":
        resultado = somaacu(listaOperacao)
    elif operation == "soma":
        resultado = sum(listaOperacao)
    elif operation == "multiplicacao":
        resultado = prod(listaOperacao)
    else:
        app.error("Error", "That function is non-existant!")
    clearlist()
    drawer(resultado)

# Variable setup
app.bg = "#424242"
version = "v1.0"
resultado = 0

# GUI

title = Text(app, text="alayomas' math utilities", size=17, color="#7F7F7F", font="Cascadia Code") # Title and subtitle
subtitleVersion = Text(app, text=version, size=12, color="#7F7F7F", font="Cascadia Code")

operacaotitle = Text(app, text="Insert operation below", color="#A0A0A0", font="Cascadia Code") # Operation box
operacao = TextBox(app, text="", width=24)

numinserttitle = Text(app, text="Insert numbers below and press [New number]", color="#A0A0A0", font="Cascadia Code") # Number box
numinsert = TextBox(app, text="0", width=24)

spacera = Text(app, text="") # Spacer A

newNumber = PushButton(app, numberAppend, text="New number") # New number button
newNumber.bg = "#565656"
newNumber.text_size = 13
newNumber.font = "Cascadia Code"

spacerb = Text(app, text="") # Spacer B

clear = PushButton(app, clearlist, text="Clear list") # Clear list button
clear.bg = "#565656"
clear.text_size = 13
clear.font = "Cascadia Code"

spacerc = Text(app, text="") # Spacer C

calculate = PushButton(app, calcular, text="Calculate") # "Calculate" 
calculate.bg = "#565656"
calculate.text_size = 13
calculate.font = "Cascadia Code"

spacerd = Text(app, text="") # Spacer D

functionlist = PushButton(app, flist, text="Function List") # Function List
functionlist.bg = "#565656"
functionlist.text_size = 11
functionlist.font = "Cascadia Code"

# BG colors
operacao.bg = "#565656"
numinsert.bg = "#565656"

# Drawing variable initialize
drawingres = Drawing(app, width="fill", height="fill")

# Display
app.display()