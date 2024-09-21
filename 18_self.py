class human:
    len = 188

    def info(self ,name1 ,age1,city1,len1 ):      
        self.name = name1  
        self.age = age1
        self.city = city1  
        self.len = len1  
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.len)
        
h1 = h2 = h3 = human()
h1.info("ahmed",20 ,"cairo" , 177)
h2.info("yasser",55 ,"cairo" , 150)
h3.info("sayed",70 ,"cairo" , 166)

"""
h2.name =input("Enter your name : ")
h2.age = int(input("Enter yor age : "))
h2.city =input("Enter your city : ")
print(h2.name)
print(h2.age)
print(h2.city)
h3.name =input("Enter your name : ")
h3.age = int(input("Enter yor age : "))
h3.city =input("Enter your city : ")
print(h3.name)
print(h3.age)
print(h3.city)
"""
