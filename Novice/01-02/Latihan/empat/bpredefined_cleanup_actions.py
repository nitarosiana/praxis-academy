#for line in open("myfile.txt"):
 #   print(line, end="")

print('===============================')
with open("myfile.txt") as f:
     for line in f:
         print(line, end="")