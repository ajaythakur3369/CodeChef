'''
Task:- 
Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day.

Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.
'''

'''
Input Format:- 
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer X — the amount of water Chef drank today.
'''

'''
Output Format:- 
For each test case, output YES if Chef followed the doctor's advice of drinking at least 2000 ml of water. Otherwise, output NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
'''

'''
Constraints:- 
 1 ≤ T ≤ 2000
 1 ≤ X ≤ 4000
'''

'''
Sample 1:- 
Input: 
3
2999
1450
2000

Output: 
YES
NO
YES
 
Explanation: 
Test case 1: Chef followed the doctor's advice since he drank 2999 ml of water which is ≥ 2000 ml.

Test case 2: Chef did not follow the doctor's advice since he drank 1450 ml of water which is < 2000 ml.

Test case 3: Chef followed the doctor's advice since he drank 2000 ml of water which is ≥ 2000 ml.
'''

t = int(input())
for i in range(0,t):
    x =  int(input())
    
    '''
    Write your code here
    '''
    
    if x >= 2000:
        print("YES")
    else:
        print("NO")