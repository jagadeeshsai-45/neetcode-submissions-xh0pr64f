class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        m=len(nums1)
        n=len(nums2)

        right=m
        left=0

        while left<=right:
            partionA=(left + right)//2
            partionB=(m+n+1)//2 - partionA

            if partionA == 0:
                leftA=float('-INF')
            else:
                leftA = nums1[partionA-1]

            if partionA == m:
                rightA=float('INF')
            else:
                rightA= nums1[partionA]

            if partionB == 0:
                leftB=float('-INF')
            else:
                leftB = nums2[partionB-1]

            if partionB == n:
                rightB=float('INF')
            else:
                rightB= nums2[partionB]

            if leftA <= rightB and leftB <= rightA :

                if (m+n)%2 ==1:
                    return max(leftA,leftB)

                return (max(leftA, leftB) + min(rightA, rightB))/2
            elif  leftA > rightB :
                right = partionA - 1
            else:
                left = partionA + 1
