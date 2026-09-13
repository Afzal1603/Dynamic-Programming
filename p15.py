import sys
from collections import *


def solve(n,S,arr):
	dp=[[None]*(S+1) for _ in range(n+1)]
	def helper(n,S):
		if S==0:
			return True
		if n==0:
			return False
		if dp[n][S]!=None:
			return dp[n][S]
		ans=helper(n-1,S)
		if S>=arr[n-1]:
			ans=ans or helper(n-1,S-arr[n-1])
		dp[n][S]=ans
		return dp[n][S]
	return helper(n,S)



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n,S=map(int,input().split())
	arr=list(map(int,input().split()))
	print(solve(n,S,arr))


if __name__=="__main__":
	main()