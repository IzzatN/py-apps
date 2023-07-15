import customtkinter as ctk
from settings import *

try:
  from ctypes import windll, byref, sizeof, c_int
except:
  pass

class App(ctk.CTk):
  def __init__(self):
    super().__init__(fg_color = GREEN)
    self.title('')
    self.iconbitmap('empty.ico')
    self.geometry('400x400')
    self.resizable(False, False)
    self.change_title_bar_color() # works only on Windows

    self.columnconfigure(0, weight = 1)
    self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')

    ResultText(self)
    WeightInput(self)

    self.mainloop()

  def change_title_bar_color(self):
    try:
      HWND = windll.user32.GetParent(self.winfo_id())
      DWMWA_ATTRIBUTE = 35
      COLOR = TITLE_HEX_COLOR
      windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
    except:
      pass

class ResultText(ctk.CTkLabel):
  def __init__(self, parent):
    font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
    super().__init__(master = parent, text = 22.5, font = font, text_color = WHITE)
    self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nsew')

class WeightInput(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(master = parent, fg_color = WHITE)
    self.grid(column = 0, row = 2, sticky = 'nsew', pady = 10, padx = 10)

    self.rowconfigure(0, weight = 1, uniform = 'b')
    self.columnconfigure(0, weight = 2, uniform = 'b')
    self.columnconfigure(1, weight = 1, uniform = 'b')
    self.columnconfigure(2, weight = 3, uniform = 'b')
    self.columnconfigure(3, weight = 1, uniform = 'b')
    self.columnconfigure(3, weight = 2, uniform = 'b')

    font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
    label = ctk.CTkLabel(self, text = '70kg', text_color = BLACK, font = font)
    label.grid(row = 0, column = 2)

    minus_button = ctk.CTkButton(
      self,
      text = '-',
      font = font,
      text_color = BLACK
    )
    minus_button.grid(
      row = 0,
      column = 0,
      sticky = 'ns',
      padx = 8,
      pady = 8
    )

if __name__ == '__main__':
  App()
