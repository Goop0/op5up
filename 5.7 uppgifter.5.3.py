import datetime, time
persnum = input(str('skriv ett personnummer (yyyymmddxxxx):'))

print(f"Det sista tecknet är {persnum[10]}")

print('du är en man om talet är jämnt')
print('du är en kvinna om talet är ojämnt')
#programmet läser inte if, bara else så jag lämnar det här för nu.