class Solution:
  def romanToInt(self, s: str) -> int:
      n = 0
      nums = {'I': 1, 'IV': 4, 'V': 5, 'VI': 6, 'IX': 9,
              'X': 10, 'XL': 40, 'L': 50, 'LX': 60,
              'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
              'DC': 600, 'CM': 900, 'M': 1000}
      while s:
          d = s[:2]
          s = s[2:]
          if d in nums:
              n += nums[d]
          else:
              d1, d2 = d[0], d[1]
              n += nums[d1]
              if d2:
                  s = d2 + s
      return n

sol = Solution()

roman_numeral = input("Enter a Roman numeral: ")

result = sol.romanToInt(roman_numeral)

print(f"The integer value is: {result}")

