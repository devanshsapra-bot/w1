def triplet(n):
    return [(a, b, c) 
            for c in range(n) 
            for a in range(c) 
            for b in range(a, c)  # b starts from a to avoid (b,a,c)
            if a + b == c]
