def solution(n, m):
    n = int(n)
    m = int(m)
    dict = {}
    for i in range(n, m):
        z = list(bin(i))
        p = z[2:]    # Just to remove the characters till b coz they are uselesss
        if i == 0:  # did this for some reason that i might not remember then
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
