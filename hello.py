import operator
from random import randint

if __name__ == '__main__':
    print('hello')

    nums = [1, 2, 3]

    for i, _ in enumerate(nums):
        j = randint(0, len(nums) - 1)
        nums[i], nums[j] = nums[j], nums[i]
    

    n = 25
    print(n)
