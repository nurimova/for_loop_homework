def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    for _ in range(n):
        s.append(k)
    return s
k=5
n=4
print(main(k,n))