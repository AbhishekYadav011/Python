def checkprimenum(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                print("its not a prime number")
        else:
            print("Its a prime number")
    else:
        print("its not a prime number")


if __name__ == "__main__":
    checkprimenum(23)
