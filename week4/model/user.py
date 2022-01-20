class User:
    def __init__(
        self,
        email = "None",
        username= "None",
        name_surname = "None",
        emailuserlk = "0",
        usernamelk = "0",
        birth_year = "1900",
        birth_month = "01",
        birth_day = "01",
        country = "None",
        active_passive = 1):

        self.email = email
        self.username = username
        self.name_surname = name_surname
        self.emailuserlk = emailuserlk
        self.usernamelk = usernamelk
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.country = country
        self.active_passive = active_passive
