- Math_BezierCurves_1
```math
b_{01} = (1 - t)b_0 + tb_1
```

- Math_BezierCurves_2
```math
b_{12} = (1 - t)b_1 + tb_2
```

- Math_BezierCurves_3
```math
b_{02} = (1 - t)b_{01} + tb_{12}
```

- Math_BezierCurves_4
```math
b_{02} = (1 - t)^2b_0 + 2t(1 - t)b_1 + t^2b_2
```

- Math_BezierCurves_5
```math
b^n(t) = b_{0n}(t) = \displaystyle\sum\limits_{j=0}^n b_j B^n_j(t)
```

- Math_BezierCurves_6
```math
B^n_j(t) = t^j(1-t)^{n - j}
```

- Math_BezierCurves_7
```math
b^n(t) = \displaystyle\sum\limits_{j=0}^n b_j t^j(1-t)^{n - j}
```
