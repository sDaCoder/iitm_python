def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    numbers1: list[str] = f1.read().strip().split("\n")
    numbers2: list[str] = f2.read().strip().split("\n")

    if(len(numbers1) == len(numbers2) and numbers1 == numbers2):
        return 'Equal'

    else:
        j: int = 0
        for i in range(len(numbers1)):
            if numbers1[i] != numbers2[j]:
                return 'No Relation'
            j += 1
        return 'Subset'
    
print(relation("public_1_1.txt", "public_1_2.txt"))