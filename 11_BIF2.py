x = [2,4,6,8,10,12,14,16,16,16]
y = x.copy()
print (list[x])
print (list[y])
print (x.count(16)) # اتكرر كام مرة
x.append(7) # بتضيف في النهاية 
x.insert(1,5) # بتتحدد المكان الي هتضيف فيه 
print(x)
x.remove(2) # بيجذف اول قيمة للرقم ده من البداية 
print(x)
x.pop(3) #بيحدف الي في الاندكس
print(x)
x.extend(y) # هنضيف ال y ع ال x
