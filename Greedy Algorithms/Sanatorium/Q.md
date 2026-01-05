# Sanatorium

### Description

Vasiliy spent his vacation in a sanatorium but completely forgot the details of his stay.

Every day in the sanatorium followed the same sequence of meals:

1. **Breakfast**
2. **Dinner**
3. **Supper**

Vasiliy may have **missed some meals** on some days, or even skipped the dining room entirely on certain days.

The only information he has is a card showing:

- `b` — number of breakfasts he had
- `d` — number of dinners he had
- `s` — number of suppers he had

Vasiliy does **not remember**:

- the time of day when he **arrived** (before breakfast, before dinner, before supper, or after supper)
- the time of day when he **left** (same four possibilities)

After arriving, Vasiliy stayed continuously until he left.  
It is also possible that he arrived and left on the **same day**.

Meals that occurred **before arrival on the first day** and **after departure on the last day** are **not counted as missed**.

Your task is to determine the **minimum possible number of meals Vasiliy could have missed**, consistent with the given counts.

---

### Input

- A single line containing three integers:
  - `b` — breakfasts
  - `d` — dinners
  - `s` — suppers

Constraints:

- `0 ≤ b, d, s ≤ 10¹⁸`
- `b + d + s ≥ 1`

---

### Output

- Print a single integer — the **minimum number of meals** Vasiliy could have missed during his stay.

---

### Sample

**Input:**

```text
3 2 1
```

**Output:**

```text
1
```
