Luxottica - Product Mix

Sets
I = products (Aviator, Wayfarer, ..., StripeArm), 25 products
J = variations (Classic, Titanium, ..., PolarizedLenses), 10 variations
K = variations from RB3603 to PolarizedLenses (RB3603, FlashLenses, Collection, Mirror, PolarizedLenses), K subset of J
R = resources (Preparation, Assembly, Quality)

Parameters
p_ij = price of product i, variation j ($/unit)
d_i = demand for product i across all variations (units)
t_rij = time of resource r needed to produce one unit of product i, variation j (minutes)
v_i = max percent of product i that can be variations in K
c_r = cost per minute of resource r ($/minute)
A_r = availability of resource r (minutes)

Decision variables
x_ij = units of product i, variation j to produce

Objective
max Z = sum over i in I, j in J of p_ij*x_ij - sum over r in R, i in I, j in J of c_r*t_rij*x_ij

Constraints
sum over j in J of x_ij <= d_i                              for all i in I
sum over i in I, j in J of t_rij*x_ij <= A_r                for all r in R
sum over k in K of x_ik <= v_i * (sum over j in J of x_ij)  for all i in I
x_ij >= 0                                                   for all i in I, j in J

Optimal solution: total profit = 206,503.23

Product            Variation        Units
Clubmaster         Outdoor          216.00
Clubmaster         Mirror           504.00
Justin             Classic          44.01
Justin             PolarizedLenses  66.01
RoundDoubleBridge  Titanium         308.02
RoundDoubleBridge  Mirror           221.98
Timeless           Outdoor          134.00
Timeless           PolarizedLenses  536.00
FlightJacket       Outdoor          78.00
FlightJacket       Collection       312.00
FrogSkins          Evolve           80.00
FrogSkins          FlashLenses      320.00
Gaskan             Evolve           150.00
Gaskan             PolarizedLenses  600.00
Flak               Titanium         132.00
Flak               RB3603           222.15
Flak               Mirror           305.85
HalfJacket         Evolve           306.00
HalfJacket         Mirror           204.00
Oval               Classic          384.00
Oval               FlashLenses      256.00
Gingham            Titanium         220.00
Gingham            Mirror           220.00
StripeArm          Evolve           129.00
StripeArm          Collection       301.00
All other x_ij = 0
