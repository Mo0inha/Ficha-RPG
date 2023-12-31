import tkinter as tk
from model.model_ViewMenu import ModelViewMenu

class ViewMenu(tk.Frame):
    def __init__(self, view_controller):
        tk.Frame.__init__(self, view_controller.master, width=500, height=500)
        self.pack_propagate(0)
        
        self.model = ModelViewMenu()
        
        label = tk.Label(self, text="Let's Play", font=("Impact", 60))
        label.pack(pady=5)
        label = tk.Label(self, text="RPG?", font=("French Script MT", 70))
        label.pack(pady=15)
        
        next_button = tk.Button(self, text="Próxima", command=lambda: view_controller.switch_view(view_controller.current_view_index + 1))
        next_button.pack()
        
        credits_button = tk.Button(self, text="Créditos", command=self.show_credits)
        credits_button.pack(pady=10)
        
        other_sheets_button = tk.Button(self, text="Outras Fichas", command=self.show_other_sheets)
        other_sheets_button.pack()
        
    def show_credits(self):
        self.model.show_credits()
    
    def show_other_sheets(self):
        self.model.show_other_sheets()
