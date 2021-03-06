import subprocess, socket, nltk, sys

import lib

def parse_sentence(sentence):
    """
    given a textual sentence, returns a parse tree for it
    in string format.
    """
    host = socket.gethostname()
    port = lib.PORT
    s = socket.socket()
    s.connect((host, port))
    s.send(sentence + "\n")
    data = ""
    while (len(data) == 0) or (data[-1] != "\n"):
        data += s.recv(1024)
    ret = data.split("\n")[0]
    t = nltk.tree.Tree(ret)
    return t

def parse(text):
    import nltk.data
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return [parse_sentence(s) for s in tokenizer.tokenize(text)]
