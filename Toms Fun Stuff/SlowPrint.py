def SlowPrint(inputword, time=0.01):
    import time
    import os
    temp = ""
    for letter in inputword:
        temp += letter
        print(temp)
        time.sleep(0.1)
        os.system("clear")
    print(temp)
