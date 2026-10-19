from pyomo.environ import *
from pyomo.opt import SolverFactory

model = AbstractModel()

# Sets and parameters
model.I = Set()                             # products
model.J = Set(ordered = True)               # variations
model.K = Set(within = model.J)             # variations RB3603 to PolarizedLenses
model.R = Set()                             # resources
model.p = Param(model.I, model.J)           # price
model.d = Param(model.I)                    # demand
model.t = Param(model.R, model.I, model.J)  # time needed to produce
model.v = Param(model.I)                    # max percent variation
model.c = Param(model.R)                    # cost per minute
model.A = Param(model.R)                    # resource availability

# Variables
model.x = Var(model.I, model.J, domain = NonNegativeReals)

def obj(model):
    revenue = sum(model.p[i,j]*model.x[i,j] for i in model.I for j in model.J)
    cost = sum(model.c[r]*model.t[r,i,j]*model.x[i,j] for r in model.R for i in model.I for j in model.J)
    return revenue - cost
model.objfn = Objective(rule = obj, sense = maximize)

def demand(model, i):
    return sum(model.x[i,j] for j in model.J) <= model.d[i]
model.demandcons = Constraint(model.I, rule = demand)

def resource(model, r):
    return sum(model.t[r,i,j]*model.x[i,j] for i in model.I for j in model.J) <= model.A[r]
model.resourcecons = Constraint(model.R, rule = resource)

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
print("Total profit:", round(value(instance.objfn), 2))
