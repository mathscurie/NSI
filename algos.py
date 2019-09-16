liste =[12,25,5,45,90,10]

def maximumliste(l):
    max=l[0]
    for i in range(1,len(l)):
        if l[i]>max:
            max=l[i]
    return(max)

