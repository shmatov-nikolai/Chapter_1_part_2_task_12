'''
Given a string that may or may not contain a letter of interest. Print the index
location of the first and last appearance of f. If the letter f occurs only once,
then output its index. If the letter f does not occur, then do not print anything.
Don't use loops in this task.
'''

string = "Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f."

if 'f' in string:
    index = string.find('f')
    index_2 = string.rfind('f',)
    if index == index_2:
        print(f'Только одно совпадение, индекс: {index}')
    elif index != index_2:
        print (f"индекс с начала: {index}, индекс с конца: {index_2}")


