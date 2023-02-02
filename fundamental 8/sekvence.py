#Bubble sort
# numbers = [9,1,3,2,5,8,7]

# print(numbers)
# while True:
#     swapped = False
#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i-1]:
#             temp = numbers[i]
#             numbers[i] = numbers[i-1]
#             numbers[i-1] = temp
#             swapped = True
#     if swapped == False:
#         break

# print(numbers)


# products = ["Phone", "Tv", "Computer"]
# prices = [155.95, 180.35, 199.99]


# for i in range(len(products)):
#     print(products[i], ":", prices[i])


# cars = ["Audi","BMW","Citroen","Kia"]

# for i in range(len(cars)):
#     print("Car:", cars[i])
#     if i == 1:
#         print("I got this piece of shit")


# products = [
#                 ["iphone", "samsung", "shaomi"],
#                 ["dell", "acer", "mac"],
#                 ["ipad", "samsung tab", "shaomi tab"]
#             ]    

# phones = ["iphone", "samsung", "shaomi"]
# laptops = ["dell", "acer", "mac"]
# tablets = ["ipad", "samsung tab", "shaomi tab"]

# # for i in products:
# #     for n in i:
# #         print(n)

# for i in range(len(products)):
#     for j in range (len(products[i])):
#         print(products[i][j])


# food = [
#             ["chocolate", "candy", "cake"],
#             ["chips", "fries", "peanuts"],
#             ["steak", "chicken", "fish"]          
#        ]

# for category in food:
#     for meal in category:
#         print(meal)





library = [
    ["shadows", "autor", 123],
    ["dust", "autor1", 234]
]
is_on = True
while  is_on == True:
    print("Choose command: 1-entry, 2-show, 3-delete, > 3-exit.")
    command = int(input("Enter command: "))

    if command == 1:
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = int(input("Enter ISBN: "))
        library.append([title, author, isbn])
        print("Book added.")

    if command == 2:
        for book in library:
            for detail in book:
                print(detail)
    
    if command == 3:
        keyword = input("What book to delete?: ")
        for book in library:
            for detail in book:
                if detail == keyword:
                    library.remove(book)
                    print("Book deleted.")

    if command > 3:
        is_on = False
