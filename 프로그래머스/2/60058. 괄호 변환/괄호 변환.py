def devide(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:i+1], w[i+1:]
            
def isCorrect(w):
    stack = []
    for word in w:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def Remake(w):
    # 1. 입력이 빈 문자열인 경우 빈 문자열 반환
    if w == '':
        return ''
    
    # 2. 문자열 w를 u, v로 분리 
    u, v = devide(w)
    
    # 3. u가 올바른 문자열이면 v에 대해서 진행
    if isCorrect(u):
        return u + Remake(v)
    
    # 4. u가 올바른 문자열이 아니라면
    else:
        correct = '(' + Remake(v) + ')'
        print(correct)
        for word in u[1:len(u)-1]:
            if word == '(':
                correct = correct + ')'
            else:
                correct = correct + '('
        return correct

def solution(p):
    answer = ''
    # 균형잡힌 괄호 문자열 : (랑 )의 갯수가 같을 경우
    # 올바른 괄호 문자열 : 짝도 모두 맞을 경우
    answer = Remake(p)
    return answer