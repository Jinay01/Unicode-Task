def solution(n, m):
    n = int(n)
    m = int(m)
    dict = {}
    for i in range(n, m):
        z = list(bin(i))
        p = z[2:]
        if i == 0:
            dict[0] = 'false'
        elif i == 1:
            dict[1] = 'false'
        else:
            for a in range(0, len(p)-1):
                if p[a] == '1':
                    if p[a] == p[a+1]:
                        dict[i] = "true"
                        break
                    else:
                        dict[i] = 'false'
    return dict
