init python:
    if not persistent.girl_icons_dict:
        persistent.girl_icons_dict = {}


    if persistent.main_menu_music is None or not file_check(persistent.main_menu_music):
        persistent.main_menu_music = "ShiningStarVocals.mp3"
    renpy.music.register_channel("menu_movie", "music", True, movie=True)

    if persistent.game_theme is None:
        persistent.game_theme = "Default"

init 201 python:
    define_mods_images.update({
        "menu_gui":"mods/customizationmod/themes/Default/menu_gui.png",
        "buried":"mods/customizationmod/themes/Default/buried.png"
    })

init 1000 python:
    customizationmod = True
    if persistent.mod_main_menu_image == None:
        search_menu_images()
        persistent.mod_main_menu_image = image_list[0]
    config.main_menu_music = persistent.main_menu_music
    if not isinstance(persistent.mod_main_menu_image, str):
        if persistent.mod_main_menu_image[1] == 1:
            config.main_menu_music = None
    
    if persistent.game_theme == "Kirin":
        s = Character("Сэнсэй", color="#FFFFFF")
        te = Character("Учитель", color="#FFFFFF")
        gui.text_color = '#FFFFFF'
        gui.interface_text_color = '#FFFFFF'

init 2000 python:
    if persistent.game_theme != "Default":
        define_mods_images.update(load_theme_image_dict(persistent.game_theme))
