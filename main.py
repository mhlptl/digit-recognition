from gui import *
from utilities import *

root = tk.Tk()
root.resizable(False, False)
root.title('Digit Recognition')
root.geometry('300x375')
app = Application(root)
root.mainloop()