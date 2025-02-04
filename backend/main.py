from flask import request, jsonify
from config import app, db
from models import UserPasswords
from save_data import logData

# als je deze url bezoekt word de functie eronder opgeroepen
@app.route("/get_paswords", methods=["GET"])
def get_paswords():
    # haal alle huidige data
    data = UserPasswords.query.all()

    # zet alles om naar json
    passwords = list(map(lambda x: x.to_json(), data))
    return jsonify({"paswords": passwords}), 200

# post om duidelijk te maken dat we iets toevoegen aan onze database
@app.route("/post_new_user", methods=["POST"])
def post_new_user():
    # try except om errors goed te handelen
    try:
        # haal alle gevraagde data op (test
        user_name = request.json.get("userName")
        password = request.json.get("password")
        gender = request.json.get("gender")
        age = request.json.get("age")

        # haal alle huidige data op
        data = UserPasswords.query.all()

        # kijk na of er al een gebruiker is met die naam
        unique_list = list(map(lambda x: (True if x.to_json()["userName"] != user_name else False), data))
        if False in unique_list:
            return jsonify({"message": "username already in use"}), 400

        # maak nieuwe gebruiker aan
        new_user = UserPasswords(user_name=user_name, password=password, gender=gender, age=age)

        # voeg de gebruiker toe aan de database
        db.session.add(new_user)
        db.session.commit()

        # zet de data om naar een txt bestand
        logData(UserPasswords.query.all())
    except Exception as e:
        print(f"something went wrong while adding the user: {e}")
        return jsonify({"message": "something went wrong while adding the user"}), 400

    return jsonify({"message": "user succesfully added"})


if __name__ == "__main__":
    app.run(debug=True)
