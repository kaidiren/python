def test(a,b='default b',**c):
    print a
    print b
    print c
    for eachc in c.keys():
        print '%s : %s'%(eachc,str(c[eachc]))

test(1220,74.0,c='gmail')
