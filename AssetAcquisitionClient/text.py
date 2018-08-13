"--wallace--"

def dec(fun):
    def wreaper(*args,**kwargs):
        fun(args[0])
        print("aaa")
        return 'ccc'
    return wreaper

@dec
def text(a):
    print(a)

# text('a')