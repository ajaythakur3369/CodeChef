'''
Task:- 
In ChefLand, human brain speed is measured in bits per second (bps). Chef has a threshold limit of X bits per second above which his calculations are prone to errors. If Chef is currently working at Y bits per second, is he prone to errors?

If Chef is prone to errors print YES, otherwise print NO.
'''

'''
Input Format:- 
The only line of input contains two space separated integers X and Y — the threshold limit and the rate at which Chef is currently working at.
'''

'''
Output Format:- 
If Chef is prone to errors print YES, otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings yes, Yes, yEs, and YES will all be treated as identical).
'''

'''
Constraints:- 
 1≤X,Y≤100
'''
 
'''
Sample 1:-
Input:
7 9

Output:
YES

Explanation:
Chef's current brain speed of 9 bps is greater than the threshold of 7 bps, hence Chef is prone to errors.
'''

'''
Sample 2:-
Input:
6 6

Output:
NO

Explanation:
Chef's current brain speed of 6 bps is not greater than the threshold of 6 bps, hence Chef is not prone to errors.
'''

'''
Sample 3:-
Input:
31 53

Output:
YES

Explanation:
Chef's current brain speed of 53 bps is greater than the threshold of 31 bps, hence Chef is prone to errors.
'''

'''
Sample 4:-
Input:
53 8

Output:
NO

Explanation:
Chef's current brain speed of 8 bps is not greater than the threshold of 53 bps, hence Chef is not prone to errors.
'''

x, y = map(int, input().split())
if y > x:
    print("YES")
else:
    print("NO")
