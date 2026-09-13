import sys
from collections import *


def solve(n,target,arr):
	dp={}
	def helper(i,s):
		if i==n:
			return 1 if s==target else 0
		if (i,s) in dp:
			return dp[(i,s)]
		plus=helper(i+1,s+arr[i])
		minus=helper(i+1,s-arr[i])
		dp[(i,s)]=plus+minus
		return dp[(i,s)]
	return helper(0,0)



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n,target=map(int,input().split())
	arr=list(map(int,input().split()))
	print(solve(n,target,arr))


if __name__=="__main__":
	main()