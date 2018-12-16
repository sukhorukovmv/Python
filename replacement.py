#!/usr/bin/python3

def replacementAtoB(s, a, b):
    def iter(s, count):
       if b.count(a) != 0 and s.count(a) != 0:
           return "Impossible"
       if s.count(a) == 0:
           return count
       else:
           count += 1
           return iter(s.replace(a, b), count)
    return iter(s, 0)

replacementAtoB(str(input()), str(input()), str(input()))

print(replacementAtoB("ababa", "a", "b"))
print(replacementAtoB("aabbcc", "aa", "aaa"))
print(replacementAtoB("abab", "ab", "ba"))
print(replacementAtoB("abbbb", "a", "ab"))

