def sum_numbers(n: int) -> int:
   valor = 1
   total = 0
   while valor <= n:
      total += valor
      valor += 1
   return total