x = 1234

if x <= 99:
    print("Błędna liczba")
else:
    cyfraJednosci = x % 10
    cyfraDziesiatek = (x // 10) % 10
    cyfraSetek = (x // 100) % 10
    print("Cyfra jedności:", cyfraJednosci, ", cyfra dziesiątek:", cyfraDziesiatek, "i cyfra setek:", cyfraSetek)