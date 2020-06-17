# INTEGRATION AND DIFFERENTIATION CALCULATOR
# AUTHOR: TEGID GOODMAN-JONES
# LAST EDITED: 17/06/20

def diff_a(a, b, c):
	new_a = a*2
	new_b = b*1
	res_equ = str(new_a) + 'x + ' + str(new_b)
	return res_equ

def diff_b(a, b, c, d):
	new_a = a*3
	new_b = b*2
	res_equ = str(new_a) + 'x^2 + ' + str(new_b) + 'x + ' + str(c) 
	return res_equ

def inte_a(a, b, c):
	new_a = a/3
	new_b = b/2
	res_equ = str(new_a) + 'x^3 + ' + str(new_b) +'x^2 + ' + str(c) + 'x + ' + 'C'
	return res_equ

def inte_b(a, b, c, d):
	new_a = a/4
	new_b = b/3
	new_c = c/2

	res_equ = str(new_a) + 'x^4 + ' + str(new_b) + 'x^3 + ' + str(new_c) + 'x^2 + ' + str(d) + 'x + ' + 'C' 
	return res_equ


print('Hello, this calculator will calculate the integral or diferential of an equation.\n\n')
calculation = input('Select what you would like to calculate:\nDifferentiation (a)\nIntegration (b)\n(a/b):  ')
if calculation is 'a':
	equation_s = input('Equation structure:\na:  ax^2 + bx + c \nb:  ax^3 + bx^2 + cx + d\n\n(a/b) : ')
	if equation_s is 'a':
		a = int(input('\na: '))
		b = int(input('b: '))
		c = int(input('c: '))
		print('\n' + diff_a(a, b, c))
	
	elif equation_s is 'b':
		a = int(input('\na: '))
		b = int(input('b: '))
		c = int(input('c: '))
		d = int(input('d: '))
		print('\n' + diff_b(a, b, c, d))

elif calculation is 'b':
	equation_s = input('Equation structure:\n[ax^2 + bx + c] (a)\n[ax^3 + bx^2 + cx + d] (b)\n(a/b) : ')
	if equation_s is 'a':
		a = int(input('\na: '))
		b = int(input('b: '))
		c = int(input('c: '))
		print('\n' + inte_a(a, b, c))
	elif equation_s is 'b':
		a = int(input('\na: '))
		b = int(input('b: '))
		c = int(input('c: '))
		d = int(input('d: '))
		print('\n' + inte_b(a, b, c, d))



	
