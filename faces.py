def main():
    x = input()
    x2 = convert(x)
    print(x2)

def convert(str1):
    str1 = str1.replace(':)', '\N{Slightly Smiling Face}')
    str1 = str1.replace(':(', '\N{Slightly Frowning Face}')
    return str1
if __name__=="__main__":
    main()
