import math
import time
start_time = time.time()
num = "73106717653132"
num_list = list(map(int, num))
answer = 0
window_size = 3
zero_counter = 0
#print(outgoing)
#print("the product is: %i" % product)
for i in range(len(num_list)-window_size+1):
  outgoing = num_list[i-1]
  incoming = num_list[i-1+window_size]
  if i == 0:
    product = math.prod(num_list[0:window_size])
    print("the first product is: %i" % product)
    print(i)
  elif incoming == 0 or outgoing == 0:
    if incoming == 0 and outgoing == 0:
      product == 0
    elif incoming == 0 and outgoing > 0:
      zero_counter +=1
      product = 0 
    elif outgoing == 0 and incoming > 0:
      zero_counter -= 1
      if zero_counter == 0:
        product = math.prod(num_list[i:i+window_size])
    elif zero_counter > 0:
      product == 0
  elif zero_counter > 0:
    product = 0
  else:
    product = (product//outgoing)*(incoming)
    #print(outgoing)
    #print(incoming)
  print("the product is: %i" % product)
  print(i)
  if product > answer:
    answer = product
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
