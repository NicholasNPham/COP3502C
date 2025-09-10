num = str(input("enter a number: "))
list = []
reversedList = []

for i in num:
    list.append(str(i))

for j in range(l-1, -1, -1):
    reversedList.append(list[j])

l = len(list) # length
counter = 0

while counter < l:
    if reversedList[counter] == list[counter]:
        counter += 1
        if counter == l:
            print(f"{num} is a Palindrome")
            break
    else:
        print(f"{num} is not a Palindromic Number")
        break

