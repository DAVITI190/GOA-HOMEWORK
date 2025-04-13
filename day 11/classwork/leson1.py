def solution(string, ending):
    return string.endswith(ending)

print(solution('abc', 'bc'))  
print(solution('abc', 'd'))    
print(solution('hello', 'lo')) 
print(solution('hello', ''))   
