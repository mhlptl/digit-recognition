import tkinter as tk


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()
		self.createDrawArea()
		self.showResults()
		self.createButtons()

	def createDrawArea(self):
		self.drawArea = tk.Canvas(self, height=250, width=745, bg='black')
		self.drawArea.grid(row=0, column=0, padx=25, pady=10)
		self.drawArea.bind('<B1-Motion>', self.draw)

	def createButtons(self):
		self.frame = tk.Frame(self)
		self.frame.grid(row=2, column=0, padx=25, pady=10)

		self.submit = tk.Button(self.frame)
		self.submit['text'] = 'Submit'
		self.submit['command'] = self.handleSubmit
		self.submit.grid(row=0, column=0, ipadx=25, padx=15)

		self.delete = tk.Button(self.frame)
		self.delete['text'] = 'Delete'
		self.delete['command'] = self.handleDelete
		self.delete.grid(row=0, column=1, ipadx=25, padx=15)

	def draw(self, event):
		x, y = event.x, event.y
		self.drawArea.create_rectangle((x,y)*2, outline='white', fill='white')

	def showResults(self):
		self.resultFrame = tk.Frame(self)
		self.resultFrame.grid(row=1, column=0, padx=25, sticky='w')
		
		self.numberLabel = tk.Label(self.resultFrame, text='Predicted Number: ')
		self.numberLabel.grid(row=0, column=0, sticky='w')

		self.resultingNumber = tk.StringVar(self)
		self.showNum = tk.Label(self.resultFrame, textvariable=self.resultingNumber)
		self.showNum.grid(row=0, column=1, sticky='e')

		self.accuracyLabel = tk.Label(self.resultFrame, text='Accuracy: ')
		self.accuracyLabel.grid(row=1, column=0, sticky='w')

		self.accuracyVar = tk.StringVar(self)
		self.accuracy = tk.Label(self.resultFrame, textvariable=self.accuracyVar)
		self.accuracy.grid(row=1, column=1, sticky='e')

	def handleSubmit(self):
		print('submitted')
	
	def handleDelete(self):
		self.drawArea.delete('all')
