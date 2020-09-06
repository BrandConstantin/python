def split_and_join(line):
    # write your code here
    spliting = line.split()
    newLine = "-".join(spliting)
    return newLine

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# print raw_input().replace(" ","-")