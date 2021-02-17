totalStudent=int(input("How many will you enters student?:  "))

nameList=[]
gradesList=[]

infoDic={}
gradesDic={}


for i in range(totalStudent):
    name=input("Enter name: ")
    surname=input("Enter surname: ")
    midterm=float(input("Enter midterm note: "))
    final=float(input("Enter final note: "))
    homework=float(input("Enter homework note: "))
    
    nameList.append(name)
    nameList.append(surname)

    gradesList.append(midterm)
    gradesList.append(final)
    gradesList.append(homework)
    
    
    infoDic[name+" "+surname]=midterm,final,homework
    
    meanNotes=(midterm+final+homework)/3
    
    gradesDic[name+" "+surname]=meanNotes

max=0
nameG=" "
    
for key,value in gradesDic.items():
    if max<gradesDic[key]:
        max=gradesDic[key]
        
for key,value in gradesDic.items():
    if max==value:
        nameG=key

   
print(nameG+" Congratulations! You have the highest score: "+str(max))   
    

    
    


