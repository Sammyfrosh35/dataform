# dataform
import tkinter 
from tkinter import ttk
from tkinter import messagebox



def enter_data():
    accepted= accept_var.get()

    if accepted =='Accepted':

        firstname = first_name_entry.get()
        secondname = last_name_entry.get()

        if firstname and secondname:

            title = title_combobox.get()
            age = age_spinbox.get()
            citizenship = nationality_combobox.get()

            #SEMESTER INFO
            semester= semester_spinbox.get()
            CE= num_courses.get()
            reg= reg_status_var.get()
            
            print('first name:', firstname, 'last name: ', secondname, 'age :', age, 'title: ', title, "nationality:", citizenship )
            print('courses registered:', CE, 'semester:', semester) 
            print('registration status:', reg)
            print('title:', title)
            print('-------------------------------')
        else:
             tkinter.messagebox.showerror("Error", 'First name and Last name are required', parent=window)
  
    else:
        tkinter.messagebox.showerror("Error", 'You have not accepted the terms', parent=window)


        

window = tkinter.Tk()
window.title('Data Entry Form')

frame = tkinter.Frame(window)
frame.pack()


#saving user info 
user_info_frame = tkinter.LabelFrame(frame, text='user Information')
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label=tkinter.Label(user_info_frame, text='Firstname')
first_name_label.grid(row=0, column=0)
last_name_label=tkinter.Label(user_info_frame, text='Last Name')
last_name_label.grid(row=0, column=1)

first_name_entry= tkinter.Entry(user_info_frame)
last_name_entry= tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label= tkinter.Label(user_info_frame, text='Title')
title_combobox = ttk.Combobox(user_info_frame, values=['Mr', 'Mrs'])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label= tkinter.Label(user_info_frame, text='Age')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to= 100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label= tkinter.Label(user_info_frame, text='Nationality')
nationality_combobox = ttk.Combobox(user_info_frame, values=['South-america', 'asia','india','nigerian','american','south africa'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#course registration

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)

register_label = tkinter.Label(courses_frame, text='Registration status')

reg_status_var=tkinter.StringVar(value='not registered')
register_check = tkinter.Checkbutton(courses_frame, text='Currently registered',
                                     variable=reg_status_var, onvalue='registered',offvalue='not registered')


register_label.grid(row=0, column=0)
register_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(courses_frame, text='Completed courses')
num_courses = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_courses_label.grid(row=0, column=1)
num_courses.grid(row=1, column=1)

semester_label = tkinter.Label(courses_frame, text='Semester')
semester_spinbox= tkinter.Spinbox(courses_frame, from_=0, to= 2)
semester_label.grid(row=0, column=2)
semester_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



#accept terms
accept_frame = tkinter.LabelFrame(frame, text='Terms and condition', )
accept_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)


accept_var=tkinter.StringVar(value='Not accepted')
accept_frame_check = tkinter.Checkbutton(accept_frame, text='I accept this terms and condition',
                                         variable=accept_var, onvalue='Accepted', offvalue='Not accepted') 
accept_frame_check.grid(row=0, column=0)

#BUTTON

button_frame_button = tkinter.Button(frame, text='Enter Data',command= enter_data )
button_frame_button.grid(row=3, column=0, sticky='news', padx=20, pady=10)



window.mainloop()