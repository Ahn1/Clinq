import logging
from flask import Flask

def Info():
	return {
		"name": "web-main",
		"version": "0.1",
		"core": False
	}

def Register(app):
	pass