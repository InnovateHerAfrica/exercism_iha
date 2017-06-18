def lone_sum(a, b, c):
  total = 0
  list_of_parameters = [a, b, c]
  for num in list_of_parameters:
    if list_of_parameters.count(num) == 1:
      total += num
  return total
