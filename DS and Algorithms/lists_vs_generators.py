rangeLimit = 1_000_000_0

listOfNumbers = [num*num for num in range(rangeLimit)]

print(f"SIZE OF LIST:{listOfNumbers.__sizeof__()}")


listOfNumbersByGenerators = (num*num for num in range(rangeLimit))

print(f"SIZE OF LIST:{listOfNumbersByGenerators.__sizeof__()}")
