def is_prime(num):
  if(num<2):
    return False
  for i in range(2,num):
    if(num%i== 0):
      return False
  return True
def calculate_prime_number(length):
      lista =[]
      ingg = 2
      while True:
          if is_prime(ingg):
            lista.append(ingg)
            if len(lista) == length:
                break
          ingg += 1  
      return lista

n = int(input('lista '))
print(calculate_prime_number(n))













