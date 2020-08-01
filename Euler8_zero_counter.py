import math
import time
start_time = time.time()
num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
num_list = list(map(int, num))
answer = 0
window_size = 13
zero_counter = 0

for i in range(len(num_list)-window_size+1):
  outgoing = num_list[i-1]
  incoming = num_list[i-1+window_size]
  if i == 0:  #handle position 0 (since you can't go -1 on this)
    product = math.prod(num_list[0:window_size])
    print("the first product is: %i" % product)
    print(i)
  elif incoming == 0 or outgoing == 0: 
    if incoming == 0 and outgoing == 0: #zero counter doesn't change because one 0 left but one 0 came in. Because 1 zero left then zero counter must already have been greater than 1. So product = 0.
      product == 0
    elif incoming == 0 and outgoing > 0: #zero counter goes up by 1 which implies zero counter is greater than 0 and so product = 0.
      zero_counter +=1
      product = 0 
    elif outgoing == 0 and incoming > 0: #zero counter goes down by 1
      zero_counter -= 1
      if zero_counter == 0: #then if zero counter is now 0 then the window has no 0's and can be calculated
        product = math.prod(num_list[i:i+window_size])
      elif zero_counter > 0: #this will capture when an incoming is greater than 1 and an outgoing is 0 AND zero counter is still greater than 0
        product = 0
  elif zero_counter > 0: #this captures where both incoming and outgoing are greater than 0 but when zero counter is still greater than 0
    product = 0
  else: #this is the expression that is used the most. it will calculate the product of a window that does not contain 0's.
    product = (product//outgoing)*(incoming)
  print("the product is: %i" % product)
  print(i)
  if product > answer:
    answer = product
print("The value of the %i adjacent digits with the greatest product is %i" % (window_size, answer))
print("--- %s seconds ---" % (time.time() - start_time))
