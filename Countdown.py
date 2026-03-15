# create a countdown for happy new year

import time
count=int (input("Enter the counter num :"))
print ("\n countdown starts now:")
for i in range (count,0,-1):
    print(i)
    time.sleep(1)

print("Whooo Happy New Year")
