#.......Modular Exponentiation (Efficient a^b % m Calculation)......
def mod_exp(base, exp, mod):
    stack = []
    while exp > 0:
        stack.append(exp % 2)
        exp //= 2
    result = 1
    while stack:
        bit = stack.pop()    
        result = (result * result) % mod
        if bit == 1:
            result = (result * base) % mod
    return result        
print(mod_exp(5, 3, 13))



























    