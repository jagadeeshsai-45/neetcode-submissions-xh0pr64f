class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        ferq=[[] for i in range(len(nums)+1)]

        for num in nums :
            count[num] =  1 + count.get(num, 0)
        for num,c in count.items():
            ferq[c].append(num)

        res=[]
        for i in range(len(ferq) - 1,0,-1):
            for num in ferq[i]:
                res.append(num)
                if len(res)==k:
                    return res

        