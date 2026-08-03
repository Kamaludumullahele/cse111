def main():
    from pprint import pprint
    from formula import FormulaError, parse_formula
    

    periodic_table_dict = make_periodic_table()
    pprint(periodic_table_dict)
    # To check whether the periodic_table_dict is created correctly!
    # exceeded requirement: print the number of elements in the periodic table
    print("Number of elements:", len(periodic_table_dict))

    # Prompt until a non-empty, valid chemical formula is entered.
    while True:
        formula = input("Enter a valid chemical formula:(eg. H2O, C6H12O6, Ca(OH)2): ")
        if formula.strip() == "":
            continue
        try:
            symbol_quantity_list = parse_formula(formula, periodic_table_dict)
            #exceeded requirement:
            print(f"Parsed formula: {symbol_quantity_list}")
            periodic_table_dict = make_periodic_table()
            for symbol, quantity in symbol_quantity_list:
                number_of_protons = periodic_table_dict[symbol][1]
            print(f"Number of protons in {formula}: {round(number_of_protons)}")
        
            break
        except FormulaError:
            print("Error: Enter a valid chemical formula. eg. H2O, C6H12O6, Ca(OH)2")
            continue

        



    # Prompt until a valid quantity is entered.
    while True:
        try:
            quantity = float(input("Enter the quantity of the compound in grams: "))
            break
        except ValueError:
            print("Please enter a number.")

    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    #total_mass = molar_mass * quantity
    print(f"Molar mass of {formula}: {molar_mass:.5f} g/mol")
    print(f"Number of moles: {quantity / molar_mass:.5f}")


raw_text = """
Symbol	Name	Atomic Mass
Ac,	Actinium,	227
Ag,	Silver,	107.8682
Al,	Aluminum,	26.9815386
Ar,	Argon,	39.948
As,	Arsenic,	74.9216
At,	Astatine,	210
Au,	Gold,	196.966569
B,	Boron,	10.811
Ba,	Barium,	137.327
Be,	Beryllium,	9.012182
Bi,	Bismuth,	208.9804
Br,	Bromine,	79.904
C,	Carbon,	12.0107
Ca,	Calcium,	40.078
Cd,	Cadmium,	112.411
Ce,	Cerium,	140.116
Cl,	Chlorine,	35.453
Co,	Cobalt,	58.933195
Cr,	Chromium,	51.9961
Cs,	Cesium,	132.9054519
Cu,	Copper,	63.546
Dy,	Dysprosium,	162.5
Er,	Erbium,	167.259
Eu,	Europium,	151.964
F,	Fluorine,	18.9984032
Fe,	Iron,	55.845
Fr,	Francium,	223
Ga,	Gallium,	69.723
Gd,	Gadolinium,	157.25
Ge,	Germanium,	72.64
H,	Hydrogen,	1.00794
He,	Helium,	4.002602
Hf,	Hafnium,	178.49
Hg,	Mercury,	200.59
Ho,	Holmium,	164.93032
I,	Iodine,	126.90447
In,	Indium,	114.818
Ir,	Iridium,	192.217
K,	Potassium,	39.0983
Kr,	Krypton,	83.798
La,	Lanthanum,	138.90547
Li,	Lithium,	6.941
Lu,	Lutetium,	174.9668
Mg,	Magnesium,	24.305
Mn,	Manganese,	54.938045
Mo,	Molybdenum,	95.96
N,	Nitrogen,	14.0067
Na,	Sodium,	22.98976928
Nb,	Niobium,	92.90638
Nd,	Neodymium,	144.242
Ne,	Neon,	20.1797
Ni,	Nickel,	58.6934
Np,	Neptunium,	237
O,	Oxygen,	15.9994
Os,	Osmium,	190.23
P,	Phosphorus,	30.973762
Pa,	Protactinium,	231.03588
Pb,	Lead,	207.2
Pd,	Palladium,	106.42
Pm,	Promethium,	145
Po,	Polonium,	209
Pr,	Praseodymium,	140.90765
Pt,	Platinum,	195.084
Pu,	Plutonium,	244
Ra,	Radium,	226
Rb,	Rubidium,	85.4678
Re,	Rhenium,	186.207
Rh,	Rhodium,	102.9055
Rn,	Radon,	222
Ru,	Ruthenium,	101.07
S,	Sulfur,	32.065
Sb,	Antimony,	121.76
Sc,	Scandium,	44.955912
Se,	Selenium,	78.96
Si,	Silicon,	28.0855
Sm,	Samarium,	150.36
Sn,	Tin,	118.71
Sr,	Strontium,	87.62
Ta,	Tantalum,	180.94788
Tb,	Terbium,	158.92535
Tc,	Technetium,	98
Te,	Tellurium,	127.6
Th,	Thorium,	232.03806
Ti,	Titanium,	47.867
Tl,	Thallium,	204.3833
Tm,	Thulium,	168.93421
U,	Uranium,	238.02891
V,	Vanadium,	50.9415
W,	Tungsten,	183.84
Xe,	Xenon,	131.293
Y,	Yttrium,	88.90585
Yb,	Ytterbium,	173.054
Zn,	Zinc,	65.38
Zr,	Zirconium,	91.224
"""

def make_periodic_table():
    """
    Returns a dictionary of the periodic table of elements.
    The keys are the element symbols, and the values are lists containing the element name and atomic mass.
    """
    periodic_table_dict = {}
    # Split the raw text into lines and process each line
    for line in raw_text.splitlines():
        # Strip whitespace from the line
        line = line.strip()
        # Split the line into parts by cutting at tabs
        parts = line.split("\t")
        if len(parts) < 3:
            continue  # Skip lines that don't have enough parts
        # Unpack the parts into symbol, name, and mass, stripping whitespace and commas
        symbol, name, mass = [x.strip().rstrip(",") for x in parts if x.strip()]

        # Skip header row
        if symbol == "Symbol":
            continue
        # Add the element to the dictionary

        periodic_table_dict[symbol] = [name, float(mass)]

    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0
    for item in symbol_quantity_list:
        symbol = item[0]
        quantity = item[1]
        if symbol in periodic_table_dict:
            atomic_mass = periodic_table_dict[symbol][1]
            total_mass += atomic_mass * quantity # abstracted from provided equation in the project description
        else:
            raise ValueError(f"Symbol '{symbol}' not found in periodic table.")

    return total_mass

if __name__ == "__main__":
  main()