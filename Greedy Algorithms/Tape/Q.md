# Tape

### Time Limit

1 second

### Memory Limit

256 megabytes

## Description

You have a long stick consisting of `m` segments, enumerated from `1` to `m`. Each segment is `1` centimeter long. Some segments are broken and need to be repaired.

You have an infinitely long repair tape. You want to cut some pieces from the tape and use them to cover all the broken segments. A piece of tape of integer length `t` placed at position `s` will cover the segments:

`s, s+1, ..., s+t−1`

You are allowed to cover non-broken segments, and pieces of tape may overlap.

You want to cut **at most `k` continuous pieces** of tape to cover all broken segments. Your goal is to **minimize the total length** of the tape pieces used.

## Input

The first line contains three integers `n`, `m`, and `k`  
`(1 ≤ n ≤ 10⁵, n ≤ m ≤ 10⁹, 1 ≤ k ≤ n)`  
— the number of broken segments, the length of the stick, and the maximum number of tape pieces allowed.

The second line contains `n` integers `b₁, b₂, ..., bₙ`  
`(1 ≤ bᵢ ≤ m)` — the positions of the broken segments.

The positions are given in **strictly increasing order**, i.e.,  
`b₁ < b₂ < ... < bₙ`.

## Output

Print a single integer — the **minimum total length** of the tape pieces.

## Examples

### Input

```
4 100 2
20 30 75 80
```

### Output

```
17
```
