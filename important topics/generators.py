

def generatorExample():
    yield '😈 '
    yield '🀄 '
    yield '🔥 '


if __name__ == '__main__':
    for iterativeItem in generatorExample():
        print(iterativeItem)
