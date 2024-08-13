#Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, 
# converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante para verificar 
# as frutas que foram armazenadas.

frutas = []

print('Digite o numero de 6 frutas:')
for i in range(6):
     i += 1     
     fruta = input(f'{i}° fruta: ')
     frutas.append(fruta)
    
frutas_tupla= tuple(frutas)
print(frutas_tupla)

    
    
    
    