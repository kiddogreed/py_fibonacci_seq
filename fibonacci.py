#fibonacci sequence 

num = int(input())

def compute_fib(num):
  a = 0
  b = 1

  if num == 1:
    print(a)
  else:
    print(a)
    print(b)

  for n in range(2, num):
    c = a + b
    a = b
    b = c 
    
    print(c)

compute_fib(num)


