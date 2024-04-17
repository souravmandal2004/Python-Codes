# with open ("youtube.txt", "w") as file:
#     file.write ("Hello World!")

import json

def load_data ():
    try:
        with open ("youtube.txt", "r") as file:
            return json.load (file)

    except FileNotFoundError:
        return []


def save_data_helper (videos):
    with open ("youtube.txt", "w") as file:
        json.dump (videos, file)

def list_all_videos (videos):
    print ()
    print ("*" * 70)
    for index, video in enumerate (videos, start=1):
        print (f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print ()
    print ("*" * 70)


def add_video (videos):
    video_name = input ("Enter the name of the video: ")
    video_time = input ("Enter the time of the video: ")
    
    videos.append ({
        "name": video_name,
        "time": video_time
    })

    save_data_helper (videos)

def update_video (videos):
    list_all_videos (videos)
    video = int (input ("Enter the video number to update: "))
    
    if (1 <= video <= len (videos)):
        name = input ("Enter the new video name: ")
        time = input ("Enter the new video time: ")
        videos[video-1] = {'name': name, 'time': time}
        save_data_helper (videos)

    else:
        print ("Invalid video selected!")


def delete_video (videos):
    list_all_videos (videos)
    video = int (input ("Enter the video number to delete: "))

    if (1 <= video <= len (videos)):
        del videos[video-1]
        save_data_helper (videos)

    else:
        print ("Invalid video selected")



def main ():
    videos = load_data ()

    while True:
        print ("\n Youtube Manager | Choose an option")
        print ("1. List all youtube videos")
        print ("2. Add a youtube video")
        print ("3. Update a youtube video details")
        print ("4. Delete a youtube video")
        print ("5. exit the app")
        choice =input ("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos (videos)

            case "2":
                add_video (videos)

            case "3":
                update_video (videos)

            case "4":
                delete_video (videos)

            case "5":
                print ("Thank you for using the app")
                break
            case _:
                print ("Invalid choice")

if __name__ == "__main__":
    main ()