

#Given an int n, return True if it is within 10 of 100 or 200. 
#Note: abs(num) computes the absolute value of a number.


#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

  def near_hundred(n):
  return ((abs(100-n)<=10) or (abs(200-n) <=10))


#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)