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

class InputER(Error):
   """Raised when the input string counts are more than test cases"""
   pass

def main():
    try:
        T = input().split()
        print(T)
        if int(T[0]) == 0:
            raise TestCaseER
        elif len(T)-1 > int(T[0]):
            raise InputER
        else:
            count = 0
            vowels = ['a', 'e', 'i', 'o', 'u']
            for i in range(1, len(T)):
                st = T[i]
                for j in vowels:
                    count += st.count(j)
                print(count)

    except TestCaseER:
        print("Please use minimum 1 test case.")
    except InputER:
        print("Please provide exact number of strings you have  provided for testing.")
    except ValueError:
        print("Please provide numeric values in each input")      

main()
