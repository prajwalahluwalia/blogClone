def isPrime(x):
     
    if (x <= 1):
        return False
 
    for i in range(2, x + 1):
        if i * i > x:
            break
         
        if (x % i == 0):
             
            # Return not prime
            return False
 
    # If prime return true
    return True
 
# Function to find the largest prime
# number possible from a subsequence
def largestPrime(s):
 
    # Stores pairs of subsequences and
    # their respective decimal value
    vec = [["", 0]]
     
    # Stores the answer
    ans = 0
 
    # Traverse the string
    for i in range(len(s)):
         
        # Stores the size of the vector
        n = len(vec)
 
        # Traverse the vector
        for j in range(n):
             
            # Extract the current pair
            temp = vec[j]
 
            # Get the binary string from the pair
            str = temp[0]
 
            # Stores equivalent decimal values
            val = temp[1]
 
            # If the current character is '1'
            if (s[i] == '1'):
                 
                # Add the character
                # to the subsequence
                temp[0] = str + '1'
 
                # Update the value by left
                # shifting the current
                # value and adding 1 to it
                temp[1] = ((val << 1) + 1)
 
            # If s[i]=='0'
            else:
 
                # Add the character
                # to the subsequence
                temp[0] = str + '0'
 
                # Update the value by left
                # shifting the current
                # value and adding 0 to it
                temp[1] = ((val << 1) + 0)
 
            # Store the subsequence in the vector
            vec.append(temp)
 
            # Check if the decimal
            # representation of current
            # subsequence is prime or not
            check = temp[1]
 
            # If prime
            if (isPrime(check)):
                 
                # Update the answer
                # with the largest one
                ans = max(ans, check)
                break
 
    # If no prime number
    # could be obtained
    if (ans == 0):
        print(-1)
    else:
        print(ans)
 
# Driver Code
if __name__ == '__main__':
     
    # Input String
    s = "110"
 
    largestPrime(s)