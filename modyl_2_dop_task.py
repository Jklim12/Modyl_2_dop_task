password = ''
for n in range (3,21):
    password = ''
    for i in range (1,n):
        for j in range (i+1,n):
            if n%(i+j)==0:
                password = password + str(i)+str(j)
    print(n,'=',password)