def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    s=[]
    for i in list1:
        s.append(i.capitalize())
    return s
list1=['rustam', 'diyor', 'alisher', 'bektosh']
print(main(list1))