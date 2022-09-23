def solution(numbers):
    answer = []
    
    def check(a, b) :
        return bin(a ^ b).count("1") <= 2
        
    def f(x) :
        if x & 1 == 0 :
            return x+1
        
        i = 0
        ret = x+1
        while not check(x, ret) :
            ret += (1 << i)
            i += 1
        return ret
    
    for number in numbers :
        answer.append(f(number))
        
    return answer