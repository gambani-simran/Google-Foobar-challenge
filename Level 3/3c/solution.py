def solution(n):
    res = 0
    num = int(n)
    
    while num > 1:
        if num & 1 == 1:
            #odd then add/subtract
            if num % 4 == 1 or num == 3:
                num = num - 1
            else:
                num = num + 1
        else:
            #even then divide by 2
            num = num >> 1
        res += 1
    return res

        


print(solution('4'))
# 2

print(solution('15'))
# 5

print(solution('16'))
# 4

print(solution('32'))
# 5

print(solution('33'))
# 6

print(solution('31'))
# 6

print(solution('124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399'))