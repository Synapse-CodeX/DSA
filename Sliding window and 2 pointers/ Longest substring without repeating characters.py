
# 1. Brute Force Approach (Time Complexity: cap O open paren cap N squared close paren)
This approach uses nested loops to check every possible substring, utilizing a `set` to track unique characters.


maxi = 0
for i in range(len(s)):
    my_set = set()
    for j in range(i, len(s)):
        if s[j] in my_set:
            break
        my_set.add(s[j])
        maxi = max(maxi, j - i + 1)
return maxi



# 2. Optimal Sliding Window Approach (Time Complexity: cap O open paren cap N close paren)
This approach uses a dictionary to store the last seen index of each character, allowing the window to jump forward efficiently when a repeat is found.


my_dict = {}
left = 0
maxi = 0
for right in range(len(s)):
    if s[right] in my_dict:
        left = max(left, my_dict[s[right]] + 1)
    my_dict[s[right]] = right
    maxi = max(maxi, right - left + 1)
return maxi