import string

with open('lesson8/design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='kauzki', sex='men')
print(contents)
