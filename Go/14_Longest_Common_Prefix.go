/*
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
*/
package main

import (
	"fmt"
	"sort"
)

func longestCommonPrefix(strs []string) string {
	sort.Slice(strs, func(i, j int) bool {
        return len(strs[i]) < len(strs[j])
    })

	num := len(strs) // how many words in the slice.
	var fir string // answer
	word := len(strs[0])
	for i := 0; i < word; i++ {
		for j := 0; j < num; j++ {
			if strs[0][i] != strs[j][i]{
				return fir
			}
		}  
		fir += string(strs[0][i])
	}

	return fir
}


func main(){

	strs := []string{"flower", "flow", "flight"}
	output := longestCommonPrefix(strs)
	fmt.Println(output)

	strs = []string{"dog", "racecar", "car"}
	output = longestCommonPrefix(strs)
	fmt.Println(output)

	strs = []string{"ab", "a"}
	output = longestCommonPrefix(strs)
	fmt.Println(output)
}

