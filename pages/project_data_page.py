from tkinter import Button, Entry, Frame, Label, Listbox, messagebox, StringVar, ttk
from tkinter import *
import tkinter as tk
from classes.user import User
from classes.project_session import ActiveProject, ActiveSession
from classes.chain import Chain
import settings


class Project_Data_Page(Frame):
    def __init__(self, root, id_proj, width, height, user: User):
        super().__init__(root, width=width, height=height)
        self.configure(bg=settings.PROGRAM_BG)

        # instantiate ActiveProject instance
        self.project = ActiveProject()
        self.project.projectID = id_proj
        # instantiate ActiveSession instance
        self.session = ActiveSession()
        # instantiate Chain instance
        self.chain = Chain()
        # define string variables
        self.projectName = StringVar()

        # define widgets
        # show selected project
        self.selected_project = Label(self, text="selected project:", bg=settings.PROGRAM_BG)
        self.selected_project.place(relx=0.1, rely=0.1, height=20)

        self.selected_project_table = ttk.Treeview(self, height=1)
        self.fill_project_table(self.project.projectID)

        # list selected project's session(s) with accompanying setup description
        self.project_sessions = Label(self, text="project session(s):", bg=settings.PROGRAM_BG)
        self.project_sessions.place(relx=0.1, rely=0.23, height=20)

        self.project_sessions_list = Listbox(self)
        self.project_sessions_list.place(relx=0.1, rely=0.28, height=60, relwidth=0.6)
        self.fill_sessions_list(self.project.projectID)

        # list chains pertaining to the selected session
        button_select_session = Button(self, text="List chains", command=self.fill_chains_list, bg=settings.BUTTON_BG,
                                       width=20)
        button_select_session.place(relx=0.75, rely=0.31)

        self.project_chains = Label(self, text="chains pertaining to selected session's setup:", bg=settings.PROGRAM_BG)
        self.project_chains.place(relx=0.1, rely=0.43, height=20)

        self.project_chains_list = Listbox(self)
        self.project_chains_list.place(relx=0.1, rely=0.48, height=80, relwidth=0.6)
        # listbox is filled when button_select_session button is clicked

        # list the selected chain's gear units
        button_select_chain = Button(self, text="List gear units", command=self.fill_gearunits_list,
                                     bg=settings.BUTTON_BG, width=20)
        button_select_chain.place(relx=0.75, rely=0.53)

        self.chain_gearunits = Label(self, text="selected chain's gear units:", bg=settings.PROGRAM_BG)
        self.chain_gearunits.place(relx=0.1, rely=0.65, height=20)

        self.chain_gearunits_list = Listbox(self)
        self.chain_gearunits_list.place(relx=0.1, rely=0.7, height=80, relwidth=0.5)
        # listbox is filled when button_select_chain button is clicked

    # define instance methods
    def fill_project_table(self, id):
        retrieved_project = self.project.select_project(id)

        self.selected_project_table.place(relx=0.2, rely=0.1)
        self.selected_project_table['columns'] = ('project', 'artist', 'start date', 'end date')
        self.selected_project_table.column("#0", width=0, stretch=NO)
        self.selected_project_table.column("project", anchor=CENTER, stretch=NO)
        self.selected_project_table.column("artist", anchor=CENTER, stretch=NO)
        self.selected_project_table.column("start date", anchor=CENTER, stretch=NO, minwidth=50)
        self.selected_project_table.column("end date", anchor=CENTER, stretch=NO, minwidth=50)
        self.selected_project_table.heading("#0", text="", anchor=CENTER)
        self.selected_project_table.heading("project", text="project", anchor=CENTER)
        self.selected_project_table.heading("artist", text="artist", anchor=CENTER)
        self.selected_project_table.heading("start date", text="start date", anchor=CENTER)
        self.selected_project_table.heading("end date", text="end date", anchor=CENTER)
        self.selected_project_table.insert('', tk.END, values=(retrieved_project.album_name,
                                                               retrieved_project.last_name + " " +
                                                               retrieved_project.first_name,
                                                               retrieved_project.start_date,
                                                               retrieved_project.end_date))

    def fill_sessions_list(self, id):
        sessions = self.session.select_project_sessions(id)
        if len(sessions) > 0:
            for session in sessions:
                self.project_sessions_list.insert(session.sessionID, f"ID: {session.sessionID} / {session.album_name}, "
                                                                     f"type {session.session_type_name}, "
                                                                     f"{session.setup_name}, "
                                                                     f"{session.setup_description}")
        else:
            self.project_sessions_list.insert(0, "No sessions have been assigned to this project.")

    def fill_chains_list(self):
        selected_id = self.project_sessions_list.curselection()
        if len(selected_id) == 0:
            messagebox.showerror("Error", "Please select an item in the listbox")
            return
        if (isinstance(selected_id[0], int)):
            chains = self.chain.select_setup_chains(selected_id[0])
            if len(chains) > 0:
                self.project_chains_list.delete(0, tk.END)
                for chain in chains:
                    self.project_chains_list.insert(chain.chainID, f"{chain.chain_name} channel: {chain.channel}")
            else:
                self.project_chains_list.delete(0, tk.END)
                self.project_chains_list.insert(0, "No chains have been assigned to this setup.")
        else:
            self.project_chains_list.insert(0, "No chains have been assigned to this setup.")

    def fill_gearunits_list(self):
        pass
