from calculadora import *
from guizero import App, Picture, TextBox, Text, PushButton, Drawing

app = App(title="a'mu b1.5", width=720, height=480)

def resultado(resultado):
    resultado.clear()
    resultado.image = ".\\why not.png"
    resultado.text(20, 20, resultado)

# Var resetting
app.bg = "#424242"
version = "b1.5"
resultado = 0

# GUI
title = Text(app, text="alayomas' math utilities", size=17, color="#7F7F7F", font="Cascadia Code")
subtitleVersion = Text(app, text=version, size=12, color="#7F7F7F", font="Cascadia Code")
operacaotitle = Text(app, text="Insert operation below", color="#A0A0A0", font="Cascadia Code")
operacao = TextBox(app, text="", width=24)
numinserttitle = Text(app, text="Insert numbers below and press [New number]", color="#A0A0A0", font="Cascadia Code")
numinsert = TextBox(app, text="", width=24)
operacao.bg = "#565656"
numinsert.bg = "#565656"
resultado = Drawing(app, width="fill", height="fill")
# operaçao numero [pushbutton,  write numero into calculadora, reset numero]
app.display()