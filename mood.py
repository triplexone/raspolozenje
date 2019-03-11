ime = input("Kako se zoveš? ")
raspolozenje = input ("Pozdrav "+ime+", kako si? ").lower ()

if raspolozenje == "dobro":
    print ("Baš mi je drago da si dobro!")
elif raspolozenje == "pospano":
    print ("A takvo je vrijeme")
elif raspolozenje == "nervozno":
    print ("Opusti se i uživaj")
elif raspolozenje == "tužan":
    print("Razvedri se")
elif raspolozenje == "sretan":
    print("Lupi dlanom ti o dlan")
elif raspolozenje == "bolesno":
    print("Tablete će ti pomoći")
else:
    print ("Ne znam što bih ti rekao")