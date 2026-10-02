import math

def main() -> int:
    """The main entry point of the program. 
    Returns an integer exit code (0 for success).
    """
    print("value  Mersenne Prime")
    for i in range(32):
        if is_prime(i) is True:
            print(str(i) + "      " + str(is_prime(((1<<i)-1))))
            #print(i)
            
    # Return 0 for success, or any non-zero integer for errors
    return 0 

def is_prime(n: int):
    # 1 or less are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def test_Mn_prime():
    assert is_prime(((1<<31)-1)) == True

if __name__ == "__main__":
    # sys.exit captures the returned integer and passes it to the OS
    main()
