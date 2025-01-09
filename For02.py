def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    st=''
    for i in range(0,n):
        st+=str(i)+', '
    return st
n=10
print(main(n))