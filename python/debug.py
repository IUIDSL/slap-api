#!/usr/bin/env python
#############################################################################
# Works via:
#   http://ec2-54-88-170-209.compute-1.amazonaws.com/rest/slap
# with httpd.conf alias:
#   Alias /rest/slap /var/www/html/rest/slap/debug.py
#
# Jeremy Yang
# 14 Sep 2014
#############################################################################
import sys,os

print "Content-type: text/plain\n\n"
print "Hello, World! This is the SLAP REST API."
