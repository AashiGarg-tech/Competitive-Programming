# Schedule Management

### Description

There are `n` workers and `m` tasks. Each task must be assigned to exactly one worker.

Each task `i` has a value `a[i]`, which represents the **worker who is proficient** in that task.

- If a worker is **proficient** in a task, they complete it in **1 hour**.
- If a worker is **not proficient**, they take **2 hours** to complete the task.

All workers:

- Work **in parallel**
- Can handle **only one task at a time**
- Start working at time `0`

Your goal is to assign all tasks to workers such that **all tasks are completed as early as possible**.

Determine the **minimum time** required to finish all tasks.

---

### Input

- The first line contains an integer `t` — the number of test cases  
  `(1 ≤ t ≤ 10⁴)`

For each test case:

- The first line contains two integers `n` and `m`  
  `(1 ≤ n ≤ m ≤ 2·10⁵)` — number of workers and tasks
- The second line contains `m` integers `a[i]`  
  `(1 ≤ a[i] ≤ n)` — the worker proficient in the `i`-th task

The sum of `m` over all test cases does not exceed `2·10⁵`.

---

### Output

For each test case, print a single integer — the **minimum time** required to complete all tasks.

---

### Sample

**Input:**

```text
4
2 4
1 2 1 2
2 4
1 1 1 1
5 5
5 1 3 2 4
1 1
1
```

**Output:**

```text
2
3
1
1
```
