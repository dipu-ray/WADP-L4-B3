# recursion problem: sum of given number
def sum(num):
  if num>0:
    summation = num+sum(num-1)
  else:
    summation=0
  return summation
print(sum(10))