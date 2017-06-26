import sys
import mechanize

br = mechanize.Browser()
br.open("https://www.example.com")

br.select_form(nr=0)

br.form['username'] = 'username'
br.form['password'] = 'password'

response = br.submit()


print 'login success'
