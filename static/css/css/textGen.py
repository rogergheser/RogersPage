n = 50
alpha = 217
beta = 127
gamma = 336
for i in range(n):
    print(f'{round(i*100/n)}% {{\n\tbackground: linear-gradient({alpha}deg, rgba(255,0,0,.8), rgba(255,0,0,0) 70.71%), ')
    print(f'\t\tlinear-gradient({beta}deg, rgba(0,255,0,.8), rgba(0,255,0,0) 70.71%), ')
    print(f'\t\tlinear-gradient({gamma}deg, rgba(0,0,255,.8), rgba(0,0,255,0) 70.71%);\n}}')
    alpha = (alpha + round(360/n)) % 360
    beta = (beta + round(360/n)) % 360
    gamma = (gamma + round(360/n)) % 360

