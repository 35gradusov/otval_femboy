default persistent.thirty_five_grad_music = {
    # 'last_track_id': None,
    'unlocked_tracks': [],  # Список ID разблокированных треков
}

init python:
    # Отвал иди нахуй
    class MusicManager(object):
        def __init__(self, fadeout=1.0, fadein=1.0):
            self._mr = MusicRoom(fadeout=fadeout, fadein=fadein)
            # У музыкальной записи есть ключи: {"filename", "title", "artist", "unlocked", "id"}
            self.tracks = []

        def add(self, filename, title=None, artist=None, always_unlocked=False):
            # Присваиваем id каждой дорожке для ссылок в persistent.
            track_id = len(self.tracks)
            entry = {
                'id': track_id,
                'filename': filename,
                'title': title if title else filename.split('/')[-1],
                'artist': artist if artist else '',
                'unlocked': bool(always_unlocked),
            }
            self.tracks.append(entry)

            try:
                self._mr.add(filename, always_unlocked=always_unlocked)
            except Exception as e:
                renpy.log('MusicManager: failed to add %s: %s' % (filename, e))

            return entry

        def get(self, track_id):
            if track_id is None:
                return None
            if 0 <= track_id < len(self.tracks):
                return self.tracks[track_id]
            return None

        def _get_persistent(self):
            mp = getattr(persistent, 'thirty_five_grad_music', None)
            if mp is None:
                mp = {
                    # 'last_track_id': None,
                    'unlocked_tracks': [],
                }
                persistent.thirty_five_grad_music = mp
            if 'unlocked_tracks' not in mp:
                mp['unlocked_tracks'] = []
            return mp

        def play(self, track_id=None):
            if track_id is None:
                track_id = self._get_persistent().get('last_track_id')

            track = self.get(track_id)
            if not track:
                renpy.log('MusicManager: no track to play (id=%s)' % repr(track_id))
                return None

            try:
                renpy.music.play(track['filename'], channel='music', loop=False)
                mp = self._get_persistent()
                mp['last_track_id'] = track['id']
                
                # Автоматически разблокируем трек при воспроизведении
                if not track.get('unlocked'):
                    track['unlocked'] = True
                    renpy.log('MusicManager: auto-unlocked track %s' % track['title'])
                
                if track['id'] not in mp['unlocked_tracks']:
                    mp['unlocked_tracks'].append(track['id'])
                
                return None
            except Exception as e:
                renpy.log('MusicManager: failed to play %s: %s' % (track['filename'], e))
                return None

        def stop(self):
            try:
                renpy.music.stop(channel='music')
            except Exception as e:
                renpy.log('MusicManager.stop: %s' % e)

        def unlocked_tracks(self):
            return [t for t in self.tracks if t.get('unlocked')]

        def unlock(self, track_id):
            # Разблокировать трек вручную.
            #     python:
            #         thirty_five_grad_mr.unlock(5)
            t = self.get(track_id)
            if t:
                t['unlocked'] = True
                mp = self._get_persistent()
                if track_id not in mp['unlocked_tracks']:
                    mp['unlocked_tracks'].append(track_id)
        
        def load_unlocked_from_persistent(self):
            mp = self._get_persistent()
            unlocked_ids = mp.get('unlocked_tracks', [])
            for track_id in unlocked_ids:
                t = self.get(track_id)
                if t:
                    t['unlocked'] = True


    thirty_five_grad_mr = MusicManager(fadeout=1.0)

    thirty_five_grad_mr.add("music/ill_be_waiting.ogg", title="Ill Be Waiting", always_unlocked=True)
    thirty_five_grad_mr.add("music/natus_city_in_the_sky_end.ogg", title="City In The Sky", artist='Natus')
    thirty_five_grad_mr.add("music/to_a_dark_lady.ogg", title="To a Dark Lady", artist='Graham Todd')
    thirty_five_grad_mr.add("music/Ihokkaido_leaves.ogg", title="Hokkaido Leaves", artist='To Life')
    thirty_five_grad_mr.add("music/Iframe_dawn_in_the_adan.ogg", title="Iframe Dawn", artist='ichiko aoba')
    thirty_five_grad_mr.add("music/summer_day.ogg", title="Summer Day", artist='Jinsang')
    thirty_five_grad_mr.add("music/The_Italians.ogg", title="The Italians", artist='Antony Genn, Martin Slattery')
    thirty_five_grad_mr.add("music/КАМАКА-—-Nerik-Cinema.ogg", title="Nerik Cinema", artist='Kamaka')
    thirty_five_grad_mr.add("music/Flawed_Mangoes_Tunnel_Vision.ogg", title="Flawed_Mangoes")
    thirty_five_grad_mr.add("music/mikumylove.ogg", title="Miku My Love", artist="Various") 
    thirty_five_grad_mr.add("music/ЧёЗаУродыНаСцене_Свет_Домашняя_версия.ogg", title="Свет Домашняя версия", artist="ЧёЗаУродыНаСцене")
    
    # thirty_five_grad_mr.add("music/drive.ogg", title="Drive")
    # thirty_five_grad_mr.add("music/sfl1.mp3", title="SFL1")

    thirty_five_grad_mr.load_unlocked_from_persistent()

    def thirty_five_grad_unlock_music_by_file(filename):
        if not filename:
            return False
        
        normalized = filename.replace('\\', '/')
        
        for track in thirty_five_grad_mr.tracks:
            track_file = track['filename'].replace('\\', '/')
            
            if track_file == normalized:
                thirty_five_grad_mr.unlock(track['id'])
                return True
            
            if track_file.startswith('music/') and normalized.startswith('music/'):
                if track_file == normalized:
                    thirty_five_grad_mr.unlock(track['id'])
                    return True
            elif track_file.startswith('music/') and track_file[6:] == normalized:
                thirty_five_grad_mr.unlock(track['id'])
                return True
            elif normalized.startswith('music/') and normalized[6:] == track_file:
                thirty_five_grad_mr.unlock(track['id'])
                return True
        
        return False
    
    # Хуйня для отслеживания последнего проигранного трека
    _last_music_playing = None
    
    def thirty_five_grad_music_check():
        global _last_music_playing
        try:
            current = renpy.music.get_playing(channel='music')
            
            if current and current != _last_music_playing:
                _last_music_playing = current
                unlocked = thirty_five_grad_unlock_music_by_file(current)
                if unlocked:
                    # Логируем успешную разблокировку для отладки
                    renpy.log("35grad_music: Auto-unlocked track: %s" % current)
                else:
                    pass
        except Exception as e:
            renpy.log("35grad_music: Error in music_check: %s" % e)
    
    # КАЛЛбэк для автоматического вызова при каждом взаимодействии
    config.interact_callbacks.append(thirty_five_grad_music_check)

init python:
    thirty_five_grad_music_page = 0


screen thirty_five_grad_musicroom():
    default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)

    tag menu modal True
    
    frame:

        area(0.0, 0.0, 1.0, 1.0)

        background thirty_five_grad_cg_directory+"notebook_1980x1080.png"
        # Верхняя панель: навигация по страницам
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 8
            $ _music_p = (getattr(persistent, 'thirty_five_grad_music', {}) or {})
            $ _page = thirty_five_grad_music_page
            $ _per_block = 6
            $ _per_page = _per_block * 2
            $ _total = len(thirty_five_grad_mr.tracks)
            $ _max_page = max(0, (_total - 1) // _per_page)
        $ _prev_page = 0 if _page <= 0 else (_page - 1)
        $ _next_page = _max_page if (_page + 1) > _max_page else (_page + 1)

        if _page > 0:
            imagebutton:
                xcenter 0.154
                ycenter 0.923
                idle "images/gui/gallery/repl_arrow_left_idle.png"
                activate_sound thirty_five_grad_button_page_sound
                action SetVariable('thirty_five_grad_music_page', _prev_page)
            # textbutton "Назад" action SetVariable('thirty_five_grad_music_page', _prev_page) style "thirty_five_grad_mus_box_button" text_style "thirty_five_grad_mus_box_button"
        else:
            imagebutton:
                xcenter 0.154
                ycenter 0.923
                idle "images/gui/gallery/repl_arrow_left_idle.png"
                sensitive False
            # textbutton "Назад" sensitive False style "thirty_five_grad_mus_box_button" 

        $ _page_label = str(_page + 1)
        $ _max_label = str(_max_page + 1)
        text "Страница [_page_label] / [_max_label]" style 'thirty_five_grad_mus_box_button_header' xcenter 0.424 ycenter 0.923
        textbutton "Назад":
            style "thirty_five_grad_mus_box_button"
            xcenter 0.324 ycenter 0.923
            action Return()


        if _page < _max_page:
            imagebutton:
                xcenter 0.848
                ycenter 0.923
                idle "images/gui/gallery/repl_arrow_right_idle.png"
                activate_sound thirty_five_grad_button_page_sound
                action SetVariable('thirty_five_grad_music_page', _next_page)
            # textbutton "Вперёд" action SetVariable('thirty_five_grad_music_page', _next_page) style "thirty_five_grad_mus_box_button" text_style "thirty_five_grad_mus_box_button"
        else:
            imagebutton:
                xcenter 0.848
                ycenter 0.923
                idle "images/gui/gallery/repl_arrow_right_idle.png"
                sensitive False
            # textbutton "Вперёд" sensitive False style "thirty_five_grad_mus_box_button"

        # Музло: две колонки
        hbox:
            xalign 0.2
            yalign 0.18
            spacing 20

            # Левая колонка
            vbox:
                xalign 0.5
                yalign 0.5  
                spacing 2
                # text "Треки (слева)" style "thirty_five_grad_mus_box_button"
                $ _start = _page * _per_page
                $ _left_slice = thirty_five_grad_mr.tracks[_start:_start + _per_block]
                for t in _left_slice:
                    if t['unlocked']:
                        hbox:
                            spacing 0.01
                            textbutton t['title'] action Function(thirty_five_grad_mr.play, t['id']) style "thirty_five_grad_mus_box_button" text_style "thirty_five_grad_mus_box_button"
                    else:
                        text t['title'] style "thirty_five_grad_mus_box_button" 

        
        hbox:
            xalign 0.75
            yalign 0.19
            spacing 20

            # Правая колонка
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 1
                # text "Треки (справа)" style "thirty_five_grad_mus_box_button"
                $ _right_slice = thirty_five_grad_mr.tracks[_start + _per_block:_start + _per_page]
                for t in _right_slice:
                    if t['unlocked']:
                        hbox:
                            spacing 0.01
                            textbutton t['title'] action Function(thirty_five_grad_mr.play, t['id']) style "thirty_five_grad_mus_box_button" text_style "thirty_five_grad_mus_box_button"
                    else:
                        text t['title'] style "thirty_five_grad_mus_box_button" 


        hbox:
            xalign 0.8
            yalign 0.9
            spacing 20

            # Правая колонка — детали и управление
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 2
                # text "Подробности" style "thirty_five_grad_mus_box_button"

                $ _last_id = _music_p.get('last_track_id')
                if _last_id is not None and thirty_five_grad_mr.get(_last_id) is not None:
                    $ _last = thirty_five_grad_mr.get(_last_id)
                    text "Название: " + _last['title'] style "thirty_five_grad_mus_box_button_info" 
                    if _last['artist']:
                        text "Исполнитель: " + _last['artist'] style "thirty_five_grad_mus_box_button_info"
                else:
                    text "Трек не выбран" style "thirty_five_grad_mus_box_button_info"

        # # Большой заголовок сверху
        # text '{font=SonySketch.ttf}{color=#5F9EA8}{size=100}Музыкальная шкатулка{/size}{/color}{/font}' xalign 0.5 yalign 0.05

        # # Кнопка назад
        # imagebutton:
        #     at thirty_five_grad_button_gal_menu
        #     focus_mask None
        #     sensitive True
        #     idle thirty_five_grad_coming_soon_directory+"back_normal.png"
        #     hover_sound thirty_five_grad_button_hover_sound
        #     activate_sound thirty_five_grad_button_release_sound
        #     hovered [Show("thirty_five_grad_hover_back_gal")]
        #     unhovered [Hide("thirty_five_grad_hover_back_gal")]
        #     action [Hide('thirty_five_grad_hover_back_gal'), Return()]
        #     yoffset 1

        add thirty_five_grad_dust_anim


