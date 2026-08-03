metals={
    "Ag" : "Silver",
    "Al" : "Aluminum",
    "Au" : "Gold",
    "Cu" : "Copper",
}
print(metals["Ag"])
print()
i = metals.get("Au")
print(i)
metals[i] = "Rhodium"
print(metals)

