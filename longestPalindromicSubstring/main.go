package main

import "fmt"

// For given string s, longPalindSubstr returns longest palindrome
// that is a substring in s.
// Assumes that palindrome is longer than 1 character.
// Function is case sensitive.
func longPalindSubstr(s string) string {
  var l = len(s)
  palindromeSoFar := ""

  // make rows for 2-D slice
  twoD := make([][]bool, l)

  // make columns for each row
  for i := 0; i < l; i++ {
      innerLen := l
      twoD[i] = make([]bool, innerLen)
      twoD[i][i] = true // diagonal repr. single character
  }

  // for substr of length 2 to l, check if they are a palindrome
  for k := 1; k<=l-1; k++ {
    for i := 0; i<l; i++ {
      j := i+k
      if j >= l {
        break
      }
      if s[i] == s[j] {
        if k==1 || twoD[i+1][j-1] == true{
          twoD[i][j] = true
          palindromeSoFar = s[i:j+1]
        }
      }
    }
  }

  if len(palindromeSoFar) == 0 {
    return "No palindrome found"
  }
  return palindromeSoFar
}

func main() {
  fmt.Println(longPalindSubstr("acat")) //returns aca
}
