import hashlib


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f"{email} {pwd_encrypted}")
        file.close()
        print(self.name, 'user created')

    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
                    print(stored_password)
        file.close()

        hash_password = hashlib.md5(password.encode()).hexdigest()
        if hash_password == stored_password:
            print('valid user')
            return True
        else:
            print('invalid user')
            return False

hero = User('Phitron', 'ph@ph.io', 'Password')
User.log_in('ph@ph.io', 'abc')