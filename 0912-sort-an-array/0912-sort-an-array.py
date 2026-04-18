class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                mergesort(nums, low, mid)
                mergesort(nums, mid + 1, high)
                merge(nums, low, mid, high)

        def merge(nums, low, mid, high):
            left,right=nums[low:mid+1],nums[mid+1:high+1]
            i,j,k=low,0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    nums[i]=left[j]
                    j+=1
                else:
                    nums[i]=right[k]
                    k+=1
                i+=1

            while j<len(left):               
                nums[i]=left[j]
                j+=1
                i+=1

            while k<len(right):               
                nums[i]=right[k]
                k+=1
                i+=1 
           
        mergesort(nums, 0, len(nums) - 1)
        return nums
        # def quicksort(nums,low, high):
        #     if low<high:
        #         p= partition(nums,low,high)
        #         quicksort(nums,low, p-1)
        #         quicksort(nums,p+1,high)
        
        # def partition(nums,low,high):
        #     rand_idx=random.randint(low,high)
        #     nums[low],nums[rand_idx]=nums[rand_idx],nums[low]
        #     pivot=nums[low]
        #     i,j=low,high

        #     while i<j:
        #         while nums[i]<=pivot and i<=high-1:
        #             i+=1
        #         while nums[j]>pivot and j>=low+1:
        #             j-=1
        #         if i < j:  
        #             nums[i],nums[j]=nums[j],nums[i]

        #     nums[low],nums[j]=nums[j],nums[low]
        #     return j

        # quicksort(nums, 0, len(nums) - 1)
        # return nums

         # temp = []
            # left, right = low, mid + 1

            # while left <= mid and right <= high:
            #     if nums[left] <= nums[right]:
            #         temp.append(nums[left])
            #         left += 1
            #     else:
            #         temp.append(nums[right])
            #         right += 1

            # while left <= mid:
            #     temp.append(nums[left])
            #     left += 1

            # while right <= high:
            #     temp.append(nums[right])
            #     right += 1

            # for i in range(len(temp)):
            #     nums[low + i] = temp[i]
