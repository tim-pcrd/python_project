from tkinter import Button, Entry, Frame, Label, messagebox, StringVar, ttk
from classes.user import User
from classes.project_session import ActiveProject
import settings


class Project_Page(Frame):
    def __init__(self, root, window_object, width, height, user: User):
        super().__init__(root, width=width, height=height)
        self.configure(bg=settings.PROGRAM_BG)
        self.window_object = window_object
        self.user = User()
        self.project = ActiveProject()
        self.message = ""      # to temporarily store error messages

        # define string variables
        self.projectName = StringVar()
        self.musicianName = StringVar()
        self.projectCurrentName = StringVar()
        self.projectNewName = StringVar()
        self.projectCompletableProjectName = StringVar()
        self.projectListAll = StringVar()

        # Create new project section => define widgets
        self.label_create = Label(self, text="Maak nieuw project", bg=settings.PROGRAM_BG)
        self.label_create.place(relx=0.1, rely=0.10)

        self.project_name = Label(self, text="naam:", bg=settings.PROGRAM_BG)
        self.project_name.place(relx=0.1, rely=0.19, height=20)

        self.project_name_box = Entry(self, textvariable=self.projectName)
        self.project_name_box.place(relx=0.1, rely=0.23, relwidth=0.25, height=20)
        self.project_name_box.focus()

        self.musician_name = Label(self, text="artiest:", bg=settings.PROGRAM_BG)
        self.musician_name.place(relx=0.1, rely=0.29, height=20)

        self.musician_name_cb = ttk.Combobox(self, textvariable=self.musicianName, state="readonly", height=5)
        self.musician_name_cb.place(relx=0.1, rely=0.33, relwidth=0.25)
        # retrieve musicians in order to fill combobox
        self.fill_musician_name_cb(self.user)

        self.create_button_frame()

        # Rename project section => define widgets
        self.label_rename = Label(self, text="Wijzig naam van project", bg=settings.PROGRAM_BG)
        self.label_rename.place(relx=0.1, rely=0.57)

        self.project_current_name = Label(self, text="project:", bg=settings.PROGRAM_BG)
        self.project_current_name.place(relx=0.1, rely=0.66)

        self.project_current_name_cb = ttk.Combobox(self, textvariable=self.projectCurrentName, state="readonly",
                                                    height=5)
        self.project_current_name_cb.place(relx=0.1, rely=0.7, relwidth=0.25)
        # retrieve all ongoing projects, populate combobox and assign default option
        self.fill_project_current_name_combobox()

        self.project_new_name = Label(self, text="nieuwe naam:", bg=settings.PROGRAM_BG)
        self.project_new_name.place(relx=0.1, rely=0.76, height=20)

        self.project_new_name_box = Entry(self, textvariable=self.projectNewName)
        self.project_new_name_box.place(relx=0.1, rely=0.8, relwidth=0.25, height=20)

        self.create_button_frame2()

        # Finalize project section => define widgets
        self.label_finalize = Label(self, text="Voltooi project", bg=settings.PROGRAM_BG)
        self.label_finalize.place(relx=0.5, rely=0.10)
        # label displaying explanatory note
        self.label_explanatory_note = Label(text="Voltooi een project door de huidige datum als " +
                                                 "einddatum op te slaan", fg='red', font=('Arial', 10, 'italic'),
                                            bg=settings.PROGRAM_BG)
        self.label_explanatory_note.place(relx=0.5, rely=0.13)

        self.project_completable_project_name = Label(self, text="project:", bg=settings.PROGRAM_BG)
        self.project_completable_project_name.place(relx=0.5, rely=0.19, height=20)

        self.project_completable_project_name_cb = ttk.Combobox(self, textvariable=self.projectCompletableProjectName,
                                                                state="readonly", height=5)
        self.project_completable_project_name_cb.place(relx=0.5, rely=0.23, relwidth=0.25)
        # populate combobox with data retrieved from database
        self.fill_project_completable_project_name_cb()

        self.create_button_frame3()

        # Show product data section => define widgets
        self.label_show = Label(self, text="Toon projectcomponenten", bg=settings.PROGRAM_BG)
        self.label_show.place(relx=0.5, rely=0.57)

        self.project_list_all = Label(self, text="naam:", bg=settings.PROGRAM_BG)
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
            combo_values.append(f"{musician.userID} {musician.last_name} {musician.first_name}")
        self.musician_name_cb["values"] = combo_values
        self.musician_name_cb.current(0)

    def fill_project_current_name_combobox(self):
        ongoing_projects = self.project.select_all_active_projects()
        combo_values = []
        for project in ongoing_projects:
            combo_values.append(f"{project.projectID} {project.album_name} / {project.last_name} {project.first_name}")
        self.project_current_name_cb["values"] = combo_values
        self.project_current_name_cb.current(0)

    def fill_project_completable_project_name_cb(self):
        completable_projects = self.project.select_all_active_projects()
        combo_values = []
        for project in completable_projects:
            combo_values.append(f"{project.projectID} {project.album_name} / {project.last_name} {project.first_name}")
        self.project_completable_project_name_cb["values"] = combo_values
        self.project_completable_project_name_cb.current(0)

    def fill_project_list_all_cb(self):
        all_projects = self.project.select_all_projects()
        combo_values = []
        for project in all_projects:
            combo_values.append(f"{project.projectID} {project.album_name} / {project.last_name} {project.first_name}")
        self.project_list_all_cb["values"] = combo_values
        self.project_list_all_cb.current(0)

    # button frames and their allocated buttons
    def create_button_frame(self):
        button_frame = Frame(self, bg=settings.PROGRAM_BG)
        button_create = Button(button_frame, text="Maak aan", command=self.create_project, bg=settings.BUTTON_BG, padx=20)
        button_reset = Button(button_frame, text="Reset", command=self.reset_create,
                              bg=settings.BUTTON_BG, padx=20)
        button_create.pack(side="left")
        button_reset.pack(side="right")
        button_frame.place(relx=0.1, rely=0.4, relwidth=0.25)

    def create_button_frame2(self):
        button_frame2 = Frame(self, bg=settings.PROGRAM_BG)
        button_rename = Button(button_frame2, text="Wijzig naam", command=self.rename_project, bg=settings.BUTTON_BG,
                               padx=20)
        button_reset2 = Button(button_frame2, text="Reset", command=self.reset_rename, bg=settings.BUTTON_BG, padx=20)
        button_frame2.place(relx=0.1, rely=0.87, relwidth=0.25)
        button_rename.pack(side="left")
        button_reset2.pack(side="right")

    def create_button_frame3(self):
        button_frame3 = Frame(self, bg=settings.PROGRAM_BG)
        button_finalize = Button(button_frame3, text="Voltooi", command=self.finalize_project, bg=settings.BUTTON_BG,
                                 padx=20)
        button_reset3 = Button(button_frame3, text="Reset", command=self.reset_finalize,
                               bg=settings.BUTTON_BG, padx=20)
        button_frame3.place(relx=0.5, rely=0.3, relwidth=0.25)
        button_finalize.pack(side="left")
        button_reset3.pack(side="right")

    def create_button_frame4(self):
        button_frame4 = Frame(self, bg=settings.PROGRAM_BG)
        button_show = Button(button_frame4, text="Toon", command=self.show_project_data, bg=settings.BUTTON_BG, padx=20)
        button_reset4 = Button(button_frame4, text="Reset", command=self.reset_show, bg=settings.BUTTON_BG, padx=20)
        button_frame4.place(relx=0.5, rely=0.77, relwidth=0.25)
        button_show.pack(side="left")
        button_reset4.pack(side="right")

    def create_project(self):
        self.message = ""     # clear any previously set error messages

        self.project.project_name = self.get_string(self.projectName.get(), "naam")

        if self.message == "":
            if self.musicianName.get():
                item_db_index = self.get_db_id_of_selected_item(self.musician_name_cb)
                if (self.project.check_project_exists(self.project.project_name)) == True:
                    messagebox.showinfo("Probleem", "Er bestaat reeds een project met deze naam, voer een andere naam" +
                                                    " in")
                    return
                result = self.project.add_project(self.project.project_name, item_db_index)
                if isinstance(result, int):
                    self.refill_comboboxes_with_modified_data()
                    messagebox.showinfo("Geslaagd", "Project toegevoegd aan databank.")
            else:
                self.message = "Selecteer aub een artiest."
                messagebox.showerror("Foutmelding", self.message)
        else:
            messagebox.showerror("Foutmelding", self.message)

    def rename_project(self):
        self.message = ""     # clear any previously set error messages

        self.project.project_new_name = self.get_string(self.projectNewName.get(), "nieuwe naam")

        if self.message == "":
            if self.projectCurrentName.get():
                item_db_index = self.get_db_id_of_selected_item(self.project_current_name_cb)
                result = self.project.rename_project(self.project.project_new_name, item_db_index)
                if isinstance(result, int):
                    self.refill_comboboxes_with_modified_data()
                    messagebox.showinfo("Geslaagd", "Naam van project met succes gewijzigd.")
            else:
                self.message = "Selecteer aub een bestaand project wiens naam je wenst te wijzigen."
                messagebox.showerror("Foutmelding", self.message)
        else:
            messagebox.showerror("Foutmelding", self.message)

    def finalize_project(self):
        self.message = ""     # clear any previously set error messages

        if self.projectCompletableProjectName.get():
            item_db_index = self.get_db_id_of_selected_item(self.project_completable_project_name_cb)
            result = self.project.finalize_project(item_db_index)
            if isinstance(result, int):
                self.refill_comboboxes_with_modified_data()
                messagebox.showinfo("Geslaagd", "De huidige datum werd met succes als einddatum aan het project" +
                                                "toegewezen.")
        else:
            self.message = "Selecteer aub een project dat je wenst te voltooien."
            messagebox.showerror("Foutmelding", self.message)

    def show_project_data(self):
        self.message = ""  # clear any previously set error messages

        if self.projectListAll.get():
            selected_project_id = self.get_db_id_of_selected_item(self.project_list_all_cb)
            self.window_object.open_project_data(selected_project_id)
        else:
            self.message = "Selecteer aub een project waarvan je de samenstelling wil bekijken."
            messagebox.showerror("Foutmelding", self.message)

    def get_string(self, val, fieldName):
        if len(val) >= 4:
            return val
        else:
            self.message += f"De waarde in het invoerveld \"{fieldName}\" moet uit minstens vier karakters bestaan.\n"

    def get_db_id_of_selected_item(self, combobox):
        selected_value = combobox.get()
        if selected_value:
            i = selected_value.find(" ")
            idx = int(selected_value[0:i])
            return idx

    def refill_comboboxes_with_modified_data(self):
        self.fill_project_current_name_combobox()
        self.fill_project_completable_project_name_cb()
        self.fill_project_list_all_cb()
