# Last updated: 9/16/2025, 2:17:51 PM
class Solution:
    def repeatLimitedString(self, s, repeatLimit):
        freq = Counter(s)
        max_heap = [(-ord(char), char, count) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            
            _, char, count = heapq.heappop(max_heap)
            add_count = min(count, repeatLimit)  
            result.append(char * add_count)
            
           
            if count > add_count:
                if not max_heap:
                    break  
                _, next_char, next_count = heapq.heappop(max_heap)
                result.append(next_char)
                
                heapq.heappush(max_heap, (-ord(char), char, count - add_count))
                if next_count > 1:
                    heapq.heappush(max_heap, (-ord(next_char), next_char, next_count - 1))
        
        return ''.join(result)
