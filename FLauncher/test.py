import customtkinter as CTk
import minecraft_launcher_lib as mll
import minecraft_launcher_lib.forge as mllForge
import minecraft_launcher_lib.fabric as mllFabric
import minecraft_launcher_lib.quilt as mllQuild
import data as d
import tkinter
from random_username.generate import generate_username
from uuid import uuid1
import subprocess
import threading
import os
from functools import cache

class SettingsWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CTk.set_appearance_mode(d.appearanceMode)
        CTk.set_default_color_theme(d.defaultColorTheme)
        self.iconbitmap("Image/LOGO.ico")
        self.geometry(d.mainWindowGeometry)
        self.title("FLauncher")
        self.resizable(False, False) 
        self.bgFrame = CTk.CTkFrame(master=self, fg_color=d.bgColor, width=800, height=500, bg_color=d.bgColor)
        self.bgFrame.place(x=0, y=0)

        self.leftFrame = CTk.CTkFrame(master=self, fg_color=d.upFrameColor, width=170, height=500, bg_color=d.setingMenyColor)
        self.leftFrame.place(x=0, y=0)

        self.houmButton =  CTk.CTkButton(
                    width=123,
                    height=30,
                    image= d.houmImage,
                    master=self.leftFrame,
                    text= "главная",
                    command=self.openHoumFrame,
                    )
        self.houmButton.place(x=15, y=15)

        self.houmButton =  CTk.CTkButton(
                    width=123,
                    height=30,
                    image= d.tasselImage,
                    master=self.leftFrame,
                    text= "оформления",
                    command=self.openTeemFrame,
                    )
        self.houmButton.place(x=15, y=60)

        self.houmButton =  CTk.CTkButton(
                    width=123,
                    height=30,
                    image= d.helpImage,
                    master=self.leftFrame,
                    text= "помощь",
                    command=self.openHelpFrame,
                    )
        self.houmButton.place(x=15, y=105)



    def openHoumFrame(self):
#        self.memory_slider.place(x=204, y=47)
        pass

    def openTeemFrame(self):
#        self.memory_slider.place_forget()
        pass

    def openHelpFrame(self):
#        self.memory_slider.place_forget()
        pass

class NewVersionWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CTk.set_appearance_mode(d.appearanceMode)
        CTk.set_default_color_theme(d.defaultColorTheme)
        self.iconbitmap("Image/LOGO.ico")
        self.geometry(d.newVersionWindowgeometry)
        self.title("FLauncher")
        self.resizable(False, False) 
        self.modLouder = "Forge"

        self.bgFrame = CTk.CTkFrame(master=self, fg_color=d.bgColor, width=400, height=400, bg_color=d.bgColor)
        self.bgFrame.place(x=0, y=0)

        self.upFrame = CTk.CTkFrame(master=self, fg_color=d.upFrameColor, width=400, height=47, bg_color=d.upFrameColor)
        self.upFrame.place(x=0, y=0)

        self.miniLogoLable = CTk.CTkLabel(master=self.upFrame, text="", image=d.miniLogo)
        self.miniLogoLable.place(x=10, y=5)

        self.imageSaizeLeibl = CTk.CTkLabel(master=self.bgFrame, text="240x101", font=("font\standart.ttf", 16), width=117, height=22)
        self.imageSaizeLeibl.place(x=10, y=55)

        self.versionNameLeibl = CTk.CTkLabel(master=self.bgFrame, text="Имя Версии", font=("font\standart.ttf", 16), width=200, height=22)
        self.versionNameLeibl.place(x=151, y=55)

        self.imageButton =  CTk.CTkButton(
                    width=117,
                    height=117,
                    image=d.plusImageImage,
                    master=self.bgFrame,
                    text= "",
                    command=self.openImage,
                    )
        self.imageButton.place(x=10, y=83)

        self.versionButton =  CTk.CTkButton(
                    width=129,
                    height=20,
                    master=self.bgFrame,
                    text= "версия",
                    command=self.openImage,
                    )
        self.versionButton.place(x=262, y=120)

        self.versionModlouderButton =  CTk.CTkButton(
                    width=129,
                    height=20,
                    master=self.bgFrame,
                    text= "версия " + self.modLouder,
                    command=self.openImage,
                    )
        self.versionModlouderButton.place(x=262, y=153)

        self.versionNameEntry = CTk.CTkEntry(master=self.bgFrame, width=240, height= 20, fg_color=d.upFrameColor)
        self.versionNameEntry.place(x=151, y=84)

        self.modLouderCombobox = CTk.CTkComboBox(master= self.bgFrame, values=d.allModLouders, width=90, height=20)
        self.modLouderCombobox.place(x=151, y=153)

    def openImage(self):
        pass

@cache
class VersionWindow(CTk.CTkToplevel):
    def __init__(self, app_instance, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CTk.set_appearance_mode(d.appearanceMode)
        CTk.set_default_color_theme(d.defaultColorTheme)
        self.iconbitmap("Image/LOGO.ico")

        self.app_instance = app_instance
 
        self.bgFrame = CTk.CTkFrame(master=self, fg_color=d.bgColor, width=800, height=500)
        self.bgFrame.place(x=0, y=0)
 
        self.geometry(d.mainWindowGeometry)
        self.title("FLauncher")
        self.resizable(False, False)

        self.tabview = CTk.CTkTabview(master=self.bgFrame, width=800, height=500)
        self.tabview.place(x= 0, y=0)
        self.tabview.add("версии")
        self.tabview.add("снепшоти")
        self.tabview.add("мои версии")
 
        self.versionCanvas = CTk.CTkCanvas(master=self.tabview.tab("версии"), bg=d.bgColor, width=800, height=500, highlightthickness=0)
        self.versionCanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        self.snapshotСanvas = tkinter.Canvas(master=self.tabview.tab("снепшоти"), bg=d.bgColor, width=800, height=500, highlightthickness=0)
        self.snapshotСanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        self.VersionCanvasFrame = CTk.CTkFrame(self.versionCanvas, bg_color=d.bgColor)
        self.versionCanvas.create_window((0, 0), window=self.VersionCanvasFrame, anchor=tkinter.NW, width=800, height=5500)

        self.SnapshotCanvasFrame = CTk.CTkFrame(self.snapshotСanvas, bg_color=d.bgColor)
        self.snapshotСanvas.create_window((0, 0), window=self.SnapshotCanvasFrame, anchor=tkinter.NW, width=800, height=30035)
 
        version_x_offset = 15
        version_y_offset = 15
        version_row_count = 0

        snapshot_x_offset = 15
        snapshot_y_offset = 15
        snapshot_row_count = 0
 
        def launch_game(version):
            threading.Thread(target=self.app_instance.launchMinecraft, args=(version,)).start()
 
        for version in d.release_versions:
            version_frame = CTk.CTkFrame(master=self.VersionCanvasFrame, fg_color=d.versionColor, width=240, height=144, bg_color=d.bgColor)
            version_frame.place(x=version_x_offset, y=version_y_offset)
 
            version_frame_down = CTk.CTkFrame(master=self.VersionCanvasFrame, fg_color=d.versionColorDown, width=240, height=43, bg_color=d.versionColorDown)
            version_frame_down.place(x=version_x_offset, y=version_y_offset + 101)
 
            version_label_down = CTk.CTkLabel(version_frame_down, text=version, fg_color="transparent", font=("Nico Moji", 12))
            version_label_down.place(x=5, y=7)
 
            version_label = CTk.CTkLabel(version_frame, text=version, fg_color="transparent", font=("Nico Moji", 24), width=240, height=101)
            version_label.place(x=0, y=0)
 
            if version not in d.installed_versions:
                install_button = CTk.CTkButton(width=14, height=14, master=version_frame_down, text="установить",fg_color= d.upFrameColor, hover_color= d.bgColor, command=lambda version=version: launch_game(version))
                install_button.place(x=150, y=10)
            else:
                play_button = CTk.CTkButton(width=14, height=14, master=version_frame_down, text="играть", command=lambda version=version: launch_game(version))
                play_button.place(x=180, y=10)
 
            version_row_count += 1
            if version_row_count >= 3:
                version_row_count = 0
                version_x_offset = 15
                version_y_offset += 190
            else:
                version_x_offset += 260
 
        self.VersionCanvasFrame.update_idletasks()
        self.versionCanvas.config(scrollregion=self.versionCanvas.bbox(tkinter.ALL))
        self.versionCanvas.bind_all("<MouseWheel>", self._on_mousewheel)

        for version in d.snapshot_versions:
            snapshot_frame = CTk.CTkFrame(master=self.SnapshotCanvasFrame, fg_color=d.versionColor, width=240, height=144, bg_color=d.bgColor)
            snapshot_frame.place(x=snapshot_x_offset, y=snapshot_y_offset)
 
            snapshot_frame_down = CTk.CTkFrame(master=self.SnapshotCanvasFrame, fg_color=d.versionColorDown, width=240, height=43, bg_color=d.versionColorDown)
            snapshot_frame_down.place(x=snapshot_x_offset, y=snapshot_y_offset + 101)
 
            snapshot_label_down = CTk.CTkLabel(snapshot_frame_down, text=version, fg_color="transparent", font=("Nico Moji", 12))
            snapshot_label_down.place(x=5, y=7)
 
            snapshot_label = CTk.CTkLabel(snapshot_frame, text=version, fg_color="transparent", font=("Nico Moji", 24), width=240, height=101)
            snapshot_label.place(x=0, y=0)
 
            if version not in d.installed_versions:
                install_button = CTk.CTkButton(width=14, height=14, master=snapshot_frame_down, text="установить",fg_color= d.upFrameColor, hover_color= d.bgColor, command=lambda version=version: launch_game(version))
                install_button.place(x=150, y=10)
            else:
                play_button = CTk.CTkButton(width=14, height=14, master=snapshot_frame_down, text="играть", command=lambda version=version: launch_game(version))
                play_button.place(x=180, y=10)
 
            snapshot_row_count += 1
            if snapshot_row_count >= 3:
                snapshot_row_count = 0
                snapshot_x_offset = 15
                snapshot_y_offset += 190
            else:
                snapshot_x_offset += 260
 
        self.SnapshotCanvasFrame.update_idletasks()
        self.snapshotСanvas.config(scrollregion=self.snapshotСanvas.bbox(tkinter.ALL))
 
        self.snapshotСanvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.snapshotСanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.versionCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

 
    def exit_program(self):
        if self.versionCanvas:
            self.versionCanvas.destroy()
        if self.snapshotСanvas:
            self.snapshotСanvas.destroy()
        self.destroy()

class APP(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.versionwindow = None
        self.newversionwindow = None
        self.settingswindow =None
        self.iconbitmap("Image/LOGO.ico")
        

        CTk.set_appearance_mode(d.appearanceMode)
        CTk.set_default_color_theme(d.defaultColorTheme)

        variable = tkinter.StringVar()
        variable.set("версии")

        self.geometry(d.mainWindowGeometry)
        self.title("FLauncher")
        self.resizable(False, False)

        self.bgFrame = CTk.CTkFrame(master=self, fg_color=d.bgColor, width=800, height=500, bg_color=d.bgColor)
        self.bgFrame.place(x=0, y=0)

        self.upFrame = CTk.CTkFrame(master=self, fg_color=d.upFrameColor, width=800, height=39, bg_color=d.bgColor)
        self.upFrame.place(x=0, y=0)

        self.downFrame = CTk.CTkFrame(master=self, fg_color=d.downFrameColor, width=800, height=55, bg_color=d.bgColor)
        self.downFrame.place(x=0, y=445)

        self.miniLogoLable = CTk.CTkLabel(master=self.upFrame, text="", image=d.miniLogo)
        self.miniLogoLable.place(x=10, y=5)

        self.exitButton = CTk.CTkButton(width=14,
                                        height=14,
                                        image=d.exitImage,
                                        master=self.upFrame,
                                        text= "",
                                        command=self.exit_program,
                                        fg_color=d.exitButtonColor,
                                        hover_color= d.exitButtonColor2)
        self.exitButton.place(x=768, y=7)

        self.setingButton = CTk.CTkButton(width=14,
                                          height=14,
                                          image=d.setingImage,
                                          master=self.upFrame,
                                          text= "",
                                          command=self.openSetting,)
        self.setingButton.place(x=730, y=7)
        
        self.versionButton = CTk.CTkButton(width=14,
                                           height=14,
                                           image=d.versionImage
                                           ,master=self.upFrame,
                                           text= "версии",
                                           command=self.openVersionWindow,)
        self.versionButton.place(x=640, y=7)
        
        self.newVersionButton = CTk.CTkButton(width=14,
                                              height=14,
                                              image=d.plusImage,
                                              master=self.upFrame,
                                              text= "новая версия",
                                              command=self.openNewVersionWindow,)
        self.newVersionButton.place(x=510, y=7)

        self.PlayButton = CTk.CTkButton(master=self.downFrame,
                                              text= "играть",
                                              command=self.startGame,)
        self.PlayButton.place(x=600, y=14)

        self.nicknameEntry = CTk.CTkEntry(master=self.downFrame)
        self.nicknameEntry.insert(0, "Nickname")
        self.nicknameEntry.place(x=15, y=14)


        self.versionComboBox = CTk.CTkComboBox(master= self.downFrame,variable=variable, values=d.installed_versions)
        self.versionComboBox.place(x=222, y=14)

        self.updateVersionsList()

        self.progressBar = CTk.CTkProgressBar(master= self, width= 800)
        self.progressBar.configure(mode="indeterminnate")
        self.progressBar.set(1)
        self.progressBar.place(x=0, y=426)
    
    def updateVersionsList(self):
        if os.path.exists(d.versions_directory):
            versions = os.listdir(d.versions_directory)
            self.versionComboBox.configure(state="normal")

            d.installed_versions = []  # Очищаем список перед обновлением, чтобы избежать дублирования
            for version in versions:
                d.installed_versions.append(version)

            # Обновляем значения выпадающего списка
            self.versionComboBox.configure(values= d.installed_versions)

        else:
           self.versionComboBox.configure(state="disabled")



    def exit_program(self):
        self.destroy()
    
    def openSetting(self):
        if self.settingswindow is None or not self.settingswindow.winfo_exists():
            self.settingswindow = SettingsWindow(self)
            self.settingswindow.lift()
            self.after(100, lambda: self.settingswindow.focus_force())
        else:
            self.settingswindow.lift()
            self.after(100, lambda: self.settingswindow.focus_force())

    def openVersionWindow(self):
        def load_versions():
            nonlocal self
            self.progressBar.start()

            versions = mll.utils.get_version_list()
            d.release_versions = [version['id'] for version in versions if version['type'] == 'release']
            d.snapshot_versions = [version['id'] for version in versions if version['type'] == 'snapshot']

            self.versionwindow = VersionWindow(self)
            

            # Обновляем интерфейс после завершения загрузки версий
            self.progressBar.stop()
            self.updateVersionsList()

        threading.Thread(target=load_versions).start()

    
    def openNewVersionWindow(self):
        if self.newversionwindow is None or not self.newversionwindow.winfo_exists():
            self.newversionwindow = NewVersionWindow(self)
            self.newversionwindow.lift()
            self.after(100, lambda: self.newversionwindow.focus_force())
        else:
            self.newversionwindow.lift()
            self.after(100, lambda: self.newversionwindow.focus_force())
    
    def startGame(self):
        threading.Thread(target=self.launchMinecraft, args=(self.versionComboBox.get(),)).start()

    def launchMinecraft(self, version):

        if self.versionwindow and self.versionwindow.winfo_exists():
            self.versionwindow.exit_program()  # Уберите эту строку из метода

        username = self.nicknameEntry.get()
        if username == "":
            username = generate_username()[0]

        options = {
            'username': username,
            'uuid': str(uuid1()),
            'token': ''
        }

        self.progressBar.start()
        mll.install.install_minecraft_version(versionid=version, minecraft_directory=d.minecraft_directory)

        self.updateVersionsList()

        subprocess.call(mll.command.get_minecraft_command(version=version, minecraft_directory=d.minecraft_directory, options=options))
        self.progressBar.stop()
        self.progressBar.set(1)

if __name__ == "__main__":
    app = APP()
    app.mainloop()