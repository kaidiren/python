def convert(func,seq):
    return [func(eachnum) for eachnum in seq]
myseq=(123,45.6,-6.2e8,999999999L)

print convert(int,myseq)
print convert(long,myseq)
print convert(float,myseq)
