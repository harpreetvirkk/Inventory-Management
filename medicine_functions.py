import csv
from tempfile import NamedTemporaryFile
import shutil
def add_medicine():
	with open('medicine.csv','a+') as csvfile:
		columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date',\
		'pur_date','comp_name', 'supp_id','cost','total','to_pur']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		
		medi_name = input("Enter medicine name:")
		med_id = input("Enter ID:")
		sale = float(input("Enter sale price:"))
		unit = float(input("Enter cost price"))
		quantity = int(input("Enter quantity"))
		min_quantity = int(input("Enter min quantity to "))
		exp_date = input("Enter exp date")
		pur_date= input("Enter purchase date")
		comp_name = input("Enter company name")
		supp_id = input("Enter supplier ID")
		cost = quantity * unit
		total = quantity *sale
		to_pur = min_quantity - quantity
		if quantity >min_quantity:
			to_pur = 0
		writer.writerow({'medi_name':medi_name,'med_id':med_id,'sale':sale,'unit':unit,'quantity':quantity,\
		'min_quantity':min_quantity,'exp_date':exp_date,'pur_date':pur_date,'comp_name':comp_name, \
		'supp_id':supp_id,'cost':cost,'total':total,'to_pur':to_pur})

def search_medicine():
    with open('medicine.csv','r') as csvfile:
        name=input('Enter the medicine to search:')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['medi_name'] == name:
                print('Name:', row['medi_name'],'\n','Quantity:',row['quantity'],'\n','Price:',row['sale'])	

def update_medicine():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['medi_name','med_id','sale','unit','quantity','min_quantity', 'exp_date',\
		'pur_date','comp_name', 'supp_id','cost','total','to_pur']
    with open('medicine.csv', 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        med_name =input('Enter the name of the medicine you want to modify')
        for row in reader:
            if row['medi_name'] == med_name:
                choice=int(input('1.To update the Name\n2.To update Cost price\n3.To update sale price.\n4.To update supplier ID'))

                if(choice==1):
                    row['medi_name']=input("Enter the new name: ")

                elif(choice==2):
                    row['cost']=input("Enter the new cost price: ")

                elif(choice==3):
                    row['sale']=input("Enter the new sale price")

                elif(choice==4):
                    row['supp_id']=input("Enter the new supplier ID")    



            row = {'medi_name':row['medi_name'],'med_id':row['med_id'],'sale':row['sale'],'unit':row['unit'],'quantity':row['quantity'],\
		    'min_quantity':row['min_quantity'],'exp_date':row['exp_date'],'pur_date':row['pur_date'],'comp_name':row['comp_name'], \
		    'supp_id':row['supp_id'],'cost':row['cost'],'total':row['total'],'to_pur':row['to_pur']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'medicine.csv')

def medicine_to_be_purchased():
	with open('medicine.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if int(row['to_pur']) >0:
				print('Name:', row['medi_name'],'\n','Quantity:',row['quantity'],'\n','Minimum Quantity:',row['min_quantity']\
				,'\n','To be purchased:',row['to_pur'],'\n','Supplier ID:',row['supp_id'])

add_medicine()
search_medicine()
update_medicine()  
medicine_to_be_purchased()              