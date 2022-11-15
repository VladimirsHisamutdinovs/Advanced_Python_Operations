names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

print(len(names))

for index, item in enumerate(names):
    print(index, item)

### traverse non-recursively

def count_leaf_items(item_list):
    count = 0
    stack = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

### recur

def count_leaf_items(item_list):
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("if sublist")
            count += count_leaf_items(item)
        else:
            print(f"leaf item \"{item}\"")
            count += 1

    print(f"-> count is {count}")
    return count

if __name__ == '__main__':
    print(count_leaf_items([]))
    print(count_leaf_items([1, 2, 3, 4, 5]))
    print(count_leaf_items([1, [2.1, 2.2], 3, [4.1, 4.2], 5]))
    
    print(count_leaf_items(names))

   
