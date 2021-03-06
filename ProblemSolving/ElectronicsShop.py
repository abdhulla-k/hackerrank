def getMoneySpent(keyboards, drives, b):
    k = [0]
    for i in keyboards:
        for j in drives:
            if i+j <= b: k.append(i+j)
    if max(k) > 0:
        return max(k)
    if max(k) == 0:
        return -1

def second(keyboards, drives, b):
    result = -1
    for i in keyboards:
        for j in drives:
            if i+j <= b:
                result = max(result, i+j)
    return result

if __name__ == '__main__':
    b = 10
    keyboards = [3, 1]
    drives = [5, 2, 8]
    print(getMoneySpent(keyboards, drives, b))
    print(second(keyboards, drives, b))