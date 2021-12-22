def design(n,m):
    #Upper portion of the mat
    i = 1
    while(i <= n//2):
        mid = m//2 
        
        j = 3*i - 1
        while(j <= mid):           
            print("-", end = "")            
            j += 1
        
        k = 2*i - 1
        while(k>0):
            print(".|.", end = "")
            k-=1

        j = mid - (3*i-1)
        while(j >= 0):
            print("-", end = "")             
            j -= 1
            
        print()
        i += 1
        
    #Middle portion 
    char = "Welcome"
    num = m//2     #m - length of "welcome"
    for i in range(num - len(char)//2):
        print("-", end = "")
        
    print("Welcome", end = "")
    
    for j in range(num - len(char)//2):
        print("-", end = "")        
    print()    
    
    #Lower portion 
    i = n//2
    while(i > 0):
        mid = m//2 
        
        j = 3*i - 1
        while(j <= mid):           
            print("-", end = "")            
            j += 1
        
        k = 2*i - 1
        while(k>0):
            print(".|.", end = "")
            k-=1

        j = mid - (3*i-1)
        while(j >= 0):
            print("-", end = "")             
            j -= 1

        i -= 1    
        print()    
    return 

if __name__ == '__main__':
    n,m = map(int, input().split())     #row x column 
    design(n,m)
    
# 9 < n < 31
# 27 < n < 93


