# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
import widget_creation as w
#from functions import *
import dataB as DB
import actions_game as AG
import ctypes         #Para obtener tamaño de pantalla
 
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
anchoScreen, altoScreen = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) 


dates_db = DB.DataB("Preguntas.db")     #Conexion with database Preguntas and creation of object
ranking_db = DB.DataB("Ranking.db")     #Conexion with database Ranking and creation of object
qa = AG.Actions_game()                  #Actions for development of the game
window = Tk() #root window
window.title("Juego de preguntas") #title of window
window.geometry(str(anchoScreen//2)+"x"+str((altoScreen//4)*3))   #size of window 1/2 and 3/4 
main_frame = Frame(window)          #main frame
main_frame.pack(fill = BOTH, expand=1)                  #fill all the window
widgets = w.Widget_creation(main_frame)     #Object creation
widgets.screen("s0")            ##show initial screen
widgets.button_init.config(command = lambda:widgets.screen("s1"))       #show screen of level 1
widgets.button_play_again.config(command = lambda:qa.play_again(widgets, dates_db))    #Reset de game next to finish it
widgets.button_quit.config(command=window.destroy)              #close the window
question_answer = qa.load_question(dates_db, widgets)           #dates of the charged question
qa.load_level(widgets, question_answer)                         #charge question of the level
widgets.confirm_button.config(command = lambda:qa.check_answer(widgets,question_answer, dates_db, ranking_db))      #Confirm selected answer   
widgets.finish_button.config(command = lambda:qa.finish_game(widgets, ranking_db))          #finish the game
widgets.button_ranking1.config(command = lambda:qa.show_ranking(widgets,ranking_db,"s0"))
widgets.button_ranking2.config(command = lambda:qa.show_ranking(widgets,ranking_db,"s2"))

window.mainloop()           #loop for the interface tkinter




    
    