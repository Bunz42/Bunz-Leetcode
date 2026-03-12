class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float("-infinity")
            A_right = A[i] if i < len(A) else float("infinity")
            
            B_left = B[j - 1] if j > 0 else float("-infinity")
            B_right = B[j] if j < len(B) else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 != 0:
                    return min(A_right, B_right)
                else:
                    return ( max(A_left, B_left) + min(A_right, B_right) ) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
                
