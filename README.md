# BZAN 531: Luxottica Product Mix (Pyomo)

A production planning LP for Luxottica: choose how many units of each of 25 products × 10 variations to make so that profit (revenue minus resource cost) is as large as possible. The constraints are demand, the availability of three resources and a blending limit on the premium variations.

## Deliverables

| # | Deliverable | File |
|---|---|---|
| 1 | Pyomo abstract model | [`Luxottica.py`](Luxottica.py) |
| 2 | Python code that builds the `.dat` file from Excel with pandas | [`Luxottica_dat.py`](Luxottica_dat.py) |
| 3 | Data file | [`Luxottica.dat`](Luxottica.dat) |
| 4 | Results file | [`Luxottica_results.yml`](Luxottica_results.yml) (solver output), [`Luxottica_output.txt`](Luxottica_output.txt) (readable summary) |
| 5 | Mathematical formulation | [`Luxottica_Formulation.md`](Luxottica_Formulation.md) |

The source data is in [`15.Luxottica_prodmix.xlsx`](15.Luxottica_prodmix.xlsx).

## Notation

| Symbol | Meaning |
|---|---|
| $p_{ij}$ | price |
| $d_i$ | demand |
| $t_{rij}$ | time needed to produce |
| $v_i$ | max percent variation |
| $c_r$ | cost per minute |
| $A_r$ | resource availability |
| $x_{ij}$ | decision variables (units produced) |

Sets: $I$ = products, $J$ = variations, $K \subseteq J$ = variations RB3603 through PolarizedLenses, $R$ = resources.

## How to run

Requirements: Python 3, `pandas`, `openpyxl`, `pyomo`, and the GLPK solver (`glpsol` on your PATH).

```bash
pip install -r requirements.txt
```

```bash
python Luxottica_dat.py
```

```bash
python Luxottica.py
```

The first script reads the Excel file and writes `Luxottica.dat`. The second solves the model, writes `Luxottica_results.yml` and prints the production plan.

## Result

Optimal profit: **$206,503.23**. All three resources (Preparation, Assembly, Quality) are fully used.
