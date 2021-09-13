with open('nums.txt', 'r') as file:
    data = [line.strip() for line in file]
input_nums = [int(e) if e.isdigit() else e for e in data[0].split(',')]
entity= int(data[1])
file.close()



def lru(list_num,n):#s -> list_num
    f,st,fault,pf = [],[],0,'No'#capcity -> n
    # print("\nString|Frame →\t",end='')
    for i in range(n):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in list_num:
        if i not in f:
            if len(f) < n:
                f.append(i)
                st.append(len(f)-1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'No'
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(n-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    # print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(list_num),fault,(fault/len(list_num))*100))
    print(f"Total Request {len(list_num)} \n",end=' ')
    print(f"Total of page faul are {(fault)}",end =' ')



def fifo(list_num,n):
    f,fault,top,pf = [],0,0,'No'
# print("Enter the reference string: ",end="")
# s = list(map(int,input().strip().split()))
# print("\nString|Frame →\t",end='')
    for i in range(n):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in list_num:
        if i not in f:
            if len(f) < n:
                f.append(i)
            else:
                f[top] = i
                top = (top+1)%n
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(n-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    # print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(list_num),fault,(fault/len(list_num))*100))
    print(f"Total Request {len(list_num)} \n",end=' ')
    print(f"Total of page faul are {(fault)}",end =' ')





def clock(list_num,n):
    f,b,fault,p,pf=[],[],0,0,'No'
    for i in range(n):
        print(i,end=' ')
    print("Fault\n   ↓\n")
    for i in list_num:
        if i not in f:
            if len(f) < n:
                f.append(i)
                b.append(1)
                p+=1
                if p == (n):
                    p = 0

            else:
                while True:
                    if b[p] == 0:
                        f.pop(p)
                        f.insert(p,i)
                        p+=1
                        if p == (n-1):
                            p = 0
                        break
                    else:
                        b[p] = 0
                        p+=1
                        if p == (n):
                            p = 0


                 
            fault+=1
            pf='Yes'        #             continue
        else:
            pf ='No'
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(n-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
    print(f"Total Request {len(list_num)} \n",end=' ')
    print(f"Total of page faul are {(fault)}",end =' ')









# lru(input_nums,entity)
# fifo(input_nums,entity)
clock(input_nums,entity)

                
                
        

            