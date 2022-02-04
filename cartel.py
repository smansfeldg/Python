import tkinter as tk
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Cartelito")

text = tk.Label(ventana, text= 'La concha de\ntu madre Bob Esponja\n',
                font=("Courier", 20)
                )
text.place(relx=0.5, rely=0.5,
           anchor='center')

ventana.mainloop()
