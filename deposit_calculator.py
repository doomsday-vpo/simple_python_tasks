deposit = float(input())
period = int(input())
percentage = float(input()) / 100

#yearly = (deposit * percentage)/12
#additional_period = period * yearly
#money_in_bank = deposit + additional_period

money_in_the_bank = deposit + period * (( deposit * percentage/12))

print(money_in_the_bank)


