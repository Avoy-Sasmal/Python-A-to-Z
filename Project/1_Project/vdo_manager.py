# we have a package called json which is used to convert string to json and json to string 
# its a file formate 
import json 




def load_data():
  try:
    with open('videos.txt','r') as file:
      test =  json.load(file)  # this will load the data from the file and convert it to a python object
     # print(type(test))
      return test
  except FileNotFoundError:
    return []  # if the file does not exist, return an empty list
  
def save_data_helper(videos):
  with open('videos.txt', 'w') as file:
    json.dump(videos,file) # this will help to write the data in the file in json format 

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for  index,videos in enumerate(videos,start = 1 ):

      print(f"{index} . {videos['name']} , Duration : {videos['time']} ") # The f before the opening quotation mark signifies that this is an f-string. F-strings allow you to embed Python expressions directly within string literals by enclosing them in curly braces {}.
    print("\n")
    print("*" * 50)  

def add_video(videos):
  name = input("Enter the video name :")
  time = input("Enter the video time:")
  videos.append({
    'name': name,
    'time' : time 
  })
  save_data_helper(videos)  # this will save the data in the file after adding a new video

def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the index of the video to update: "))
  if 1 <= index <= len(videos):
    name = input("Enter the name :")
    time = input("Enter the time :")
    videos[index - 1 ] = {'name': name , 'time': time }
    save_data_helper(videos)
  else : 
    print("invalid Index Selected")  

def delete_video(videos):
  list_all_videos(videos)
  index = int(input('Enter the Video Number want to be deleted'))
  if 1 <= index <= len(videos):
    del videos[index - 1 ] # is it return a new list or return the same list 
    save_data_helper(videos)
    print("\n Successfully Delted ")
  else :
    print('Invalid video Index sleected')

def main():# ctrl +  "]" short cut for indenting the code
  videos = load_data() # this function will go to the file and grab dat from there 
  while True:
    print("\n Youtube Manager  | choose an option ")
    print("1. List all youtube videos ")
    print("2. Add a new youtube video ")
    print("3. update a youtube video details ")
    print("4. Delete a youtube video ") 
    print("5. Exit ")
    choice = input("Enter the Choice : ")
   # print(videos)
    match choice:
      case '1':
        list_all_videos(videos)
      case '2' :
        add_video(videos)
      case '3': 
        update_video(videos)
      case '4':
        delete_video(videos) 
      case '5':
        print("Exiting the Youtube Manager. Goodbye!")
        break  
      case _:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":  # __ this synatx know as dundar (underscore underscore )
  main()  # this is the main function which will run when the script is executed