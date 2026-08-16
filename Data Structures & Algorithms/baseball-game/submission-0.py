class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for op in operations:
            if op not in ['D', '+', 'C']:
                result.append(int(op))
            elif op == 'D':
                previous = int(result[-1])
                result.append(2 * previous)
            elif op == '+':
                result.append(int(result[-1]) + int(result[-2]))
            elif op == 'C':
                result.pop()
        return sum(result)
