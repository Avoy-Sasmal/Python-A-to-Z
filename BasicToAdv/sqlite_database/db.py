import sqlite3
con = sqlite3.connect('storage.db')
cur = con.cursor()


# in tripple code which i have write it will exam go same as it is 
cur.execute('''
  CREATE  TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL ,
            time TEXT NOT NULL            
)''')


def list_all():
  cur.execute(''' SELECT * FROM  videos''')
  for row in cur.fetchall():
      if(row == 0):
        print('vlaue is empty ')
      else :
         print(row)

def add_vdo(name,time):
      cur.execute(" INSERT INTO videos (name,time) VALUES(?,?)", (name , time ))

def update_video(index, name , time):
   cur.execute("UPDATE videos SET name= ?, time = ? WHERE id = ?",(name,time,index))
   con.commit()

def delete_vdo(video_id):
   cur.execute("DELETE FROM videos WHERE id = ? ",(video_id,)) # alwasy remeber the syntax fopr single valu passed also you have tp give the " ,"
   con.commit()

def main():
  while (True) :
    print ("Welcome to vdo manager :")
    print("1. for add vdo ")
    print("2. for update vdo ")
    print("3. delete vdo")
    print("4. show all the vdo ")
    print("5. Exit ")
    choice = input("ENter your choice : ")

    if(choice == '1'):
      name = input("Enter the the name of the videos : ")
      time = input("Enter the the time  : ")
      add_vdo(name, time )

    elif(choice == '2'):
       index = int(input("Enter the index number: ")) 
       name = input("Enter the updated name :  ") 
       time = input("Enter the updated time : ")
       update_video(index, name , time)

    elif(choice == '3' ) :
       video_id = int(input('Enter the index Number : '))  
       delete_vdo(video_id)

    elif(choice == '4') :
        list_all()

    elif(choice == '5'):
       print('Thank You !! \n successfully exit ')   
       break
    else :
        print("Invalid Choice pleae re Enter ")
 
  con.close() 


if __name__ == '__main__':
  main()