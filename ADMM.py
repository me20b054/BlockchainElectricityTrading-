B11 = 0.0003
B12 = B21 = 0.0004
B13 = B31 = 0.0005
B22 = 0.0008
B23 = B32 = 0.0009
B33 = 0.01

B = [[B11, B12, B13], [B21, B22, B33], [B31, B32, B33]]

# line limits
f12_max = 100
f21_max = -f12_max
f13_max = 100
f31_max = -f13_max
f23_max = 100
f32_max = -f23_max

# Algorithm parameters
tol_lambda = 0.1
tol_z = 0.1
rho = 0.14

# line reactances
x12, x13, x23 = 0.05, 0.05, 0.05

# Max and min limits of generation and load
# pg1_min, pg2_min, pg3_min = 100, 100, 100
# pg1_max, pg2_max, pg3_max = 500, 500, 500

# pd1_min, pd2_min, pd3_min = 100, 100, 100
# pd1_max, pd2_max, pd3_max = 500, 500, 500

# constants for node1
a1, b1, c1 = 1, 2, 3
d1, e1, f1 = 4, 5, 6

iter = 0
maxiter = 100 
pg = [-b1 / (2 * a1) ,-b2 / (2 * a2) ,-b3 / (2 * a3) ] 
pd = [ -e1 / (2 * d1),-e2 / (2 * d2) , -e3 / (2 * d3)]
pg_max,pg_min = [500,500,500],[100,100,100]
pd_max,pd_min = [500,500,500],[100,100,100] 

# local variables for node1
# pg1 = -b1 / (2 * a1)
# pd1 = -e1 / (2 * d1)
# theta_1 = 7

for i in range(len(pg_max)):
    if pg[i] > pg_max[i]:
        pg[i] = pg_max[i] 
    elif pg[i] < pg_min[i]:
        pg[i ]= pg_min[i] 
    else:
        pg[i] 

for i in range(len(pd_max)): 
    if pd[i] > pd_max[i]:
        pd[i] = pd_max[i] 
    elif pd1 < pd1_min:
        pd[i] = pd_min[i] 
    else:
        pd[i]

# coupling varaibles for node1
theta2_1, theta3_1 = 10, 11

# constants for node2
a2, b2, c2 = 1, 2, 3
d2, e2, f2 = 4, 5, 6

# local variables for node2
pg2, pd2, theta_2 = -b2 / (2 * a2), -e2 / (2 * d2), 7

# coupling varaibles for node2
theta1_2, theta3_2 = 10, 11

# constants for node1
a3, b3, c3 = 1, 2, 3
d3, e3, f3 = 4, 5, 6
# local variables for node1
pg3, pd3, theta_3 = -b3 / (2 * a3), -e3 / (2 * d3), 7

# coupling varaibles for node3
theta1_3, theta2_3 = 10, 11

lamda_1, lamda_2, lamda_3 = 0, 0, 0
z1, z2, z3 = 0, 0, 0



f1 = (
    (a1 * (pg1**2) + b1 * (pg1**2) + c1)
    - (d1 * (pd1**2) + e1 * pd1 + f1)
    + lamda_1 * (theta_1 - z1)
    + lamda_2 * (theta2_1 - z2)
    + lamda_3 * (theta3_1 - z3)
    + 0.5
    * rho
    * (
        (lamda_1 * (theta_1 - z1)) ** 2
        + (lamda_2 * (theta2_1 - z2)) ** 2
        + (lamda_3 * (theta3_1 - z3)) ** 2
    )
)

f2 = (
    (a2 * (pg2**2) + b2 * (pg2**2) + c2)
    - (d2 * (pd2**2) + e2 * pd2 + f2)
    + lamda_1 * (theta1_2 - z1)
    + lamda_2 * (theta_2 - z2)
    + lamda_3 * (theta3_2 - z3)
    + 0.5
    * rho
    * (
        (lamda_1 * (theta1_2 - z1)) ** 2
        + (lamda_2 * (theta_2 - z2)) ** 2
        + (lamda_3 * (theta3_2 - z3)) ** 2
    )
)

f2 = (
    (a3 * (pg3**2) + b3 * (pg3**2) + c3)
    - (d3 * (pd3**2) + e3 * pd3 + f3)
    + lamda_1 * (theta1_3 - z1)
    + lamda_2 * (theta2_3 - z2)
    + lamda_3 * (theta_3 - z3)
    + 0.5
    * rho
    * (
        (lamda_1 * (theta1_3 - z1)) ** 2
        + (lamda_2 * (theta2_3 - z2)) ** 2
        + (lamda_3 * (theta_3 - z3)) ** 2
    )
)

while (tol_lambda > 0.000001 & tol_z > 0.00001 & iter < maxiter):
    # updating local and global variables for node1
    theta_1 =  z1 - (1 / (rho * lambda_1))
    theta2_1, theta3_1 = z2 - (1 / (rho * lambda_2)), z3 - (1 / (rho * lambda_3))
    z1 = (theta_1 + theta1_2 + theta1_3) / 3 
    lambda_1 = lambda_1 + rho * (theta_1 - z1)
    # updating local and global variables for node2
    pg2, pd2, theta2 = -b2 / (2 * a2), -e2 / (2 * d2), z2 - (1 / (rho * lambda_2))
    theta1_2, theta3_2 = z1 - (1 / (rho * lambda_1)), z3 - (1 / (rho * lambda_3))
    z2 = (theta_2 + theta2_1 + theta2_3) / 3
    lambda_2 = lambda_2 + rho * (theta_2 - z2)
    # updating local and global variables for node3
    pg3, pd3, theta3 = -b3 / (2 * a3), -e3 / (2 * d3), z3 - (1 / (rho * lambda_3))
    theta1_3, theta2_3 = z1 - (1 / (rho * lambda_1)), z2 - (1 / (rho * lambda_2))
    z3 = (theta_3 + theta3_1 + theta3_2) / 3
    lambda_3 = lambda_3 + rho * (theta_3 - z3)
    # constraints
    (theta_1 - theta2_1) / x12 <= f12_max
    (theta_1 - theta3_1) / x13 <= f13_max
    (theta_2 - theta1_2) / x12 <= f21_max
    (theta_2 - theta3_2) / x23 <= f23_max
    (theta_3 - theta1_3) / x13 <= f31_max
    (theta_3 - theta2_3) / x23 <= f32_max 
