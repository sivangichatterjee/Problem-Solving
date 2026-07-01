class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # zeroes=arr.count(0)
        # n=len(arr)
        # read=n-1
        # write=n+zeroes-1
        # while read>=0:
        #     if write<n:
        #         arr[write]=arr[read]
        #     if arr[read]==0:
        #         write-=1
        #         if write<n:
        #             arr[write]=0

        #     write-=1
        #     read-=1
        zeroes=arr.count(0)
        n=len(arr)
        result=[]
        for i in range(len(arr)):
            if len(result)<n:
                result.append(arr[i])
            if arr[i]==0 and len(result)<n:
                result.append(0)
            
        for i in range(len(result)):
            arr[i]=result[i]



        