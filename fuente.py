from tkinter import Tk, font 
from tkinter.ttk import Button, Label 
  
  
class App: 
    def __init__(self, master: Tk) -> None: 
        self.master = master 
  
        
        self.defaultFont = font.nametofont("TkDefaultFont") 
  
        
        
        self.defaultFont.configure(family="New Wild Words", 
                                   size=19, 
                                   weight=font.BOLD) 
  

        self.label = Label(self.master, text="Etiqueta") 
        self.label.pack() 
        
        self.btn = Button(self.master, text="Boton") 
        self.btn.pack() 
  
  
if __name__ == "__main__": 
    
    root = Tk() 
    root.geometry("300x150") 
    root.title("Etiqueta") 
  
    #print(font.names()) 
  
    app = App(root) 

    root.mainloop() 
