- Math_Transform_1
```math
M_T = \begin{bmatrix}1&0&0&t_x \\0&1&0&t_y \\0&0&1&t_z \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_2
```math
M_S = \begin{bmatrix}k_x&0&0&0 \\0&k_y&0&0 \\0&0&k_z&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_3
```math
M_{Rx} = \begin{bmatrix}1&0&0&0 \\0&cos\theta&-sin\theta&0 \\0&sin\theta&cos\theta&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_4
```math
M_{Ry} = \begin{bmatrix}cos\theta&0&sin\theta&0 \\0&1&0&0 \\-sin\theta&0&cos\theta&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_5
```math
M_{Rz} = \begin{bmatrix}cos\theta&-sin\theta&0&0 \\sin\theta&cos\theta&0&0 \\0&0&1&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_6
```math
M_R = M_{Rz}M_{Rx}M_{Ry}
```

- Math_Transform_7
```math
M_{model} = \begin{bmatrix}1&0&0&x \\0&1&0&y \\0&0&1&z \\0&0&0&1 \end{bmatrix} \begin{bmatrix}1&0&0&0 \\0&cos\theta&-sin\theta&0 \\0&sin\theta&cos\theta&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_8
```math
M_{view} = \begin{bmatrix}1&0&0&0 \\0&1&0&0 \\0&0&-1&0 \\0&0&0&1 \end{bmatrix} \begin{bmatrix}1&0&0&-x \\0&1&0&-y \\0&0&1&-z \\0&0&0&1 \end{bmatrix} \begin{bmatrix}1&0&0&0 \\0&cos(-\theta)&-sin(-\theta)&0 \\0&sin(-\theta)&cos(-\theta)&0 \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_9
```math
M_{ortho} = \begin{bmatrix}\frac{2}{r - l}&0&0&0 \\0&\frac{2}{t - b}&0&0 \\0&0&-\frac{2}{f - n}&0 \\0&0&0&1 \end{bmatrix} \begin{bmatrix}1&0&0&-\frac{r + l}{2} \\0&1&0&-\frac{t + b}{2} \\0&0&1&\frac{f + n}{2} \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_10
```math
M_{ortho} = \begin{bmatrix}\frac{2}{r - l}&0&0&-\frac{r + l}{r - l} \\0&\frac{2}{t - b}&0&-\frac{t + b}{t - b} \\0&0&-\frac{2}{f - n}&-\frac{f + n}{f - n} \\0&0&0&1 \end{bmatrix}
```

- Math_Transform_11
```math
x' = -\frac{nx}{z}
```

- Math_Transform_12
```math
y' = -\frac{ny}{z}
```

- Math_Transform_13
```math
M \begin{bmatrix} x\\y\\z\\1 \end{bmatrix} = \begin{bmatrix} -\frac{nx}{z}\\-\frac{ny}{z}\\z'\\1 \end{bmatrix} =  \begin{bmatrix} nx\\ny\\z' \cdot -z\\-z \end{bmatrix} 
```

- Math_Transform_14
```math
M  = \begin{bmatrix}n&0&0&0 \\0&n&0&0 \\A&B&C&D \\0&0&-1&0 \end{bmatrix}
```

- Math_Transform_15
```math
\begin{bmatrix}n&0&0&0 \\0&n&0&0 \\A&B&C&D \\0&0&-1&0 \end{bmatrix} \begin{bmatrix} x\\y\\-n\\1 \end{bmatrix} = \begin{bmatrix} nx\\ny\\-n \cdot n\\-n\end{bmatrix} 
```

- Math_Transform_16
```math
M  = \begin{bmatrix}n&0&0&0 \\0&n&0&0 \\0&0&C&D \\0&0&-1&0 \end{bmatrix}
```

- Math_Transform_17
```math
\begin{bmatrix}n&0&0&0 \\0&n&0&0 \\0&0&C&D \\0&0&-1&0 \end{bmatrix} \begin{bmatrix} x\\y\\-f\\1 \end{bmatrix} = \begin{bmatrix} nx\\ny\\-f \cdot f\\-f\end{bmatrix} 
```

- Math_Transform_18
```math
-Cn + D = -n^2
```

- Math_Transform_19
```math
-Cf + D = -f^2
```

- Math_Transform_20
```math
M  = \begin{bmatrix}n&0&0&0 \\0&n&0&0 \\0&0& n + f & nf \\0&0&-1&0 \end{bmatrix}
```

- Math_Transform_21
```math
M_{presp}  = \begin{bmatrix}\frac{2}{r - l}&0&0&-\frac{r + l}{r - l} \\0&\frac{2}{t - b}&0&-\frac{t + b}{t - b} \\0&0&-\frac{2}{f - n}&-\frac{f + n}{f - n} \\0&0&0&1 \end{bmatrix} \begin{bmatrix}n&0&0&0 \\0&n&0&0 \\0&0& n + f & nf \\0&0&-1&0 \end{bmatrix}
```

- Math_Transform_22
```math
M_{presp}  = \begin{bmatrix}\frac{2n}{r - l}&0&0&\frac{r + l}{r - l} \\0&\frac{2n}{t - b}&0&\frac{t + b}{t - b} \\0&0&-\frac{f + n}{f - n}&-\frac{2nf}{f - n} \\0&0&-1&0 \end{bmatrix}
```

- Math_Transform_23
```math
\begin{bmatrix}\frac{2}{r - l}&0&0&-\frac{r + l}{r - l} \\0&\frac{2}{t - b}&0&-\frac{t + b}{t - b} \\0&0&-\frac{2}{f - n}&-\frac{f + n}{f - n} \\0&0&0&1 \end{bmatrix}  \begin{bmatrix} x\\y\\z\\1 \end{bmatrix} =  \begin{bmatrix} \frac{2}{r - l}x - \frac{r + l}{r - l}\\ \frac{2}{t - b}y - \frac{t + b}{t - b} \\-\frac{2}{f - n}z - \frac{f + n}{f - n} \\1 \end{bmatrix}
```

- Math_Transform_24
```math
\begin{bmatrix}\frac{2n}{r - l}&0&\frac{r + l}{r - l}&0 \\0&\frac{2n}{t - b}&\frac{t + b}{t - b}&0 \\0&0&-\frac{f + n}{f - n}&-\frac{2nf}{f - n} \\0&0&-1&0 \end{bmatrix}  \begin{bmatrix} x\\y\\z\\1 \end{bmatrix} = \begin{bmatrix} \frac{2n}{r - l}x + \frac{r + l}{r - l}z \\ \frac{2n}{t - b}y + \frac{t + b}{t - b}z \\ -\frac{f + n}{f - n}z - \frac{2nf}{f - n} \\-z \end{bmatrix}
```

- Math_Transform_25
```math
\begin{bmatrix}\frac{2n}{r - l}&0&\frac{r + l}{r - l}&0 \\0&\frac{2n}{t - b}&\frac{t + b}{t - b}&0 \\0&0&-\frac{f + n}{f - n}&-\frac{2nf}{f - n} \\0&0&-1&0 \end{bmatrix}  \begin{bmatrix} x\\y\\z\\1 \end{bmatrix} = \begin{bmatrix} -\frac{2n}{r - l} \cdot \frac{x}{z} - \frac{r + l}{r - l} \\ -\frac{2n}{t - b} \cdot \frac{y}{z} - \frac{t + b}{t - b} \\ \frac{f + n}{f - n} + \frac{2nf}{f - n} \cdot \frac{1}{z} \\1 \end{bmatrix}
```
