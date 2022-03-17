start_num=int(input("enter teh starting number:"))
end_num=int(input("enter the ending number:"))
for num in range(start_num,end_num+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
