from tkinter import *

# Pencere tasarımı
root = Tk()
root.title('Normal To-Do List')
root.geometry('400x550')

# Başlık
Label(root, text='Normal Python To Do List', font=("Arial", 20), wraplength=400).place(x=35, y=0)

# Listbox ve Scrollbar
tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Arial', 12), height=20, width=30)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=322, y=50, height=350)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=50, y=50)

# Adding ve Deleting fonksiyonları
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    listbox.insert(END, new_task)
    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')
def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)
    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()
        tasks_list_file.truncate()
        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)
        tasks_list_file.close()

# Item ekleme
with open(r"C:\Users\red__\vs_folder_jp\tasks.txt.txt", 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

new_item_entry = Entry(root, width=37)
new_item_entry.place(x=50, y=440)

# Butonlar
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Arial', 12),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=50, y=470)
delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Arial', 12),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=160, y=470)

root.update()
root.mainloop()

