import sys

def irange(start, stop=None, step=1):
    if stop is None:
        stop = int(start)
        num = 1L
    else:
        stop = int(stop)
        num = int(start)
    step = int(step)
    while num < stop:
        yield num
        num += step

def isprime(n):
    n = abs(long(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in irange(3, long(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def is_lucky(num):
    digis = str(num)

    total = 0
    for dig in digis:
        total += long(dig)

    if(isprime(total)):
        total = 0
        for dig in digis:
            total += (long(dig) * long(dig))

        if(isprime(total)):
            return True
    return False

def calc(STDIN):
    T = 0
    A = 0
    B = 0

    for line in STDIN:
        try:
            Count = 0
            
            Start = long(line.split(" ")[0])
            Stop = long(line.split(" ")[1])
            Lng = long(Stop-Start)

            for x in xrange(0, Lng):
                if(is_lucky(x+Start)):
                    Count += 1

            print Count
        except:
            T = line

if(__name__ == "__main__"):
    print "RUNNING LOCAL"

    custSTDIN = list()
    custSTDIN.insert(0, "1 20")
    calc(custSTDIN)

else:
    calc(sys.stdin.readlines())
