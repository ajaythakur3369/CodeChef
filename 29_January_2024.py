'''
Task:- 
Chef defines a pair of positive integers (a, b) to be a Oneful Pair, if a+b+(a⋅b) = 111

For example, (1,55) is a Oneful Pair, since 1+55+(1⋅55) = 56+55 = 111.
But (1,56) is not a Oneful Pair, since 1+56+(1⋅56) = 57+56 = 113≠111.

Given two positive integers a and b, output Yes if they are a Oneful Pair. And No otherwise.
'''

'''
Input Format:- 
The only line of input contains two space-separated integers a and b.
'''

'''
Output Format:- 
Output Yes, if (a,b) form a Oneful Pair. Output No if they do not.

You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).
'''

'''
Constraints:- 
 1 ≤ a, b ≤ 1000 
'''

'''
Sample 1:- 
Input: 
1 55
Output: 
Yes
Explanation:
(1,55) is a Oneful Pair, since 1+55+(1⋅55) = 56+55 = 111.
'''

'''
Sample 2:- 
Input: 
1 56 
Output: 
No 
Explanation: 
(1,56) is not a Oneful Pair, since 1+56+(1⋅56) = 57+56 = 113 ≠ 111
'''

a,b = map(int,input().split())

'''
Write your code here
'''

c = a + b + (a*b)
if c == 111: 
    print("YES")
else: 
    print("No")









