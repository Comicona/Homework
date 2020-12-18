h = input('Please, enter your height in meters:')
m = input('Please, enter your mass in kilograms:')

I = float(m) / float(h)**2

print('Your IBM is ' + str(int(I))
     + '\n20' + '='*(int(I)-20) + '|' + '='*(50-int(I)) + '50')
