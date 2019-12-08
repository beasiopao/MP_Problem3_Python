import sys as s
import numpy as np
import ast as a

#Input of experimental points [xi,yi]
exp_pts = input('Enter a set of arrays: ') #NOTE: Example format of input array [0,1],[2,3],...,[h,k]
arr = np.asarray(a.literal_eval(exp_pts))
sa = len(arr)
X = arr[0:sa,0]; Y = arr[0:sa,1]; pts=[];

def polynomials_coeff():
    for z in range(1,sa):
        if z>10:
            print('-------------------')
            print('The program can only accept polynomials from the 1st degree up to the 10th degree. Try Again!')
            s.exit()
        elif z<=10:
            for w in range(1,sa):
                pf = np.polyfit(X,Y,w)
                e = Y - np.polyval(pf,X)
                normalize = np.linalg.norm(e)
                pts.append(normalize)
                
                l_norm = min(pts)
                i = pts.index(l_norm)
                BFL = np.polyfit(X,Y,i)

    #Outputs
    print('-------------------')
    print('Coefficients of the polynomial that would best apprximate the data: ',BFL)

polynomials_coeff()
    