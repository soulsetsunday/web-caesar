import webapp2
import caesar
import cgi

def build_page(textarea_content):
    rot_label="<label>Rotate by:</label><br>"
    rotation_input = "<input type='number' name='rotation'> <br>"
    rotation_combined=rot_label+rotation_input
        
    message_label="<label>Type a message</label><br>"
    textarea = "<textarea name='message'>"+textarea_content+"</textarea>"
    message_combined=message_label+textarea
        
    header = "<h2>Web Caesar</h2>"
    submit = "<input type='submit'/>"
    form = "<form method='post'>"+rotation_combined+message_combined+"<br>"+submit+"</form>"
    
    return header+form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)
        
    def post(self):
        message = self.request.get("message")
        rotation = self.request.get('rotation')
        encrypted_message = caesar.encrypt(message, int(rotation))
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
