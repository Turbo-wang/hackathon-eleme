#!/usr/bin/env python
# encoding: utf-8

import web
import urllib
import sys

paths = (
    '/login', 'Login',

)
i
class Login:
    def GET(self):

    def POST(self, request):
        name = request.POST.get("username", "")
        pwd = request.POST.get("password", "")
        if name and pwd:




