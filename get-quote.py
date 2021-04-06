import random


def primary():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print("我是第一行：" + quotes[0])
    print("我是第最后一行：" + quotes[13])
    print("我是第最后一行：" + quotes[len(quotes) - 1])
    print("123456")
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(rnd)
    print(quotes[rnd])


if __name__ == "__main__":
    primary()
