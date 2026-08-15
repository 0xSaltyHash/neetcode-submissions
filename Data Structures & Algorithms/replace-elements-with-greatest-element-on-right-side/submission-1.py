class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        length = len(arr)
        answer = [0] * length
        for i in range(length-1, -1, -1):
            answer[i] = right_max
            right_max = max(arr[i], right_max)
        return answer