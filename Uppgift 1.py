# Ta emot input från användaren (pris exklusive moms)
pris_exkl_moms = float(input("Ange pris exklusive moms: "))

# Beräkna pris inklusive 25% moms
pris_inkl_moms = pris_exkl_moms * 1.25

# Skriv ut resultatet (pris inklusive moms)
print(f"Pris inklusive 25% moms: {pris_inkl_moms:.1f}")
