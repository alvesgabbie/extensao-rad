import tkinter as tk
from tkinter import ttk

class InventorySystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Controle de Estoque - RD Locações")
        self.geometry("1000x600")

        # Títulos
        self.title_label = tk.Label(self, text="RD Locações", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.subtitle_label = tk.Label(self, text="Controle de Estoque", font=("Arial", 18))
        self.subtitle_label.pack(pady=5)

        # Frame principal
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=10)

        # Produtos e seus estoques
        self.products = {
            "Betoneira": {"alugados": 0, "estoque": 61},
            "Martelete 30kg": {"alugados": 0, "estoque": 2},
            "Martelete 10kg": {"alugados": 0, "estoque": 2},
            "Martelete 5kg": {"alugados": 0, "estoque": 1},
            "Andaime": {"alugados": 0, "estoque": 1200},
            "Plataforma": {"alugados": 0, "estoque": 60},
            "Compactador de Solo": {"alugados": 0, "estoque": 2}
        }

        self.create_product_widgets()

    def create_product_widgets(self):
        for product, info in self.products.items():
            frame = tk.Frame(self.main_frame)
            frame.pack(pady=5, fill="x")

            product_label = tk.Label(frame, text=product, font=("Arial", 14), width=20, anchor="w")
            product_label.pack(side=tk.LEFT, padx=10)

            alugados_label = tk.Label(frame, text=f"Alugados: {info['alugados']}", font=("Arial", 14), width=20)
            alugados_label.pack(side=tk.LEFT, padx=10)

            estoque_label = tk.Label(frame, text=f"Estoque: {info['estoque']}", font=("Arial", 14), width=20)
            estoque_label.pack(side=tk.LEFT, padx=10)

            rent_button = ttk.Button(frame, text="Registrar Aluguel")
            rent_button.pack(side=tk.LEFT, padx=10)

            return_button = ttk.Button(frame, text="Registrar Devolução")
            return_button.pack(side=tk.LEFT, padx=10)

if __name__ == "__main__":
    app = InventorySystem()
    app.mainloop()
