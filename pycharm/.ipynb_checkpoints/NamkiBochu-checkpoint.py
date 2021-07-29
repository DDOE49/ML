############### 전역변수 ###############
i = 0
summary = 0

############### 재귀 ###############
def sigma_even(n):
    global i
    if i>=n:
        i=0
        return 0
    i+=1
    return (i*2)+sigma_even(n)

############### 꼬리재귀 ###############
def sigma_even_loop(n):
    return sigma_even_loop2(n, 0)

def sigma_even_loop2(n, res):
    global i
    global summary
    if i>=n:
        i=0
        summary=0
        return res
    i+=1
    return sigma_even_loop2(n, res+(i*2))

############### While ###############
def sigma_even_while(n):
    global i
    global summary
    while i < n:
        i+=1
        summary += i*2
        if(i>=n):
            i=0
            break
    return summary

############### test code ###############
print("even(0)",sigma_even(0),"loop(0)",sigma_even_loop(0),"while(0)",sigma_even_while(0))
print("even(1)",sigma_even(1),"loop(1)",sigma_even_loop(1),"while(1)",sigma_even_while(1))
print("even(7)",sigma_even(7),"loop(7)",sigma_even_loop(7),"while(7)",sigma_even_while(7))