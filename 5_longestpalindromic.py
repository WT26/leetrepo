class Solution(object):
    # Correct way
    def longestPalindrome(self, s):
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(self, s, i, i)
            len2 = self.expandAroundCenter(self, s, i, i + 1)
            leni = max(len1, len2)
            if (leni > end - start):
                start = i - (leni - 1) / 2
                end = i + leni / 2
        return s[int(start):int(end) + 1]


    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1

        return R - L - 1


        # Magic way, credits Joe Wallis Stackexchange. Still too slow in some cases
        #string = s.replace('', '^')
        #longest = 0
        #position = 0
        #length = len(string)
        #for index in range(length):
        #    stretch = 0
        #    for stretch in range(1, min(index + 1, length - index)):
        #        text = string[index - stretch:index + stretch + 1]
        #        if text != text[::-1]:
        #            stretch -= 1
        #            break
        #    if stretch > longest:
        #        longest = stretch
        #        position = index
        #position -= longest
        #return string[position:position + (2*longest + 1)].replace('^', '')

        # Own, too slow version(takes atleast 5x time).
    #    longest = ""
    #    i_longest = -1
    #    lenlong = 0
    #    cur_string = ""
    #    cur_i = 0
    #    while True:
    #        cur_string += s[cur_i]
    #        if cur_string[0] == cur_string[len(cur_string) - 1]:
    #            if self.isPalindrome(self, cur_string):
    #                longest = cur_string
    #                lenlong = len(longest)
    #                i_longest = cur_i - (lenlong - 1)
#
    #        if cur_i == (len(s) - 1):
    #            cur_string = cur_string[1:]
    #            excessive = len(cur_string) - lenlong
    #            cur_string = cur_string[:-(excessive)]
#
    #            if excessive <= 0:
    #                break
    #            cur_i = i_longest + lenlong + 1
    #            i_longest += 1
    #        else:
    #            cur_i += 1
    #    return longest
#
    #def isPalindrome(self, s):
    #    result = True
    #    str_len = len(s)
    #    if s[0] != s[len(s) - 1]:
    #        return False
    #    for i in range(0, int(str_len/2)):
    #        if s[i] != s[str_len-i-1]:
    #            result = False
    #            break
    #    return result
s = Solution
print(s.longestPalindrome(s, "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"))