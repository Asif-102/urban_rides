import random

class BRTA:
    def __init__(self):
        self.__license = {}
    
    def driving_test(self, email):
        score = random.randint(0, 100)
        if score >= 33:
            print('congrats, you have passed')
            license_number = random.randint(5000, 9999)
            self.__license[email] = license_number
            return license_number
        else:
            print('sorry you failed')
            return False

    def validate_license(self, email, license):
        for key, value in enumerate(self.__license):
            if key == email and value == license:
                return True
        return False