class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        wordsMap = {}
        for word in words:
            if word not in wordsMap:
                wordsMap[word] = 1
            else:
                wordsMap[word] += 1

        word_length = len(words[0])
        words_length = len(words)
        s_length = len(s)
        result = []

        for i in range(s_length - word_length * words_length + 1):
            j = 0
            cur_dict = {}
            while j < words_length:
                word = s[i + word_length * j:i + word_length * j + word_length]
                if word not in wordsMap:
                    break
                if word not in cur_dict:
                    cur_dict[word] = 1
                else:
                    cur_dict[word] += 1
                if cur_dict[word] > wordsMap[word]:
                    break
                j += 1
            if j == words_length:
                result.append(i)
        return result


    def findSubstring60(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ''' 
        O(nm)
        n, m, k = len(s), len(words[0]), len(words)
        暴力做法，枚举开始位置，判断之后长度m*k的子串是否由给定字符串集合组成，最坏复杂度为O(nmk)。
        对于长度为m的字符串，0与m位置开始的区别，只在于少了s[0:m]，多了s[m*k+1:(m+1)*k]，所以产生了许多
        冗余操作。我们根据开始位置0~m-1分类，扫描字符串s，使用一个滑动窗口记录当前匹配了那些字符串，当下一个
        字符串不在words中，清空窗口(任意包含该串的均不合法)，如果记录的出现次数超过了words中数量，表示需要滑动窗口，
        在滑动窗口时，直到所有Word出现的次数均合法，结束滑动。
        窗口中单词数量等于k时，更新答案。
        '''
        result = []
        lenWord = len(words[0])
        numOfWords = len(words)
        lenSubstring = lenWord * numOfWords
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        for i in range(min(lenWord, len(s)-lenSubstring+1)):
            curr = {}
            strStart = i  # 拼接字符串开始的位置
            wordStart = strStart  # 中间一个单词开始的位置
            while strStart + lenSubstring <= len(s):  # 如果没有越界
                word = s[wordStart: wordStart+lenWord]  # 获取一个单词
                wordStart += lenWord  # 更新下一个单词的开始位置
                if word not in dic:  # 如果出现了不存在的单词，则清空当前字典，重新添加
                    strStart = wordStart  # 重置 字符串开始位置和单词开始位置
                    curr.clear()
                else:
                    if word in curr:  # 如果已经存在，加一，否则新建一个
                        curr[word] += 1
                    else:
                        curr[word] = 1
                    while curr[word] > dic[word]:  # 如果出现次数超过了，向后移动滑动窗口--（移动覆盖）直到所有的
                        curr[s[strStart: strStart+lenWord]] -= 1
                        strStart = strStart + lenWord
                    if wordStart - strStart == lenSubstring:
                        result.append(strStart)
        return result


if __name__ == '__main__':
    solu = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    s = "abccababacdefg"
    words = ["a", "b", "c"]
    result = solu.findSubstring60(s, words)

    print(result)