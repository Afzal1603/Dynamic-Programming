import sys
from collections import *

def solve(n,amt,coins):
	dp=[[-1]*(amt+1) for _ in range(n+1)]
	def helper(n,a):
		if a==0:
			return 1
		if n==0:
			return 0
		if dp[n][a]!=-1:
			return dp[n][a]
		ans=helper(n-1,a)
		if a>=coins[n-1]:
			ans=ans+helper(n,a-coins[n-1])
		dp[n][a]=ans
		return ans
	ans=helper(n,amt)
	return ans


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n,amt=map(int,input().split())
	coins=list(map(int,input().split()))
	print(solve(n,amt,coins))



if __name__=="__main__":
	main()