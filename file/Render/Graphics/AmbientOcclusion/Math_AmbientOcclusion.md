- Math_AmbientOcclusion_1
```math
\omega = \frac{s}{r}

```

- Math_AmbientOcclusion_2
```math
\Omega = \frac{A}{r^2}

```

- Math_AmbientOcclusion_3
```math
d\Omega = \frac{A_{ABCD}}{r^2} = \frac{s_{AB} \space s_{AD}}{r^2} 
```

- Math_AmbientOcclusion_4
```math
d\theta = \frac{s_{AB}}{r}
\\\
\\\
d\phi = \frac{s_{AD}}{rsin\theta}
```

- Math_AmbientOcclusion_5
```math
d\Omega = \frac{rd\theta \space rsin\theta d\phi}{r^2} = sin\theta d\theta d\phi 
```

- Math_AmbientOcclusion_6
```math
\Phi = \frac{dQ}{dt}

```
- Math_AmbientOcclusion_7
```math
I = \frac{d\Phi}{d\Omega}

```

- Math_AmbientOcclusion_8
```math
E = \frac{d\Phi}{dA}

```

- Math_AmbientOcclusion_9
```math
L = \frac{dE}{d\Omega \space cos\theta}= \frac{dI}{dA \space cos\theta} = \frac{d^2\Phi}{d\Omega \space dA \space cos\theta}

```


- Math_AmbientOcclusion_10
```math
L_o(\bold p, \bold v) =  L_e(\bold p, \bold v) + \int_{l\in\Omega} f(\bold l, \bold v)L_i(\bold p, \bold l)(\bold n \cdot \bold l)d\bold l

```