
def meter(f):
    def wr(*a, **kw):
        print("pre decore")
        res = f(*a, **kw)
        print("POST decore")
        return res
    return wr


def a1(n):
    print ("body")
    return n**2




print (a1(5),"\n___\n")

a1 = meter( a1 )

print (a1(5))




