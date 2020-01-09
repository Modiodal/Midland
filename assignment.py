import statistics as st
import numpy as np
from scipy.stats import t

mul_R = np.sqrt(.9445)
print('Multiple R is equal to: ' + str(mul_R))
R_sqr = .9445
#r square = ssr / sst
#sse = ssr + sse

#observations = n
#independent variables = p
n = 10
p = 1
df_sse = n - p -1
print('SSE DF is equal to: ' + str(df_sse))

df_sst = n - 1
print('SST DF is equal to: ' + str(df_sst))

#ssr = (Anova) Regression SS
ssr = 5027.26
sst = ssr / R_sqr
print('The SST is equal to: ' + str(sst))

sse = sst - ssr
print('The SSE is equal to: ' + str(sse))

#std_err_of_est_p1 also = 'nse'
std_err_of_est_p1 = sse / df_sse
std_err_of_est_p2 = np.sqrt(std_err_of_est_p1)
print('The Standard Error is equal to: ' + str(std_err_of_est_p2))

#part 2
msr = ssr / p
print('\nMSR is equal to: ' + str(msr))
mse = sse / df_sse
print('MSE is equal to: ' + str(mse))
F = msr / mse
print('F is equal to: ' + str(F))

#part 3, intercept = b(0), hours = b(1)
sb1 = .088
t = 11.671
b1 = sb1 * t
print('Coefficient of b1: ' + str(b1))

###########################################
###########################################
"""
Assignment Part 2 (should b)
"""
#USE THE T TEST TO TEST THE FOLLOWING HYPOTHESES (ALPHA = .05)
#below gives us the T stat for 'hours'
b1_1 = 1.06
sb1_1 = .11
t2 = b1_1 / sb1_1
print('\n \n \nT stat of hours: ' + str(t2))
alpha = 0.05
df_alpha = alpha / 2
#df = n - p -1
df = 8
#search t-table for .025 and 8 deg of freedom = (2.306)
crit_val = 2.306
if abs(t2) > abs(crit_val):
    print('Reject Hull Hypothesis')
else:
    print('DO NOT Reject Null Hypothesis')

#USE THE F TEST TO TEST THE FOLLOWING HYPOTHESES (ALPHA = .05)
#pt 2 of assignment 2
mul_R_1 = .9573
R_sqr_1 = round(mul_R_1 ** 2, 4)
ssr_1 = 5363
sst_1 = ssr_1 / R_sqr_1
print('\nThe SST is equal to: ' + str(sst_1))
sse_1 = sst_1 - ssr_1
print('The SSE is equal to: ' + str(sse_1))
#df = (Anova Residual (df))
df_sse_1 = 8
mse_1 = sse_1 / df_sse_1
print('The MSE is equal to: ' + str(mse_1))
F_1 = ssr_1 / mse_1
print('F is equal to: ' + str(F_1))
#search f-table for .05 and 1 deg of freedom numerator, 8 deg of freedom denominator = (5.32)
#FOR F TEST WE DO NOT DIVIDE ALPHA BY 2
crit_val_1 = 5.32
if abs(F_1) > abs(crit_val_1):
    print('Reject Hull Hypothesis')
else:
    print('DO NOT Reject Null Hypothesis')
#pt 3 of assignment 2
#ex. -7.56 + 1.06(100) = 98.44
#bo_1 = coefficient 'Intercept' = b0-1, coefficient 'Hours' = b1_2
b0_1 = -7.56
b1_2 = 1.06
hours_1 = 100
tot_points = b0_1 + b1_2 * hours_1
print('The total points earned by a student that spent ' + str(hours_1) + ' studying is: ' + str(tot_points))