from itertools import permutations

def parse(expression) :
    ret = []
    val = ""
    for c in expression :
        if c.isdigit() :
            val += c
        else :
            ret.append(val)
            ret.append(c)
            val = ""
    ret.append(val)
    return ret

def solution(expression):
    answer = 0
    cal = {
        "+" : (lambda a, b: str(int(a) + int(b))),
        "-" : (lambda a, b: str(int(a) - int(b))),
        "*" : (lambda a, b: str(int(a) * int(b)))
    }
    
    expression = parse(expression)
    for priority in permutations(("+", "-", "*")) :
        before = expression
        after = []
        for current in priority :
            if len(before) == 1 :
                break
            operand = ""
            operator = ""
            for c in before :
                if c.isdigit() or len(c) > 1 :
                    operand = c
                else :
                    if operator == current :
                        after.append(cal[operator](after.pop(), operand))
                    else :
                        if operator :
                            after.append(operator)
                        if operand :
                            after.append(operand)
                    operand = ""
                    operator = c
            if operator == current :
                after.append(cal[operator](after.pop(), operand))
            else :
                
                after.append(operator)
                after.append(operand)
            before = after
            after = []
        answer = max(answer, abs(int(before[0])))
        
    return answer