
import sys
import PySimpleGUI as sg

layout = [

    [sg.Text('Calculador de Sinais de Raízes de uma equação do segundo grau')],

    [sg.Text('Informe A:', key = 'A'), sg.Input( key = 'ValA')],

    [sg.Text('Informe B:', key = 'B'), sg.Input( key = 'ValB')],

    [sg.Text('Informe C:', key = 'C'), sg.Input(key = 'ValC')],

    [sg.Button('Calcular', key = 'CALCULAR')],

    [sg.Text('Seu resultado aparecerá aqui', key = 'RESULTADO')]

]

window = sg.Window('Calculador de Sinais de Raízes de uma equação do segundo grau', layout)

while True:
    evento, valores = window.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'CALCULAR':
        A = float(valores['ValA'])
        B = float(valores['ValB'])
        C = float(valores['ValC'])
                
        p = float(C / A)

        delta = delta = float((B**2)-
        (4*A*C))

        s = float((-B)/A)

        ifp =("Seu produto resultou em: "+ str(p) +", logo, a equação possue duas raízes de sinais iguais")

        elsep = ("As raízes possuem sinais opostos")

        ifd = ("Δ resultou em um valor positivo: "+ str(delta) +", consequentemente a soma resultou em: "+ str(s))

        elsed = ("Δ resultou em um valor menor que 0 (negativo), o resultado obtido foi: "+ str(delta))

        ifs = ("x1 e x2 são positivos (x1; x2 > 0)")

        elses = ("x1 e x2 são negativos (x1; x2 < 0)")
                                
        if (p > 0) and (delta >= 0) and (s > 0):
            output_string = f'{ifp},\n {ifd},\n {ifs}'
            window['RESULTADO'].update(output_string)

        if (p < 0):
            output_string = f'{elsep}'
            window['RESULTADO'].update(output_string)
        
        if (p > 0) and (delta < 0 ):
            output_string = f'{ifp},\n {elsed},'
            window['RESULTADO'].update(output_string)

        if (p > 0) and (delta >= 0) and (s <= 0):
            output_string = f'{ifp},\n {ifd},\n {elses}'
            window['RESULTADO'].update(output_string)

    


window.close()