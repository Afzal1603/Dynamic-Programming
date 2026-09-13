import sys
from collections import *

def solve(n,t,arr):
	dp=[-1]*(t+1)
	def helper(t):
		if t==0:
			return 1
		if dp[t]!=-1:
			return dp[t]
		ans=0
		for x in arr:
			if t>=x:
				ans+=helper(t-x)
		dp[t]=ans
		return ans
	return helper(t)



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n,t=map(int,input().split())
	arr=list(map(int,input().split()))
	print(solve(n,t,arr))



if __name__=="__main__":
	main()