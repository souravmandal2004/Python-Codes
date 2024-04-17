import sqlite3

con = sqlite3.connect ("youtube_videos.db")
cursor = con.cursor()

cursor.execute ('''
    CREATE TABLE IF NOT EXISTS Videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_all_videos ():
    cursor.execute ("SELECT * FROM Videos")
    rows = cursor.fetchall ()
    for row in rows:
        print (row)

def add_video (name, time):
    cursor.execute ("INSERT INTO Videos (name, time) VALUES (?,?)", (name, time))
    con.commit()
    print ("Added video")
def update_video (video_id, new_name, new_time):
    cursor.execute ("UPDATE Videos SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    con.commit ()

def delete_video (video_id):
    cursor.execute ("DELETE FROM videos WHERE id=?", (video_id,))
    con.commit ()
    
def main ():
    while True:
        print ("\n Youtube Manager | Choose an option")
        print ("1. List all youtube videos")
        print ("2. Add a youtube video")
        print ("3. Update a youtube video details")
        print ("4. Delete a youtube video")
        print ("5. exit the app")
        choice = input ("Enter your choice: ")

        if choice == "1":
            list_all_videos ()

        elif choice == "2":
            name = input ("Enter the name of the video: ")
            time = input ("Enter the time of the video: ")
            add_video (name, time)
            
        elif choice == "3":
            video_id = input ("Enter the id of the video to update :")
            name = input ("Enter the updated name: ")
            time = input ("Enter the updated time: ")
            update_video (video_id, name, time)

        elif choice == "4":
            video_id = input ("Enter the id of the video to delete :")
            delete_video (video_id)

        elif choice == "5":
            print ("Thank you for using the app")
            break

        else:
            print ("Invalid choice")
            
    con.close ()

if __name__ == '__main__':
    main ()