m = [[85, 95, 78],[76, 88, 95],[90, 92, 89]]
for i in range(len(m)):
    total=sum(m[i])
    average=total/len(m[i])
    print(f"student {i+1}: total={total}, and average= {average}")
