
primeFile = open('task_8_file.txt')
content = primeFile.read()[::-1]
primeFile.seek(0)
newFile = open('new_file.txt', 'w+')
newFile.write(content)
newFile.seek(0)

print(primeFile.read())
primeFile.close()

print(newFile.read()[::-1])
newFile.close()