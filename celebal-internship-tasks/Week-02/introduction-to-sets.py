# introduction to sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    
    diff_heights = set(array)
    
    avg = sum(diff_heights) / len(diff_heights)
    
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())  
    arr = list(map(int, input().split())) 
    result = average(arr)  
    print(result)  
