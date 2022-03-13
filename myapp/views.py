from django.shortcuts import render
import os
import shelve
# Create your views here.
class CreateDrug:
	my_table = dict()
	def __init__(self, name, day, month, year, count):
		self.name = name
		self.day = int(day)
		self.month = int(month)
		self.year = int(year)
		self.count = int(count)
		self.id = None
	@property
	def count(self):
		return self.__count
	@count.setter
	def count(self, count):
		if count > 0:
			self.__count = count
		else:
			self.delete()
	def save(self):
		db = CreateDrug.my_table
		keys = list(db.keys())
		count = len(keys)
		if count > 0:
			self.id = int(keys[-1])+1
		else:
			self.id = 1
		db[str(self.id)] = self
	def objects():
		db = CreateDrug.my_table	
		obj = []
		for item in db:
			obj.append(db[item])
		return obj

	def delete(self):
		db = CreateDrug.my_table	
		del db[str(self.id)]
def main(request):
	if request:
		rqt = request.GET
		if len(rqt) == 6:
			drug = CreateDrug(rqt['iname'], rqt['iday'], rqt['imonth'], rqt['iyear'],rqt['iquantity'])
			drug.save()


	try:
		for i in CreateDrug.objects():
			base.append(i.name)
			base.append(i.day)
			base.append(i.month)
			base.append(i.year)
			base.append(i.count)
		print('asldalskjdlasjda = ', CreateDrug.objects())
		return render(request, 'index.html', {"selff" : CreateDrug.objects()})
	except:
		return render(request, 'index.html')
