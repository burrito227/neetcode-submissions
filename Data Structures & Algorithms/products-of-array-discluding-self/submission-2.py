class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        products = []

        for i in range(len(nums)):
            products.append(product)
            product *= nums[i]

        print(products)
        product = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            products[j] *= product
            product *= nums[j]

        return products