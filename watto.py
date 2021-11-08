class TrieNode:
    def __init__(self, s):
        self.val = s
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode(" ")

    def insert(self, word: str) -> None:
        if(word[0] not in self.root.children):
            temp = TrieNode(word[0])
            self.root.children[word[0]] = temp
            
            for i in range(1, len(word)):
                nex = TrieNode(word[i])
                temp.children[word[i]]= nex
                temp = nex
            temp.end = True
        else:
            ended = False
            ended_at = 0
            temp = self.root.children[word[0]]
            for i in range(1, len(word)):
                if(word[i] in temp.children):
                    temp = temp.children[word[i]]
                else:
                    ended = True
                    ended_at = i
                    break
            if(ended):
                for i in range(ended_at, len(word)):
                    nex = TrieNode(word[i])
                    temp.children[word[i]]= nex
                    temp = nex
            temp.end = True
                    
    
    def differByOne(self, word, count=0, start=True, temp=0):
        
        if(start):
            temp = self.root
        answer = False
        if(word == ""):
            count += 1
            if(count > 1):
                return False
            return True
        if(word[0] not in temp.children):
            count += 1
        for children in temp.children:
            answer =  self.differByOne(word[1:], count=count, start=False, temp=temp.children[children]) or answer
        
                    
        if(count >1):
            return False
        return True

        
def solution(store, questions):
    root = Trie()
    for item in store:
        root.insert(item)
    for question in questions:
        if(root.differByOne(question)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solution(['aaaaa', 'acacaca', 'abc', 'acdj'], ['aabaa','ccacacc','caaac', 'acc'])