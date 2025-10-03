## Hash tables
Hash function is a function where you put in a string(any kind of data-sequence of bytes) and you get back a number
They map strings to numbers

# Example
Start with an empty array
[0,1,2,3,4]
You'll store all your prices in this array, add price of mango to the hash function
mango -> 3
The hash function outputs "3" so let's store the price of an apple 
at index 3 in the array

tomato -> 0
The hash function says 0 let's store the price of milk at index 0

Pears -> 4
The hash function says 4, let's store the price of pears at index 4

guava -> 2
The hash function says 2, let's store the price of guava at index 2

pineapple -> 1
The hash function says 1, let's store the price of pineapple at index 1

Now the whole array is full of prices
[1.54, 1.52, 8.91, 3.01, 4.34]

Python hash tables are called dictionaries, you can make a new hash table using empty braces

book = {}

book is a new hash table, let's add some prices to book
book{"apple"} = 0.66
book{"milk"} = 0.45
book{"avocado"} = 1.49
print(book)
 {'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}

 Now suppose you want to find milk, just pass the key in to the hash
 print(phone_book["milk"])
 0.45