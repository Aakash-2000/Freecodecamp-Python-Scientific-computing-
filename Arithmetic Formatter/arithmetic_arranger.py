def arithmetic_arranger(problems,opt=False):
    row_1=[]
    row_2=[]
    row_3=[]
    row_4=[]
    count=0
    arranged_problems = "" 
    if len(problems)>5:
        return "Error: Too many problems."
    else:
        for i in problems:
            i=i.split(" ")
           
            if i[1]=="*":
                return "Error: Operator must be '+' or '-'."
            if i[1]=="/":
                return "Error: Operator must be '+' or '-'."
            if i[2].isdigit() == False:
                return "Error: Numbers must only contain digits."
                
            if i[0].isdigit() == False:
                return "Error: Numbers must only contain digits."
            if len(i[0])>4:
                return "Error: Numbers cannot be more than four digits."
            if len(i[2])>4:
                return "Error: Numbers cannot be more than four digits."
                
            
                
        
    
    for i in problems:
        i=i.split(" ")
        if i[1]=="+":
            c=str(int(i[0])+int(i[2]))
        if i[1]=="-":
            c=str(int(i[0])-int(i[2]))
        
        a = len(i[0])
        b = len(i[2])
        longest_op = max(a,b)
        
        if(a>b):
            i[2]=i[2].rjust(longest_op," ")
            i[0]=i[0].rjust(a+2," ")
            
            
            
        if(b>a):
            
            
            i[0]=i[0].rjust(longest_op+2," ")
        if (a==b):
            i[0]=i[0].rjust(a+2," ")
            
        i[1]=" ".join(i[1:])
        row_3.append("-"*len(i[1]))
        c=c.rjust(len(i[1])," ")
        row_4.append(c)
        row_2.append(i[1])
        row_1.append(i[0])
    if opt == True:
        l1 = "    ".join(row_1)
        l2 = "    ".join(row_2)
        l3 = "    ".join(row_3)
        l4 = "    ".join(row_4)
        return l1+"\n"+l2+"\n"+l3+"\n"+l4
        
    else:
        l1 = "    ".join(row_1)
        l2 = "    ".join(row_2)
        l3 = "    ".join(row_3)
        return l1+"\n"+l2+"\n"+l3
    
        
        
         
            
            
 
    
       
        
