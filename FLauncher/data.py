from PIL import Image
import customtkinter as CTk
import minecraft_launcher_lib
import os

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'FLauncher')
config_file_path = os.path.join(minecraft_directory, 'Client.ini')
versions_directory = os.path.join(minecraft_directory, 'versions')

nickname = "Nicname"

installed_versions = []
allModLouders = ["Forge", "Fabric", "Quilt"]

appearanceMode = "dark"
defaultColorTheme = "theme/violet.json"

mainWindowGeometry = "800x500"
newVersionWindowgeometry = "400x400"

bgColor = "#313131"
upFrameColor = "#454346"
downFrameColor = "#525053"
exitButtonColor = "#A73030"
exitButtonColor2 = "#872727"
versionColor = "#222222"
versionColorDown = "#1A1A1A"
setingMenyColor = "#404040"

miniLogo = CTk.CTkImage(dark_image=Image.open("Image\LOGO_mini.png"), size=(100, 22))
exitImage = CTk.CTkImage(dark_image=Image.open("Image\Exit.png"), size=(17, 17))
setingImage = CTk.CTkImage(dark_image=Image.open("Image\Seting.png"), size=(17, 17))
versionImage = CTk.CTkImage(dark_image=Image.open("Image\Version.png"), size=(17, 17))
plusImage = CTk.CTkImage(dark_image=Image.open("Image\Plus.png"), size=(17, 17))
plusImageImage = CTk.CTkImage(dark_image=Image.open("Image\Image.png"), size=(50, 39))
houmImage = CTk.CTkImage(dark_image=Image.open("Image\Houm.png"), size=(25, 20))
tasselImage = CTk.CTkImage(dark_image=Image.open("Image\Tassel.png"), size=(25, 25))
helpImage = CTk.CTkImage(dark_image=Image.open("Image\Help.png"), size=(18, 25))

release_versions = None
snapshot_versions = None