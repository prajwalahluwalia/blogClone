from cmath import pi


def check(arr):
    count = 0
    hm={}
    s=''
    for i in range(len(arr)):
        print(count, hm, arr[i])
        if count == 5 and i<len(arr)-1:
            val = list(hm.keys())[0]
            hm.pop(val)
            count-=2
        hm[arr[i]]=i
        count+=1
    
    if len(hm)==0:
        print(s)
    hm = sorted(hm.items(), key=lambda x:x[1])
    
    print(hm)
    for i in range(len(hm)):

        s+=hm[i][0]
        s+="-"
        count+=1
    print(s[:len(s)-1])

arr = ["A", "B", "C", "D", "E", "D", "Q", "Z", "C" ]
# arr = ["A", "B", "A", "C", "A", "B"]
check(arr)