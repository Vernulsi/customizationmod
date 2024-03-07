init offset = 100
screen music_room:
    tag menu
    add "lofirin.png"
    frame:
        background "#0008"
        xpadding 12
        ypadding 12
        yfill True
        side ("c b"):
            side ("c r"):
                viewport id "song_scroller":
                    draggable True
                    mousewheel True
                    xmaximum 384
                    vbox:
                        for music in modMusicList:
                            textbutton music[1] action mmr.Play(music[0])
                        for music in persistent.my_music:
                            textbutton music[1] action MusicCheck(music[0]) #mmr.Play(music[0]) #Function(music_check, music[0])
                vbar value YScrollValue("song_scroller") top_bar Solid("#fff2") bottom_bar Solid("#fff2") thumb Solid("#fff4")
            vbox:
                null height 20
                side ("l c r"):
                    xfill True
                    textbutton "< Пред." action [UpdateMusic(), mmr.Previous()]
                    textbutton "      | | Пауза" action Function(renpy.music.set_pause, not renpy.music.get_pause('music'), 'music')
                    textbutton "След. >" action [UpdateMusic(), mmr.Next()]
                null height 10
                textbutton "Установить в меню" action [If(renpy.music.get_playing(), true=[SetVariable("persistent.main_menu_music", renpy.music.get_playing()), SetVariable("config.main_menu_music", renpy.music.get_playing())])]
                hbox:
                    textbutton "Главное Меню" action ShowMenu("main_menu")
                    textbutton "Обновить" action UpdateMusic()
    text "{color=#FFFFFF}Сейчас играет:{/color}" xpos 427 ypos 970 size 48 outlines [(3,color('#000000'),1,1)]
    text (music_text()) xpos 427 ypos 1020 size 50 outlines [(3,color('#000000'),1,1)] color "#FFFFFF"
    on "replaced" action If(config.main_menu_music, true=If(config.main_menu_music == renpy.music.get_playing(), false=Play("music", config.main_menu_music)), false=Function(renpy.music.stop))
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    textbutton _("Вернуться"):
        style "return_button"
        if main_menu:
            action ShowMenu("main_menu")
        else:
            action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

screen main_menu():
    tag menu
    style_prefix "main_menu"
    add menu_image(persistent.mod_main_menu_image):
        if persistent.mod_main_menu_image is not None:
            xpos 432
            ypos 24
    add define_mods_images["menu_gui"]
    textbutton _("Изменить Картинку Меню"):
        action [Function(search_menu_images), ShowMenu("main_menu_mod_choise")]
        xpos 60 ypos 750
    textbutton _("Изменить Тему Игры"):
        action ShowMenu("theme_setter")
        xpos 60 ypos 800
    frame:
        pass
    use navigation
    imagebutton:
        xalign 0.17 yalign 0.84
        idle im.Scale("gui/discord_icon.png", 70, 70)
        hover im.Scale("gui/discord_icon.png", 80, 80)
        action OpenURL("https://discord.gg/KJd6ytUb2B")
    imagebutton:
        xalign 0.11 yalign 0.838
        idle im.Scale("gui/vk.png", 90, 70)
        hover im.Scale("gui/vk.png", 100, 80)
        action OpenURL("https://vk.com/club208168532")
    imagebutton:
        xalign 0.07 yalign 0.84
        idle im.Scale(define_mods_images["buried"], 70, 70)
        hover im.Scale(define_mods_images["buried"], 80, 80)
        action OpenURL("https://discord.gg/YhPMYv8p5B")
    on "replace" action If(config.main_menu_music and not renpy.music.get_playing() and not persistent.mod_main_menu_image[1] == 1, true=Play('music', config.main_menu_music))

screen main_menu_mod_choise:
    tag menu
    use game_menu(_("Выбор меню"), scroll="viewport"):
        style_prefix "aff"
        vpgrid :
            cols 2
            align (0.6, 0.45)
            spacing 80
            for img in image_list:
                if img[1] == 1:
                    imagebutton:
                        idle im.FactorScale(im.Scale("mods/customizationmod/images/def_image.png", 1459, 803), 0.4, bilinear=True)
                        action [SetVariable("persistent.mod_main_menu_image", img), If(config.main_menu_music == None, false=[SetVariable("config.main_menu_music", None), Function(renpy.music.stop)]), Return()]
                if img[1] == 3:
                    imagebutton:
                        idle im.FactorScale(im.Crop(img[0], (432, 24, 1459, 803)), 0.4, bilinear=True)
                        action [SetVariable("persistent.mod_main_menu_image", img), If(config.main_menu_music == None, true=[SetVariable("config.main_menu_music", persistent.main_menu_music)]), Return()]
                if img[1] == 2:
                    imagebutton:
                        idle im.FactorScale(im.Scale(img[0], 1459, 803), 0.4, bilinear=True)
                        action [SetVariable("persistent.mod_main_menu_image", img), If(config.main_menu_music == None, true=[SetVariable("config.main_menu_music", persistent.main_menu_music)]), Return()]
            if (len(image_list) % 2) == 1:
                null

screen theme_setter():
    tag menu
    use game_menu(_("Выбор Темы"), scroll="viewport"):
        style_prefix "aff"
        vpgrid :
            cols 1
            align (0.6, 0.45)
            spacing 80
            imagebutton:
                idle 'mods/customizationmod/themes/Kirin/idle_Kirin.png'
                hover 'mods/customizationmod/themes/Kirin/hover_Kirin.png'
                action Function(set_theme, 'Kirin')
            imagebutton:
                idle 'mods/customizationmod/themes/Default/idle_Default.png'
                hover 'mods/customizationmod/themes/Default/hover_Default.png'
                action Function(set_theme, 'Default')

screen icon_setter():
    tag menu
    $ trans = {
        'chika':'Чика', 'yumi':'Юми', 'ayane':'Аянэ', 'sana':'Сана', 'makoto':'Макото', 'miku':'Мику', 'futaba':'Футаба', 'rin':'Рин', 'ami':'Ами', 'maya':'Майя', 'molly':'Молли', 'tsuneyo':'Цунэя', 'uta':'Юта', 'io':'Ио', 'nodoka':'Нодока', 'otoha':'Отоха', 'touka':'Тоука', 'yasu':'Ясу', 'noriko':'Норико', 'kirin':'Кирин', 'sara':'Сара', 'haruka':'Харука', 'kaori':'Каори', 'chinami':'Чинами', 'karin':'Карин', 'maki':'Маки', 'yuki':'Юки', 'niki':'Ники', 'wakana':'Вакана', 'osako':'Осако', 'tsubasa':'Цубаса', 'tsukasa':'Цукаса', 'imani':'Имани', 'rika':'Рика', 'nao':'Нао'
    }
    add define_mods_images["mod_menu"]
    use menu_mod(_("Изменение Иконок Персонажей"), scroll="viewport"):
        style_prefix "aff"
        vpgrid:
            cols 5
            align (1, 1)
            spacing 80
            for girl in ['chika', 'yumi', 'ayane', 'sana', 'makoto', 'miku', 'futaba', 'rin', 'ami', 'maya', 'molly', 'tsuneyo', 'uta', 'io', 'nodoka', 'otoha', 'touka', 'yasu', 'noriko', 'kirin', 'sara', 'haruka', 'kaori', 'chinami', 'karin', 'maki', 'yuki', 'niki', 'wakana', 'osako', 'tsubasa', 'tsukasa', 'imani', 'rika', 'nao']:
                # imagebutton:
                #     idle  persistent.girl_icons_dict[girl]['icon']
                #     hover get_im_ico_p(persistent.girl_icons_dict[girl]['icon'], trans[girl][0].upper() + trans[girl][1:])
                #     focus_mask True
                #     action [Function(swap_icon, girl)]
                imagebutton:
                    idle  persistent.girl_icons_dict[girl]['icon']
                    hover im.Composite((190,190), (0,0), persistent.girl_icons_dict[girl]['icon'], (0,0), 'mods/customizationmod/images/' + girl + '.png')
                    focus_mask True
                    action [Function(swap_icon, girl)]
    
    on "show" action Function(search_icons)
screen eventtrackermaincharahub ():
    tag menu
    $ trans = {
                'chika':'Чика', 'yumi':'Юми', 'ayane':'Аянэ', 'sana':'Сана', 'makoto':'Макото', 'miku':'Мику', 'futaba':'Футаба', 'rin':'Рин', 'ami':'Ами', 'maya':'Майя', 'molly':'Молли', 'tsuneyo':'Цунэя', 'uta':'Юта', 'io':'Ио', 'nodoka':'Нодока', 'otoha':'Отоха', 'touka':'Тоука', 'yasu':'Ясу', 'noriko':'Норико', 'kirin':'Кирин'
    }
    use game_menu(_("Основные Персонажи"), scroll="viewport"):

        style_prefix "aff"

        grid 5 4:
            align (1, 1)
            xspacing 60
            yspacing 20

            for girl in ['chika', 'yumi', 'ayane', 'sana', 'makoto', 'miku', 'futaba', 'rin', 'ami', 'maya', 'molly', 'tsuneyo', 'uta', 'io', 'nodoka', 'otoha', 'touka', 'yasu', 'noriko', 'kirin']:
                # imagebutton:
                #     idle  persistent.girl_icons_dict[girl]['icon']
                #     hover get_im_ico_p(persistent.girl_icons_dict[girl]['icon'], trans[girl][0].upper() + trans[girl][1:])
                #     focus_mask True
                #     action [ShowMenu('gamemenu' + girl)]
                imagebutton:
                    idle  persistent.girl_icons_dict[girl]['icon']
                    hover im.Composite((190,190), (0,0), persistent.girl_icons_dict[girl]['icon'], (0,0), 'mods/customizationmod/images/' + girl + '.png')
                    focus_mask True
                    action [ShowMenu('gamemenu' + girl)]
    on "show" action Function(search_icons)
screen eventtrackersidecharahub ():
    tag menu
    $ trans = {
                'sara':'Сара', 'haruka':'Харука', 'kaori':'Каори', 'chinami':'Чинами', 'karin':'Карин', 'maki':'Маки', 'yuki':'Юки', 'niki':'Ники', 'wakana':'Вакана', 'osako':'Осако', 'tsubasa':'Цубаса', 'tsukasa':'Цукаса', 'imani':'Имани', 'rika':'Рика', 'nao':'Нао'
    }
    use game_menu(_("Дополнительные Персонажи"), scroll="viewport"):

        style_prefix "aff"

        grid 5 3:
            align (1, 1)
            xspacing 60
            yspacing 20

            for girl in ['sara', 'haruka', 'kaori', 'chinami', 'karin', 'maki', 'yuki', 'niki', 'wakana', 'osako', 'tsubasa', 'tsukasa', 'imani', 'rika', 'nao']:
                # imagebutton:
                #     idle  persistent.girl_icons_dict[girl]['icon']
                #     hover get_im_ico_p(persistent.girl_icons_dict[girl]['icon'], trans[girl][0].upper() + trans[girl][1:])
                #     focus_mask True
                #     action [ShowMenu('gamemenu' + girl)]
                imagebutton:
                    idle  persistent.girl_icons_dict[girl]['icon']
                    hover im.Composite((190,190), (0,0), persistent.girl_icons_dict[girl]['icon'], (0,0), 'mods/customizationmod/images/' + girl + '.png')
                    focus_mask True
                    action [ShowMenu('gamemenu' + girl)]
    on "show" action Function(search_icons)