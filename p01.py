import sys
from collections import *


def solve(n):
	dp=[-1]*(n+1)
	def helper(n):
		if n==1 or n==2:
			dp[n]=n
			return n
		if dp[n]!=-1:
			return dp[n]
		dp[n]= helper(n-1)+helper(n-2)
		return dp[n]
	ans=helper(n)
	print(dp)
	return ans

def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	print(solve(n))
	



if __name__=="__main__":
	main()