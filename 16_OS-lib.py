import os
"""
print(os.getcwd())    # عشان تطبع الامتداد بتاع الملف الي انا فيه
os.mkdir("C:/vs code/python/LOL")  # عشان اعمل فولدر جديد 

os.makedirs("C:/vs code/python/LOL/course/pop/push")

path = "C:/vs code"
dir_list = os.listdir(path)         # دول عشان اعرف اي الي جوده الباث ده 
print (dir_list)

# os.remove("")       # دي بتمسح حاجة معينة زي الملفات بندخل الباث بتاعها بس 
os.removedirs("LOL\course\pop\push")   # دي بتمسح الفولدرات

print(os.path.exists('C:/vs code/python/heart1/text.txt'))      # هما بنشوف الملف موجود في الباث ده ولا اي
#os.remove("C:/vs code/python/heart1/text.txt")                 # هنا بنمسح عادي

os.rename("C:/vs code/python/test1/text1.txt" , "C:/vs code/python/test1/text2.txt") # دي بتعدل ع الاسم القديم بتخلية يبقي الجديد

with open("C:/vs code/python/test1/text2.txt" , 'w') as f:
    f.write("hello world !!!!")                         # دي عشان نكتب حاجة في الفايل 
    
with open("C:/vs code/python/test1/text2.txt" , 'r') as f:
    print(f.read())                                     # دي عشان نقرا الفايل
"""