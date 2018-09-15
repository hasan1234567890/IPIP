from Tkinter import*
import socket
pencere=Tk()
pencere.geometry('100x200')
pencere.title('ip bulma programi')
k=Entry()
k.pack()
def bul():
   a=k.get()
   l=socket.gethostbyname(a)
   label=Label(text=l)
   label.pack()
dugme=Button(text='ip bul',command=bul)
dugme.pack()
mainloop()
