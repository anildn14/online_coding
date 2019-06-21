# When you sign up for an account somewhere, some websites do not actually store your password in their databases.
# Instead, they will transform your password into something else using a cryptographic hashing algorithm.

# After the password is transformed, it is then called a password hash. Whenever you try to login, the website
# will transform the password you tried using the same hashing algorithm and simply see if the password hashes
# are the same.

# Create the function that converts a given string into an md5 hash. The return value should be encoded in hexadecimal.

# You will need to use the NodeJS Crypto Module or libcrypto for the C and NASM versions.

# ###Code Examples

# passHash('password')
#   //--> '5f4dcc3b5aa765d61d8327deb882cf99'

# passHash('abc123')
#   //--> 'e99a18c428cb38d5f260853678922e03'
# If you want to externally test a string, look at this website.

# If you are completely lost, I recommend you check out my previous Introduction to NodeJS.

# As a side note, md5 can be exploited, so never use it for anything secure. The reason I used it in this kata
# is simply because it is a very common hashing algorithm and many people will recognize the name.

import hashlib
def pass_hash(str):
    return hashlib.md5(str).hexdigest()
    return hashlib.md5(str.encode()).hexdigest()


def pass_hash(str):
    return __import__('hashlib').md5(str.encode('utf-8')).hexdigest()

import hashlib
def pass_hash(str):
    return hashlib.md5(str.encode("utf")).hexdigest()

print pass_hash('password')
print pass_hash('abc123')