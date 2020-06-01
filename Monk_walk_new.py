'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

class Error(Exception):
   """Base class for other exceptions"""
   pass

class TestCaseER(Error):
   """Raised when the input value for test cases is zero"""
   pass

def main():
    try:
        T = int(input())
        if T == 0:
            raise TestCaseER
        else:
            i = 0
            vowels = ['a', 'e', 'i', 'o', 'u']
            while i < T:
                st = input()
                count = 0
                for j in vowels:
                    count += st.lower().count(j)
                i = i+1
                print(count)

    except TestCaseER:
        print("Please use minimum 1 test case.")
    except ValueError:
        print("Please provide numeric values in each input")      

main()
