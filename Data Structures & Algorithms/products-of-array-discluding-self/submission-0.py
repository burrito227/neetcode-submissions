class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zero_index = -1
        negative_counter = 0

        for i, num in enumerate(nums):
            if num == 0:
                if zero_index >= 0:
                    print("A 2nd zero was detected...")
                    return [0] * len(nums)

                print("Zero detected...")
                zero_index = i

                continue

            if num <= 0:
                print("Negative number detected...")
                negative_counter += 1

            full_product *= num


        even_negatives = negative_counter % 2 == 0

        if zero_index >= 0:
            # If there is only 1 zero detected, then all is 0 except where index matches the zero
            products = [0] * len(nums)
            products[zero_index] = full_product

            return products
            
        products = []
        for num in nums:
            products.append(int(full_product / num))

        return products