'''
Task:- 
Currently there are courses for 4 languages, and hence there are 8 courses in this section. But suppose there are courses for N languages, what will be the total number of courses in this section?
'''

'''
Input Format:- 
The only line of input will contain a single integer N, denoting the number of languages for which there are courses.
'''

'''
Output Format:- 
Output on a single line the total number of courses in the section.
'''

'''
Constraints:- 
1 ≤ N ≤ 100
'''

'''
Sample 1:- 
Input: 
4
Output
8 
Explanation:   
If there are 4 languages, then there will be 2∗4 = 8 courses in total.
'''

'''
Sample 2:- 
Input: 
9 
Output:  
18 
Explanation:    
If there are 9 languages, then there will be 2∗9 = 18 courses in total.
'''

'''
Cook your dish here
'''

n = int(input())
total_courses = 2 * n
print(total_courses)