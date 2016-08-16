import webapp2
import cgi

form = """
    <h2>Enter some text to ROT13:</h2>
    <form action="/" method="POST">
        <textarea name="text" style="height: 100px; width: 400px;">%(user_input)s</textarea>
        <br>
        <input type="submit">
    </form>
    """


class MainHandler(webapp2.RequestHandler):

    def write_form(self, text=''):
        self.response.write(form % {'user_input':text})

    def get(self):
        #print(self.request)
        self.response.write(form % {'user_input':''})

    def post(self):
        user_input = rot13(self.request.get('text'))
        self.write_form(text=user_input)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)


def rot13(user_input):
    alpha = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
             'k': 'x',
             'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h',
             'v': 'i',
             'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
    resp = ""
    for s in user_input:
        if s.isupper() and s.lower() in alpha:
            resp += alpha.get(s.lower()).upper()
        elif s in alpha:
            resp += alpha.get(s)
        else:
            resp += s
    return cgi.escape(resp)

