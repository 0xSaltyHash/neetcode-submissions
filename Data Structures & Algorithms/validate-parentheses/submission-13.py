class Solution:
    def isValid(self, s: str) -> bool:
        result = False
        pairs_lookup = {'{': '}', '(':')', '[': ']'}
        stack = []
        for char in s:
            if char in pairs_lookup.keys():
                stack.append(char)
            elif len(stack):
                latest_opening = stack.pop()
                result = (char == pairs_lookup[latest_opening])
                if not result:
                    break
            else:
                result = False
                break
        if len(stack):
            result = False
        return result