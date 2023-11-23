# help(print)

first_name = 'Pero'
last_name = 'Peric'
phone = '+385 9_ 1234 567'
end_value = ' '

#print()
#print(first_name, end=' ') # end=' ' označava da ne ide u novi red nego stavi samo razmak
#print(first_name, last_name, phone)
#print(first_name, last_name, phone, sep=' ') - ako nema sep podrazumijeva se da je razmak

#print(first_name, last_name, phone, sep=', ')

print(first_name, end=' ')
print(last_name, phone, sep=', ', end='\n')

print(first_name, end = end_value)
print(last_name, phone, sep=', ', end=end_value)
