import sys
from collections import *

def solve(n,arr):

	def rob(nums):
		t=len(nums)
		dp=[-1]*(t+1)
		def helper(i):
			if i>=t:
				return 0
			if dp[i]!=-1:
				return dp[i]
			dp[i]= max(nums[i]+helper(i+2),helper(i+1))
			return dp[i]
		return helper(0)
	return max(rob(arr[1:]),rob(arr[:-1]))



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	arr=list(map(int,input().split()))
	print(solve(n,arr))
if __name__=="__main__":
	main()