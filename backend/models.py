from config import db, app


class UserPasswords(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # zodat sql de data kan terugvinden
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(70), nullable=False, unique=True)
    gender = db.Column(db.String(25), nullable=True)
    age = db.Column(db.Integer, nullable=False)

    # om de data in de juiste format te steken zodat je het via json kan versturen
    def to_json(self):
        return {
            "userName": self.user_name,
            "password": self.password,
            "gender": self.gender,
            "age": self.age
        }
