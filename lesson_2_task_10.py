
def bank():
    import math
    debit = math.ceil(float(input('Введите размер вклада:')))
    time = int(input('Введите срок вклада:'))
    bet = math.ceil(float(input('Введите процент по вкладу:')))
    for n in range(time+1):
        n = n + 1
        if n > time:
            print ('Размер вклада через', time, 'лет:',debit)
        else: 
            debit = debit + debit*bet*0.01
bank()