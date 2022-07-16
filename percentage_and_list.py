'''=================to find the average using dict by user input====================='''
 
if __name__ == '__main__':
    n = int(input('enter number of persons :'))
    student_marks = {}
    for _ in range(n):
        name,*line= input('enter name and marks using split :').split()
        scores = list(map(float, line))
        student_marks[name] = scores
        print(student_marks)
    query_name = input('person name whose avg you wants to know :')
    output = list(student_marks[query_name])    
per = sum(output)/len(output)
print("%.2f" % per)   

# input:
  
# enter number of persons :3
# enter name and marks using split :goutham 56 23 45 62
# {'goutham': [56.0, 23.0, 45.0, 62.0]}
# enter name and marks using split :sathwik 65 82 65 22
# {'goutham': [56.0, 23.0, 45.0, 62.0], 'sathwik': [65.0, 82.0, 65.0, 22.0]}
# enter name and marks using split :ravi 85 23 58 23 
# {'goutham': [56.0, 23.0, 45.0, 62.0], 'sathwik': [65.0, 82.0, 65.0, 22.0], 'ravi': [85.0, 23.0, 58.0, 23.0]}
# person name whose avg you wants to know :sathwik
  
# output:
# 58.50



'''=============perform the different list methods by user input======================'''

f __name__ == '__main__':
    N = int(input('enter number of list methods to perform :')) # 5
    L=[];
    for i in range(0,N):
        cmd=input('enter method name, value(s) :').split()   #insert 0 5,append 40,insert 2 20,sort,print
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "print":
            print(L)#[5, 20, 40]
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        else:
            L.reverse()
            
# input:
# enter number of list methods to perform :5
# enter method name, value(s):insert 0 5
# enter method name, value(s):append 40
# enter method name, value(s):insert 2 20
# enter method name, value(s):sort
# enter method name, value(s):print
  
# output:
# [5, 20, 40]
    
