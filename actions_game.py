# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:49:07 2021

@author: forte
"""
from tkinter import *
import random
from tkinter import messagebox

class Actions_game:
    
    def __Init__(self):
        self.question = ()
        
    ## take to the question and answer to the screen   
    def load_level(self, widgets, question):
        widgets.question = question
        #update level and score in screen
        widgets.id_level_label.set("Nivel "+str(widgets.level))
        widgets.id_score_label.set(str(widgets.score)+" Puntos")
        #load question and answers
        widgets.id_question_label.set(question[2])      #question
        widgets.id_ans1_rb.set(question[4])
        widgets.id_ans2_rb.set(question[5])
        widgets.id_ans3_rb.set(question[6])
        widgets.id_ans4_rb.set(question[7])
        
        # widgets.id_question_label.set("¿pregunta "+str(widgets.level)+"?")
        # widgets.id_ans1_rb.set("respuesta 1")
        # widgets.id_ans2_rb.set("respuesta 2")
        # widgets.id_ans3_rb.set("respuesta 3")
        # widgets.id_ans4_rb.set("respuesta 4")
        
        
    #compare if the answer of user is correcto or not 
    def check_answer(self, widgets, question, dates_db, ranking_db):

        question = self.question
        if widgets.answer.get() > 3 and widgets.answer.get() < 8:   #when is diferent to the interval, radiobutton is unselected
            if question[3] == question[widgets.answer.get()]:   #if correct_answer == answer:  
                self.next_level(widgets, dates_db, ranking_db)
            else:
                widgets.score = 0
                messagebox.showinfo("Respuesta incorrecta", "La respuesta es incorrecta.")
                widgets.screen("s2")    #show final screen
        else:
            messagebox.showwarning("Advertencia","Por favor, seleccione una respuesta")
        
      
    ## Pass to next level while the level be less or equal to 5 level. If win 5 level, finishe the game
    def next_level(self, widgets, dates, ranking_db):
        widgets.answer.set(1)
        if widgets.level+1 <= 5:
            widgets.score += 10*widgets.level
            widgets.level += 1
            question = self.load_question(dates, widgets)
            self.load_level(widgets, question)
        
        else:
            widgets.score += 100    #Score final level
            self.finish_game(widgets, ranking_db)
        
    #play again the game
    def play_again(self, widgets, dates_db):
        widgets.score = 0
        widgets.level = 1
        widgets.forget_widgets(widgets.list_widgets_s2)
        #widgets.screen("s1")    #show level 1 of the game
        widgets.frame1.pack(side=TOP)
        widgets.frame2.pack(side=TOP)
        question = self.load_question(dates_db, widgets)
        self.load_level(widgets, question)      #load a question of the level


    #load an aleatory question of the database
    def load_question(self, dates_db,widgets):
        random_number = random.randint(1,5)+5*(widgets.level-1)
        question = dates_db.execution("SELECT * FROM questions WHERE ID="+str(random_number))
        self.question = question[0]
        return question[0]
    
    
    def finish_game(self, widgets, ranking_db):         #button "Finalizar juego" in any moment
        #ranking_db.openConection("Ranking.db")
        values_ranking = "'"+widgets.id_entry_init.get()+"',"+str(widgets.score)
        ranking_db.execution( "INSERT INTO ranking ('USERNAME','SCORE') VALUES ("+values_ranking+")" )       #save score in ranking
        #ranking_db.closeConnection()
        widgets.screen("s2")    #show final screen
        

        
        
   ####show ranking in a new frame whith scroll at the right     
    def show_ranking(self,widgets,ranking_db, s):
        dates = ranking_db.execution("SELECT * FROM ranking")
        len_dates = len(dates)
        widgets.forget_widgets(widgets.list_widgets_s0)
        widgets.forget_widgets(widgets.list_widgets_s2)        
        
        ####configure scrollbar
        #widgets.canvas1.configure(scrollregion = widgets.canvas1.bbox("all"))       #update range of scroll
        widgets.canvas1.pack(fill= BOTH, side=TOP, expand=1)
        widgets.yscrollbar.pack(side=RIGHT, fill=Y)     #Y: Llenar hasta el eje Y
        widgets.canvas1.configure(yscrollcommand= widgets.yscrollbar.set)
        widgets.canvas1.bind('<Configure>', lambda e:widgets.canvas1.configure(scrollregion = widgets.canvas1.bbox("all")))
        widgets.canvas1.create_window((0,0),window=widgets.frame3, anchor="nw")
        
        rowi = 0
        Label(widgets.frame3, text = "Usuario", font=widgets.fontTextBold).grid(row=rowi, column=0, padx=3)
        Label(widgets.frame3, text = "Puntuación", font=widgets.fontTextBold).grid(row=rowi, column=1, padx=3)
        rowi+=1
        self.list_ranking = []
        for i in range(len_dates):
            labelx = Label(widgets.frame3, text = dates[i][1], font=widgets.fontText)
            labelx.grid(row=rowi, column=0, padx=3)
            self.list_ranking.append(labelx)
            labely = Label(widgets.frame3, text = dates[i][2], font=widgets.fontText)
            labely.grid(row=rowi, column=1, padx=3)
            self.list_ranking.append(labely)
            rowi+=1
            
        self.back_button = Button(widgets.frame3, text="Volver", width=widgets.width_button, font=widgets.fontTextBold, command=lambda:self.back_ranking(s, widgets))
        self.back_button.grid(row=rowi, column=0, columnspan = 2, pady=20)
        
   
        
   
    ####Return to previous screen to continue with the development of the game
    def back_ranking(self, s, widgets):      #back to previous screen
        widgets.canvas1.configure(scrollregion = widgets.canvas1.bbox("all"))       #update range of scroll
        
        #hide the widgets of screen
        self.back_button.grid_remove()
        widgets.forget_widgets(self.list_ranking)
        widgets.frame3.pack_forget()
        widgets.canvas1.pack_forget()
        
        widgets.screen(s)    #show previous screen