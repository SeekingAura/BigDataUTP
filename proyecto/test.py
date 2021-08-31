import random
import sys

def reservoir_sampling(l, k):
    it = iter(l)
    try:
        result = [next(it) for _ in range(k)] # use xrange if on python 2.x
    except StopIteration:
        raise ValueError("Sample larger than population")

    for i, item in enumerate(it, start=k):
        s = random.randint(0, i)
        if s < k:
            result[s] = item

    random.shuffle(result)
    return result

with open(sys.argv[1]) as infile:
    # Get headerline
    for line in infile:
        print(line)
        break
    
    # If you want a random seed...
    # random.seed(34)
    # Get data
    for line in reservoir_sampling(infile, 100):
        print(line)