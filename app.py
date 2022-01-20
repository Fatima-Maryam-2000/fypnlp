from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/nlp/<user_id>', methods=['POST'])
def name(user_id):
    # validate user id
    if (validate(user_id=user_id)):
        text_a = request.args.get("text_a")
        text_b = request.args.get("text_b")
        return str(similarityCheck(text_a, text_b))
    return "Invalid User, Event will be logged"


def validate(user_id):
    # validation here
    if (user_id == str(1234)):
        print("User " + str(user_id) + " authentication")
        return True
    print("User " + str(user_id) + " unauthorized")
    logger("Log this bhaiya g 😁")
    return False


def similarityCheck(ideaA, ideaB):
    # nlp algorithm here 😃
    # store similarity check score in 'score variable here'
    score = 97.9
    return score


def logger(loggedText):
    # logging code here
    print("Logging: " + str(loggedText))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="3000")
