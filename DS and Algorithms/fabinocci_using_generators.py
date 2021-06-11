def fabinocciNo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    limit = int(input("Enter the Range to generate Fabinocci:"))
    fabinoccisSeries = [num for num in fabinocciNo() if num <= limit]
    print(fabinoccisSeries)
    for num in fabinocciNo():
        if num >= limit:
            break
        print(num)
