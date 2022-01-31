import functools

class Solution:
    def largestNumber(self,nums):
        s = [str(i) for i in nums]

        def cmp(a,b):
            if (a + b) > (b + a):
                return 1
            if (a + b) < (b + a):
                return -1
            return 0

        s.sort(reverse=True,key=functools.cmp_to_key(cmp))
        return str(int("".join(s)))

if __name__ == '__main__':
    l = Solution()
    m = l.largestNumber
    nums = [10,22,34,1,55,332,19]
    print(m(nums))