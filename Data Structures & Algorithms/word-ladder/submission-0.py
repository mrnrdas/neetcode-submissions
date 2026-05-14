from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)

        
        visit = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            current_length = len(queue)

            for _ in range(current_length):
                word = queue.popleft()
                
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)

            res += 1

        return 0