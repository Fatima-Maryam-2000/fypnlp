from flask import Flask
from flask import request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
app = Flask(__name__)


@app.route('/nlp/<user_id>', methods=['POST'])
def name(user_id):
    # validate user id
    if (validate(user_id=user_id)):
        # in last approach we sent data as query parameter with ?text_a=something&text_b=something
        # as you can see below next two commented lines
        # text_a = request.args.get("text_a")
        # text_b = request.args.get("text_b")
        # now we're sending data as body. so now we select body in thunder client rather than header.
        # header dont support sending of large data body does.
        request_data = request.get_json()
        text_a = request_data["text_a"]
        text_b = request_data["text_b"]
        print(text_a)
        print(text_b)
        return str(similarityCheck(text_a, text_b))
    return "Invalid User, Event will be logged"


def validate(user_id):
    # validation here
    if (user_id == str(1234)):
        print("User " + str(user_id) + " authentication")
        return True
    print("User " + str(user_id) + " unauthorized")
    logger("Log this bhaiya g")
    return False


def similarityCheck(ideaA, ideaB):
    # nlp algorithm here 😃
    # store similarity check score in 'score variable here'
    # Create TF-idf model...//comment///stop_words=token_stop,tokenizer=tokenizer
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform([ideaA] + [ideaB])

    # Calculate similarity
    cosine_similarities = linear_kernel(doc_vectors[0:1],
                                        doc_vectors).flatten()
    document_scores = [item.item() for item in cosine_similarities[1:]]
    # [0.0, 0.287]
    score = 0
    for x in document_scores:
        score = x * 100
        #print(score)

    return score


def logger(loggedText):
    # logging code here
    print("Logging: " + str(loggedText))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
