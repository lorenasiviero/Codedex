#Python Built-in List Methods:
# 1. append() - Adds an element to the end of the list
# 2. clear() - Removes all elements from the list
# 3. copy() - Returns a shallow copy of the list
# 4. count() - Returns the number of occurrences of a specified value
# 5. extend() - Adds the elements of a list (or any iterable), to the end of the current list
# 6. index() - Returns the index of the first element with the specified value
# 7. insert() - Adds an element at the specified position
# 8. pop() - Removes the element at the specified position
# 9. remove() - Removes the first item with the specified value
# 10. reverse() - Reverses the order of the list
# 11. sort() - Sorts the list
#

#Example of using the list methods
#dna = ['AUG', 'AUC', 'UCG']
#dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
#dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
#dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
#dna.pop(0)            # ['GAU', 'UCG', 'UAA']


books = ['Harry Potter',
         '1984',
         'The Fault in Our Stars',
         'The Mom Test',
         'Life in Code']

print(books)

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)