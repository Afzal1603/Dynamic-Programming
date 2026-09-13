import sys
from collections import *


def solve(n,W,w,v):
	dp=[[-1]*(W+1) for _ in range(n+1)]
	def helper(n,W):
		if n==0 or W==0:
			return 0
		if dp[n][W]!=-1:
			return dp[n][W]
		ans=helper(n-1,W)
		if W>=w[n-1]:
			ans=max(ans,v[n-1]+helper(n-1,W-w[n-1]))
		dp[n][W]=ans
		return dp[n][W]
	return helper(n,W)



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n,W=map(int,input().split())
	w=list(map(int,input().split()))
	v=list(map(int,input().split()))
	print(solve(n,W,w,v))


if __name__=="__main__":
	main()