#https://www.hackerrank.com/challenges/summing-the-n-series/problem
T=int(input())
for i in range(0,T):
	N=int(input())
	print(N*N%1000000007)
