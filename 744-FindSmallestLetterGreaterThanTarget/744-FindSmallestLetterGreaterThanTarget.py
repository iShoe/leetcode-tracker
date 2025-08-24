# Last updated: 8/24/2025, 12:23:34 AM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        result = letters[0]

        for char in letters:
            if ord(char) > ord(target):
                result = char
                break
        
        return result

        