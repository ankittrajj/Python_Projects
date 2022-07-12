import yagmail

user = 'your_username@gmail.com'
app_password = 'your_app_password' # a token for gmail
to = 'your_recipent@gmail.com'

subject = 'test subject 1'
content = ['mail body content','pytest.ini','test.png']

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully')