import json
from constants.messages import CustomMessages
from helpers.location_helper import LocationHelper
from helpers.regex_helper import RegexHelper
from model.user import User

class FileHelper:
    regexHelper = RegexHelper()
    locationHelper = LocationHelper()
    
    def scrapJsonFile(self, path):
        userList = list()

        try:
            with open(path) as jsonFile:
                allJsonDatas = json.load(jsonFile)

                for data in allJsonDatas:
                    user = User()

                    user.email = data["email"]
                    user.username = data["username"]
                    user.name_surname = data["profile"]["name"]

                    user.country = self.getCountry(data["profile"]["location"]["lat"], data["profile"]["location"]["long"])

                    user.birth_day = self.getBirthInfo(data["profile"]["dob"])["day"]
                    user.birth_month = self.getBirthInfo(data["profile"]["dob"])["month"]
                    user.birth_year = self.getBirthInfo(data["profile"]["dob"])["year"]

                    user.usernamelk = self.isUserNamelk(user.username, user.name_surname)
                    user.emailuserlk = self.isEmailUserlk(user.email, user.username)

                    userList.append(user)
        except:
            print(CustomMessages.JSON_FILE_ERROR)

        return userList

    def getBirthInfo(self,date):
        birthDate = self.regexHelper.parseBirthDate(date)
        return birthDate

    def isEmailUserlk(self, email, username):
        username = self.regexHelper.parseUsername(username)
        email = self.regexHelper.parseEmail(email)

        return "1" if username in email else "0"
        
    def isUserNamelk(self, username, name_surname):
        name_surname = name_surname.lower().split()
        name = self.regexHelper.parseUsername(username)

        return "1" if name in name_surname else "0"

    def getCountry(self, latitude, longitude):
        country = self.locationHelper.getLocation(latitude, longitude)
        return country


        
       