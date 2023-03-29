# відкриваємо файли для зчитування

f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')

def readdata(f):
    # зчитуємо вміст файлів
    f_lines = []
    for line in f:
        f_lines.append(line)
    return f_lines

def same(f1, f2):
    same_lines = []
    for line in f1:
        if line in f2:
            same_lines.append(line)
    return same_lines


    # зчитуємо вміст файлів
f1_lines = readdata(f1)
f2_lines = readdata(f2)