equation1 = 'y^2-12y+20=0'
equation2 = 'z^2+17z+72=0'
equation3 = 'x^2-7x-44=0'
equation4 = 'y^2+9y+8=0'
equation5 = 'b^2-2b-63=0'

def solve_equation(a=1,b=0,c=0)->str:
    d=b**2-(4*a*c)
    if d<0:
        return 'Нет корней'
    elif d==0:
        return f'{-b/(2*a)}'
    elif d>0:
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d**0.5)/(2*a)
        return f'{x1},{x2}'

print(solve_equation(b=int(equation1[3:6]),c=int(equation1[7:10])))
print(solve_equation(b=int(equation2[3:6]),c=int(equation2[7:10])))
print(solve_equation(b=int(equation3[3:5]),c=int(equation3[6:9])))
print(solve_equation(b=int(equation4[3:5]),c=int(equation4[6:8])))
print(solve_equation(b=int(equation5[3:5]),c=int(equation5[6:9])))