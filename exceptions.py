import sys

lists = ['a',0,4]

for each in lists:
    try:
        print("masukkan",each)
        r = 1/int(each)
        break
    except:
        print("uppss",sys.exc_info()[0],"terjadi.")
        print("masukkan berikiutnya.")
        print()
print("kembalikan dari",each, "=",r)