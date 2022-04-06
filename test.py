import filecmp

d1 = "E:\test\test1.txt"
d2 = "E:\test\test2.txt"
files = ['intro.txt']

# shallow comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
print('Shallow comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)

# deep comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
print('Deep comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)