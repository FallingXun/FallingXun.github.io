- Math_Shadow_1
```math
w_{Penumbra} = \frac{(d_{Receiver} - d_{Blocker}) w_{Light} }{d_{Blocker}}
```

- Math_Shadow_2
```math
P\{|X - \mu| \ge a\} \le \frac{\sigma ^2}{a^2}
```

- Math_Shadow_3
```math
P\{X' \ge a'\} \le \frac{\sigma ^2}{\sigma ^2 + a'^2}
```

- Math_Shadow_4
```math
P\{X \ge a\} \le \frac{\sigma ^2}{\sigma ^2 + (a - \mu)^2}
```

- Math_Shadow_5
```math
\mu = E(X) = pd_2 + (1 - p)d_1
```

- Math_Shadow_6
```math
\sigma ^ 2 = E(X^2) - E(X)^2 = (p - p^2)(d_2 - d_1)^2
```

- Math_Shadow_7
```math
\frac{\sigma ^2}{\sigma ^2 + (d_2 - \mu)^2} = \frac{(p - p^2)(d_2 - d_1)^2}{(p - p^2)(d_2 - d_1)^2 + (d_2 - (pd_2 + (1 - p)d_1))^2} = p
```

- Math_Shadow_8
```math
average = \frac{sum[j] - sum[i - 1]}{j - (i - 1)}
```

- Math_Shadow_9
```math
average = \frac{RB - LB - RT + LT}{(R-L)(B-T)} =  \frac{sum[r, b] - sum[l - 1 , b] - sum[r, t - 1] + sum[l - 1, t - 1]}{(r - (l - 1))(b - (t - 1))} 
```

- Math_Shadow_10
```math
\frac{N_{unocc}}{N}z_{unocc} + \frac{N_{occ}}{N}z_{occ} = z_{avg}
```

- Math_Shadow_11
```math
z_{occ} = \frac{z_{avg} - z_{unocc}P\{X \ge a\} }{1 - P\{X \ge a\}}
```

- Math_Shadow_12
```math
SDF(P) = \sqrt{(x_O - x_P)^2 + (y_O - x_P)^2} - r
```

- Math_Shadow_13
```math
\theta = arcsin \frac{SDF(\vec p)}{\vec p - \vec o}
```

- Math_Shadow_14
```math
value = \min(\frac{k \cdot SDF(\vec p)}{\vec p - \vec o}, 1.0)
```

- Math_Shadow_15
```math
r_1 ^ 2 - (y - r_1) ^ 2 = r_2 ^ 2 - y ^ 2
```

- Math_Shadow_16
```math
y = \frac{r_2 ^ 2 }{2 r_1}
```

- Math_Shadow_17
```math
d = \sqrt{r_2 ^ 2 - y ^ 2}
```

- Math_Shadow_18
```math
value = \min(\frac{d}{w \max((\vec p_i - \vec o) - y)}, 1.0)
```

- Math_Shadow_19
```math
y = \frac{SDF(\vec p_i) ^ 2 }{2 \cdot SDF(\vec p_{i-1})}
```

- Math_Shadow_20
```math
d = \sqrt{SDF(\vec p_i) ^ 2 - (\frac{SDF(\vec p_i) ^ 2 }{2 \cdot SDF(\vec p_{i-1})}) ^ 2}
```
