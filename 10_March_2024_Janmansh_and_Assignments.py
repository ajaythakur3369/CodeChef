'''
Task:- 
Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?
'''

'''
Input Format:-
 The first line will contain T - the number of test cases. Then the test cases follow.
 The first and only line of each test case contains one integer X - the time when Janmansh starts doing the assignemnts.
'''

'''
Output Format:- 
For each test case, output Yes if he can complete the assignments on time. Otherwise, output No.
You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).
'''

'''
Constraints:- 
 1≤T≤10
 1≤X≤9
'''

'''
Sample 1:- 
Input:
2
7
9

Output:
Yes
No

Explanation:
Test case-1: He can start at 7pm and finish by 10 pm. Therefore he can complete the assignments.
Test case-2: He can not complete all the 3 assignments if he starts at 9 pm.
'''

'''
Cook your dish here
'''

for _ in range(int(input())):
    n = int(input())
    if n<=10-3:
        print("YES")
    else:
        print("No")