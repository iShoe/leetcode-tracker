# Last updated: 1/29/2026, 3:30:18 AM
1class Solution:
2
3    def is_special(self, character: str) -> bool:
4        special_characters = {
5            "!",
6            "@",
7            "#",
8            "$",
9            "%",
10            "^",
11            "&",
12            "*",
13            "(",
14            ")",
15            "-",
16            "+"
17        }
18
19        if character in special_characters:
20            return True
21
22        return False
23
24    def strongPasswordCheckerII(self, password: str) -> bool:
25        lowercase_ok = False
26        uppercase_ok = False
27        digit_ok = False
28        special_ok = False
29        
30        length = 0
31        prev_c = ""
32
33        for i, c in enumerate(password):
34            length += 1
35            if c.islower():
36                lowercase_ok = True
37            elif c.isupper():
38                uppercase_ok = True
39            elif c.isdigit():
40                digit_ok = True
41            elif self.is_special(c):
42                special_ok = True
43
44
45            if c == prev_c:
46                return False 
47            
48            prev_c = c
49        
50
51        if length >= 8 and lowercase_ok and uppercase_ok and digit_ok and special_ok:
52            return True
53        
54        return False
55