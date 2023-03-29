
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

def diff(f1, f2):  # знаходимо рядки, які містяться лише в одному з файлів
    diff_lines = []
    for line in f1:
        if line not in f2:
            diff_lines.append(line)
    for line in f2:
        if line not in f1:
            diff_lines.append(line)
    return diff_lines

def writeinfile(file1, file2):
    for line in file1:
        file2.write(line)
    file2.close()

f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')

f1_lines = readdata(f1)
f2_lines = readdata(f2)

same_fil = same(f1_lines, f2_lines)

diff_fil = diff(f1_lines, f2_lines)

same_file = open('same.txt', 'w')
diff_file = open('diff.txt', 'w')

writeinfile(same_fil, same_file)
writeinfile(diff_fil, diff_file)

f1.close()
f2.close()