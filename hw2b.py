import math
# as described on https://byjus.com/maths/secant-method/
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Using the secant method to find the root values between the points x0 and x1.
    """
    for _ in range(maxiter):
        fx_0 = fcn(x0)
        fx_1 = fcn(x1)
        if abs(fx_1 - fx_0) < 1e-10:  # Use a very small number to avoid division by zero
            return None  # Bail out if we get a very small denominator
        x2 = x1 - fx_1 * (x1 - x0) / (fx_1 - fx_0)  # Standard secant formula
        if abs(x2 - x1) < xtol:
            return x2
        x0, x1 = x1, x2  # Update x0 and x1 for the next iteration, tried to make this a loop initially...*Big Sigh*
    return x1  # Estimation of the root after max iterations

def main():
    """
    Using the provided functions to call out the Secant definition and printing the results.
    """
    fa = lambda x: math.cos(2 * x) * x**3
    fb = lambda x: x - 3 * math.cos(x)

    # Applying Secant method to find roots of the first function with specified parameters
    print("Finding root for the function: cos(2x) * x^3 = 0")
    root1 = Secant(fa, x0=1, x1=2, maxiter=5, xtol=1e-4)
    print(f"Root with maxiter=5 and xtol=1e-4: {root1}")

    # Applying Secant method to find roots of the second function with different parameters
    print("\nFinding root for the function: x - 3cos(x) = 0")
    root2 = Secant(fb, x0=0.1, x1=2, maxiter=15, xtol=1e-8)
    print(f"Root with maxiter=15 and xtol=1e-8: {root2}") #changing the default value of iterations from 10 to 15

if __name__ == "__main__":
    main()
# used LlamaGPT to fix some minor syntax errors, it provided output for lines 26-28 because I got lazy