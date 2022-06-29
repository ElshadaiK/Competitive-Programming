class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people.sort(key=lambda x:(-x[0], x[1]))
        print(people)
        for item in people:
            queue.insert(item[1], item)
        return queue