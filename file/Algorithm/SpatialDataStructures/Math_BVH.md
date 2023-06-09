- Math_BVH_1
```math
C(T) = \sum\limits_{node \in inner \ nodes} SA(node)
```

- Math_BVH_2
```math
C_C = SA(4) + \Delta SA(3) + \Delta SA(1)
```

- Math_BVH_3
```math
\Delta SA(node) = SA(node \bigcup E) - SA(node)
```

- Math_BVH_4
```math
C_1 = SA(1 \bigcup E)
```

- Math_BVH_5
```math
C_{low} = SA(E) + \Delta SA(1)
```

- Math_BVH_6
```math
C(T) = SA(2) + SA(3) =  SA(A \bigcup B) + SA(C \bigcup D) 
```

- Math_BVH_7
```math
C'(T) = SA(2) + SA'(3) = SA(A \bigcup B) + SA(A \bigcup B \bigcup D) 
```