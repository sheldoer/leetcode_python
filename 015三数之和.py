class Solution:
    def threeSum(self, nums):
        length=len(nums)
        ls=[]
        same=[]
        for i in range(length):
            for j in range(i+1,length):
                if 0-nums[i]-nums[j] in nums[j+1:]:
                    lst=[nums[i],nums[j],0-nums[i]-nums[j]]
                    if set(lst)not in same:
                        ls.append(lst)
                        same.append(set(lst))
        print(ls)
        
p1=Solution()
print(p1.threeSum([-1,0,1,2,-1,-4]))
