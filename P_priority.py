PRO = [("p1", 0, 4, 2), 
             ("p2", 1, 2, 4), 
             ("p3", 2, 3, 6), 
             ("p4", 3, 5, 10), 
             ("p5", 4, 1, 8),
             ("p6", 5, 4, 12),
             ("p7", 6, 6, 9)]
PRO.sort(key=lambda x: x[1])

#Q-no. of process

Q = len(PRO)
Comp_Time = [0] * Q
Turn_Arr_time= [0] * Q
Wait_Time = [0]*Q
Res_Time = [0] * Q
Initally_time = [-1] * Q

R_B_T = [PRO[i][2] for i in range(Q)]
Prior = [PRO[i][3] for i in range(Q)]
C_Time = 0
S = []

while len(S) < Q:
    higher = -1
    lower = float('inf')
    SELected = -1
    for i in range(Q):
        if R_B_T[i] > 0 and PRO[i][1] <= C_Time:
            if Prior[i] > higher:
                higher = Prior[i]
                SELected = i
            elif Prior[i] == higher and R_B_T[i] < lower:
                lower = R_B_T[i]
                SELected = i

    if SELected == -1:
        C_Time += 1
    else:
        if Initally_time[SELected] == -1:
            Initally_time[SELected] = C_Time
        R_B_T[SELected] -= 1
        C_Time += 1
        if R_B_T[SELected] == 0:
            Comp_Time[SELected] = C_Time
            S.append(PRO[SELected])
        else:
            # Updation of priority
            Prior[SELected] += 1

# CAlculate
for i in range(Q):
    Turn_Arr_time[i] = Comp_Time[i] - PRO[i][1]
    Wait_Time[i] = Turn_Arr_time[i] - PRO[i][2]
    Res_Time[i] = Initally_time[i] - PRO[i][1]

# REsult
print("P_id\tArr_T\tBur_T\tPRIority\tComp_T\tTurn_AT\tWait_T\tResp_T")
T_Turn_Arr_time = 0
T_Wait_Time = 0
T_Res_Time = 0
for i in range(Q):
    print(f"{PRO[i][0]}\t{PRO[i][1]}\t{PRO[i][2]}\t{PRO[i][3]}\t\t{Comp_Time[i]}\t{Turn_Arr_time[i]}\t{Wait_Time[i]}\t{Res_Time[i]}")
    T_Turn_Arr_time += Turn_Arr_time[i]
    T_Wait_Time += Wait_Time[i]
    T_Res_Time += Res_Time[i]

# AVerage
A_Turn_Arr_time = T_Turn_Arr_time / Q
A_Wait_Time = T_Wait_Time / Q
A_Res_Time = T_Res_Time / Q

print("\n Calculating Average")
print(f"\n ATAT: {A_Turn_Arr_time:.1f}")
print(f"AWT: {A_Wait_Time:.1f}")
print(f"ART: {A_Res_Time:.1f}")
