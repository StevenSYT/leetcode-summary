class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        diff_masks = set()

        for word in dictionary:
            if len(word) != n:
                continue
            diff_mask = 0
            for i, ch in enumerate(word):
                if ch != target[i]:
                    diff_mask |= (1 << i)
            diff_masks.add(diff_mask)

        if not diff_masks:
            return str(n)

        abbrevs = []

        for abb_mask in range(1 << n):
            if all(abb_mask & diff_mask for diff_mask in diff_masks):
                abbrevs.append(self.gen_abbrev(target, abb_mask))

        return min(abbrevs, key=lambda x: len(x))

    def gen_abbrev(self, target, mask):
        res = ''
        count_abb = 0

        for i, ch in enumerate(target):
            if (mask & (1 << i) > 0):
                if count_abb:
                    res += str(count_abb)
                    count_abb = 0
                res += ch

            else:
                count_abb += 1

        if count_abb:
            res += str(count_abb)

        return res