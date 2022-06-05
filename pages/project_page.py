from tkinter import Button, Entry, Frame, Label, Listbox, messagebox, StringVar, ttk
from classes.user import User
from classes.project_session import ActiveProject
import settings


class Project_Page(Frame):
    def __init__(self, root, width, height, user: User):
        super().__init__(root, width=width, height=height)
        self.configure(bg=settings.PROGRAM_BG)
        self.user = User()
        self.project = ActiveProject()

        # define string variables
        self.projectName = StringVar()
        self.musicianName = StringVar()
        self.projectCurrentName = StringVar()
        self.projectNewName = StringVar()
        self.projectCompletableProjectName = StringVar()
        self.projectListAll = StringVar()

        # Create new project section => define widgets
        self.label_create = Label(self, text="Create new project", bg=settings.PROGRAM_BG)
        self.label_create.place(relx=0.1, rely=0.10)

        self.project_name = Label(self, text="project name:", bg=settings.PROGRAM_BG)
        self.project_name.place(relx=0.1, rely=0.19, height=20)

        self.project_name_box = Entry(self, textvariable=self.projectName)
        self.project_name_box.place(relx=0.1, rely=0.23, relwidth=0.25, height=20)
        self.project_name_box.focus()

        self.musician_name = Label(self, text="musician:", bg=settings.PROGRAM_BG)
        self.musician_name.place(relx=0.1, rely=0.29, height=20)

        self.musician_name_cb = ttk.Combobox(self, textvariable=self.musicianName, state="readonly", height=5)
        self.musician_name_cb.place(relx=0.1, rely=0.33, relwidth=0.25)
        # retrieve musicians in order to fill combobox
        self.fill_musician_name_cb(user)

        self.create_button_frame()

        # self.sessions_lb = Label(self, width=30, text="Assign session(s) to project:", bg=settings.PROGRAM_BG, \
        # anchor=E).grid(row=2, column=0)
        # self.sessions_list = Listbox(self, width=40, height=8)
        # self.session = ActiveSession()
        # self.sessions = self.session.select_all_sessions()
        # for session in self.sessions:
        #     self.sessions_list.insert(session.sessionID, f"{session.session_type_name} {session.setup_name} \
        #     {session.setup_description}")
        # self.sessions_list.grid(row=2, column=1)
        # apply padding to all widgets
        # for child in self.winfo_children():
        #     child.grid_configure(padx=10, pady=15)

        # Rename project section => define widgets
        self.label_rename = Label(self, text="Rename existing project", bg=settings.PROGRAM_BG)
        self.label_rename.place(relx=0.1, rely=0.57)

        self.project_current_name = Label(self, text="project:", bg=settings.PROGRAM_BG)
        self.project_current_name.place(relx=0.1, rely=0.66)

        self.project_current_name_cb = ttk.Combobox(self, textvariable=self.projectCurrentName, state="readonly",
                                                    height=5)
        self.project_current_name_cb.place(relx=0.1, rely=0.7, relwidth=0.25)
        # retrieve all ongoing projects, populate combobox and assign default option
        self.fill_project_current_name_combobox()

        self.project_new_name = Label(self, text="new name:", bg=settings.PROGRAM_BG)
        self.project_new_name.place(relx=0.1, rely=0.76, height=20)

        self.project_new_name_box = Entry(self, textvariable=self.projectNewName)
        self.project_new_name_box.place(relx=0.1, rely=0.8, relwidth=0.25, height=20)

        self.create_button_frame2()

        # Finalize project section => define widgets
        self.label_finalize = Label(self, text="Finalize project", bg=settings.PROGRAM_BG)
        self.label_finalize.place(relx=0.5, rely=0.10)

        self.project_completable_project_name = Label(self, text="project:", bg=settings.PROGRAM_BG)
        self.project_completable_project_name.place(relx=0.5, rely=0.19, height=20)

        self.project_completable_project_name_cb = ttk.Combobox(self, textvariable=self.projectCompletableProjectName,
                                                                state="readonly", height=5)
        self.project_completable_project_name_cb.place(relx=0.5, rely=0.23, relwidth=0.25)
        # populate combobox with data retrieved from database
        self.fill_project_completable_project_name_cb()

        self.create_button_frame3()

        # Show product data section => define widgets
        self.label_show = Label(self, text="Show project data", bg=settings.PROGRAM_BG)
        self.label_show.place(relx=0.5, rely=0.57)

        self.project_list_all = Label(self, text="project name:", bg=settings.PROGRAM_BG)
        self.project_list_all.place(relx=0.5, rely=0.66, height=20)

        self.project_list_all_cb = ttk.Combobox(self, textvariable=self.projectListAll, state="readonly", height=5)
        self.project_list_all_cb.place(relx=0.5, rely=0.7, relwidth=0.25)
        self.fill_project_list_all_cb()

        self.create_button_frame4()

    # define instance methods
    # reset entry fields
    def reset_create(self):
        self.projectName.set("")
        self.musicianName.set("")

    def reset_rename(self):
        self.projectCurrentName.set("")
        self.projectNewName.set("")

    def reset_finalize(self):
        self.projectCompletableProjectName.set("")

    def reset_show(self):
        self.projectListAll.set("")

    # provide comboboxes with data retrieved from database
    def fill_musician_name_cb(self, user):
        musicians = user.select_all_musicians(3)
        combo_values = []
        for musician in musicians:
            combo_values.append(f"{musician.last_name} {musician.first_name}")
        self.musician_name_cb["values"] = combo_values
        self.musician_name_cb.current(0)

    def fill_project_current_name_combobox(self):
        ongoing_projects = self.project.select_all_active_projects()
        combo_values = []
        for project in ongoing_projects:
            combo_values.append(f"{project.album_name} / {project.last_name} {project.first_name}")
        self.project_current_name_cb["values"] = combo_values
        self.project_current_name_cb.current(0)

    def fill_project_completable_project_name_cb(self):
        completable_projects = self.project.select_all_active_projects()
        combo_values = []
        for project in completable_projects:
            combo_values.append(f"{project.album_name} / {project.last_name} {project.first_name}")
        self.project_completable_project_name_cb["values"] = combo_values
        self.project_completable_project_name_cb.current(0)

    def fill_project_list_all_cb(self):
        all_projects = self.project.select_all_projects()
        combo_values = []
        for project in all_projects:
            combo_values.append(f"{project.album_name} / {project.last_name} {project.first_name}")
        self.project_list_all_cb["values"] = combo_values
        self.project_list_all_cb.current(0)

    # button frames and their allocated buttons
    def create_button_frame(self):
        button_frame = Frame(self, bg=settings.PROGRAM_BG)
        button_create = Button(button_frame, text="Create", bg=settings.BUTTON_BG, padx=20)
        button_reset = Button(button_frame, text="Reset", command=self.reset_create,
                              bg=settings.BUTTON_BG, padx=20)
        button_create.pack(side="left")
        button_reset.pack(side="right")
        button_frame.place(relx=0.1, rely=0.4, relwidth=0.25)

    def create_button_frame2(self):
        button_frame2 = Frame(self, bg=settings.PROGRAM_BG)
        button_rename = Button(button_frame2, text="Rename", bg=settings.BUTTON_BG, padx=20)
        button_reset2 = Button(button_frame2, text="Reset", command=self.reset_rename, bg=settings.BUTTON_BG, padx=20)
        button_frame2.place(relx=0.1, rely=0.87, relwidth=0.25)
        button_rename.pack(side="left")
        button_reset2.pack(side="right")

    def create_button_frame3(self):
        button_frame3 = Frame(self, bg=settings.PROGRAM_BG)
        button_finalize = Button(button_frame3, text="Finalize", bg=settings.BUTTON_BG, padx=20)
        button_reset3 = Button(button_frame3, text="Reset", command=self.reset_finalize,
                               bg=settings.BUTTON_BG, padx=20)
        button_frame3.place(relx=0.5, rely=0.3, relwidth=0.25)
        button_finalize.pack(side="left")
        button_reset3.pack(side="right")

    def create_button_frame4(self):
        button_frame4 = Frame(self, bg=settings.PROGRAM_BG)
        button_show = Button(button_frame4, text="Show", bg=settings.BUTTON_BG, padx=20)
        button_reset4 = Button(button_frame4, text="Reset", command=self.reset_show, bg=settings.BUTTON_BG, padx=20)
        button_frame4.place(relx=0.5, rely=0.77, relwidth=0.25)
        button_show.pack(side="left")
        button_reset4.pack(side="right")
