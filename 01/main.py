import sys
import re

def __main__():
    fh = open(sys.argv[1] + ".in")
    ans = 0
    for line in fh:
        raw = line.strip()
        print(raw)

        # digits = re.findall(r'\d+', raw)
        # print(int(digits[0][0]) * 10 + int(digits[-1][-1]))
        # ans += int(digits[0][0]) * 10 + int(digits[-1][-1])

        nums = []
        words = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
        for i in range(len(raw)):
            current_char = raw[i]
            # print(current_char)

            if (current_char.isnumeric()):
                nums.append(int(current_char))
                # print("numeric", nums)
                continue
            # print("chek")
            for word in words.keys():
                if raw[i] == word[0] and word in raw[i:i+5]:
                    # print("checked:", raw[i:i+5])
                    nums.append(words[word])
                    # print("word", nums)
                    break
        print(nums)
        ans += nums[0] * 10 + nums[-1]
    fh.close()
    print(ans)

    

# ==================================================

__main__()