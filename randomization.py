import random
import time


# call this once before using other functions
# returns seed used
def initialize_rng(seed=time.time()):
    random.seed(seed)
    return seed


# random int number from 1 to n (inclusive)
def generate_random_from_range(n):
    return random.randint(1, n)


# random number (0;1) for probability
def generate_probability():
    return random.uniform(0, 1)


# returns n randomly selected elements from source (no duplicates)
def select_from_list(source, n):
    return_value = random.sample(source, n).copy()
    return return_value

# randomizes order of elements from source (does not modify original)
def randomize_order(source):
    staging = source.copy()
    random.shuffle(staging)
    return staging
