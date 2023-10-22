def rec(i, x):
    if(i >= 7 or x[-1] < 1 or x[-1] > 5):
        return
    
    rec(i+1, [*x, x[-1]+1])
    rec(i+1, [*x, x[-1]-1])

    if(i == 6):
        print(f"{x},")

for i in range(5):
    rec(0, [i+1])