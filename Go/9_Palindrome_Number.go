/*
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints: -231 <= x <= 231 - 1
 
Follow up: Could you solve it without converting the integer to a string?
*/
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

	res = isPalindrome(-121) // False
	fmt.Println(res)

	res = isPalindrome(1234560) // False
	fmt.Println(res)

	res = isPalindrome(75957) // True
	fmt.Println(res)
}