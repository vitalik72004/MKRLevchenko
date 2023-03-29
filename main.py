# відкриваємо файли для зчитування

f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')

def readdata(f):
    # зчитуємо вміст файлів
    f_lines = []
    for line in f:
        f_lines.append(line)
    return f_lines