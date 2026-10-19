from pyomo.environ import *
from pyomo.opt import SolverFactory

model = AbstractModel()

# Sets
model.I = Set()                             # products (Aviator, Wayfarer, ...)
model.J = Set(ordered = True)               # variations (Classic, Titanium, ..., PolarizedLenses)
model.K = Set(within = model.J)             # variations from RB3603 to PolarizedLenses
model.R = Set()                             # resources (Preparation, Assembly, Quality)

# Parameters
model.p = Param(model.I, model.J)           # selling price of product i, variation j ($/unit)
model.d = Param(model.I)                    # max demand of product i, all variations (units)
model.t = Param(model.R, model.I, model.J)  # minutes of resource r to make one unit of i, j
model.v = Param(model.I)                    # max fraction of product i that can be K variations
model.c = Param(model.R)                    # cost per minute of resource r ($/min)
model.A = Param(model.R)                    # availability of resource r (minutes)

# Decision variables: units of product i, variation j to produce
model.x = Var(model.I, model.J, domain = NonNegativeReals)

# Objective: revenue minus cost of resources used
def obj(model):
    revenue = sum(model.p[i,j]*model.x[i,j] for i in model.I for j in model.J)
    cost = sum(model.c[r]*model.t[r,i,j]*model.x[i,j] for r in model.R for i in model.I for j in model.J)
    return revenue - cost
model.objfn = Objective(rule = obj, sense = maximize)

# (1) Demand: total production of product i across all variations
def demand(model, i):
    return sum(model.x[i,j] for j in model.J) <= model.d[i]
model.demandcons = Constraint(model.I, rule = demand)

# (2) Resource availability
def resource(model, r):
    return sum(model.t[r,i,j]*model.x[i,j] for i in model.I for j in model.J) <= model.A[r]
model.resourcecons = Constraint(model.R, rule = resource)

# (3) Blending: variations RB3603..PolarizedLenses can't exceed v_i of product i's total
def blend(model, i):
    return sum(model.x[i,k] for k in model.K) <= model.v[i]*sum(model.x[i,j] for j in model.J)
model.blendcons = Constraint(model.I, rule = blend)


instance = model.create_instance("Luxottica.dat")
opt = SolverFactory('glpk')
results = opt.solve(instance)
instance.solutions.store_to(results)
results.write(filename = "Luxottica_results.yml")

print("Product  Variation  Units")
for i in instance.I:
    for j in instance.J:
        if value(instance.x[i,j]) > 1e-6:
            print(i, j, round(value(instance.x[i,j]), 2))
print()
print("Resource  Used  Available")
for r in instance.R:
    print(r, round(value(instance.resourcecons[r].body), 2), value(instance.A[r]))
print()
print("Total profit:", round(value(instance.objfn), 2))
