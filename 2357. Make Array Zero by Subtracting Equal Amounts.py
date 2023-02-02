def minimumOperations(self, nums: List[int]) -> int:
        unique = list(set(nums) - {0})
        return len(unique)