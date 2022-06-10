from tkinter import messagebox, ttk
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

        # store id for each returned object in the appropriate list
        self.list_sessionIds = []
        self.list_chainIds = []

        # define widgets
        # show selected project
        self.selected_project = Label(self, text="project:", bg=settings.PROGRAM_BG)
        self.selected_project.place(relx=0.1, rely=0.1, height=20)

        self.selected_project_table = ttk.Treeview(self, height=1)
        self.fill_project_table(self.project.projectID)

        # list selected project's session(s) with accompanying setup description
        self.project_sessions = Label(self, text="projectsessie(s):", bg=settings.PROGRAM_BG)
        self.project_sessions.place(relx=0.1, rely=0.23, height=20)

        self.project_sessions_list = Listbox(self)
        self.project_sessions_list.place(relx=0.1, rely=0.28, height=60, relwidth=0.6)
        self.fill_sessions_list(self.project.projectID)

        # list chains pertaining to the selected session
        button_select_session = Button(self, text="Toon ketens", command=self.fill_chains_list, bg=settings.BUTTON_BG,
                                       width=20)
        button_select_session.place(relx=0.75, rely=0.31)

        self.setup_chains = Label(self, text="ketens binnen de op de geselecteerde sessie toegepaste setup:",
                                  bg=settings.PROGRAM_BG)
        self.setup_chains.place(relx=0.1, rely=0.43, height=20)

        self.setup_chains_list = Listbox(self)
        self.setup_chains_list.place(relx=0.1, rely=0.48, height=80, relwidth=0.6)
        # listbox is filled when button_select_session button is clicked

        # list the selected chain's gear units
        button_select_chain = Button(self, text="toon gear units", command=self.fill_gearunits_list,
                                     bg=settings.BUTTON_BG, width=20)
        button_select_chain.place(relx=0.75, rely=0.53)

        self.chain_gearunits = Label(self, text="gear units in geselecteerde keten:", bg=settings.PROGRAM_BG)
        self.chain_gearunits.place(relx=0.1, rely=0.66, height=20)

        self.chain_gearunits_list = Listbox(self)
        self.chain_gearunits_list.place(relx=0.1, rely=0.71, height=80, relwidth=0.6)
        # listbox is filled when button_select_chain button is clicked

    # define instance methods
    def fill_project_table(self, project_id):
        retrieved_project = self.project.select_project(project_id)

        self.selected_project_table.place(relx=0.2, rely=0.1)
        self.selected_project_table['columns'] = ('project', 'artiest', 'startdatum', 'einddatum')
        self.selected_project_table.column("#0", width=0, stretch=NO)
        self.selected_project_table.column("project", anchor=CENTER, stretch=NO)
        self.selected_project_table.column("artiest", anchor=CENTER, stretch=NO)
        self.selected_project_table.column("startdatum", anchor=CENTER, stretch=NO, minwidth=50)
        self.selected_project_table.column("einddatum", anchor=CENTER, stretch=NO, minwidth=50)
        self.selected_project_table.heading("#0", text="", anchor=CENTER)
        self.selected_project_table.heading("project", text="project", anchor=CENTER)
        self.selected_project_table.heading("artiest", text="artiest", anchor=CENTER)
        self.selected_project_table.heading("startdatum", text="startdatum", anchor=CENTER)
        self.selected_project_table.heading("einddatum", text="einddatum", anchor=CENTER)
        self.selected_project_table.insert('', tk.END, values=(retrieved_project.album_name,
                                                               retrieved_project.last_name + " " +
                                                               retrieved_project.first_name,
                                                               retrieved_project.start_date,
                                                               retrieved_project.end_date))

    def fill_sessions_list(self, project_id):
        sessions = self.session.select_project_sessions(project_id)
        if len(sessions) > 0:
            self.list_sessionIds.clear()
            for session in sessions:
                self.list_sessionIds.append(session.sessionID)
                self.project_sessions_list.insert(END, f"{session.album_name}, "
                                                       f"{session.session_name}, "
                                                       f"type {session.session_type_name}, "
                                                       f" setup: {session.setup_name}, "
                                                       f"{session.setup_description}")
        else:
            pass

    def fill_chains_list(self):
        self.setup_chains_list.delete(0, tk.END)
        self.chain_gearunits_list.delete(0, tk.END)
        selection = self.project_sessions_list.curselection()
        if len(selection) == 0:
            messagebox.showerror("Foutmelding", "Selecteer indien mogelijk een sessie")
            return
        selected_list_index = self.project_sessions_list.curselection()[0]
        selected_session_id = self.list_sessionIds[selected_list_index]
        if isinstance(selected_session_id, int) and selected_session_id > 0:
            chains = self.chain.select_setup_chains(selected_session_id)
            if len(chains) > 0:
                self.list_chainIds.clear()
                for chain in chains:
                    self.list_chainIds.append(chain.chainID)
                    self.setup_chains_list.insert(END, f"{chain.chain_name} channel: {chain.channel}")
            else:
                messagebox.showinfo("Info", "Aan deze sessie zijn nog geen ketens gekoppeld")

    def fill_gearunits_list(self):
        self.chain_gearunits_list.delete(0, tk.END)
        selection = self.setup_chains_list.curselection()
        if len(selection) == 0:
            messagebox.showerror("Foutmelding", "Selecteer indien mogelijk een optie uit de lijst")
            return
        selected_list_index = self.setup_chains_list.curselection()[0]
        selected_chain_id = int(self.list_chainIds[selected_list_index])
        if isinstance(selected_chain_id, int) and selected_chain_id > 0:
            self.chain.empty_gearunits_list()
            gearunits = self.chain.select_chain_gearunits(selected_chain_id)
            if len(gearunits) > 0:
                for gearunit in gearunits:
                    self.chain_gearunits_list.insert(END, f"{gearunit.gearunit_name}, " 
                                                          f"type: {gearunit.gearunit_type_name}, " 
                                                          f"positie {gearunit.unit_position}")
            else:
                messagebox.showinfo("Info", "Er zijn nog geen gear units aan de geselecteerde keten gekoppeld")
