def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s=[]
    for i in range(1,N+1):
        if i%2==1:
            s.append(i)
            sum1=sum(s)
    return sum1
print(main(8))