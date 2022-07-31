class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.item_len = int(math.sqrt(self.n))
        self.bulks = [sum(nums[i:i + self.item_len]) for i in range(0, self.n, self.item_len)]
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        diff = self.nums[index] - val
        self.bulks[index // self.item_len] -= diff
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        total, start, end = 0, left // self.item_len, right // self.item_len
        if start == end:
            return sum(self.nums[left:right+1])
        for i in range(left, (start + 1) * self.item_len):
            total += self.nums[i]

        if start + 1 <= end:
            total += sum(self.bulks[start+1:end])

        for i in range(end * self.item_len, right + 1):
            total += self.nums[i]

        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)