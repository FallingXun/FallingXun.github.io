- Math_1
```math
v_{pt'[0]} = \frac{v_{j[0]} - v_{i[0]}}{v_{j[2]} - v_{i[2]}} \cdot (v_{pt[2]} - v_{i[2]}) + v_{i[0]}
```

- Math_2
```math
\bold{p} = \alpha\bold{a} + \beta\bold{b} + \gamma\bold{c}
```

- Math_3
```math
\alpha = \frac{S_{\Delta pbc}}{S_{\Delta abc}}, \beta = \frac{S_{\Delta pca}}{S_{\Delta abc}}, \gamma = \frac{S_{\Delta pab}}{S_{\Delta abc}}
```

- Math_4
```math
|pp_t| \cdot cos\theta = \frac{|pq| \cdot |pp_t| \cdot cos\theta}{|pq|} = \frac{\bold{p}\bold{q} \cdot \bold{p}\bold{p_t}}{|pq|}
```

- Math_5
```math
\frac{|pp_t| \cdot cos\theta}{|pq|} = \frac{\bold{p}\bold{q} \cdot \bold{p}\bold{p_t}}{|pq| \cdot |pq|}
```

- Math2_1
```math
|\bold{normal}|cos\theta = normal.y < cos {\theta}_{walkableSlopeAngle}
```

- Math_6
```math
\overrightarrow{AP} = u\overrightarrow{AB} + v\overrightarrow{AC}
```

- Math_7
```math
\overrightarrow{AP} \cdot \overrightarrow{AB}= u(\overrightarrow{AB} \cdot \overrightarrow{AB}) + v(\overrightarrow{AB} \cdot \overrightarrow{AC})
\\
\
\\
\overrightarrow{AP} \cdot \overrightarrow{AC}= u(\overrightarrow{AB} \cdot \overrightarrow{AC}) + v(\overrightarrow{AC} \cdot \overrightarrow{AC})
```

- Math_8
```math
u = \frac{(\overrightarrow{AP} \cdot \overrightarrow{AB})(\overrightarrow{AC} \cdot \overrightarrow{AC}) - (\overrightarrow{AP} \cdot \overrightarrow{AC})(\overrightarrow{AC} \cdot \overrightarrow{AB})}{(\overrightarrow{AB} \cdot \overrightarrow{AB})(\overrightarrow{AC} \cdot \overrightarrow{AC}) - (\overrightarrow{AB} \cdot \overrightarrow{AC})(\overrightarrow{AB} \cdot \overrightarrow{AC})}
\\
\
\\
v = \frac{(\overrightarrow{AP} \cdot \overrightarrow{AC})(\overrightarrow{AB} \cdot \overrightarrow{AB}) - (\overrightarrow{AP} \cdot \overrightarrow{AB})(\overrightarrow{AB} \cdot \overrightarrow{AC})}{(\overrightarrow{AB} \cdot \overrightarrow{AB})(\overrightarrow{AC} \cdot \overrightarrow{AC}) - (\overrightarrow{AB} \cdot \overrightarrow{AC})(\overrightarrow{AB} \cdot \overrightarrow{AC})}
```

- Math_9
```math
y_P = y_A + u \cdot y_{\overrightarrow{AB}} + v \cdot y_{\overrightarrow{AC}}
```

- Math_10
```math
\begin{equation*}
\left\{
\begin{aligned}    
& (c_x - p_{1x}) ^ 2 + (c_z - p_{1z}) ^ 2 = (c_x - p_{2x}) ^ 2 + (c_z - p_{2z}) ^ 2   \\   
& (c_x - p_{1x}) ^ 2 + (c_z - p_{1z}) ^ 2 = (c_x - p_{3x}) ^ 2 + (c_z - p_{3z}) ^ 2
\end{aligned}
\right.
\end{equation*}
```

- Math_11
```math
\begin{equation*}
\left\{
\begin{aligned}    
& c_x(p_{2x} - p_{1x}) + c_z(p_{2z} - p_{1z}) = \frac{(p_{2x} ^ 2 + p_{2z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2)}{2}
\\
& c_x(p_{3x} - p_{1x}) + c_z(p_{3z} - p_{1z}) = \frac{(p_{3x} ^ 2 + p_{3z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2)}{2}
\end{aligned}
\right.
\end{equation*}
```

- Math_12
```math
c_z = \frac{(p_{2x} ^ 2 + p_{2z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2) - 2c_x(p_{2x} - p_{1x})}{2(p_{2z} - p_{1z})}
```

- Math_13
```math
c_x(p_{3x} - p_{1x}) + \frac{(p_{2x} ^ 2 + p_{2z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2) - 2c_x(p_{2x} - p_{1x})}{2(p_{2z} - p_{1z})}(p_{3z} - p_{1z}) = \frac{(p_{3x} ^ 2 + p_{3z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2)}{2}
```

- Math_14
```math
c_x = \frac{[(p_{3x} ^ 2 + p_{3z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2)](p_{2z} - p_{1z}) - [(p_{2x} ^ 2 + p_{2z} ^ 2) - (p_{1x} ^ 2 + p_{1z} ^ 2)](p_{3z} - p_{1z})}{2[(p_{3x} - p_{1x})(p_{2z} - p_{1z}) - (p_{2x} - p_{1x})(p_{3z} - p_{1z})]}
\\\
\\\
= \frac{(p_{2x} ^ 2 + p_{2z} ^ 2)(p_{3z} - p_{1z}) - (p_{3x} ^ 2 + p_{3z} ^ 2)(p_{2z} - p_{1z}) + (p_{1x} ^ 2 + p_{1z} ^ 2)(p_{2z} - p_{3z})}{2[(p_{2x} - p_{1x})(p_{3z} - p_{1z}) - (p_{3x} - p_{1x})(p_{2z} - p_{1z})]}
```

- Math_15
```math
p_{1Sq} = p_{1x} ^ 2 + p_{1z} ^ 2
\\\
\\
p_{2Sq} = p_{2x} ^ 2 + p_{2z} ^ 2
\\\
\\
p_{3Sq} = p_{3x} ^ 2 + p_{3z} ^ 2
\\\
\\
S_{\Delta 123} = \frac{\overrightarrow {p_1 p_2} \times \overrightarrow {p_1 p_3}}{2} = \frac{(p_{2x} - p_{1x})(p_{3z} - p_{1z}) - (p_{3x} - p_{1x})(p_{2z} - p_{1z})}{2}
```

- Math_16
``` math
c_x = \frac{p_{1Sq}(p_{2z} - p_{3z}) + p_{2Sq}(p_{3z} - p_{1z}) + p_{3Sq}(p_{1z} - p_{2z})}{2S_{\Delta 123}}
```

- Math_17
``` math
c_z = \frac{p_{1Sq}(p_{3x} - p_{2x}) + p_{2Sq}(p_{1x} - p_{3x}) + p_{3Sq}(p_{2x} - p_{1x})}{2S_{\Delta 123}}
```