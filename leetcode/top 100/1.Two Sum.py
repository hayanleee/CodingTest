# leetcode 아이디 : white___ / 메일 : gmail

def twoSum(nums, target):
    for e, i in enumerate(nums):
        find_value = target - i
        try:
            location = nums.index(find_value, e+1)
            # return [e, location]
            print([e, location])
        except ValueError:
            pass

twoSum([3,3], 6)
