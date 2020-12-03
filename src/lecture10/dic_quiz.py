months = {"first":"January","second":"February","third":"March","fourth":"April","fifth":"May","sixth":"June","seventh":"July","eighth":"August","ninth":"September","tenth":"October","eleventh":"November","twelfth":"December",1:"first",2:"second",3:"third",4:"fourth",5:"fifth",6:"sixth",7:"seventh",8:"eighth",9:"ninth",10:"tenth",11:"eleventh",12:"twelfth"}

for i in range(1,13):
    print("The " + months[i] + " month is " + months[months[i]])
