
- Math_DepthNormalTexture_1
```math
z_{_{NDC}} = -\frac{2}{f - n} \cdot z_{_{view}} - \frac{f + n}{f - n}
```

- Math_DepthNormalTexture_2
```math
z_{_{depth}} = \frac{z_{_{NDC}} + 1}{2}
```

- Math_DepthNormalTexture_3
```math
z_{_{eye}} = -z_{_{view}} = n + (f-n)z_{_{depth}}
```

- Math_DepthNormalTexture_4
```math
 _{\_ProjectionParams} = [(1) \space\space,\space\space (n) \space\space,\space\space (f) \space\space, \space\space (\frac{1}{f})]
```

- Math_DepthNormalTexture_5
```math
z_{_{NDC}} = \frac{f + n}{f - n} + \frac{2nf}{f - n} \cdot \frac{1}{z_{_{view}}}
```

- Math_DepthNormalTexture_6
```math
z_{_{view}} = \frac{1}{(\frac{1}{n}-\frac{1}{f})z_{_{depth}} - \frac{1}{n}}
```

- Math_DepthNormalTexture_8
```math
z_{_{eye}} = -z_{_{view}} = \frac{1}{(\frac{1}{f}-\frac{1}{n})z_{_{depth}} + \frac{1}{n}}
```

- Math_DepthNormalTexture_8
```math
z_{_{linear01}} = \frac{z_{_{eye}}}{f} = \frac{1}{(1-\frac{f}{n})z_{_{depth}} + \frac{f}{n}}
```

- Math_DepthNormalTexture_9
```math
z_{_{linear01FromNear}} = \frac{z_{_{eye}} - n}{f - n} = \frac{z_{_{depth}}}{(1-\frac{f}{n})z_{_{depth}} + \frac{f}{n}}
```

- Math_DepthNormalTexture_10
```math
 _{\_zBufferParams} = [(1 - \frac{f}{n}) \space\space,\space\space (\frac{f}{n}) \space\space,\space\space (\frac{1}{f} - \frac{1}{n}) \space\space, \space\space (\frac{1}{n})]
```

- Math_DepthNormalTexture_11
```math
x_{_{view}} = x_{_{near-left-top}} + (x_{_{near-right-top}} - x_{_{near-left-top}}) \cdot u
\\\
\\\
y_{_{view}} = y_{_{near-left-top}} + (y_{_{near-left-bottom}} - y_{_{near-left-top}}) \cdot v
\\\
\\\
z_{_{view}} = z_{_{near-center}} + (z_{_{far-center}} - z_{_{near-center}}) \cdot \frac{z_{_{eye}}}{f}
```

- Math_DepthNormalTexture_12
```math
x_{_{view}} = x_{_{near}} \cdot \frac{z_{_{eye}}}{n}
\\\
\\\
y_{_{view}} = y_{_{near}} \cdot \frac{z_{_{eye}}}{n}
\\\
\\\
z_{_{view}} = z_{_{near}} \cdot \frac{z_{_{eye}}}{n}
```


- Math_DepthNormalTexture_13
```math
x_{_{view}} = [x_{_{near-left-top}} + (x_{_{near-right-top}} - x_{_{near-left-top}}) \cdot u ] \cdot \frac{z_{_{eye}}}{n}
\\\
\\\
y_{_{view}} = [y_{_{near-left-top}} + (y_{_{near-left-bottom}} - y_{_{near-left-top}}) \cdot v ]\cdot \frac{z_{_{eye}}}{n}
\\\
\\\
z_{_{view}} = z_{_{near}} \cdot \frac{z_{_{eye}}}{n}
```

- Math_DepthNormalTexture_14
```math
\frac{x_0}{x} = \frac{z_0 - z_o}{z - z_o}
\\\
\\\
\frac{y_0}{y} = \frac{z_0 - z_o}{z - z_o}
```

- Math_DepthNormalTexture_15
```math
x_0 = \frac{x}{z + 1}
\\\
\\\
y_0 = \frac{y}{z + 1}
```