## to activate the virtual environemnt
- source /fypenv/bin/activate

## to install all the dependencies use

- for windows and Linux
  pip install -r requirements.txt
- for mac
  pip3 install -r requirements.txt

# API call model
- http://127.0.0.1:5000/nlp/1234?text_a=some text here&text_b=some text there
- here the /nlp is the endpoint and after endpoint, you give your user_id. (right now only 1234). then you enter text_a and text_b upon whom you want to apply working
