import tkinter as tk
from tkinter import ttk
import dolar_api


# Funcion del evento
def dolar_info():
    # Llamamos a la API cada vez que que demos click para actulizar los valores
    dolar_api.DolarExchangeAPI().call()

    label_oficial.config(text=f'Dolar Oficial\n'
                              f'Compra: {dolar_api.dolar_oficial.info_buy()}\n'
                              f'Venta: {dolar_api.dolar_oficial.info_sell()}')

    label_blue.config(text=f'Dolar Blue\n'
                           f'Compra: {dolar_api.dolar_blue.info_buy()}\n'
                           f'Venta: {dolar_api.dolar_blue.info_sell()}')

    label_bcra.config(text=f'Dolar BCRA\n'
                           f'Compra: {dolar_api.dolar_bcra.info_buy()}\n'
                           f'Venta: {dolar_api.dolar_bcra.info_sell()}')


# Creamos la ventana y le damos caracteristicas
main_window = tk.Tk()
main_window.geometry('600x400')
main_window.title('Dolar APP')
main_window.config(background='gray')

# Creamos una etiqueta de bienvenida
label_welcome = ttk.Label(main_window,
                          text="Cotización del dolar en tiempo real",
                          font=("Helvetica", 14),
                          foreground='black',
                          background='gray62',
                          wraplength=300,
                          justify='center')
label_welcome.grid(column=1, row=0, sticky='NWSE')

# Configurar el grid
main_window.rowconfigure(1, weight=2)
main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=2)

# Creamos las etiquetas para los tipos de cambio

# label para el dolar oficial
label_oficial = ttk.Label(main_window,
                          text=f'Dolar Oficial\n'
                               f'Compra: {dolar_api.dolar_oficial.info_buy()}\n'
                               f'Venta: {dolar_api.dolar_oficial.info_sell()}',
                          font=("Helvetica", 14),
                          foreground='black',
                          background='gray62',
                          wraplength=200,
                          justify='center')
label_oficial.grid(column=0, row=1)

# label para el dolar blue
label_blue = ttk.Label(main_window,
                       text=f'Dolar Blue\n'
                            f'Compra: {dolar_api.dolar_blue.info_buy()}\n'
                            f'Venta: {dolar_api.dolar_blue.info_sell()}',
                       font=("Helvetica", 14),
                       foreground='black',
                       background='gray62',
                       wraplength=200,
                       justify='center')
label_blue.grid(column=1, row=1)

# label para el dolar bcra
label_bcra = ttk.Label(main_window,
                       text=f'Dolar BCRA\n'
                            f'Compra: {dolar_api.dolar_bcra.info_buy()}\n'
                            f'Venta: {dolar_api.dolar_bcra.info_sell()}',
                       font=("Helvetica", 14),
                       foreground='black',
                       background='gray62',
                       wraplength=200,
                       justify='center')
label_bcra.grid(column=2, row=1)

# Definimos el botón para actualizar la cotización
refresh_button = ttk.Button(main_window, text='Actualizar', command=dolar_info)
refresh_button.grid(row=2, column=1, sticky='NSWE', padx=20, pady=50)

# Le damos estilo al botón
button_style = ttk.Style()
button_style.theme_use('alt')
button_style.configure('TButton',
                       font=('Helvetica', 12),
                       foreground='black',
                       background='gray',
                       width=20,
                       focuscolor='none')

# Iniciamos la ventana hasta que se cierra el programa
main_window.mainloop()
