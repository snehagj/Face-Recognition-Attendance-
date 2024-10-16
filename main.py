from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #first image
        img=Image.open(r"E:\TY\Project 2\face recognition\images\1.jpeg")
        img=img.resize((450,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"E:\TY\Project 2\face recognition\images\2.jpeg")
        img1=img1.resize((450,130))
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img2=img.resize((450,130))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img3=img.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="Face Recognization Attendance System" ,font=("times new roman",35,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0, width=1530, height=130)


        #student button
        img4=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img4=img.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)


        #detect face button
        img5=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img5=img.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=400,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=400,y=300,width=220,height=40)


        #Attendance face button
        img6=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img6=img.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=700,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b3_1.place(x=700,y=300,width=220,height=40)


        #Help button
        img7=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img7=img.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1000,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=1000,y=300,width=220,height=40)


        #Train data button
        img8=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img8=img.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=100,y=350,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=100,y=550,width=220,height=40)


        #Photos button
        img9=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img9=img.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=400,y=350,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6_1.place(x=400,y=550,width=220,height=40)


        #Developer button
        img10=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img10=img.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=700,y=350,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_1.place(x=700,y=550,width=220,height=40)


        #Exit button
        img11=Image.open(r"E:\TY\Project 2\face recognition\images\3.jpeg")
        img11=img.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=1000,y=350,width=220,height=220)

        b7_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_1.place(x=1000,y=550,width=220,height=40)




if __name__ == "__main__":
    root = Tk()
    obj=Face_recognition_system(root)
    root.mainloop()