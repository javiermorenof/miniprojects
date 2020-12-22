import string
import numpy as np

def generate_passwords(lenght=20, special_characters=True):
    
    letters = string.ascii_letters
    numbers =  string.digits
    punctuation = string.punctuation
    
    if special_characters == True:
        elements = letters + numbers + punctuation
    else:
        elements = letters + numbers
    
    passwd = np.random.choice(list(elements), lenght, replace=True)
    password = str()
    
    for k in passwd:
        password += str(k)
    
    return password

if __name__ == "__main__":
    print(generate_passwords())