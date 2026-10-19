# Luxottica Product Mix — Mathematical Formulation

## Sets and indices

| Set | Index | Description |
|---|---|---|
| $I$ | $i$ | Products (Aviator, Wayfarer, Clubmaster, …, StripeArm), $\lvert I \rvert = 25$ |
| $J$ | $j$ | Variations (Classic, Titanium, Gradient, Evolve, Outdoor, RB3603, FlashLenses, Collection, Mirror, PolarizedLenses), $\lvert J \rvert = 10$ |
| $K \subseteq J$ | $k$ | Variations from RB3603 to PolarizedLenses: {RB3603, FlashLenses, Collection, Mirror, PolarizedLenses} |
| $R$ | $r$ | Resources (Preparation, Assembly, Quality) |

## Parameters

| Parameter | Description | Units |
|---|---|---|
| $p_{ij}$ | Selling price of product $i$, variation $j$ | $/unit |
| $d_i$ | Maximum demand for product $i$ (all variations combined) | units |
| $t_{rij}$ | Time of resource $r$ needed to produce one unit of product $i$, variation $j$ | minutes/unit |
| $v_i$ | Maximum fraction of product $i$'s production that can be variations in $K$ | fraction |
| $c_r$ | Cost per minute of resource $r$ | $/minute |
| $A_r$ | Availability of resource $r$ | minutes |

## Decision variables

$x_{ij}$ = number of units of product $i$, variation $j$ to produce, for all $i \in I,\ j \in J$

## Objective: maximize profit (revenue minus resource cost)

$$
\max \; Z = \sum_{i \in I} \sum_{j \in J} p_{ij}\, x_{ij} \;-\; \sum_{r \in R} \sum_{i \in I} \sum_{j \in J} c_r\, t_{rij}\, x_{ij}
$$

## Constraints

**(1) Demand.** Total production of each product across all its variations can't exceed its demand:

$$
\sum_{j \in J} x_{ij} \le d_i \qquad \forall\, i \in I
$$

**(2) Resource availability.** Minutes of each resource used can't exceed what's available:

$$
\sum_{i \in I} \sum_{j \in J} t_{rij}\, x_{ij} \le A_r \qquad \forall\, r \in R
$$

**(3) Blending.** For each product, production of variations RB3603 through PolarizedLenses can't exceed fraction $v_i$ of that product's total production:

$$
\sum_{k \in K} x_{ik} \le v_i \sum_{j \in J} x_{ij} \qquad \forall\, i \in I
$$

**(4) Non-negativity.**

$$
x_{ij} \ge 0 \qquad \forall\, i \in I,\ j \in J
$$

## Model size

- 250 decision variables ($25 \times 10$)
- 53 constraints: 25 demand + 3 resource + 25 blending

## Optimal solution

**Maximum profit = $206,503.23**. All three resources are used up (Preparation 40,000, Assembly 50,000 and Quality 60,000 minutes). See `Luxottica_output.txt` for the production plan and `Luxottica_results.yml` for the full solver output.
