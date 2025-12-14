def convert(m):
    new = []
    for i in m:
        for j in i:
            new.append(j)
              
    
    return new

test = [[2,3],[4,2,1]]
test2 = [[5,0,3,7,5],[9,0,9,1,2]]
print(convert(test))
print(convert(test2))