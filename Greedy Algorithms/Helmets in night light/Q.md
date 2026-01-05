# Helmets in Night Light

### Description

Pak Chanek is the chief of a village named Khuntien. He needs to notify all `n` residents about an important announcement.

First, Pak Chanek can directly share the announcement with any resident at a cost of `p` per person.

After that, residents who have received the announcement (either directly from Pak Chanek or from another resident) can share it further using a magical helmet-shaped device.

For each resident `i`:

- The resident can share the announcement with **at most `a[i]` other residents**.
- Each such share costs **`b[i]`**.

Pak Chanek can control the entire sharing process.

Determine the **minimum total cost** required to notify **all `n` residents**.

### Input

- The first line contains an integer `t` — the number of test cases `(1 ≤ t ≤ 10⁴)`.
- For each test case:
  - The first line contains two integers `n` and `p`  
    `(1 ≤ n ≤ 10⁵, 1 ≤ p ≤ 10⁵)` — the number of residents and the cost of direct notification.
  - The second line contains `n` integers `a[i]`  
    `(1 ≤ a[i] ≤ 10⁵)` — the maximum number of residents each resident can notify.
  - The third line contains `n` integers `b[i]`  
    `(1 ≤ b[i] ≤ 10⁵)` — the cost per share for each resident.

It is guaranteed that the sum of `n` over all test cases does not exceed `10⁵`.

### Output

For each test case, print a single integer representing the **minimum cost** to notify all residents.

---

### Sample

**Input:**

```text
3
6 3
2 3 2 1 1 3
4 3 2 6 3 6
1 100000
100000
1
4 94
1 4 2 3
103 96 86 57
```

**Output:**

```
16
100000
265

```
