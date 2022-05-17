/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints: 1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
*/
package main

import (
	"fmt"
)
// I: 73, V: 86, X: 88, L: 76, C: 67, D: 68, M: 77  
// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

func romanToInt(s string) int {
	var add int = 0
	var next int = 0

	roman_value := make(map[int]int)
	roman_value[73] = 1
	roman_value[86] = 5
	roman_value[88] = 10
	roman_value[76] = 50
	roman_value[67] = 100
	roman_value[68] = 500
	roman_value[77] = 1000
	

	value := 0
	for i:=0; i < len(s); i++ {

		add = roman_value[int(s[i])]

		if i != len(s)-1 {
			next = roman_value[int(s[i+1])]
			switch {
				case add == 1:
					if next == 5 {
						add = 4
						i++
					} else if next == 10 {
						add = 9
						i++
					} 
				case add == 10:
					if next == 50 {
						add = 40
						i++
					} else if next == 100 {
						add = 90
						i++
					} 
				case add == 100:
					if next == 500 {
						add = 400
						i++
					} else if next == 1000 {
						add = 900
						i++
					} 
			}
		}
		value += add
		}
	return value
	}

func main(){
	s := "III"
	out:= romanToInt(s)
	fmt.Println(out)
	fmt.Println("---")

	s = "LVIII"
	out = romanToInt(s)
	fmt.Println(out)
	fmt.Println("---")

	s = "MCMXCIV"
	out = romanToInt(s)
	fmt.Println(out)
}
