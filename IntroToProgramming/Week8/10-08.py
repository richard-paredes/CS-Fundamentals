if __name__ == "__main__":
    num = 20
    result = ""
    # to get binary numbers
    while(num > 0):

        result = str(num%2) + result
        num = num // 2
    # result[::-1] #-reverses string
    print(result)
