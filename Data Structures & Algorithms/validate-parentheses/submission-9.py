class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"]": "[", ")":"(", "}":"{"}
        track = []
        for c in s:
            if c in mapping:
                if track and track[-1] == mapping[c]:
                    track.pop()
                else:
                    return False
            else:
                track.append(c)
        if not track:
            return True
        else:
            return False