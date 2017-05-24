#importing of various user-defined and in-built modules
from functools import partial
from  Tkinter import  *
from math import *
import tkMessageBox
from gui import *
#------------------------------------------------------
'''Class Calc links the buttons to its corresponding functions.'''
class Calc:				
     data=''
     flag=0
     countkey=0
     memory=[]     
     i=0
     error=None
     def __init__(self,root,List,List2,text,text1,label):           #the constructor of class Calc will initialize its data members with the addresses of various 									 #widgets on the screen             
           self.Mybuttons=List
           self.Btn_list=List2
           self.text=text
           self.memory_text=text1
           self.label=label
           self.LinkButtons()
           self.root=root

     def LinkButtons(self):					#function LinkButtons() links the buttons to the corresponding functions
                                                                #keyword partial is used to call function calculate() with different arguments
           for i in range(len(self.Mybuttons)):
                cmd=partial(self.calculate , self.Btn_list[i])     
                self.Mybuttons[i].configure(command=cmd)



     def PrintResult(self,val):				       #function PrintResult() calculates the value of expression using in-built function eval()
							       #and prints the result.	
            result=eval(val)
            result='%g'%(result) 
                         
            self.text.delete(0.0,END)
            self.text.insert(0.0,result)
            
            return result
     

     def calculate(self,key):                                   #function calculate() checks which button is pressed and then appends the text on each button to 
            if key!='Recall':                                      #a static variable(data) of the class Calc.
                  self.memory_text.delete(0.0,END)			#it also checks for any errors during  the computational process.	
                   
            
            if key== 'EXIT':
                  self.root.quit()
            if key=='=':
               Calc.countkey=0
               Calc.flag+=1
               val=self.text.get(0.0,END)
               Calc.memory.insert(0,val)
               Calc.error=0                 
                      
                     
               
                   
               try:
                   result=self.PrintResult(val)
                   Calc.data=str(result)
               except ZeroDivisionError:
                   Calc.error=1
                   tkMessageBox.showwarning("WARNING!","Invalid !! Division By Zero!!")
               except ValueError:
                   Calc.error=1
                   tkMessageBox.showwarning("WARNING!","Invalid Input!!")     
               except NameError:
                   Calc.error=1
                   tkMessageBox.showwarning("WARNING!","Invalid Syntax!!")    
               except SyntaxError:
                   Calc.error=1
                   tkMessageBox.showwarning("WARNING!","Invalid Syntax!!")        
               except Exception:
                   Calc.error=1
                   tkMessageBox.showwarning("WARNING!","Invalid Syntax!!")            
       
            elif key=='C':					#clears the text in the textbox widget
                      self.text.delete(0.0,END)
                      Calc.data=''


            elif key=='del':                                    #deletes the rightmost character on the screen ; works just like backspace key
                      Calc.data=Calc.data[:len(Calc.data)-1]
                      self.text.delete(0.0,END)
                      self.text.insert(0.0,Calc.data)

            elif key=='Recall':			                #displays the previously occurred  operations in the memory text-box		
                    
                      self.memory_text.delete(0.0,END)
                      if Calc.i<len(Calc.memory):
        
                         self.memory_text.insert(0.0,Calc.memory[Calc.i])
                         Calc.i+=1
                      else: 
                         Calc.i=0
                         tkMessageBox.showwarning("!!Warning!!","MEMORY UNDERFLOW!!!")
                         self.memory_text.delete(0.0,END) 
                          
            else:     
                      if key=='fact':
                          key='factorial'
                      if key in ['sin','cos','tan','asin','acos','atan','log','log10','exp','factorial','floor','ceil','sqrt']:
                         key=key+'('        
                                                   
                               
                      Calc.countkey+=1
                      if Calc.flag!=0:
                           if Calc.countkey==1 and key not in ['+','-','*','/'] and Calc.error==0:
                                  self.text.delete(0.0,END)
                                  Calc.data=''
                                  Calc.data+=key 

                                  self.text.insert(0.0,Calc.data)
                           else:
                                   self.text.delete(0.0,END)
                                   Calc.data+=key
                                   self.text.insert(0.0,Calc.data)
                      
                      else:
                           self.text.delete(0.0,END)
                           Calc.data+=key
                           self.text.insert(0.0,Calc.data)         

root=Tk()
GUI = Gui(root)                                   		                                        #An object GUI of Class Gui of module mod2 is created
Mybuttons, Btn_list, textBox_widget,textBox_widget1,label=returnList()  		                #returnList function of module mod2 is called
CALC = Calc(root,Mybuttons, Btn_list, textBox_widget,textBox_widget1,label)              		#An object CALC of Class Calc is created
root.title("Python Calculator")
icon=PhotoImage(file="calc.gif")
root.call('wm','iconphoto',root._w,icon)								#used for creating the icon for the application
root.mainloop()                                 
