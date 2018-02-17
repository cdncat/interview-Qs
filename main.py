## Coinbag Question

# cc stands for coinCombos
# For a list of coins, where each element represents a coin's value
# and (monetary) amount:
# calculate the number of ways we combine the elements in coins to sum to amount
# can use each element 0, 1, or more times
# example: cc(5, [1,2]) returns 3

def cc(amount, coins):
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

# some test cases:
# print(cc(1, [1]))
# print(cc(2, [1,2]))
# print(cc(5, [1,2,3]))
# print(cc(7, [4]))
