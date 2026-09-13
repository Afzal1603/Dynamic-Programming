import sys
from collections import *

def solve(n,arr):
	ans=arr[0]
	curr=arr[0]
	for i in range(1,n):
		curr=max(arr[i],curr+arr[i])
		ans=max(curr,ans)
	return ans



def main():
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")
	n=int(input())
	arr=list(map(int,input().split()))
	print(solve(n,arr))


if __name__=="__main__":
	main()