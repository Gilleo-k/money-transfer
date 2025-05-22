""" 
f =open('test.txt', 'w')

f.close
"""
""" 
with open('test.txt', 'a') as f:  # w, r, a ==> t or b
    f.write("\nThe first line")
"""
with open('test.txt', 'r') as f1:
    content = f1.readlines()
    print(content)
    
with open('test.txt', 'w') as f2:
    for line in content:
        if 'image' in line:
            f2.write("image: httpd")
        else:
            f2.write(line)