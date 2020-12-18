h = input('Please, enter your height in meters:')
m = input('Please, enter your mass in kilograms:')

I = float(m) / float(h)**2

if (int(I)>=15 and int(I)<=50):
    print('Your IBM is ' + str(int(I))
     + '\n15' + '='*(int(I)-15) + '|' + '='*(50-int(I)) + '50')
else:
    print('Your IBM is ' + str(int(I))
    +'\nSorry, your IBM seems to be incorrect or out of range')
