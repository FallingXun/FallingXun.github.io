- Math_DepthNormalTexture_1
```math
z_{_{NDC}} = \frac{f + n}{f - n} + \frac{2nf}{f - n} \cdot \frac{1}{z_{_{view}}}
```

- Math_DepthNormalTexture_2
```math
z_{_{depth}} = \frac{z_{_{NDC}} + 1}{2}
```

- Math_DepthNormalTexture_3
```math
z_{_{view}} = \frac{1}{(\frac{1}{n}-\frac{1}{f})z_{_{depth}} - \frac{1}{n}}
```

- Math_DepthNormalTexture_4
```math
z_{_{eye}} = -z_{_{view}} = \frac{1}{(\frac{1}{f}-\frac{1}{n})z_{_{depth}} + \frac{1}{n}}
```

- Math_DepthNormalTexture_5
```math
z_{_{linear01}} = \frac{z_{_{eye}}}{f} = \frac{1}{(1-\frac{f}{n})z_{_{depth}} + \frac{f}{n}}
```

- Math_DepthNormalTexture_6
```math
z_{_{linear01FromNear}} = \frac{z_{_{eye}} - n}{f - n} = \frac{1}{(1-\frac{f}{n})z_{_{depth}} + \frac{f}{n}}
```

- Math_DepthNormalTexture_7
```math
\_zBufferParams = [(1 - \frac{f}{n}) \space\space,\space\space (\frac{f}{n}) \space\space,\space\space (\frac{1}{f} - \frac{1}{n}) \space\space, \space\space (\frac{1}{n})]
```