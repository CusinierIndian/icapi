from decorators.decorators import async
from flask_mail import Mail, Message
from flask import render_template
from config import app
class Mailer:
	def __init__(self):
		self.mail = Mail(app)
	@async
	def sendAsyncMail(self, subject, senders, receivers, body, details):
		with app.app_context():
			with self.mail.connect() as conn:
				msg = Message(subject=subject, recipients=receivers, sender=senders)
				msg.html = render_template(body, details=details)
				conn.send(msg)





