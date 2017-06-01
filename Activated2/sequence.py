def sequence(numbers, seq):
    seq_l = len(seq)
    while len(numbers) >= seq_l:
        if numbers[0:seq_l] == seq :
            return True
        numbers = numbers[1:]
    return False

    
