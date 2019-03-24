

# brute force
#     def containsDuplicate(self, nums: 'List[int]') -> 'bool':
#         if not nums: return False

#         temp = []
#         for n in nums:
#             if n not in temp: temp.append(n)
#             else: return True

#         return False

# Counter
#     def containsDuplicate(self, nums):
#         if not nums: return False

#         c = Counter(nums)
#         for key in c:
#             if c[key] > 1: return True
#         return False

# Sort
#     def containsDuplicate(self, nums):
#         if not nums: return False

#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]: return True
#         return False


def contains_duplicate(nums):
    """
    Set
    :param nums:
    :return:
    """
    if not nums:
        return False
    return len(nums) != len(set(nums))
