from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from math import sqrt

class Display(Label):
    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        self.operand = ''
        self.func = '' 

    def num(self, s):
        if int(s) == s:
            return str(int(s))
        else:
            return str(s)

    def key(self, key):
        if self.func != '' and self.operand == '':
            self.operand = self.text
            self.text = ''      
        self.text = (self.text + key).lstrip('0')

    def function(self, func):      
        if func == '=' and self.operand != "" and self.text != "":
            if self.func == '+':
                self.text = self.num(float(self.operand) + float(self.text))
            if self.func == '-':
                self.text = self.num(float(self.operand) - float(self.text))
            if self.func == '/':
                self.text = self.num(float(self.operand) / float(self.text))
            if self.func == '*':
                self.text = self.num(float(self.operand) * float(self.text))
            if self.func == '%':
                 self.text = self.num(float(self.operand) * (100/float(self.text)))
            self.operand = ''
            self.func = ''
        elif func == '+-':
            if self.text != "":
                self.text = self.num(-1*float(self.text))
        elif func == 'sqrt':
            if self.text != "":
                self.text = self.num(sqrt(float(self.text))) 
        else:
            self.func = func

    def back(self):
        self.text = self.text[:-1]

    def clear(self):
        self.text = '0'
    
class MyCalc(Widget):
    pass
   
class CalcApp(App):
    def build(self):
        pass
 
if __name__=="__main__":
    CalcApp().run()
