def remove_char(st, i):
    for j in range(len(st)):
        if j==i:
            st=st.replace(st[i],"",1)
    return st
st = input("Enter the String: ")
i = int(input("Enter the ith value to be removed: "))
print(remove_char(st,i-1))