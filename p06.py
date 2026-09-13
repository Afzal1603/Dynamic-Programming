import sys
from collections import *

def solve(n):
	dp=[-1]*(n+1)
	def helper(n):
		if n<=0:
			return 0
		if n==1 or n==2:
			return 1
		if dp[n]!=-1:
			return dp[n]
		dp[n]=helper(n-1)+helper(n-2)+helper(n-3)
		return dp[n]
	return helper(n)


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	print(solve(n))



if __name__=="__main__":
	main()