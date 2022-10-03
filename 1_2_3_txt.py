
with open("1.txt", encoding='utf-8') as file_obj:
    line1 = len(file_obj.readlines())

with open("2.txt", encoding='utf-8') as file_obj:
    line2 = len(file_obj.readlines())

with open("3.txt", encoding='utf-8') as file_obj:
    line3 = len(file_obj.readlines())


if line1 > line2 and line1 > line3:
    with open("1.txt", encoding='utf-8') as file_obj:
        aaa = file_obj.read()
        if line2 > line3:
            with open("2.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("3.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()
        else:
            with open("3.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("2.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()

if line2 > line1 and line2 > line3:
    with open("2.txt", encoding='utf-8') as file_obj:
        aaa = file_obj.read()
        if line1 > line3:
            with open("1.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("3.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()
        else:
            with open("3.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("1.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()

if line3 > line1 and line3 > line2:
    with open("3.txt", encoding='utf-8') as file_obj:
        aaa = file_obj.read()
        if line1 > line2:
            with open("1.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("2.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()
        else:
            with open("1.txt", encoding='utf-8') as file_obj:
                aaa += file_obj.read()
                with open("2.txt", encoding='utf-8') as file_obj:
                    aaa += file_obj.read()

print(aaa)


