import tkinter as tk

from RPLCD	import CharLCD
import RPi.GPIO as GPIO

lcd = CharLCD(cols=16, rows=2, pin_rs=17, pin_e=18, pins_data=[6, 13, 19, 26], numbering_mode=GPIO.BCM)


lcd.clear()
lcd.write_string("    Welcome")
lcd.cursor_pos=(1,0)
lcd.write_string(" Embedded Linux")

class ProjectWindow:
	
	def __init__(self, master):
		
		# Bar Title
		master.title("Project Title Name ")
		
		#Text 
		self.LocText1 = tk.Label(master, text="By Eng: Muhammad (Ali) Ammar ", fg="blue", font=("Arial", 13, "bold"))
		self.LocText1.place(x=0,y=0)
		
		
		self.button1 = tk.Button(master, text="Enter Lcd Text", command=self.LCDCallback)
		self.button1.place(x=0, y=200)  # Set x and y coordinates in pixels
		
		self.Entry1 = tk.Entry(master, width = 15)
		self.Entry1.place(x= 230, y = 200)
		
		##### to call function automaticlly if button is pressed 
		self.Entry1.bind("<Return>", self.LCDCallback )
		

        
	def LCDCallback(self,event = None):
		
		lcd_str = self.Entry1.get()
		lcd.clear()
		lcd.write_string(lcd_str)
		self.Entry1.delete(0,'end')
		
	


container = tk.Tk()
container.geometry("400x400+500+150")
container.resizable(False,False)

ProjectWindow(container)

container.mainloop()

