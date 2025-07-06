# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

import re
for _ in range(int(input())):
    try:
        re.compile(input().strip())
        print(True)
    except re.error:
        print(False)