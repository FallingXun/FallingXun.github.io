- Math_KDTree_1
```math
X_i = [X_i(1), X_i(2), ... , X_i(k)]
```
- Math_KDTree_2
```math
S_m(X_q) = \{ X|D(X, X_q) \le D(X_q, X_m) \}
```

- Math_KDTree_3
```math
v_m(X_q) = \int_{S_m(X_q)} dX
```

- Math_KDTree_4
```math
u_m(X_q) = \int_{S_m(X_q)} p(X)dX
\\
\
\\
0 \le u_m(X_q) \le 1
```

- Math_KDTree_5
```math
f(x, \alpha, \beta) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)} 
\\
\
\\
0 \le x\le 1 
\\
\
\\
\alpha,\beta \gt 0
```

- Math_KDTree_6
```math
x = u_m
\\
\
\\
\alpha = m
\\
\
\\
\beta = N - m + 1
```

- Math_KDTree_7
```math
E[X] = \frac{\alpha}{\alpha + \beta}
\\
\
\\
E[u_m(X_q)] = \frac{m}{N + 1}
```

- Math_KDTree_8
```math
u_m(X_q) \approx  p'(X_q)v(X_q)
```

- Math_KDTree_9
```math
E[v_m(X_q)] \approx \frac{m}{(N + 1)p'(X_q)}
```

- Math_KDTree_10
```math
E[v_b(X_b)] \approx \frac{b}{(N + 1)p'(X_b)}
```

- Math_KDTree_11
```math
V_m(X_q) = G(k)v_m(X_q)
\\
\
\\
E[V_m(X_q)] = E[v_m(X_q)] G(k) \approx \frac{mG(k)}{(N + 1)p'(X_q)}
```

- Math_KDTree_12
```math
L' = [\frac{e_m(X_q)}{e_b(X_q)} + 1] ^ k = \{[\frac{mG(k)}{b}] ^ \frac{1}{k} + 1\} ^ k
```

- Math_KDTree_13
```math
R' \le bL' = b\{[\frac{mG(k)}{b}] ^ \frac{1}{k} + 1\} ^ k
```

- Math_KDTree_14
```math
R' \le \{[mG(k)] ^ \frac{1}{k} + 1\} ^ k
```