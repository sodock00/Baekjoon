def solution(array, commands):
    answer = []
    print(array)
    for i in range(len(commands)):
        i, j, k = commands[i]
        print(i,j,k)
        crop_array = array[i-1:j]
        crop_array.sort()
        answer.append(crop_array[k-1])
    return answer