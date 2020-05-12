def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type n: int,>=0
    :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError
    elif x < 0:
        raise ValueError
    if x in (0, 1):
        return tuple([x])
    fact_list = []
    while x != 1:
        for i in range(2, x+1):
            if x % i == 0:
                fact_list.append(i)
                x //= i
    return tuple(fact_list)


if __name__ == "__main__":
    print(factorize(0))

