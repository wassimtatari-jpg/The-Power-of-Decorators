class myclass:
    def __init__(self,value):
        self.hiddenvalue=value
    @property
    def value(self):
        return self.hiddenvalue
    @value.setter
    def value(self,new_value):
        self.hiddenvalue=new_value
oj=myclass(10)
print(oj.value)
oj.value=15
print(oj.value)


        
  
   