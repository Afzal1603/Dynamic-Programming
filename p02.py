import sys
from collections import *

def solve(n,arr):
	dp=[-1]*(n)
	def helper(i):
		if i>=n:
			return 0
		if dp[i]!=-1:
			return dp[i]
		dp[i]=arr[i] + min(helper(i+1),helper(i+2))
		return dp[i]
	ans= min(helper(0),helper(1))
	return ans


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	arr=list(map(int,input().split()))
	print(solve(n,arr))

if __name__=="__main__":
	main()