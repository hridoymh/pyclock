from tkinter import *
import pyglet
import time

pyglet.font.add_file("Pacifico.ttf")





def g_t():
    l_time = time.strftime("%H:%M")
    ls = time.strftime("%S")
    b1.config(text=l_time)
    b2.config(text=ls)
    b1.after(200,g_t)

def test():
    b2.config(text="done")




main = Tk()

main.overrideredirect(True)
main.geometry("600x300+850+0")
main.wm_attributes("-transparentcolor","#f0f0f0")





b1 = Label(main, text="ok", font=("Pacifico",100),fg="#eeeeee")
b1.place(x=100,y=0)
b2 = Label(main, text="ok", font=("Pacifico",50),fg="#fe0233")
b2.place(x=370,y=100)

task = Label(main, text="your next task.", fg="#19ffa7")
task.place(x=370,y=110)



g_t()
main.mainloop()