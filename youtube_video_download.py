import customtkinter
import tkinter as tk
from pytube import YouTube

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
resaltion="700x700"
root=customtkinter.CTk()
root.geometry(resaltion)

root.title("You Tube Downloader")

        
def prepare():
    def progresss(stream,chunk,bytes_r):
            total_size=stream.filesize
            down=total_size-bytes_r
            p=down/total_size*100
            per=str(int(p))
            downloaded.configure(text=per+"%")
            progress.set(float(per)/100)
            downloaded.update()
            process.update()
    continter=0
    for widget in root.winfo_children():
        continter+=1
        if continter>=5:
            widget.destroy()

    def downloadd():
            
        continter=0 
        for widget in root.winfo_children():
            continter+=1
            if continter==11:
                widget.destroy()
                downloaded.configure(text="0%")
                downloaded.update()
                progress.set(0)
        kind=str(quality.get())
        kindd=video_type.index(kind)
        ur[kindd].download()
            

        
        finish=customtkinter.CTkLabel(master=root,text="Video Download Finishd",font=("Roborto",20),text_color="green")
        finish.place(y=480,x=250)
    try:
        urll=url_in.get()
        url=YouTube(urll,on_progress_callback=progresss)
        ur=url.streams.all()
            
        video_type=[]
        for i in ur:
            quality_values=[]
            strr=""
            quality_values.append(i.resolution)
            quality_values.append(i._filesize_mb)
            quality_values.append(i.mime_type)
            for l in quality_values:
                strr+=str(l)+"/"
            video_type.append(strr)
        
        quality_label1=customtkinter.CTkLabel(master=root,text="Quality/Size(Mb)/Type",font=("Roborto",16),text_color="#ffffff")
        quality_label1.place(y=240,x=350)
        quality_label=customtkinter.CTkLabel(master=root,text="Select The Quality:",font=("Roborto",20),text_color="#ffffff")
        quality_label.place(y=270,x=100)
        quality=customtkinter.CTkOptionMenu(master=root,values=video_type,text_color="black",fg_color="#eaebed",width=100)
        quality.place(x=330,y=270)
            
            
        
        downlad=customtkinter.CTkButton(master=root,text="Download",text_color="black",fg_color="#eaebed",command=downloadd)
        downlad.place(x=260,y=320)  
            
        progress=customtkinter.CTkProgressBar(master=root,width=400,orientation="horizontal")
        progress.set(0)
        progress.place(x=130,y=380)
            
        downloaded=customtkinter.CTkLabel(master=root,text="0%",font=("Roborto",14),text_color="#ffffff")
        downloaded.place(x=330,y=400)
            
    except :
        error=customtkinter.CTkLabel(master=root,text="Faild At Preparing",font=("Roborto",20),text_color="red")
        error.place(y=320,x=250)       
    
titl=customtkinter.CTkLabel(master=root,text="You Tube Downloader",font=("Roborto",24),text_color="#ffffff")
titl.place(y=30,x=250)

url_in_label=customtkinter.CTkLabel(master=root,text="Enter The URL Of Video:",font=("Roborto",20),text_color="#ffffff")
url_in_label.place(y=120,x=100)

url_in=customtkinter.CTkEntry(master=root,placeholder_text="URL")
url_in.place(y=120,x=400)

process=customtkinter.CTkButton(master=root,text="Preparing",text_color="black",fg_color="#eaebed",command=prepare)
process.place(x=260,y=170)


root.mainloop()