- Math_Lambert
```math
\bold c_{diffuse} = (\bold c_{light} \cdot \bold m_{diffuse})\max{(0, n \cdot I)}
```

- Math_HalfLambert
```math
\bold c_{diffuse} = (\bold c_{light} \cdot \bold m_{diffuse})(\alpha (\bold{\hat{n}} \cdot \bold I) + \beta)
```

- Math_Phong
```math
\bold c_{specular} = (\bold c_{light} \cdot \bold m_{specular})\max{(0, \bold{\hat{v}} \cdot \bold r)} ^ {m_{glass}}
```

- Math_BlinnPhong
```math
\bold c_{specular} = (\bold c_{light} \cdot \bold m_{specular})\max{(0, \bold{\hat n} \cdot \bold{\hat h})} ^ {m_{glass}}
```

- Math_BlinnPhong_h
```math
\bold{\hat h} = \frac{\bold{\hat v} + \bold{\hat I}}{| \bold{\hat v} + \bold{\hat I} |}
```

- Math_SchlickFresnel
```math
F_{schlick}(\bold v , \bold n) = F_0 + (1 - F_0)(1 - \bold v \cdot \bold n)^5 
```