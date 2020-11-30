t = str(input('skriv en text ')) #användaren skriver en text
print(len(t)) # koden räknar ut hur många tecken
print(f'det första tecknet är {t[0]}') # skriver ut vad det första tecknet är, den börjar alltid 1 till höger så därför skrev jag 0 så programmet ser 1
h = len(t) # sätter ett värde på h som är samma sak som hur många tecken
h = h -1 # drar bort 1 från det
print(f'det sista tecknet är {t[h]}') # skriver in vad det sista tecknet är
if t[0]==t[h]: # om båda är exact samma så blir programmet lycklig
    print('båda har samma tecken')
elif t[0] != t[h]: # om båda inte är exact samma så blir programmet olyckligt
    print('båda har inte samma tecken')