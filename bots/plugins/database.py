from pymongo import MongoClient
import pymongo

import traceback

URI ="Your mongodb URI"

class DataBase(object):
	def __init__(self):
		self.client =  MongoClient(URI, ssl=True)
		self.db = self.client.base_line
		self.col = self.db
		
	def add_bot(self, mid, **kwg):
		try:
			data = {
				"_id":mid,
				"other":kwg
			}
			if self.listed(bots=True) == None:
				self.col.bot_db.insert_one(data)
				return True
		except pymongo.errors.DuplicateKeyError:
			return False
	
	def add_group(self, mid: str, **kwg):
		try:
			data = {
				"_id":mid,
				"other":kwg
			}
			if self.listed(groups=True) == None:
				self.col.group_db.insert_one(data)
				return True
		except pymongo.errors.DuplicateKeyError:
			return False
			
	def add_admin(self, mid: str, **kwg):
		try:
			data = {
				"_id":mid,
				"other":kwg
			}
			if mid in self.listed(admin=True) == None:
				self.col.admin_db.insert_one(data)
				return True
		except pymongo.errors.DuplicateKeyError:
			return False
	
	def add_users(self, mid: str, into:str, **kwg):
		try:
			data = {
				"_id":mid,
				"is":into,
				"other":kwg
			}
			if self.listed(users=True) == None:
				self.col.users_db.insert_one(data)
				return True
		except pymongo.errors.DuplicateKeyError:
			return False
	
	def listed(self,
					admin: bool = False,
					bots: bool = False,
					groups: bool = False,
					users: bool = False):

		if admin:return [i["_id"] for i in self.col.admin_db.find()]
		elif bots:return [i["_id"] for i in self.col.bot_db.find()]
		elif groups:return [i["_id"] for i in self.col.group_db.find()]
		elif users:return [i["_id"] for i in self.col.users_db.find()]