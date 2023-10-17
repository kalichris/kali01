#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  amw.py
#  
#  Copyright 2023 root <root@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from playwright.sync_api import sync_playwright
from amazoncaptcha import AmazonCaptcha

class main():
	def __init__(self):
		with sync_playwright() as PW:
			date={
				"url":"https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fr%2520on%2520Amazon.com%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
				"user":"",
				"passwd":""
			}
			brawser=  PW.chromium.launch()
			pg_site= brawser.new_page()
			pg_site.goto(date["url"])
			print("opened %s"%(pg_site.title()))
			pg_site.fill("input#ap_email",date["user"])
			pg_site.click("input[type=submit]")
			pg_site.screenshot(path="screenshot1.png")
			pg_url=pg_site.url
			print("opened %s"%(pg_site.title()))
			print("opened %s"%(pg_url))
			pg_site.wait_for_timeout(6000)
			pg_site.wait_for_selector('img')
			img_element = pg_site.query_selector('img')
			src = img_element.get_attribute('src')
			print("img src %s"%(src))
			captcha = AmazonCaptcha.fromlink(src)
			solution = captcha.solve()
			print("solve »s"%(solution))
			pg_site.fill("input#captchacharacters",solution)
			pg_site.click("button[type=submit]")
			pg_site.screenshot(path="screenshot2.png")
			print("opened %s"%(pg_site.title()))
			print("opened %s"%(pg_url))
			pg_site.wait_for_selector('input#ap_password')
			pg_site.screenshot(path="screenshot2.png")
			pg_site.fill("input#ap_password",date["passwd"])
			pg_site.click("input#signInSubmit")
			print("opened %s"%(pg_site.title()))
			pg_site.screenshot(path="screenshot4.png")

if __name__ == '__main__':
	main()
