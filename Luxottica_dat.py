import pandas as pd

# Reads 15.Luxottica_prodmix.xlsx with pandas and writes the Pyomo data file Luxottica.dat
xls = "15.Luxottica_prodmix.xlsx"
t = pd.read_excel(xls, "time")              # Resource, Product, Variation, Time
p = pd.read_excel(xls, "Price")             # Product, Variation, Price
d = pd.read_excel(xls, "Demand")            # Product, Demand
v = pd.read_excel(xls, "MaxPercVar")        # Product, MaxPercVar
c = pd.read_excel(xls, "UnitCost")          # Resource, UnitCost
A = pd.read_excel(xls, "Availability")      # Resource, Availability

f = open("Luxottica.dat", "w")

# Sets
products = d.Product.unique()
variations = p.Variation.unique()
resources = c.Resource.unique()
# Subset of variations from "RB3603" to "PolarizedLenses" (used in the blending constraint)
start = list(variations).index("RB3603")
end = list(variations).index("PolarizedLenses")
premium = variations[start:end + 1]

f.write("set I := " + " ".join(products) + " ;\n\n")
f.write("set J := " + " ".join(variations) + " ;\n\n")
f.write("set K := " + " ".join(premium) + " ;\n\n")
f.write("set R := " + " ".join(resources) + " ;\n\n")

# Parameters
f.write("param p :=\n")
p.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n\n")

f.write("param d :=\n")
d.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n\n")

f.write("param t :=\n")
t.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n\n")

f.write("param v :=\n")
v.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n\n")

f.write("param c :=\n")
c.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n\n")

f.write("param A :=\n")
A.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
f.write(";\n")

f.close()
