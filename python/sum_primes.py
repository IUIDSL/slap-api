#!/usr/bin/python
# File: sum_primes.py
# Author: VItalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com

import math, sys, time
import pp

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2,n) if isprime(x)])

def test():
	# tuple of all parallel python servers to connect with
	ppservers = ()
	#ppservers = ("10.0.0.1",)

	if len(sys.argv) > 1:
    		ncpus = int(sys.argv[1])
    		# Creates jobserver with ncpus workers
    		job_server = pp.Server(ncpus, ppservers=ppservers)
	else:
    		# Creates jobserver with automatically detected number of workers
    		job_server = pp.Server(ppservers=ppservers)

	print "Starting pp with", job_server.get_ncpus(), "workers"

	job1 = job_server.submit(sum_primes, (100,), (isprime,), ("math",))

	result = job1()
	print result
	return result

test()
