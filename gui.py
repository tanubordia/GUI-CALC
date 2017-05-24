from Tkinter import *

class Gui:
   Mybuttons=[]				#Mybuttons is a static_variable containing the addresses of various widgets on the screen
   btn_list=[]				#btn_list is a static variable containing the text to be displayed on each button 
   text=None
   memory_text=None
   label=None
   def __init__(self,root):
      self.f=root
      self.createWidgets()
       



   def createWidgets(self):		#createWidgets function create and places the buttons on the window
            Gui.btn_list=[
              '7', '8', '9', '*', 'C','sin','asin',
              '4', '5', '6', '/', 'del','cos','acos',
               '1' ,'2', '3', '-', 'sqrt','tan','atan',
                '0', '.', '=', '+', 'pi','log','fact',
                 '(',')','log10','e','floor','ceil','exp','Recall','EXIT']
            r=3
            c=0
            i=0
            for b in Gui.btn_list:                       # this loop creates and places the buttons on the window
                Gui.Mybuttons.append(Button(self.f,text=b,width=3,height=1,bd=3,padx=10,pady=10,activebackground="#8BC34A",relief=RAISED,font=(None,10,"bold")))
                if i not in [35,36]:
                   Gui.Mybuttons[i].grid(row=r,column=c,sticky=W)
                elif i==35:
                   Gui.Mybuttons[i].grid(row=8,column=0,columnspan=3,sticky=W+E)
                elif i==36:
                   Gui.Mybuttons[i].grid(row=8,column=3,columnspan=4,sticky=W+E)
               
                i+=1
                c+=1
                if c==7:
                    c=0
                    r+=1
             
                    
            
            Gui.text=Text(self.f,width=30,height=2,bd=10,font=25,bg="#eeeeee")
            Gui.text.grid(row=0,column=0,columnspan=7,sticky=E+W)
            Gui.label=Label(self.f,text="Memory:",width=7,font=(None ,10,"bold"))
            Gui.label.grid(row=2,column=0,padx=2,pady=2,columnspan=2,sticky=W)
            Gui.memory_text=Text(self.f,width=27,height=1,bd=6,bg="#424242",fg="#ffffff",font=20)
            Gui.memory_text.grid(row=2,column=1,padx=7,pady=7,columnspan=6,sticky=E)
            self.Configure()
   def Configure(self):					# configure function assigns values to some additional attributes which are different for every button
                     for i in range(37):
                        if i in [0,1,2,7,8,9,14,15,16,21]:
                            Gui.Mybuttons[i].configure(bg="#212121",fg="#ffffff")
                        elif i == 4:
                            Gui.Mybuttons[i].configure(bg="#3949AB",fg="#212121")
                        elif i== 11:
                            Gui.Mybuttons[i].configure(bg="#FF5722",fg="#212121")
                        elif i==35:
                            Gui.Mybuttons[i].configure(bg="#0097a7",fg="#212121")
                        elif i==36:
                            Gui.Mybuttons[i].configure(bg="#d50000",fg="#212121")
                        else:
                            Gui.Mybuttons[i].configure(bg="#bdbdbd",fg="#212121")


'''function returnList() returns 3 values when the function is called from module mod1
1) List containing the addresses of all the buttons
2) List containing the text to be displayed on each button
3) address of text box widget'''
def returnList():				 
      return Gui.Mybuttons, Gui.btn_list ,Gui.text ,Gui.memory_text ,Gui.label                     
