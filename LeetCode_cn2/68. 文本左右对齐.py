from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        cur = []
        cnt = 0

        for w in words:
            if cnt + len(w) + len(cur) > maxWidth:

                for i in range(maxWidth - cnt):
                    cur[i % (len(cur) - 1 or 1) ] += " "

                res.append(''.join(cur))
                cur = []
                cnt = 0

            cur.append(w)
            cnt += len(w)

        res.append(' '.join(cur).ljust(maxWidth))
        return res