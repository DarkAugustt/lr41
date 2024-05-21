import random





def string_to_int(s):
    """
    @brief Converts a string to an integer using its ASCII values.
    @param s The input string.
    @return The resulting integer.
    """
    res = 0
    for c in s:
        res = res * 256 + ord(c)
    return res


def int_to_string(n):
    """
    @brief Converts an integer back to a string using its ASCII values.
    @param n The input integer.
    @return The resulting string.
    """
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]


def is_prime(n, num_of_iter=10):
    """
    @brief Tests if a number is prime using the Miller-Rabin primality test.
    @param n The number to test.
    @param num_of_iter The number of iterations for the test (default is 10).
    @return True if the number is likely prime, False otherwise.
    """
    if n % 2 == 0:
        return False
    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1
    for _ in range(num_of_iter):
        a = random.randint(2, n - 1)
        if pow(a, t, n) == 1:
            continue
        i = 0
        while i < s:
            if pow(a, 2 ** i * t, n) == n - 1:
                break
            i += 1
        if i == s:
            return False
    return True


def gen_primes(nbit=80):
    """
    @brief Generates two prime numbers.
    @param nbit The bit length of the primes to generate (default is 80).
    @return A tuple containing two prime numbers.
    """
    while True:
        k = random.getrandbits(nbit)
        p = k ** 6 + 7 * k ** 4 - 40 * k ** 3 + 12 * k ** 2 - 114 * k + 31377
        q = k ** 5 - 8 * k ** 4 + 19 * k ** 3 - 312 * k ** 2 - 14 * k + 14011
        if is_prime(p) and is_prime(q):
            return p, q


def encrypt(msg, n, e=65537):
    """
    @brief Encrypts a message using RSA encryption.
    @param msg The message to encrypt (as an integer).
    @param n The modulus for the RSA encryption.
    @param e The public exponent for the RSA encryption (default is 65537).
    @return The encrypted message.
    """
    return pow(msg, e, n)


# Generate prime numbers p and q
p, q = gen_primes()
n = p * q

# Read the flag from the file and convert to an integer
inf = open("flag.txt", "rt")
flag = inf.read()
flag = string_to_int(flag)
inf.close()

# Encrypt the flag using RSA
enc = encrypt(flag, n)

# Write the encrypted flag and the modulus to the output file
outf = open("output.txt", "wt")
res = "N = " + str(n) + "\nenc = " + str(enc)
outf.write(res)
outf.close()
