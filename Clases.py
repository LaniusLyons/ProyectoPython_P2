class Devices:
	def __init__(self,device_list=None):
		if device_list is None:
			self.device_list=[]
		else:
			self.device_list=device_list
			
class Device:
	def __init__(self,id=None,user_agent=None,fall_back=None,groups_list=None):
		self.id=id
		self.user_agent=user_agent
		self.fall_back=fall_back
		if groups_list is None:
			self.groups_list=[]
		else:
			self.groups_list=groups_list
			
class Group:
	def __init__(self,id=None,capabilities_list=None):
		self.id=id
		if capabilities_list is None:
			self.capabilities_list=[]
		else: 
			self.capabilities_list=capabilities_list
			
class Capability:
	def __init__(self,name=None,value=None):
		self.name=name
		self.value=name