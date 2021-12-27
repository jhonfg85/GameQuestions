# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 22:56:46 2021

@author: forte
"""
from tkinter import *
import tkinter as ttk

class Widget_creation():
    def __init__(self, frame_main):
        self.frame_main = frame_main
        self.level = 1
        self.score = 0
        self.ranking = 0
        self.id_question_label = StringVar()
        self.id_ans1_rb = StringVar()
        self.id_ans2_rb = StringVar()
        self.id_ans3_rb = StringVar()
        self.id_ans4_rb = StringVar()
        self.id_score_label = StringVar()
        self.id_entry_init = StringVar()
        #self.confirm_button = Button()
        self.width_button = 15
        self.fontTextBold = ('Arial', 12, 'bold')
        self.fontText = ("Arial", 12)
        self.id_level_label = StringVar()
        self.frame2 = Frame(self.frame_main)
        self.confirm_button = Button(self.frame2, text="Confirmar respuesta", width=self.width_button, font=self.fontTextBold)
        self.finish_button = Button(self.frame2, text="Finalizar juego",  width=self.width_button, font=self.fontTextBold)
        self.list_widgets_s2 = []
        self.button_play_again = Button(self.frame_main, text="Jugar de nuevo", width=self.width_button, font=self.fontTextBold)
        self.button_quit = Button(self.frame_main, text = "Salir", width=self.width_button, font=self.fontTextBold)
        self.answer = IntVar()      #Value of radiobutton choosen
        self.button_ranking1 = Button(self.frame_main, text="Ranking", width=self.width_button, font=self.fontTextBold)
        self.button_ranking2 = Button(self.frame_main, text="Ranking", width=self.width_button, font=self.fontTextBold)
        self.canvas1= Canvas(self.frame_main)
        self.frame3 = Frame(self.canvas1)
    
        self.button_init = Button(self.frame_main, text="Iniciar", width=self.width_button, font=self.fontTextBold )
        self.yscrollbar = ttk.Scrollbar(self.canvas1, orient=VERTICAL, command=self.canvas1.yview)

        



        
        
    def screen (self, s):           #creation of screens
        if(s=="s0"):
            self.label_init = Label(self.frame_main, text = "Username:", font=self.fontTextBold)
            self.label_init.pack(side=TOP, pady = 20)
            
            self.entry_init = Entry(self.frame_main, textvariable = self.id_entry_init, width=self.width_button, font=self.fontText )
            self.entry_init.pack(side= TOP, pady = 20)
            self.id_entry_init.set("User")
            self.button_init.pack(side=TOP, pady = 5)
            #self.button_hist = Button(self.frame_main, text="Ranking", width=self.width_button, font=self.fontTextBold)
            self.button_ranking1.pack(side=TOP, pady = 5)
            self.list_widgets_s0 = [self.label_init, self.label_init, self.entry_init, self.button_init, self.button_ranking1]
        
        elif(s=="s1"):
            self.level = 1
            self.forget_widgets(self.list_widgets_s0)       #hide widgets of screen 0
            self.forget_widgets(self.list_widgets_s2)       #hide widgets of screen 2
            self.frame1 = Frame(self.frame_main)
            self.frame1.pack(side= TOP, pady=20)
           
            self.level_label = Label(self.frame1, textvariable=self.id_level_label, font=self.fontTextBold)
            self.level_label.pack(side=LEFT, padx=20)
            
            self.score_label = Label(self.frame1, textvariable = self.id_score_label, font=self.fontTextBold)
            self.score_label.pack(side=RIGHT, padx = 20)
            
            #self.frame2 = Frame(self.frame_main)
            self.frame2.pack(side= TOP)
            #self.id_question_label = StringVar()
            question_label = Label(self.frame2, textvariable = self.id_question_label, font=self.fontTextBold, wraplength=400)
            question_label.pack(side = TOP, padx=20)
            #self.id_question_label.set("¿pregunta 1?")
            #self.id_ans1_rb = StringVar()
            
            #value represents de position of every answer in database for comparison
            ans1_rb = Radiobutton(self.frame2, textvariable=self.id_ans1_rb, variable=self.answer, value=4, font=self.fontText)
            ans1_rb.pack(side=TOP, pady=10)
            ans2_rb = Radiobutton(self.frame2, textvariable=self.id_ans2_rb, variable=self.answer, value=5, font=self.fontText)
            ans2_rb.pack(side=TOP, pady=10)
            ans3_rb = Radiobutton(self.frame2, textvariable=self.id_ans3_rb, variable=self.answer, value=6, font=self.fontText)
            ans3_rb.pack(side=TOP, pady=10)
            ans4_rb = Radiobutton(self.frame2, textvariable=self.id_ans4_rb, variable=self.answer, value=7, font=self.fontText)
            ans4_rb.pack(side=TOP, pady=10)
            
            #self.confirm_button = Button(self.frame2, text="Confirmar respuesta")
            self.confirm_button.pack(side=TOP, pady=5)
            
            self.finish_button.pack(side=TOP, pady=5)            
            self.list_widgets_s1 =[self.frame1, self.frame2]

        elif(s == "s2"):
            self.forget_widgets(self.list_widgets_s1)
            end_label = Label(self.frame_main, text="Fin del juego", font=self.fontTextBold)
            end_label.pack(side= TOP, padx=20, pady=20)
            score_label = Label(self.frame_main, text="Puntaje: "+str(self.score), font=self.fontTextBold)
            score_label.pack(side=TOP, padx=20, pady=20)
            #ranking_label = Label(self.frame_main, text="Puesto "+str(self.ranking)+" del ranking", font=self.fontText)
            #ranking_label.pack(side=TOP, pady=15)
            #self.button_play_again = Button(self.frame_main, text="Jugar de nuevo")
            self.button_play_again.pack(side=TOP, pady=5)
            self.button_ranking2.pack(side=TOP, pady=5)
            self.button_quit.pack(side=TOP, pady=5)
            self.list_widgets_s2=[score_label, self.button_play_again, self.button_ranking2, self.button_quit, end_label] 
            
            
            
    def forget_widgets(self, list_to_forget):
        
        for i in list_to_forget:
            try:
                i.pack_forget()
            except:
                i.grid_forget()