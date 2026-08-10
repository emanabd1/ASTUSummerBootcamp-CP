for i in range(int(input())):
    n,k=map(int,input().split())
    level=list(map(int,input().split()))
    course=list(map(int,input().split()))
    my_dict={i:[] for i in range(1,k+2)}
    for index,val in enumerate(course,start=1):
        my_dict[val].append(index)
    ans=[]
    for i in range(k,0,-1):
        for c in my_dict[i]:
            level=i  
            while level <k+1:
                    ans.append(c)
                    level+=1
    print(len(ans))
    print(*ans)