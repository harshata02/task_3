class firstclass:
    val1=0
    val2=0
    val3=0
    val4=0
    val5=0


    def __init__(self,a,b,c,d,e):
        print('this is constructor')
        self.val1 = a
        self.val2 = b
        self.val3 = c
        self.val4 = d
        self.val5 = e

    def addvalue(self):

        print(f'addition ={self.val1 +self.val2 +self.val3 +self.val4 +self.val5}')

    def subvalue(self):
        print(f'subtraction={self.val1 -self.val2 -self.val3 -self.val4 -self.val5}')

    def productvalue(self):
        print(f'multiplication={self.val1  * self.val2 * self.val3 * self.val4 * self.val5}') 

    def divvalue(self):
        print(f' div={self.val1 /self.val2 /self.val3 /self.val4 /self.val5}')

    def maxvalue(self):
        print(f' max={max(self.val1 ,self.val2 ,self.val3 ,self.val4 ,self.val5)}') 

    def minvalue(self):
        print(f'min={min(self.val1 ,self.val2 ,self.val3 ,self.val4 ,self.val5)}') 

    def meanvalue(self):
        print(f'avg={(self.val1 +self.val2 +self.val3 +self.val4 +self.val5)/5}') 

    def seventyfivevalue(self):
        print(f'value={(3*(self.val1 +self.val2 +self.val3 +self.val4 +self.val5)/4)}') 

    def fiftypercent(self):
        print(f'value={(1*(self.val1 +self.val2 +self.val3 +self.val4 +self.val5 )/2)}') 

    def twentyfive_percent(self):
        print(f'value={(1*(self.val1 +self.val2 +self.val3 +self.val4 +self.val5 )/4)}')       


   





f1= firstclass(10,20,30,40,50)  
f1.addvalue()
f1.subvalue()
f1.productvalue()  
f1.divvalue() 
f1.maxvalue()
f1.minvalue() 
f1.meanvalue()
f1.seventyfivevalue()
f1.fiftypercent()
f1.twentyfive_percent()

print('f1.val1=',f1.val1) 
print('f1.val2=',f1.val2)
print('f1.val3=',f1.val3)
print('f1.val4=',f1.val4)
print('f1.val5=',f1.val5)



           
    
         






        
        