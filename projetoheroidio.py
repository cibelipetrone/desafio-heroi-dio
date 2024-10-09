nome = input ("Digite o nome do herói: ")
xp = int(input("Digite o XP do herói: "))

while (xp < 1000 ):
        print ("XP insuficiente para classificação, continue jogando")
        xp = int(input("Digite o XP do herói: "))

if (xp <= 1000):
    nivel = "Ferro"
elif (xp >= 1001 and xp <= 2000):
    nivel = "Bronze"
elif (xp >= 2001 and xp <= 5000):   
    nivel = "Prata"    
elif (xp >= 5001 and xp <= 7000):
    nivel = "Ouro"
elif (xp >= 7001 and xp <= 8000):  
    nivel = "Platina"  
elif (xp >= 8001 and xp <= 9000): 
    nivel = "Ascendente"   
elif (xp >= 9001 and xp <= 10000): 
    nivel = "Imortal"   
elif (xp >= 10001):
    nivel = "Radiante"  

print ("Herói: " + nome)
print ("Nível do herói: " + nivel)