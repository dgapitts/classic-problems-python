def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for step in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
        print( str(pi) + " - interim result at sequence step  "  +str(step)  )
    return pi

if __name__ == "__main__":  
    print(calculate_pi(1000000))
