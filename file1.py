def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

//this is a comment
//This is another way
def isPalindrome(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
   print("No")
