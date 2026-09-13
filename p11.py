import sys
from collections import *


def solve(n,triangle):
	dp=[]
	for i in range(n):
		dp.append([-1]*len(triangle[i]))
	def helper(i,j):
		if i==n-1:
			return triangle[i][j]
		if dp[i][j]!=-1:
			return dp[i][j]
		right=helper(i+1,j+1)
		down=helper(i+1,j)
		dp[i][j]=triangle[i][j]+min(down,right)
		return dp[i][j]
	return helper(0,0)


def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	triangle=[]
	for _ in range(n):
		temp=list(map(int,input().split()))
		triangle.append(temp)
	print(solve(n,triangle))


if __name__=="__main__":
	main()