import random
import time


# call this once before using other functions
# returns seed used
def initialize_rng(seed=time.time()):
    random.seed(seed)
    return seed


# random number from 1 to n (inclusive)
def generate_random_from_range(n):
    return random.randint(1, n)


# returns n randomly selected elements from source (no duplicates)
def select_from_list(source, n):
    return random.sample(source, n)


# randomizes order of elements from source (does not modify original)
def randomize_order(source):
    staging = source.copy()
    random.shuffle(staging)
    return staging
