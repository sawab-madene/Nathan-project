# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:12:11 2021

@author: hp
"""
#%% library
import tkinter as tk
from PIL import Image,ImageTk
import random
import time
#%%function  
"""id card is down=1 or up=0"""
def IsDown(L):
    down=0;
    for i in range(8):
        if L[i]==1:
            down=1;   #is not down anymore
            break;
        else: 
            pass;
    return down;       
"""every line in matrix is card list after one flip"""        
def calcul(L):
    index=[];
    M=[];
    while (IsDown(L)==1):
        while (True):  #choose only up card 
            random_index=random.choice(range(0,8));
            if (L[random_index]==1):
                index.append(random_index);
                break;
        if index[-1]==7:
            L[index[-1]]=0;
        else:
            L[index[-1]]=0;
            L[index[-1]+1]=0 if L[index[-1]+1]==1 else 1; 
        M.append(L[:]);
    return M,index;
"""display cards and arrows"""
def image_update(M,index,n,h,f0,f1,img_l,p,w):
    for i in range (n):
        for j in range (8):
            #display arrows
            if j==index[i]:
                if i==0:
                    arrow_id1=p.create_line(85+j*170,65,85+j*170,165,arrow=tk.LAST,width=5,fill='red'); 
                    arrow_id2=p.create_line(85+(j+1)*170,65,85+(j+1)*170,165,arrow=tk.LAST,width=5,fill='blue'); 
                else:
                    p.coords(arrow_id1,85+j*170,65,85+j*170,165);
                    p.coords(arrow_id2,85+(j+1)*170,65,85+(j+1)*170,165);
            # display cards
            if matrix[i][j]==0 :
                img_l=tk.Label(w,image=f0);
                img_l.place(x=j*170,y=h-600);
                
            else:
                img_l=tk.Label(w,image=f1);
                img_l.place(x=j*170,y=h-600);
            time.sleep(0.1);
            w.update()
""" freez for 5 second"""
def stop():
    time.sleep(5);
#%%                                       GUI
"""main window"""
window=tk.Tk();
window.title('Nathan');
window.state('zoomed');
w,h=window.winfo_screenwidth(),window.winfo_screenheight();
"""widgets"""
#canvas
paper=tk.Canvas(window,width=w,height=h);
paper.place(x=0,y=0);
#image
face0=Image.open('joker 0.png');                   #import image 
face0=face0.resize((160,250),Image.ANTIALIAS);     # resizing
face0=ImageTk.PhotoImage(face0)                    #create image widget;

face1=Image.open('joker 1.png');                   #import image 
face1=face1.resize((160,250),Image.ANTIALIAS);     #resizing
face1=ImageTk.PhotoImage(face1)                    #create image widget;

for i in range (8):
    img_label=tk.Label(window,image=face1);
    img_label.place(x=i*170,y=h-600);
#%%                                       calculation & result
"""call calcul function"""
start_List=[1,1,1,1,1,1,1,1]                       #list of 8 down cards 
matrix,card_index=calcul(start_List)
row_num=len(matrix);
#%%                                         GUI continuation
#Buttons
run_button=tk.Button(window,text="RUN",bg='white',bd=4,font=('Arial',15,'bold'),width=15,height=1,command=lambda:image_update(matrix,card_index,row_num,h,face0,face1,img_label,paper,window));
run_button.place(x=w/2-50,y=h-250); 
pause_button=tk.Button(window,text="PAUSE",bg='white',bd=4,font=('arial',15,'bold'),width=15,height=1,command=stop); 
pause_button.place(x=w/2-50,y=h-200);

window.mainloop();                   