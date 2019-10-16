with open(r'C:\Users\hyr\Desktop\第二天\data.txt','r+') as a:
    s = a.readlines()
    print(s)
    s1 = []
    for i in s:
        s1.append(i.strip('\n'))
    print(s1)
    s1.sort()
    #s1.reverse()
with open(r'C:\Users\hyr\Desktop\第二天\aaa.txt','w+') as b:
    for i in s1:
        b.write(i+'\n')
        #print()