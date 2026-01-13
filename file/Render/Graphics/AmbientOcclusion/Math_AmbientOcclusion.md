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
L_o(\bold p, \bold v) =  L_e(\bold p, \bold v) + \int_{\bold l\in\Omega} f(\bold l, \bold v)L_i(\bold p, \bold l)(\bold n \cdot \bold l)d\bold l

```

- Math_AmbientOcclusion_11
```math
E = \int_{\Omega} L \space cos\theta \space d \Omega =\int_0^{2\pi}  \int_0^{\frac{\pi}{2}} L' cos\theta sin\theta \space d{\theta} d{\phi} =  \pi L'

```

- Math_AmbientOcclusion_12
```math
E =  L' \int_{\Omega}\space v cos\theta \space d \Omega

```

- Math_AmbientOcclusion_13
```math
k =  \int_{\Omega}\space v cos\theta \space d \Omega
```

- Math_AmbientOcclusion_14
```math
k_{max} = \int_{\Omega}\space 1 \cdot cos\theta \space d \Omega = \pi
\\\
\\\
k_{min} = \int_{\Omega}\space 0 \cdot cos\theta \space d \Omega = 0
```

- Math_AmbientOcclusion_15
```math
k' = \frac{1}{\pi} \int_{\Omega}\space v cos\theta \space d \Omega
```



