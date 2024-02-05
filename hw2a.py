import math

def PDF(x, mu, sigma):
    """
    Probability density function for a Gaussian distribution.

    :param x: The variable.
    :param mu: Mean of the distribution.
    :param sigma: Standard deviation of the distribution.
    :return: The probability density function evaluated at x.
    """
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def Simpsons(f, a, b, n):
    """
    Numerical integration using Simpson's 1/3rd rule.

    :param f: The function to integrate.
    :param a: Lower limit of the integral.
    :param b: Upper limit of the integral.
    :param n: Number of (even) interval steps from a to b.
    :return: An estimated value of the integral.
    """
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)

    # Print the value of `h` for debugging before returning the result
    # print(f"This is the value for h: {h:.4f}")
    return s * h / 3

def Probability(PDF, args, c, GT=True):
    """
    Calculates the probability for a given condition and distribution.

    :param PDF: Probability density function (callback).
    :param args: Tuple containing mu and sigma.
    :param c: Limit of integration.
    :param GT: Boolean indicating if calculating for x > c.
    :return: The calculated probability.
    """
    mu, sigma = args

    if GT:
        a, b = c, mu + 5 * sigma
    else:
        a, b = c, mu - 5 * sigma

    n = 100  # Number of intervals
    integral = Simpsons(lambda x: PDF(x, mu, sigma), a, b, n)
    return integral if GT else -integral

def main():
    """
    Function to demonstrate the use of the Probability function
    with specific values for mu, sigma, and c.
    """
    mu_sigma_pairs = [(100, 12.5), (100, 3)]
    conditions = [False, True]  # Less than for the first, greater than for the second

    #asked my llamaGPT to give me a better way to ouptut the parameters, discovered zip funcitons
    #yay learning new things
    for (mu, sigma), condition in zip(mu_sigma_pairs, conditions):
        # Dynamically calculate c based on the condition, this matched the requirements better than what is commented
        # c_values = [105, 100 + 2 * sigma]
        c = 105 if not condition else mu + 2 * sigma
        prob = Probability(PDF, (mu, sigma), c, GT=condition)
        print(f"P(x{'>' if condition else '<'}{c}|N({mu},{sigma}))={prob:.4f}")

if __name__ == "__main__":
    main()
