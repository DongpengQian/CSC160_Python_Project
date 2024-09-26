def computepay (hours, rate):

   if 0 < hours <= 40 and rate > 0: 
      pay = hours * rate
      return pay
   elif hours >= 40 and rate > 0:
      pay = 40 * rate + (hours - 40) * rate * 1.5
      return pay
   else: 
      return ('Not valid, enter a different number.')

hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
print('Pay:', computepay(hours, rate))