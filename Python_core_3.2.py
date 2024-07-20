from random import randint, sample
def get_numbers_ticket(min, max, quantity):  
    return sorted(sample(range(min, max), quantity))

print(get_numbers_ticket(10,20,5))
print(get_numbers_ticket(10,15,5))
print(get_numbers_ticket(10,4,5))
print(get_numbers_ticket(10,14,6))