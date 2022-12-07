'''Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.'''

num = int(input('Digite um número: '))

if(num>=0 and num<=25):
    print('[0, 25]')
elif(num>=25 and num<=50):
    print('[25, 50]')
elif(num>=50 and num<=75):
    print('[50, 75]')
elif(num>=75 and num<=100):
    print('[75, 100]')
else:
    print('Fora do intervalo')