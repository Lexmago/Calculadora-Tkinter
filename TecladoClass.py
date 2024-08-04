import tkinter as tk
from tkinter import Button
from funcion_suma import suma
from funcion_resta import resta
from funcion_multi import multi
from funcion_div import div

class Teclado():
    def __init__(self, window):
        self.window = window
        self.window.title("--- Calculadora ---")
        self.window.geometry("500x460")
        self.window.resizable(False, False)
        self.window.configure(bg="cadetblue")

        self.frame = tk.Frame(self.window, bg="cadetblue")
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky='s')

        self.display = tk.Frame(self.window, bg='white', width=442, height=80)
        self.display.grid(row=0, column=0, padx=10, pady=28, sticky='n')
        self.display.grid_propagate(False)

        self.fuente = ("Helvetica", 20)

        self.btn7 = tk.Button(self.frame, text="7", command=self.siete, width=5, height=2, font=self.fuente, anchor="center")
        self.btn8 = tk.Button(self.frame, text="8", command=self.ocho, width=5, height=2, font=self.fuente, anchor="center")
        self.btn9 = tk.Button(self.frame, text="9", command=self.nueve, width=5, height=2, font=self.fuente, anchor="center")

        self.btn4 = tk.Button(self.frame, text="4", command=self.cuatro, width=5, height=2, font=self.fuente, anchor="center")
        self.btn5 = tk.Button(self.frame, text="5", command=self.cinco, width=5, height=2, font=self.fuente, anchor="center")
        self.btn6 = tk.Button(self.frame, text="6", command=self.seis, width=5, height=2, font=self.fuente, anchor="center")

        self.btn1 = tk.Button(self.frame, text="1", command=self.uno, width=5, height=2, font=self.fuente, anchor="center")
        self.btn2 = tk.Button(self.frame, text="2", command=self.dos, width=5, height=2, font=self.fuente, anchor="center")
        self.btn3 = tk.Button(self.frame, text="3", command=self.tres, width=5, height=2, font=self.fuente, anchor="center")

        self.btnsum = tk.Button(self.frame, text="+", command=self.mas, width=5, height=2, font=self.fuente, anchor="center")
        self.btnrest = tk.Button(self.frame, text="-", command=self.menos, width=5, height=2, font=self.fuente, anchor="center")
        self.btnmult = tk.Button(self.frame, text="x", command=self.por, width=5, height=2, font=self.fuente, anchor="center")
        self.btndiv = tk.Button(self.frame, text="/", command=self.entre, width=5, height=2, font=self.fuente, anchor="center")
        self.btnigual = tk.Button(self.frame, text="=", command=self.igual, width=5, height=2, font=self.fuente, anchor="center", bg="steelblue", fg="white")
        self.btncero = tk.Button(self.frame, text="0", command=self.cero, width=5, height=2, font=self.fuente, anchor="center")
        self.btnsqr = tk.Button(self.frame, text="c", command=self.clear, width=5, height=2, font=self.fuente, anchor="center", bg= "silver", fg="black")

        self.btn7.grid(row=0, column=0, padx=5, pady=5)
        self.btn8.grid(row=0, column=1, padx=5, pady=5)
        self.btn9.grid(row=0, column=2, padx=5, pady=5)

        self.btn4.grid(row=1, column=0, padx=5, pady=5)
        self.btn5.grid(row=1, column=1, padx=5, pady=5)
        self.btn6.grid(row=1, column=2, padx=5, pady=5)

        self.btn1.grid(row=2, column=0, padx=5, pady=5)
        self.btn2.grid(row=2, column=1, padx=5, pady=5)
        self.btn3.grid(row=2, column=2, padx=5, pady=5)

        self.btndiv.grid(row=0, column=3, padx=5, pady=5)
        self.btnmult.grid(row=1, column=3, padx=5, pady=5)
        self.btnsum.grid(row=2, column=3, padx=5, pady=5)
        self.btnrest.grid(row=3, column=3, padx=5, pady=5)

        self.btnigual.grid(row=3, column=2, padx=5, pady=5)
        self.btncero.grid(row=3, column=1, padx=5, pady=5)
        self.btnsqr.grid(row=3, column=0, padx=5, pady=5)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.display_current_value = '0' # --El valor que se muestra en el Display de la calculadora--

        #-------------------------------------------------------#
        self.label = tk.Label(self.display, text=self.display_current_value, bg="white", font=("Helvetica", 46), anchor='e')
        self.label.grid(row=0, column=0, sticky='se')
        self.display.grid_columnconfigure(0, weight=1)
        self.display.grid_rowconfigure(0, weight=1)
        #-------------------------------------------------------#

    def uno(self):
        self.display_current_value += '1'
        
        if self.display_current_value == '01':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def dos(self):
        self.display_current_value += '2'
        
        if self.display_current_value == '02':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def tres(self):
        self.display_current_value += '3'
        
        if self.display_current_value == '03':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def cuatro(self):
        self.display_current_value += '4'
        
        if self.display_current_value == '04':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def cinco(self):
        self.display_current_value += '5'
        
        if self.display_current_value == '05':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

    def seis(self):
        self.display_current_value += '6'
        
        if self.display_current_value == '06':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def siete(self):
        self.display_current_value += '7'
        
        if self.display_current_value == '07':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def ocho(self):
        self.display_current_value += '8'
        
        if self.display_current_value == '08':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

    
    def nueve(self):
        self.display_current_value += '9'
        
        if self.display_current_value == '09':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def clear(self):
        self.display_current_value = '0'

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def cero(self):
        self.display_current_value += '0'
        
        if self.display_current_value == '00':
            sincero = self.display_current_value[1:]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')


    def mas(self):
        self.display_current_value += '+'
        
        if self.display_current_value == '0+':
            sincero = self.display_current_value[:1]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

    def menos(self):
        self.display_current_value += '-'
        
        if self.display_current_value == '0-':
            sincero = self.display_current_value[:1]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

    def por(self):
        self.display_current_value += 'x'
        
        if self.display_current_value == '0x':
            sincero = self.display_current_value[:1]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

    def entre(self):
        self.display_current_value += '/'
        
        if self.display_current_value == '0/':
            sincero = self.display_current_value[:1]
            self.display_current_value = sincero

        self.label.config(text=self.display_current_value)
        self.label.grid(row=0, column=0, sticky='se')

# -------------------------------------------------------------- #
    def igual(self):
        if '+' in self.display_current_value:
            r = suma(self.display_current_value)
            self.display_current_value = str(r)

            self.label.config(text=self.display_current_value)
            self.label.grid(row=0, column=0, sticky='se')

        if '-' in self.display_current_value:
            r = resta(self.display_current_value)
            self.display_current_value = str(r)

            self.label.config(text=self.display_current_value)
            self.label.grid(row=0, column=0, sticky='se')

        if 'x' in self.display_current_value:
            r = multi(self.display_current_value)
            self.display_current_value = str(r)

            self.label.config(text=self.display_current_value)
            self.label.grid(row=0, column=0, sticky='se')
        
        if '/' in self.display_current_value:
            r = div(self.display_current_value)
            r = round(r, 4)
            self.display_current_value = str(r)

            self.label.config(text=self.display_current_value)
            self.label.grid(row=0, column=0, sticky='se')