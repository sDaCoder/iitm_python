mat = [[1, 2], [3, 4]]

num_words = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'
}

def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    
    string = ""
    for rows in mat:
        for i in range(len(rows)):
            string += f"{num_words[rows[i]].lower()},"
        string = string[:-1]
        string += '\n'

    string = string.strip()
    f = open("words.csv", "w")
    f.write(string)
    return string
        
print(num_to_words(mat))
