def odd_numbers(n: int) -> list[int]:
   l = []
   valor = 1
   while valor <= n:
      l.append(valor)
      valor += 1

   impar = []
   for _ in l:
      if _ %2 != 0:
         impar.append(_)
   return impar
