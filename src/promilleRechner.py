# calculations
def calcAlcMass(volume: float, alcoholPercentage: float, reductionFactor: float) -> float:
    return 10.0 * volume * alcoholPercentage * reductionFactor


def calcBloodAlc(massAlcohol: float, massPerson: float, reductionFactor: float) -> float:
    return massAlcohol / (massPerson * reductionFactor)


def getReductionFactor(sortPerson: str) -> float:
    if (sortPerson in ["j", "jugendlich"]):
        return 0.6
    elif (sortPerson in ["m", "männlich"]):
        return 0.7
    elif (sortPerson in ["w", "weiblich"]):
        return 0.6
    else:
        return float(sortPerson)


# inputs
volumeDrank = float(input("Wie viel wurde getrunken? (Liter)\n"))
alcoholPercentage = float(input("Wie viel Alkohol war enthalten? (%)\n"))
massPerson = float(input("Wie viel wiegt die Person? (kg)\n"))
sortPerson = input(
    "Ist die Person jugendlich (j), erwachsen und männlich (m) oder erwachsen und weiblich (w)? [eigene Reduktionsfaktoreingabe auch möglich]\n")

reductionFactor = getReductionFactor(sortPerson)
massAlcohol = calcAlcMass(volumeDrank, alcoholPercentage, reductionFactor)
bloodAlcohol = calcBloodAlc(massAlcohol, massPerson, reductionFactor)

# output
print(
    f"Die errechnete Blutalkoholkonzentration beträgt ungefähr {round(bloodAlcohol, 2)} Promille")
