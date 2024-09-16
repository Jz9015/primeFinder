import time
num = int(input("Enter a number: "))
start = time.time()
safety = float(num/2)
testNum = 2
output = float(1)
while testNum<=safety:
    output = num/testNum
    testNum+=1
    if output-round(output,0)==0:
        print(num,"is not prime.","First factors are",testNum-1,f"{output:.0f}.")
        end = time.time()
        print(end-start)
        exit()
print(num,"is prime")
end = time.time()
print("RunTime: "+str(end-start))