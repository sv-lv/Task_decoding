'''(Собеседование Amazon)
Кодирование длин серий - это быстрый и простой метод кодирования строк.
Основная идея состоит в том, чтобы представить повторяющиеся
последовательные символы как один счетчик и символ. Например,
строка «AAAABBBCCDAA» будет закодирована как «4A3B2C1D2A».

Реализуйте кодирование и декодирование длин серий.
Вы можете предположить, что кодируемая строка не содержит цифр
и состоит исключительно из буквенных символов. Вы можете предположить,
что декодируемая строка действительна.'''

code = input('Введите строку для кодирования: ')
lit_list = list(code)
num_list = [] #создание нового списка из количества повторяющихся символов
su = 1 #подсчет
for i in range(len(code)):
    if i == 0: num_list.append(su)
    elif code[i] == code[i-1]:
        su += 1
        num_list.append(su)
        lit_list[i-1] = 'ъъ'
    else:
        su = 1
        num_list.append(su)
print(num_list)
print(lit_list)

new = []
for j in range(len(lit_list)):
    new.append(num_list[j])
    new.append(lit_list[j])
print(new)

for k in range(len(new)):
    if new[k] == 'ъъ':
        new[(k-1)] = 'ъъ'

n_new=[]
for d in new:
    d = str(d)
    n_new.append(d)

nn=''.join(n_new) #преобразование списка в строку


print(nn.replace('ъъ',''))