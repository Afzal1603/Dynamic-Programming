import sys
from collections import *

def solve(n,arr):
	total=sum(arr)
	target=total//2
	dp = [[None] * (target + 1) for _ in range(n + 1)]

	def helper(i,s):
		if s==0:
			return True
		if i==0:
			return False
		if dp[i][s]!=None:
			return dp[i][s]
		ans=helper(i-1,s)
		if s>=arr[i-1]:
			ans =ans or helper(i-1,s-arr[i-1])
		dp[i][s]=ans
		return dp[i][s]

	helper(n,target)
	best=0
	for s in range(target+1):
		if helper(n,s):
			best=s
	return total-2*best


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	arr=list(map(int,input().split()))
	print(solve(n,arr))


if __name__=="__main__":
	main()