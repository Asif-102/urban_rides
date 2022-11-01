import hashlib

email = 'xyz@gmail.com'
pwd = 'Password'

pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = 'xyz@gmail.com'
your_password = 'Password' # dc647eb65e6711e155375218212b3964

hashed_your_password = hashlib.md5(your_password.encode()).hexdigest()
if email == your_email and pwd_hash == hashed_your_password:
    print('right user')
else:
    print('wrong password')

hacker_email = 'xyz@gmail.com'
hacker_password = 'dc647eb65e6711e155375218212b3964'

print(pwd)
print(pwd_hash)
