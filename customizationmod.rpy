#Картинка меню
init python:
    image_list = []
    default_image_list = []
    def search_menu_images():
        image_format = [".jpg", ".jpeg", ".jxl", ".png", ".webp"]
        video_format = [".mp4", ".ogv", ".webm", ".mkv", ".avi"]
        global image_list
        import os
        new_images = []
        # ВИДЕО
        mod_path = "mods/customizationmod/your_menu_video"
        system_mod_path = os.path.join(config.gamedir, mod_path)
        if not os.path.exists(system_mod_path):
            os.makedirs(system_mod_path)
        for file in os.listdir(system_mod_path):
            if os.path.splitext(file)[1].lower() in video_format:
                new_images.append((mod_path + '/' + file, 1))
        # Картинки
        mod_path = "mods/customizationmod/your_menu_image"
        system_mod_path = os.path.join(config.gamedir, mod_path)
        if not os.path.exists(system_mod_path):
            os.makedirs(system_mod_path)
        for file in os.listdir(system_mod_path):
            if os.path.splitext(file)[1].lower() in image_format:
                new_images.append((mod_path + '/' + file, 2))
        # Картинки меню
        mod_path = "mods/customizationmod/menu_image"
        system_mod_path = os.path.join(config.gamedir, mod_path)
        if not os.path.exists(system_mod_path):
            os.makedirs(system_mod_path)
        for file in os.listdir(system_mod_path):
            if os.path.splitext(file)[1].lower() in image_format:
                new_images.append((mod_path + '/' + file, 3))
        new_images.append(("gui/main_menu.png", 3))
        image_list = new_images
    search_menu_images()
    def file_check(file_path):
        import os
        if file_path is not None and os.path.exists(os.path.join(config.gamedir, file_path)) and renpy.loadable(file_path):
            return True
        return False
    def menu_image(obj):
        if obj is None:
            if file_check(persistent.main_menu_image):
                return Crop((432, 24, 1459, 803), Image(persistent.main_menu_image))
            else:
                return Crop((432, 24, 1459, 803), Image(gui.main_menu_background))
        else:
            if file_check(obj[0]):
                if obj[1] == 1:
                    return Movie(play=obj[0], channel="menu_movie", side_mask=True, size=(1459, 803))            
                if obj[1] == 2:
                    return im.Scale(obj[0], 1459, 803)
                if obj[1] == 3:
                    return Crop((432, 24, 1459, 803), Image(obj[0]))
            else :
                return Crop((432, 24, 1459, 803), Image(gui.main_menu_background))
# Темы
init python:
    def set_theme(theme):
        import zipfile
        import os
        persistent.game_theme = theme
        with zipfile.ZipFile(os.path.join(config.gamedir, "mods/customizationmod/themes/{}/{}.zip".format(theme,theme)), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(config.gamedir))
        # try:
        #     define_mods_images.update(load_theme_image_dict(theme))
        # except:
        #     pass
        renpy.reload_script()
        # gui.rebuild()
    def load_theme_image_dict(theme):
        import json
        import os
        with open(os.path.join(config.gamedir, 'mods/customizationmod/themes/{}/themes.json'.format(theme)), 'r') as file:
            return json.load(file)
#Музыка
init 1 python:
    def update_music():
        global mmr, modMusicList
        mmr = mMusicRoom(fadeout=1.0)
        modMusicList = [
            ("10c.mp3",'10c'),
            ("amiawake.mp3",'Am I Awake?'),
            ("amiamiami.mp3",'Ami’s Theme'),
            ("anewyou.mp3",'A New You'),
            ("andlove.mp3",'And Love'),
            ("anothernewsong.mp3",'Another New Song'),
            ("backwardsdancing.mp3",'Backwards Dancing'),
            ("Calmbar.mp3",'Bar Theme'),
            ("beginningoftheend.mp3",'Beginning of the End'),
            ("behindabathroom.mp3",'Behind a Bathroom, Under the Blazing Sun'),
            ("beyondthewayoftime.mp3",'Beyond the Way of Time'),
            ("BloodAndSunset.mp3",'Blood & Sunset'),
            ("BlueAir.mp3",'Blue Air'),
            ("breeze.mp3",'Breeze (D&D Theme)'),
            ("brighterdays.mp3",'Brighter Days (Otoha’s Theme)'),
            ("Cafe.mp3",'Cafe Theme'),
            ("CityLife.mp3",'City Life (Porn Shop Theme)'),
            ("closeto.mp3",'Close To Nothing'),
            ("Comfort.mp3",'Comfort'),
            ("Contemplation.mp3",'Contemplation'),
            ("darkbedroomwaltz.mp3",'Dark Bedroom Waltz'),
            ("Daybreak.mp3",'Daybreak'),
            ("amisings.mp3",'Doki Doki, Fuwa Fuwa feat. Ami Arakawa'),
            ("Encounter.mp3",'Encounter'),
            ("maidcafe.mp3",'FLAVOR BEAM!!!!! (Maid Cafe Theme)'),
            ("christmasyay.mp3",'Generic Christmas Song'),
            ("gentle.mp3",'Gentle Theme'),
            ("glasswalker.mp3",'Glasswalker'),
            ("goodmorning.mp3",'Good Morning'),
            ("goodnight.mp3",'Goodnight'),
            ("Hallelujah.mp3",'Hallelujah'),
            ("HammockOfPeace.mp3",'Hammock of Peace'),
            ("HappyandPlotting.mp3",'Happy & Plotting'),
            ("highspeedprinter.mp3",'High Speed Printer (Miku’s Theme)'),
            ("holyplace.mp3",'Holy Place'),
            ("hometown.mp3",'Hometown'),
            ("ibelieve.mp3",'I Believe'),
            ("icantseeher.mp3",'I Can’t See Her (Nodoka’s Theme)'),
            ("ihaveto.mp3",'I Have to Love You feat. Maya Makinami'),
            ("iloveyou.mp3",'I Love You'),
            ("Ichiyarakka.mp3",'Ichiyarakka'),
            ("io.mp3",'Io’s Theme'),
            ("itsingsinitssleep.mp3",'It Sings in it’s Sleep'),
            ("JustBeHappy.mp3",'Just Be Happy'),
            ("justlights.mp3",'Just Lights'),
            ("kashiwagi.mp3",'Kashiwagi (Tojo Ramen Theme)'),
            ("KimiToAkiNoBouken.mp3",'Kimi To Aki No Bouken'),
            ("lastdailysong.mp3",'Last Daily Song'),
            ("letsfuckingo.mp3",'LET’S FUCKIN’ GO!!!!!'),
            ("lifeismostlygood.mp3",'Life is Mostly Good'),
            ("littlebunny.mp3",'Little Bunny'),
            ("love.mp3",'Love Song'),
            ("utasings.mp3",'Lovely, My Prince feat. Uta Ushibori'),
            ("marshmallow.mp3",'Marshmallow'),
            ("meanttobe.mp3",'Meant to Be'),
            ("memories.mp3",'Memories'),
            ("merrychristmasmrlawrence.mp3",'Merry Christmas, Mr. Lawrence'),
            ("molly.mp3",'Molly’s Theme'),
            ("morningmoon.mp3",'Morning Moon (Library Theme)'),
            ("NewHope.mp3",'New Hope (Chapel Theme)'),
            ("Noriko.mp3",'Noriko’s Theme'),
            ("NormalDay.mp3",'Normal Day'),
            ("notabluearchivesong.mp3",'Not A Blue Archive Song'),
            ("oldweather.mp3",'Old Weather'),
            ("PhantomThief.mp3",'Phantom Thief'),
            ("pianomelancholy3.mp3",'Pianos Become the Teeth'),
            ("prairie.mp3",'Prairie'),
            ("Recognize.mp3",'Recognize'),
            ("recovery.mp3",'Recovery'),
            ("acoustic.mp3",'Relaxation'),
            ("Remember.mp3",'Remember (Niki’s Theme)'),
            ("Mall.mp3",'Retail Machine (Mall Theme)'),
            ("retrospect.mp3",'Retrospect'),
            ("Sakuya4.mp3",'Sakuya (Dojo Theme)'),
            ("samhain.mp3",'Samhain'),
            ("sensei.mp3",'Sensei'),
            ("AsobeatSex1.mp3",'Sex Theme 1'),
            ("AsobeatSex2.mp3",'Sex Theme 2'),
            ("AsobeatSex3.mp3",'Sex Theme 3'),
            ("asobeatsex4.mp3",'Sex Theme 4'),
            ("AsoBeatSex5.mp3",'Sex Theme 5'),
            ("Asobeatsex6.mp3",'Sex Theme 6'),
            ("asobeatsex7.mp3",'Sex Theme 7'),
            ("Asobeatsex8.mp3",'Sex Theme 8'),
            ("asobeatsexdark.mp3",'Sex Theme (Dark)'),
            ("ShiningStarVocals.mp3",'Shining Star feat. Niki Nakayama'),
            ("shiningstarinstrumental.mp3",'Shining Star (Instrumental)'),
            ("shrinemaiden.mp3",'Shrine Maiden'),
            ("shrinesong.mp3",'Shrinesong'),
            ("sidecharacter.mp3",'Side Character (Sara’s Theme)'),
            ("TheSleepingCity.mp3",'The Sleeping City'),
            ("sleepsong.mp3",'Sleepsong'),
            ("sleepystreets2.mp3",'Sleepy Streets'),
            ("smellsofsummer.mp3",'Smells of Summer feat. Noriko Nakayama'),
            ("yasusings.mp3",'Soba Ni Ite feat. Yasu Yasui'),
            ("soda.mp3",'Soda'),
            ("starvingtodeathoutofreachofthesun.mp3",'Starving to Death, Out of Reach of the Sun'),
            ("stpartynight.mp3",'St. Party Night'),
            ("stopwind.mp3",'Stopwind (Yasu’s Theme)'),
            ("strawberry.mp3",'Strawberry Lover'),
            ("summerwind.mp3",'Summer Wind'),
            ("SweetVermouth.mp3",'Sweet Vermouth (Dorm Theme)'),
            ("thingsthathurt.mp3",'Things That Hurt'),
            ("TokimekiLabyrinth.mp3",'Tokimeki Labyrinth feat. Niki Nakayama'),
            ("tsukiokamanor.mp3",'Tsukioka Manor'),
            ("rapid.mp3",'ULTRA MEGA BATTLE THEME'),
            ("undersea.mp3",'Undersea'),
            ("unmatchingeyes.mp3",'Unmatching Eyes'),
            ("WeWereAngels.mp3",'We Were Angels'),
            ("yumiska.mp3",'Yumi Ska (Yumi’s Theme)'),
        ]
        for m in modMusicList:
            mmr.add(m[0], always_unlocked=True)
        search_music()
    def search_music():
        global mmr
        import os
        my_music = []
        m_directory = 'mods/customizationmod/music'
        m_s_directory = os.path.join(config.gamedir, m_directory)
        if not os.path.exists(m_s_directory):
            os.makedirs(m_s_directory)
        music_format = ['.ogg', '.mp3', '.opus', '.wav']
        for file in os.listdir(m_s_directory):
            if os.path.splitext(file)[1].lower() in music_format:
                my_music.append((u'mods/customizationmod/music/' + file, os.path.splitext(file)[0]))
        for m in my_music:
            mmr.add(m[0], always_unlocked=True)
        persistent.my_music = my_music
    update_music()
    def music_text():
        if renpy.music.get_playing():
            for music in modMusicList + persistent.my_music:
                if renpy.music.get_playing() == music[0]:
                    return music[1]
            return '{s} Ч т о - т о  н е  т а к{/s}'
        else:
            return '{s}Н и ч е г о  н е т{/s}'
    def music_check(m):
        if file_check(m):
            mmr.play(m)
        else:
            renpy.restart_interaction()
    @renpy.pure
    class UpdateMusic(Action):
        def __call__(self):
            # mmr.Play(modMusicList[0][0])()
            update_music()
            renpy.restart_interaction()
    class MusicCheck(Action):
        def __init__(self, m):
            self.m = m
            self.selected = self.get_selected()
        def __call__(self):
            if file_check(self.m):
                mmr.play(self.m)
            renpy.restart_interaction()
        def get_sensitive(self):
            return mmr.is_unlocked(self.m)

        def get_selected(self):
            return renpy.music.get_playing(mmr.channel) == self.m

        def periodic(self, st):
            if self.selected != self.get_selected():
                self.selected = self.get_selected()
                renpy.restart_interaction()

            mmr.periodic(st)

            return .1
init -1 python:
    class mMusicRoom(MusicRoom):
        def play(self, filename=None, offset=0, queue=False):
            """
            Starts the music room playing. The file we start playing with is
            selected in two steps.

            If `filename` is an unlocked file, we start by playing it.
            Otherwise, we start by playing the currently playing file, and if
            that doesn't exist or isn't unlocked, we start with the first file.

            We then apply `offset`. If `offset` is positive, we advance that many
            files, otherwise we go back that many files.

            If `queue` is true, the music is queued. Otherwise, it is played
            immediately.
            """

            playlist = self.unlocked_playlist(filename)

            if not playlist:
                return

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)

            checked_playlist = []
            for m in playlist:
                if file_check(m):
                    checked_playlist.append(m)
            playlist = checked_playlist
            try:
                idx = playlist.index(filename)
            except ValueError:
                idx = 0

            idx = (idx + offset) % len(playlist)

            if self.single_track:
                playlist = [ playlist[idx] ]
            elif self.loop:
                playlist = playlist[idx:] + playlist[:idx]
            else:
                playlist = playlist[idx:]

            if queue:
                renpy.music.queue(playlist, channel=self.channel, loop=self.loop)
            else:
                renpy.music.play(playlist, channel=self.channel, fadeout=self.fadeout, fadein=self.fadein, loop=self.loop)
#Иконки
init 1 python:
    def swap_icon(girl):
        search_icons()
        for idx, ico in enumerate(persistent.girl_icons_dict[girl]['list_icons']):
            if ico == persistent.girl_icons_dict[girl]['icon']:
                persistent.girl_icons_dict[girl]['icon'] = persistent.girl_icons_dict[girl]['list_icons'][(idx + 1) % len(persistent.girl_icons_dict[girl]['list_icons'])]
                return
            persistent.girl_icons_dict[girl]['icon'] = persistent.girl_icons_dict[girl]['list_icons'][0]
    def search_icons():
        import os
        image_format = [".jpg", ".jpeg", ".jxl", ".png", ".webp"]
        directory = 'mods/customizationmod/your_icon'
        s_directory = os.path.join(config.gamedir, directory)
        girls = ['chika', 'yumi', 'ayane', 'sana', 'makoto', 'miku', 'futaba', 'rin', 'ami', 'maya', 'molly', 'tsuneyo', 'uta', 'io', 'nodoka', 'otoha', 'touka', 'yasu', 'noriko', 'kirin', 'sara', 'haruka', 'kaori', 'chinami', 'karin', 'maki', 'yuki', 'niki', 'wakana', 'osako', 'tsubasa', 'tsukasa', 'imani', 'rika', 'nao']
        for girl in girls:
            girl_path = s_directory + '/' + girl
            if not os.path.exists(girl_path):
                os.makedirs(girl_path)
            g = persistent.girl_icons_dict.setdefault(girl, {})
            if not file_check(g.setdefault('icon', girl + 'thumb1.png')):
                g['icon'] = girl + 'thumb1.png'
            g = g.setdefault('list_icons', [])
            g.clear()
            g.append(girl + 'thumb1.png')
            for file in os.listdir(girl_path):
                if os.path.splitext(file)[1].lower() in image_format:
                    g.append(directory + '/' + girl + '/' + file)
    # def get_im_ico_p(background, text):
    #     text = Text(text, size=50, antialias=True, color='#ffffff', font='Hellowins.ttf', outlines=[ (absolute(2), "#000", absolute(0), absolute(0)) ])
    #     x, y = text.size()
    #     x = 95 - round(x/2)
    #     y = 95 - round(y/2)
    #     return im.Composite((190,190), (0,0), background, (x,y), text)
    # def get_im_ico_p(background, girl):
        # text = Text(text, size=50, antialias=True, color='#ffffff', font='Hellowins.ttf', outlines=[ (absolute(2), "#000", absolute(0), absolute(0)) ])
        # x, y = text.size()
        # x = 95 - round(x/2)
        # y = 95 - round(y/2)
        # return im.Composite((190,190), (0,0), background, (x,y), text)
    search_icons()