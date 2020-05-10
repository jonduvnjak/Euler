import math
import time
start_time = time.time()
num = "7316717653132"
num_list = list(map(int, num))
answer = 0
window_size = 2
zero_counter = 0
#print(outgoing)
#print("the product is: %i" % product)
for i in range(len(num_list)-window_size):
  outgoing = num_list[i-1]
  incoming = num_list[i-1+window_size]
  print(incoming)
  if i == 0:
    product = math.prod(num_list[0:window_size])
    print("the first product is: %i" % product)
  elif incoming == 0 or outgoing == 0:
    if incoming == 0:
      zero_counter += 1
    if outgoing == 0:
      zero_counter -= 1
  else:
    product = (product//outgoing)*(incoming)
    print("the product is: %i" % product)
    #print(outgoing)
    #print(incoming)
  if product > answer:
    answer = product
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
