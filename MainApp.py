import tkinter as tk
from tkinter import ttk, Menu

#updated
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
def run_app():
    try:
        # Load the stock tickers from the config file
        #stock_list = read_stock_config("stocks.txt")
        app = MainApp()
        app.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_app()
