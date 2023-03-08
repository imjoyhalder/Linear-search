
# linear search 
position = -1 
def search(n,list):
    i = 0
    while i<len(list):
        if list[i]==n:
            globals()["position"]=i
            
            return True
        i+=1
    return False
n = int(input("Enter your number: "))
list = [1,2,3,7,3,10,8,9]
if search(n,list):
    print("Found")
    print(f"{n} position is {position+1}")
else: 
    print("Not found")