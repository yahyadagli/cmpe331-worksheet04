"""
    Stage: Development-01
    @author:Mustafa Yahya Dağlı, 119202067
    @author:Burak Seymen, 117202076
"""

import tkinter as tk


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()
        self.window.title("Şişli Kütüphanesi")
        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Kullanıcı")
        self.lbl02 = tk.Label(text="Şifre")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Giriş")
        self.btn02 = tk.Button(text="İptal")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        if event.widget == self.btn01:
            if self.txt01.get() == "admin" and self.txt02.get() == "şifre":
              self.window = tk.Tk()

              self._initializeGUI()
              self._addGUIElementsToFrame()
              self.window.title("Çevrimiçi Kütüphane")
        
              self.window.mainloop()  
        if event.widget == self.btn02:
            if not self.txt01.get() == "admin" and self.txt02.get() == "şifre":
                pass


# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
