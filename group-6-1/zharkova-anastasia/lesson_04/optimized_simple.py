def optimized(i):          
    k = 0
    for y in range(2,int(i**1/2)+1): 
        if i % y == 0:               
            k += 1           
    if k == 0:              
        return 'Число ', x, ' является простым числом'
    else:                   
        return 'Введённое число не является простым'


x = int(input('Введите число для проверки: '))
print(*optimized(x), sep = '') 