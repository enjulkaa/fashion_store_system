from tkinter import*
import mysql.connector
import csv
from tkinter import ttk

root=Tk()
root.title("FASHION-STORE-MANAGEMENT-SYSTEM!!")
root.geometry("900x900")

#making functions
#1:clear function!
def clear_():
    first_name_box.delete(0,END)
    last_name_box.delete(0,END)
    email_id_box.delete(0,END)
    city_box.delete(0,END)
    state_box.delete(0,END)
    country_box.delete(0,END)
    pincode_box.delete(0,END)
    address_box.delete(0,END)
    phone_no_box.delete(0,END)
    payment_method_box.delete(0,END)
    discount_code_box.delete(0,END)
    price_paid_box.delete(0,END)
    
#2:add function!
def add_customer():
    sql_command="INSERT INTO  purchaser_details(first_name,last_name,email_id ,city,state,country,pincode,address,phone_no,payment_method,discount_code,price_paid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(first_name_box.get(),last_name_box.get(),email_id_box.get(),city_box.get(),state_box.get(),country_box.get(),pincode_box.get(),address_box.get(),phone_no_box.get(),payment_method_box.get(),discount_code_box.get(),price_paid_box.get())
    my_cursor.execute(sql_command,values)
    mydb.commit()
    clear_()


#3:write to csv function!
def write_to_csv(result):
    with open('purchaser_details.csv',"a",newline="") as f:
        w=csv.writer(f,dialect="excel")
        for record in result:
            w.writerow(record)

#4:show details function!
def show_details():
    show_detail_query=Tk()
    show_detail_query.title("DETAILS OF CUSTOMERS")
    show_detail_query.geometry("1080x600")
    my_cursor.execute("SELECT* FROM purchaser_details")
    result=my_cursor.fetchall()
    for index,x in enumerate(result):
        num=0
        for y in x:
            lookup_label=Label(show_detail_query,text=y)
            lookup_label.grid(row=index,column=num)
            num+=1
    csv_button=Button(show_detail_query,text="SAVE TO EXCEL",command=lambda:write_to_csv(result))
    csv_button.grid(row=index+2,column=0)

#5:search customer function!
def search_customer():
    sql=" "
    search_customer_query=Tk()
    search_customer_query.title("SEARCH ALL CUSTOMERS")
    search_customer_query.geometry("1100x500")
    def search_now():
        selected=drop.get()
        if selected=="SEARCH BY..":
            test=Label(search_customer_query,text="You have picked nothing !")
            test.grid(row=2,column=0)
        if selected=="FIRST NAME":
            sql="SELECT* FROM purchaser_details WHERE first_name=%s"
            
            
        if selected=="EMAIL ID":
            sql="SELECT* FROM purchaser_details WHERE email_id=%s"
            
            
        if selected=="STATE":
            sql="SELECT* FROM purchaser_details WHERE state=%s"
      
            
        if selected=="CITY":
            sql="SELECT* FROM purchaser_details WHERE city=%s"
          
            
        searched=search_box.get()
        #sql="SELECT* FROM purchaser_details WHERE first_name=%s"
        name=(searched,)
        result=my_cursor.execute(sql,name)
        result=my_cursor.fetchall()
        if not result:
            result="Oops!! Record Not Found...."
            searched_label=Label(search_customer_query,text=result)
            searched_label.grid(row=2,column=0)

        else:
            for index,x in enumerate(result):
                num=0
                index+=3
                for y in x:
                    searched_label=Label(search_customer_query,text=y)
                    searched_label.grid(row=index,column=num)
                    num+=1


            
        #searched_label=Label(search_customer_query,text=result)
        #searched_label.grid(row=4,column=0,padx=10,columnspan=2)
         

    
    search_label=Label(search_customer_query,text="Search:")
    search_label.grid(row=0,column=0,padx=10,pady=10)
    search_box=Entry(search_customer_query)
    search_box.grid(row=0,column=1,padx=10,pady=10)
    search_button=Button(search_customer_query,text="SEARCH CUSTOMERS",command=search_now)
    search_button.grid(row=1,column=0,padx=10)

    drop=ttk.Combobox(search_customer_query,value=["SEARCH BY..","FIRST NAME","EMAIL ID","STATE","CITY"])
    drop.current(0)
    drop.grid(row=0,column=2)







#establishing connection#
mydb=mysql.connector.connect(host="localhost",user="root",passwd="nisha",database="PROJECT_")

my_cursor=mydb.cursor()
#my_cursor.execute("CREATE DATABASE PROJECT_")
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
    #print(db)
#creating label
title_label=Label(root,text="FASHION-STORE-MANAGEMENT-SYSTEM!!",font=("times new roman",30,"bold"),bd=10,relief=RIDGE)
title_label.grid(row=0,column=0,columnspan=2,pady="15")

#my_cursor.execute("DROP TABLE purchaser_details")
my_cursor.execute("CREATE TABLE  IF NOT EXISTS  purchaser_details(first_name VARCHAR(255),\
                   last_name VARCHAR(67),\
                   email_id VARCHAR(76),\
                   city VARCHAR(85),\
                   state VARCHAR(90),\
                   country VARCHAR(56),\
                   pincode VARCHAR(34),\
                   address VARCHAR(197),\
                   phone_no VARCHAR(180),\
                   payment_method VARCHAR(29),\
                   discount_code VARCHAR(25),\
                   price_paid VARCHAR(67))")



#creating labels again for entry fields
first_name_label=Label(root,text="FIRST NAME").grid(row=1,column=0,sticky="w",padx=10)
last_name_label=Label(root,text="LAST NAME").grid(row=2,column=0,sticky="w",padx=10)
email_id_label=Label(root,text="EMAIL ID").grid(row=3,column=0,sticky="w",padx=10)
city_label=Label(root,text="CITY").grid(row=4,column=0,sticky="w",padx=10)
state_label=Label(root,text="STATE").grid(row=5,column=0,sticky="w",padx=10)
country_label=Label(root,text="COUNTRY").grid(row=6,column=0,sticky="w",padx=10)
pincode_label=Label(root,text="PINCODE").grid(row=7,column=0,sticky="w",padx=10)
address_label=Label(root,text="ADDRESS").grid(row=8,column=0,sticky="w",padx=10)
phone_no_label=Label(root,text="PHONE NO").grid(row=9,column=0,sticky="w",padx=10)
payment_method_label=Label(root,text="PAYMENT METHOD").grid(row=10,column=0,sticky="w",padx=10)
discount_code_label=Label(root,text="DISCOUNT CODE").grid(row=11,column=0,sticky="w",padx=10)
price_paid_label=Label(root,text="PRICE PAID").grid(row=12,column=0,sticky="w",padx=10)

#creating entry boxes

first_name_box=Entry(root)
first_name_box.grid(row=1,column=1)

last_name_box=Entry(root)
last_name_box.grid(row=2,column=1,pady=5)

email_id_box=Entry(root)
email_id_box.grid(row=3,column=1,pady=5)

city_box=Entry(root)
city_box.grid(row=4,column=1,pady=5)

state_box=Entry(root)
state_box.grid(row=5,column=1,pady=5)

country_box=Entry(root)
country_box.grid(row=6,column=1,pady=5)

pincode_box=Entry(root)
pincode_box.grid(row=7,column=1,pady=5)

address_box=Entry(root)
address_box.grid(row=8,column=1,pady=5)

phone_no_box=Entry(root)
phone_no_box.grid(row=9,column=1,pady=5)

payment_method_box=Entry(root)
payment_method_box.grid(row=10,column=1,pady=5)

discount_code_box=Entry(root)
discount_code_box.grid(row=11,column=1,pady=5)

price_paid_box=Entry(root)
price_paid_box.grid(row=12,column=1,pady=5)

#creating buttons
add_customer_button=Button(root,text="ADD",command=add_customer)
add_customer_button.grid(row=13,column=0,padx=15,pady=10,sticky="w")

clear_button=Button(root,text="CLEAR",command=clear_)
clear_button.grid(row=13,column=1,pady=10)

show_button=Button(root,text="SHOW DETAILS",command=show_details)
show_button.grid(row=14,column=0, sticky="w",padx=10,pady=10)

search_button=Button(root,text="SEARCH",command=search_customer)
search_button.grid(row=14,column=1,pady=10)













root.mainloop()
