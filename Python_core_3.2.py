from random import randint, sample
def get_numbers_ticket(min, max, quantity): 
    min = 1
    max = 500
    quantity = 5   
    return(sorted(sample(range(min, max), quantity)))