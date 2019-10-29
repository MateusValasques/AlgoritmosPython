import random
import sys
random.seed(sys.argv[1])
print(random.sample(range(1,200), 10))