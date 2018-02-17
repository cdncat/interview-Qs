def cc(amount, coins):
  print(amount, coins)
  counter = 0
  if not coins:
    return 0
    
  for i, coin in enumerate(coins):
    if coin == amount:
      counter+=1
      continue
    if amount < coin:
      continue
    if amount%coin == 0:
      counter+=1
      
    quotient = amount//coin
    
    for j in range(1,quotient+1):
      result = cc(amount-j*coin, coins[i+1:])
      counter+=result

  return counter
      
    
# print(cc(1, [1]))
# print(cc(2, [1,2]))
# print(cc(1, [2]))
# print(cc(2, [1]))
print(cc(5, [1,2,3]))