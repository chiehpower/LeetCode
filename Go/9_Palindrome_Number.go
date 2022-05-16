package main

import "fmt"

func isPalindrome(x int) bool {
	switch  {
		case x == 0:
			return true
		case x < 0 :
			return false
		case x%10 == 0 :
			return false
	}
	
	a := make([]int, 0, 32)
	for x > 0 {
		a = append(a, x%10)
		x /= 10
	}
	le := len(a)
	// fmt.Println("The len is", le)
	half_le := le/2

	for i:=0; i<half_le; i++ {
		if a[i] != a[le-1-i] {
			return false
		}
	} 

	return true
}

func main(){

	res := isPalindrome(121) // True
	fmt.Println(res)

	res = isPalindrome(9449) // True
	fmt.Println(res)

	res = isPalindrome(1234560) // False
	fmt.Println(res)

	res = isPalindrome(75957) // True
	fmt.Println(res)
}