def largest_prime_factor(number) :
     factors = []
     factor = 2
     while number > 1 :
	while number % factor == 0 :
		factors.append(factor)
                number = number / factor
        factor  = factor +  1
     return max(factors)
