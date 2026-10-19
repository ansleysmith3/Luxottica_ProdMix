import pandas as pd

xls = "15.Luxottica_prodmix.xlsx"
t = pd.read_excel(xls, "time")
p = pd.read_excel(xls, "Price")
d = pd.read_excel(xls, "Demand")
v = pd.read_excel(xls, "MaxPercVar")
c = pd.read_excel(xls, "UnitCost")
A = pd.read_excel(xls, "Availability")

f = open("Luxottica.dat", "w")

# Sets
products = d.Product.unique()
variations = list(p.Variation.unique())
resources = c.Resource.unique()
premium = variations[variations.index("RB3603"):variations.index("PolarizedLenses") + 1]

f.write("set I := " + " ".join(products) + " ;\n\n")
f.write("set J := " + " ".join(variations) + " ;\n\n")
f.write("set K := " + " ".join(premium) + " ;\n\n")
f.write("set R := " + " ".join(resources) + " ;\n\n")

# Parameters
for name, df in [("p", p), ("d", d), ("t", t), ("v", v), ("c", c), ("A", A)]:
    f.write("param " + name + " :=\n")
    df.to_csv(f, sep=" ", header=False, index=False, lineterminator="\n")
    f.write(";\n\n")

f.close()
