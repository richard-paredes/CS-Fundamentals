nvar = 0
def problem_a(find_single_sol):
    global nvar
    nvar = 0
    found = False
    solutions = []

    # brute force
    # for a in range(1,51):
    #     for b in range(1, 51):
    #         for c in range(1, 51):
    #             for d in range(1, 51):
    #                 for e in range(1, 51):
    #                         for f in range(1, 51):
    #                             if (a == b+c+e+f) and (d == e+f+21) and (d**2 == e*e*a + 417) and (e + f < a):
    #                                 return [[a,b,c,d,e,f]]

    for d in range(23, 51):
        nvar += 1
        for e in range(1, 50):
            nvar += 1
            f = d - e - 21
            nvar += 1
            if (f > 0):
                for a in range(e+f, 51):
                    nvar += 1
                    if (d**2 == e*e*a + 417):
                        for b in range(1, a):
                            nvar += 1
                            c = a-b-e-f
                            nvar += 1
                            if (c > 0):
                                if not found and find_single_sol:
                                    found = True
                                    return [[a,b,c,d,e,f]]
                                solutions.append([a,b,c,d,e,f])

    # print(nvar, ":", len(solutions))
    return solutions

def problem_b(find_single_sol):
    global nvar
    nvar = 0
    found = False
    solutions = []
    prev_solutions = problem_a(False)

    for sol in (prev_solutions):
        a = sol[0]
        b = sol[1]
        c = sol[2]
        d = sol[3]
        e = sol[4]
        f = sol[5]

        # brute force
        # for g in range(1, 51):
        #     for h in range(1, 51):
        #         for i in range(1, 51):
        #             for j in range(1, 51):
        #                 if (h*j+e*12 == (g+i)**2) and (a+d == (f-g)**2 - 1) and (4*j == g**2 + 39) and ((i-g)**8 == (f-h)**3) and ((g-c)**2 == f*c*c + 1):
        #                     return [[a,b,c,d,e,f,g,h,i,j]]

        g = int((f*c*c + 1)**(1/2) + c)
        if ((g-c)**2 == f*c*c + 1) and (a+d == (f-g)**2 - 1):
            for j in range(1, 51):
                nvar += 1
                if (4*j == g**2 + 39):
                    for i in range(1, 51):
                        nvar += 1
                        h = int(((g+i)**2 - e*12) / j)
                        nvar += 1
                        if (i-g)**9 == (f-h)**3 and h*j+e*12 == (g+i)**2 and h > 0 and h < 51:
                            if not found and find_single_sol:
                                found = True
                                return [[a,b,c,d,e,f,g,h,i,j]]
                            solutions.append([a,b,c,d,e,f,g,h,i,j])
    
    # print(nvar, ":", len(solutions))
    return solutions

def problem_c(find_single_sol):
    global nvar
    nvar = 0
    found = False
    solutions = []
    prev_solutions = problem_b(False)

    for sol in prev_solutions:
        a = sol[0]
        b = sol[1]
        c = sol[2]
        d = sol[3]
        e = sol[4]
        f = sol[5]
        g = sol[6]
        h = sol[7]
        i = sol[8]
        j = sol[9]

        # brute force
        # for k in range(1, 51):
        #     for l in range(1, 51):
        #         for m in range(1, 51):
        #             for n in range(1, 51):
        #                 for o in range(1, 51):
        #                     if (2*m == k**2 - 6) and ((n-o)**3 + 7 == (f-i)*n) and (n**2 == m**2 + 291) and (o**2 == g*h*i*b + 133) and (m+o == k**2 - 10) and (l**3 + i == (l+b)*k):
        #                         return [[a,b,c,d,e,f,g,h,j,k,l,m,n,o]]

        o = int((g*h*i*b + 133)**(1/2))
        if (o**2 == g*h*i*b + 133):
            for n in range(1, 51):
                nvar += 1
                if (n-o)**3 + 7 == (f-i)*n:
                    m = (n**2 - 291)**(1/2)
                    nvar += 1
                    if (m.is_integer() and n**2 == m**2 + 291 and m > 0 and m < 51):
                        m = int(m)
                        k = (m + o + 10)**(1/2)
                        nvar += 1
                        if (k.is_integer() and m + o == k**2 - 10 and 2*m == k**2 - 6 and k > 0 and k < 51):
                            k = int(k)
                            for l in range(1, 51):
                                nvar += 1
                                if l**3 + i == (l+b)*k:
                                    # print(nvar, ":", len(solutions))
                                    if not found and find_single_sol:
                                        found = True
                                        return [[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]]
                                    solutions.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]) # keep return type consistent with other functions


def is_solution(problem, sol):    
    if not sol:
        print(f"No solution found for Problem {problem} after {nvar} variable assignments")
        return False

    variables = "ABCDEFGHIJKLMNO"
    a = sol[0]
    b = sol[1]
    c = sol[2]
    d = sol[3]
    e = sol[4]
    f = sol[5]
    
    if not (a == b+c+e+f):
        print("Failed C1")
        return False
    if not (d == e + f + 21):
        print("Failed C2")
        return False
    if not (d**2 == e*e*a + 417):
        print("Failed C3")
        return False
    if not (e + f < a):
        print("Failed C4")
        return False

    if problem == "A":
        solution = [f"{variables[i]}: {sol[i]}" for i in range(len(sol[:6]))]
        print(f"Solution for Problem {problem} after {nvar} variable assignments: \n{solution}\n")
        return True

    g = sol[6]
    h = sol[7]
    i = sol[8]
    j = sol[9]

    if not (h*j + e*12 == (g+i)**2):
        print("Failed C5")
        return False
    if not (a + d == (f-g)**2 - 1):
        print("Failed C6")
        return False
    if not (4*j == g**2 + 39):
        print("Failed C7")
        return False
    if not ((i-g)**9 == (f-h)**3):
        # print((i-g)**9, (f-h)**3)
        print("Failed C8")
        return False
    if not ((g-c)**2 == f*c*c + 1):
        print("Failed C9")
        return False

    if problem == "B":
        solution = [f"{variables[i]}: {sol[i]}" for i in range(len(sol[:10]))]
        print(f"Solution for Problem {problem} after {nvar} variable assignments: \n{solution}\n")
        return True

    k = sol[10]
    l = sol[11]
    m = sol[12]
    n = sol[13]
    o = sol[14]

    if not (2*m == k**2 - 6):
        print("Failed C10")
        return False
    if not ((n-o)**3 + 7 == (f-i)*n):
        print("Failed C11")
        return False
    if not (n**2 == m**2 + 291):
        print("Failed C12")
        return False
    if not (o**2 == g*h*i*b + 133):
        print("Failed C13")
        return False
    if not (m+o == k**2 - 10):
        print("Failed C14")
        return False
    if not (l**3 + i == (l+b)*k):
        print("Failed C15")
        return False

    if problem == "C":
        solution = [f"{variables[i]}: {sol[i]}" for i in range(len(sol[:15]))]
        print(f"Solution for Problem {problem} after {nvar} variable assignments: \n{solution}\n")
        return True

def main():
    try:
        # print(is_solution("C", [31,1,2,49,8,20,11,12,13,40,10,3,47,50,43]))
        print(is_solution("C", [28, 1, 1, 47, 8, 18, 11, 12, 13, 40, 10, 3, 47, 50, 43]))
        # print("Program Options Available:\n"\
        #     "A : Solve problem A\n"\
        #     "B : Solve problem B\n"\
        #     "C : Solve problem C\n"\
        #     "* : Solve all problems")
        # problem_to_solve = input("Please enter which Problem to solve (A, B, C, *): ")
        # print()
        
        # if problem_to_solve.upper().startswith("A"):
        #     a_solutions = problem_a(True)
        #     is_solution("A", a_solutions[0] if a_solutions else None)
        # elif problem_to_solve.upper().startswith("B"):
        #     b_solutions = problem_b(True)
        #     is_solution("B", b_solutions[0] if b_solutions else None)
        # elif problem_to_solve.upper().startswith("C"):
        #     c_solutions = problem_c(True)
        #     is_solution("C", c_solutions[0] if c_solutions else None)
        # elif problem_to_solve.upper().startswith("*"):
        #     a_solutions = problem_a(True)
        #     is_solution("A", a_solutions[0] if a_solutions else None)
        #     b_solutions = problem_b(True)
        #     is_solution("B", b_solutions[0] if b_solutions else None)
        #     c_solutions = problem_c(True)
        #     is_solution("C", c_solutions[0] if c_solutions else None)
        # else:
        #     print("Invalid request")
    except:
        print("Invalid operation")

main()