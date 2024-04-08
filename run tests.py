import csv
menu_loop=1

def start_test():
    file=input("Enter test name (eg: 'test'): ")
    file=file+".csv"
    with open(file, "w",newline="") as f:
        w=csv.writer(f)
        w.writerow(["Q","A"])
        for i in range(int(input("Enter no of qs: "))):
            print("\n",i+1,end="")
            ans=input(":")
            w.writerow([i+1,ans.upper()])
    edit_loop=1
    while edit_loop==1:
        op=input("Do you want to make any changes? (Y/N): ")
        if op=='y' or op=='Y':
            edit(file)
        elif op=='n' or op=='N':
            edit_loop=0
        else:
            print("Wrong input!")

def edit(file):
    ans=[]
    with open(file,"r") as f:
        r=csv.reader(f)
        next(r)
        for i in r:
            ans.append(i)           
    if ans==[]:
        print("No results found.")
        return
    
    print("\nYour answers:\n Q | A")
    for i in range(len(ans)):
        if i<9:
            print((ans[i])[0]," |",(ans[i])[1])
        elif i<99:
            print((ans[i])[0],"|",(ans[i])[1])
            
    with open(file,"w",newline="") as f:
        w=csv.writer(f)
        q=int(input("Enter question number: "))
        for i in range(len(ans)):
            if (ans[i])[0]==str(q):
                print("\n",i+1,end="")
                a=input(":")
                ans[i]=[q,a.upper()]
        w.writerow(["Q","A"])
        w.writerows(ans)
    print()
    for i in range(len(ans)):
        if i<9:
            print((ans[i])[0]," |",(ans[i])[1])
        elif i<99:
            print((ans[i])[0],"|",(ans[i])[1])
        else:
            print((ans[i])[0],"|",(ans[i])[1])
            
    
def review():
    file=input("Enter test name (eg: 'test'): ")
    file=file+".csv"
    ans=[]
    ak=[]
    with open(file, "r") as an:
        r=csv.reader(an)
        next(r)
        for i in r:
            ans.append(i)
    answer=input("Enter answer key file name (eg: 'engak'): ")
    answer=answer+".csv"
    with open(answer, "r") as a:
        r=csv.reader(a)
        next(r)
        for i in r:
            ak.append(i)
    m=0
    print("Wrong answers:\n Q | X | ✓")
    for i in range(len(ans)):
        if (ak[i])[0]==(ans[i])[0]:
            if (ak[i])[1]==(ans[i])[1]:
                m=m+1
            else:
                if i<9:
                    if (ans[i])[1]=="":
                        print((ak[i])[0]," |",(ans[i])[1]," |",(ak[i])[1])
                    else:
                        print((ak[i])[0]," |",(ans[i])[1],"|",(ak[i])[1])
                        
                elif i<99:
                    if (ans[i])[1]=="":
                        print((ak[i])[0],"|",(ans[i])[1]," |",(ak[i])[1])
                    else:
                        print((ak[i])[0],"|",(ans[i])[1],"|",(ak[i])[1])
                else:
                    print((ak[i])[0],"|",(ans[i])[1],"|",(ak[i])[1])                    
    print("\nTotal Marks: ",m,"\n")

def menu():
    print("Enter menu option:\n1. Start new test\n2. Review test\n3. Exit")
    op=int(input("Enter option: "))
    print("")
    if op==1:
        start_test()
    elif op==2:
        review()
    elif op==3:
        global menu_loop
        menu_loop=0
    else:
        print("Wrong input!\n")

while (menu_loop==1):
    menu()
