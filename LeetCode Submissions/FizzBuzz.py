'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        if n == 1:
            return ["1"]
        for x in range(1,n+1):
            if x % 3 == 0 and x%5 == 0:
                output.append("FizzBuzz")
            elif x % 3 == 0:
                output.append("Fizz")
            elif x % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(x))
        return output
                
            
            
            