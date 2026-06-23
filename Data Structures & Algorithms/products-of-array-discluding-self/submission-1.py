class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zero_index = -1

        for i, num in enumerate(nums):
            if num == 0:
                if zero_index >= 0:
                    #print("A 2nd zero was detected...")
                    return [0] * len(nums)

                #print("Zero detected...")
                zero_index = i

                continue

            full_product *= num

        if zero_index >= 0:
            # If there is only 1 zero detected, then all is 0 except where index matches the zero
            products = [0] * len(nums)
            products[zero_index] = full_product

            return products
            
        products = []
        for num in nums:
            products.append(full_product // num)

        return products