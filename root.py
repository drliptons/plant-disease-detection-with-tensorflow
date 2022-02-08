import tkinter as tk
import time

from user_interface import UserInterface


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window title
        self.title("Plant Disease Detection")

        # Window configurations
        self.geometry("600x720")
        self.configure(bg="#F7FBFC")

        # Delay closing window before close
        self.protocol("WM_DELETE_WINDOW", self._close_delay)

        # Initialize user interface
        self._ui = tk.Frame(self)
        self._ui = UserInterface(self)
        self._ui.pack()

    def _close_delay(self):
        time.sleep(0.5)
        self.destroy()
