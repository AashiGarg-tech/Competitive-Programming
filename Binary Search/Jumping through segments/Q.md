# Jumping Through Segments

### Time Limit

5 seconds

### Memory Limit

256 megabytes

## Description

Polycarp is designing a level for a game. The level consists of `n` segments on the number line, where the `i`-th segment starts at coordinate `lᵢ` and ends at coordinate `rᵢ`.

The player starts the level at coordinate `0`. In one move, they can move to any point that is within a distance of **no more than `k`**.

After the `i`-th move, the player must land within the `i`-th segment, i.e., at a coordinate `x` such that:

`lᵢ ≤ x ≤ rᵢ`

This means:

- After the **first move**, the player must be inside the first segment (`l₁` to `r₁`)
- After the **second move**, the player must be inside the second segment (`l₂` to `r₂`)
- ...
- After the **n-th move**, the player must be inside the `n`-th segment (`lₙ` to `rₙ`)

The level is considered **completed** if the player reaches the `n`-th segment following the rules above.

Polycarp realized that for some values of `k`, completing the level is impossible. To avoid making the level too easy, he asks you to determine the **minimum integer `k`** for which it is possible to complete the level.

## Input

The first line contains a single integer `t`  
`(1 ≤ t ≤ 10⁴)` — the number of test cases.

For each test case:

- The first line contains a single integer `n`  
  `(1 ≤ n ≤ 2 · 10⁵)` — the number of segments.
- The following `n` lines each contain two integers `lᵢ` and `rᵢ`  
  `(0 ≤ lᵢ ≤ rᵢ ≤ 10⁹)` — the boundaries of the `i`-th segment.

Segments may intersect.

It is guaranteed that the sum of `n` over all test cases does not exceed `2 · 10⁵`.

## Output

For each test case, output a single integer — the **minimum value of `k`** with which it is possible to complete the level.

## Example

### Input

```
4
5
1 5
3 4
5 6
8 10
0 1
3
0 2
0 1
0 3
3
3 8
10 18
6 11
4
10 20
0 5
15 17
2 2
```

### Output:

```text
7
0
5
13
```
