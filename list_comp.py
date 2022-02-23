

def main():
    
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    
    even_sq = list(
        map(lambda e: e**2, filter(lambda e: e > 8 and e < 20, even))) 
    print(even_sq)

    even_sq = [e ** 2 for e in even]
    print(even_sq)

    odd_sq = [e ** 2 for e in odd if e > 7 and e < 17]
    print(odd_sq)


if __name__ == "__main__":
    main()