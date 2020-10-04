# followed tips from https://programming-journey.com/not-so-trivial-problem/ - member posted link in problem set discussion
# similar to lrishov's code

longString = ""
currentString = ""

# iterate through length of string. starting a s[0] through the entire length of the string.
for i in range(0, len(s)):
# compare the current character, or index, to the previous character, or index. for example, take string s = 'khase'. 
# is k > h? no. is h > a? no. is a > s? yes. to check whether the letters are in alphabetical order, the previous character 
# is greater than the current character. a > b > c... etc. since we can't directly compare letters, we're looking at the index. 
    if s[i] < s[i-1]: 
# concatenate the letter(s) into a string. back to s = 'khase'. if a > s, our string will be 'as'
        currentString = ''
# continue adding letters to find the longest substring. so, if s = 'khase', after 'as' is e. does s > e? no.
# so out longest substring is 'as'. but if s = 'khast' then s > t, so our string becomes 'ast'
    currentString += s[i]
# so now we have to find the LONGEST substring. if s = 'khast', 'as' is our previous string and 'ast' is our current string.
# is 'ast' > 'as'? yes? so 'ast' is our longest string. so, we find our longest substring when the current substring
# is greater than the previous substring. 
    if len(currentString) > len(longString):
        longString = currentString 
print("Longest substring in alphabetical order is:", longString)
