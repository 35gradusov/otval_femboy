default persistent.thirty_five_grad_gallery = {
    'unlocked': [],  # Список id разблокированных CG
    'viewed': [],    # Список просмотренных CG
}

init python:
    # Отвал, иди нахуй
    class GalleryManager(object):
        
        def __init__(self):
            self._gallery = Gallery()
            self.items = []  # Список всех CG
            self.categories = set()
            self._gallery.locked_button = thirty_five_grad_cg_directory + "locked_preview.png"
            
        def add(self, cg_id, filename, title=None, category="Общее", 
                description="", thumbnail=None, unlock_condition=None, always_unlocked=False, add_images=None):
            
            item_index = len(self.items)
            
            if add_images is None:
                add_images = []
            
            entry = {
                'id': cg_id,
                'index': item_index,
                'filename': filename,
                'title': title if title else cg_id,
                'category': category,
                'description': description,
                'thumbnail': thumbnail if thumbnail else filename, # путь к превью
                'unlock_condition': unlock_condition,
                'always_unlocked': always_unlocked,
                'add_images': add_images,
            }
            
            self.items.append(entry)
            self.categories.add(category)
            self._gallery.button(cg_id)

            if unlock_condition and not always_unlocked:
                self._gallery.condition(unlock_condition)
            elif always_unlocked:
                self._gallery.condition("True")
            else:
                self._gallery.condition("'" + cg_id + "' in persistent.thirty_five_grad_gallery.get('unlocked', [])")
            if filename.startswith("cg "):
                self._gallery.image(filename)
            else:
                self._gallery.image(filename)
            self._gallery.unlock(cg_id)            
            return entry
            
        def get(self, cg_id):
            for item in self.items:
                if item['id'] == cg_id:
                    return item
            return None
            
        def get_by_category(self, category):
            if category == "Все":
                return self.items
            return [item for item in self.items if item['category'] == category]

        # Хуйня для проверки, разблокирован ли CG
        def is_unlocked(self, cg_id):
            item = self.get(cg_id)
            if not item:
                return False 

            if item['always_unlocked']:
                return True            
            
            if self.check_seen_cg(cg_id):
                return True                
            
            if item['unlock_condition']:
                try:
                    return eval(item['unlock_condition'])
                except:
                    return False

            p_gal = getattr(persistent, 'thirty_five_grad_gallery', {})
            
            if not p_gal:
                p_gal = {'unlocked': [], 'viewed': []}
                persistent.thirty_five_grad_gallery = p_gal
            return cg_id in p_gal.get('unlocked', [])

        # Хуйня для проверки, был ли CG просмотрен в игре
        def check_seen_cg(self, cg_id):
            item = self.get(cg_id)
            if not item:
                return False
            
            filename = item['filename']
            
            if self._check_single_image(filename):
                return True
            
            add_images = item.get('add_images', [])
            for add_img in add_images:
                if self._check_single_image(add_img):
                    return True
            
            return False

        # Также хуйня для проверки, был ли CG просмотрен в игре
        def _check_single_image(self, filename):
            if not filename:
                return False            
            if filename.startswith("cg "):
                if renpy.seen_image(filename):
                    return True
                image_name = filename[3:]  
                if renpy.seen_image(image_name):
                    return True
                if renpy.seen_image("cg" + image_name):
                    return True
            elif filename.startswith("bg "):
                if renpy.seen_image(filename):
                    return True
                image_name = filename[3:]
                if renpy.seen_image(image_name):
                    return True
                if renpy.seen_image("bg" + image_name):
                    return True
            else:
                if renpy.seen_image(filename):
                    return True            
            return False

        # Хуйня для разблокировки CG вручную 
        def unlock(self, cg_id):
            p_gal = getattr(persistent, 'thirty_five_grad_gallery', {})
            if not p_gal:
                p_gal = {'unlocked': [], 'viewed': []}
                persistent.thirty_five_grad_gallery = p_gal
                
            if cg_id not in p_gal['unlocked']:
                p_gal['unlocked'].append(cg_id)
                renpy.log("35grad_gallery: Manually unlocked CG '%s'" % cg_id)
        # Хуйня для блокировки CG вручную        
        def lock(self, cg_id):
            p_gal = getattr(persistent, 'thirty_five_grad_gallery', {})
            if not p_gal:
                return
            
            if cg_id in p_gal.get('unlocked', []):
                p_gal['unlocked'].remove(cg_id)
            
            if cg_id in p_gal.get('viewed', []):
                p_gal['viewed'].remove(cg_id)

        # Хуйня для отметки CG как просмотренного
        # Возможно стоит удалить
        def mark_viewed(self, cg_id):
            p_gal = getattr(persistent, 'thirty_five_grad_gallery', {})
            if not p_gal:
                p_gal = {'unlocked': [], 'viewed': []}
                persistent.thirty_five_grad_gallery = p_gal
                
            if cg_id not in p_gal['viewed']:
                p_gal['viewed'].append(cg_id)
                
        # Хуйня для проверки, был ли CG просмотрен в игре                
        def is_viewed(self, cg_id):
            p_gal = getattr(persistent, 'thirty_five_grad_gallery', {})
            if not p_gal:
                return False
            return cg_id in p_gal.get('viewed', [])
            
        def get_stats(self):
            total = len(self.items)
            unlocked = sum(1 for item in self.items if self.is_unlocked(item['id']))
            viewed = sum(1 for item in self.items if self.is_viewed(item['id']))
            unlocked_percent = int((unlocked * 100.0 / total)) if total > 0 else 0
            viewed_percent = int((viewed * 100.0 / total)) if total > 0 else 0
            
            return {
                'total': total,
                'unlocked': unlocked,
                'viewed': viewed,
                'unlocked_percent': unlocked_percent,
                'viewed_percent': viewed_percent
            }
            
        def show_cg(self, cg_id):
            self.mark_viewed(cg_id)
            return Show("thirty_five_grad_cg_viewer", cg_id=cg_id, transition=Dissolve(0.5))


    thirty_five_grad_gallery = GalleryManager()
        
    # Пролог
    thirty_five_grad_gallery.add('cg_transition_prolog', 'cg thirty_five_grad_transition_prolog_main', title="Пролог", category="Пролог", thumbnail=thirty_five_grad_cg_directory+'transition_prolog_main.png')
    thirty_five_grad_gallery.add('cg_bus_station', 'cg thirty_five_grad_alex_bus_station', title="Автобусная станция", category="Пролог", description="Киви+Лена", thumbnail=thirty_five_grad_cg_directory+'cg_bus_station.png', add_images=['cg thirty_five_grad_alex_bus_station blured'])
    thirty_five_grad_gallery.add('photo_1_nor.png', thirty_five_grad_cg_directory+'photo_1_nor.png', title="Старая фотография", category="Пролог", thumbnail=thirty_five_grad_cg_directory+'photo_1_nor.png')
    
    # День 1
    thirty_five_grad_gallery.add('cg_transition_day_1', 'cg thirty_five_grad_transition_day_1_main', title="День 1", category="День 1", thumbnail=thirty_five_grad_cg_directory+'transition_day_1_main.png')
    thirty_five_grad_gallery.add('cg_inter_day_1', 'cg thirty_five_grad_inter_day_1', title="Славя и Лёша", category="День 1", thumbnail=thirty_five_grad_cg_directory+'cg_day1_slavya.jpg')
    thirty_five_grad_gallery.add('cg_art2_1', 'cg thirty_five_grad_miku_art_stolov', title="Мику в столовой", category="День 1", thumbnail=thirty_five_grad_cg_directory+'cg_day1_miku.png')
    thirty_five_grad_gallery.add('cg_lesha_mirror', 'cg thirty_five_grad_nefor_mirror', title="Лёша зеркало", category="День 1", description="Лёша смотрит в зеркало", thumbnail=thirty_five_grad_cg_directory+'cg_day1_mirror.png')
    thirty_five_grad_gallery.add('cg_miku_wash', 'cg thirty_five_grad_pancu_shot', title="Мику моет пол", category="День 1", description="Мику моет пол", thumbnail=thirty_five_grad_cg_directory+'cg_day1_pshot.png')
    
    # День 2
    thirty_five_grad_gallery.add('cg_day2_miku_transition', thirty_five_grad_cg_directory+'transition_day2.png', title="Мику день 2 переход", category="День 2", description="Мику день 2 переход", thumbnail=thirty_five_grad_cg_directory+'transition_day2.png')
    thirty_five_grad_gallery.add('cg_day2_alisa', 'cg thirty_five_grad_alice_day_2', title="Алиса", category="День 2", description="Алиса день 2", thumbnail=thirty_five_grad_cg_directory+'cg_day2_alice.png')
    thirty_five_grad_gallery.add('cg_day2_miku', 'cg thirty_five_grad_day2_miku', title="Мику день 2", category="День 2", description="Мику день 2", thumbnail=thirty_five_grad_cg_directory+'cg_day2_miku.png')
    
    # День 3
    thirty_five_grad_gallery.add('cg_day3_music_miku', 'cg thirty_five_grad_day3_miku', title="День 3", category="День 3", thumbnail=thirty_five_grad_cg_directory+'cg_day3_musclub.png')
    thirty_five_grad_gallery.add('cg_day3_miku_dinner', 'cg thirty_five_grad_day3_miku_dinner', title="Мику столовая", category="День 3", thumbnail=thirty_five_grad_cg_directory+'cg_day3_dinner.png')

    def thirty_five_grad_unlock_cg(cg_id):
        # python: thirty_five_grad_unlock_cg('cg_bus_station')
        thirty_five_grad_gallery.unlock(cg_id)
        
    def thirty_five_grad_debug_gallery():
        # Выводит статус всех CG
        # python: thirty_five_grad_debug_gallery()
        renpy.log("=== 35GRAD GALLERY DEBUG ===")
        for item in thirty_five_grad_gallery.items:
            cg_id = item['id']
            filename = item['filename']
            is_unlocked = thirty_five_grad_gallery.is_unlocked(cg_id)
            
            seen_status = "SEEN" if thirty_five_grad_gallery._check_single_image(filename) else "NOT SEEN"
            
            renpy.log("CG: %s | File: %s | Unlocked: %s | Seen: %s" % (cg_id, filename, is_unlocked, seen_status))
        
        renpy.log("=========================")
        renpy.notify("Инфа об галереи выведена в лог и Отвал фембойчик.")


init python:
    thirty_five_grad_gallery_page = 0
    thirty_five_grad_gallery_filter = "Все"
    
    def thirty_five_grad_get_gallery_page_data(filter_category, page_num, items_per_page=12):
        filtered_items = thirty_five_grad_gallery.get_by_category(filter_category)
        filtered_count = len(filtered_items)
        
        total_pages = (filtered_count + items_per_page - 1) // items_per_page
        if total_pages < 1:
            total_pages = 1
        
        current_page = page_num
        if current_page > total_pages - 1:
            current_page = total_pages - 1
        if current_page < 0:
            current_page = 0
            
        start_idx = current_page * items_per_page
        
        end_idx = start_idx + items_per_page
        if end_idx > filtered_count:
            end_idx = filtered_count
            
        page_items = filtered_items[start_idx:end_idx]
        
        return {
            'filtered_items': filtered_items,
            'filtered_count': filtered_count,
            'total_pages': total_pages,
            'current_page': current_page,
            'start_idx': start_idx,
            'end_idx': end_idx,
            'page_items': page_items,
            'items_per_page': items_per_page,
        }


screen thirty_five_grad_gallery_screen():
    
    tag menu
    modal True
    
    add thirty_five_grad_cg_directory + "notebook_1980x1080.png"
    
    frame:
        area (0.05, 0.05, 0.9, 0.9)
        background Solid("#00000099")
        
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            
            # Заголовок со статистикой
            hbox:
                spacing 20
                xalign 0.5
                
                $ stats = thirty_five_grad_gallery.get_stats()
                # $ stats_unlocked = stats['unlocked']
                # $ stats_total = stats['total']
                $ stats_percent = stats['unlocked_percent']
                text "{size=48}Галерея{/size}" style "thirty_five_grad_text_normal"
                text "Разблокировано:([stats_percent]%)" style "thirty_five_grad_text_small"
            
            # Фильтр по категориям
            hbox:
                spacing 8
                xalign 0.5
                
                $ category_order = ["Пролог", "День 1", "День 2", "День 3"]
                $ ordered_cats = [c for c in category_order if c in thirty_five_grad_gallery.categories]
                $ other_cats = sorted([c for c in thirty_five_grad_gallery.categories if c not in category_order])
                $ categories = ["Все"] + ordered_cats + other_cats
                
                for cat in categories:
                    $ is_active = (thirty_five_grad_gallery_filter == cat)
                    if is_active:
                        textbutton cat:
                            style "thirty_five_grad_mus_control_button"
                            action SetVariable('thirty_five_grad_gallery_filter', cat), SetVariable('thirty_five_grad_gallery_page', 0)
                    else:
                        textbutton cat:
                            style "thirty_five_grad_mus_box_button"
                            action SetVariable('thirty_five_grad_gallery_filter', cat), SetVariable('thirty_five_grad_gallery_page', 0)
            
            # Сетка превью
            $ page_data = thirty_five_grad_get_gallery_page_data(thirty_five_grad_gallery_filter, thirty_five_grad_gallery_page)
            $ filtered_items = page_data['filtered_items']
            $ filtered_count = page_data['filtered_count']
            $ total_pages = page_data['total_pages']
            $ current_page = page_data['current_page']
            $ start_idx = page_data['start_idx']
            $ end_idx = page_data['end_idx']
            $ page_items = page_data['page_items']
            $ items_per_page = page_data['items_per_page']
            
            vpgrid:
                cols 4
                rows 3
                spacing 10
                xalign 0.5
                
                for item in page_items:
                    $ is_unlocked = thirty_five_grad_gallery.is_unlocked(item['id'])
                    $ is_viewed = thirty_five_grad_gallery.is_viewed(item['id'])
                    $ cg_action = thirty_five_grad_gallery.show_cg(item['id'])
                    
                    vbox:
                        spacing 5
                        xsize 240
                        ysize 200
                        
                        # Превью изображения
                        if is_unlocked:
                            imagebutton:
                                idle Transform(item['thumbnail'], size=(220, 140), fit="contain")
                                hover Transform(item['thumbnail'], size=(220, 140), fit="contain", alpha=0.8)
                                action cg_action
                                xalign 0.5
                                at transform:
                                    on idle:
                                        linear 0.2 zoom 1.0
                                    on hover:
                                        linear 0.2 zoom 1.05
                        else:
                            # Заблокированное превью
                            frame:
                                xsize 220
                                ysize 140
                                xalign 0.5
                                background Solid("#333333")
                                text "?" xalign 0.5 yalign 0.5 size 60 color "#666666"
                        
                        # Название
                        if is_unlocked:
                            $ name_color = "#FFFFFF" if is_viewed else "#AAAAAA"
                            text item['title']:
                                style "thirty_five_grad_text_small"
                                color name_color
                                xalign 0.5
                                size 22
                        else:
                            text "???" style "thirty_five_grad_text_small" color "#666666" xalign 0.5 size 22
            
            hbox:
                spacing 8
                xalign 0.5
                
                $ page_display = current_page + 1
                $ prev_page = current_page - 1
                $ next_page = current_page + 1
                
                if current_page > 0:
                    textbutton "◄ Назад":
                        style "thirty_five_grad_mus_control_button"
                        action SetVariable('thirty_five_grad_gallery_page', prev_page)
                else:
                    textbutton "◄ Назад":
                        style "thirty_five_grad_mus_control_button"
                        sensitive False
                
                text "Страница [page_display] / [total_pages]" style "thirty_five_grad_text_normal"
                
                if current_page < total_pages - 1:
                    textbutton "Вперёд ►":
                        style "thirty_five_grad_mus_control_button"
                        action SetVariable('thirty_five_grad_gallery_page', next_page)
                else:
                    textbutton "Вперёд ►":
                        style "thirty_five_grad_mus_control_button"
                        sensitive False
            
            textbutton "Назад":
                style "thirty_five_grad_mus_box_button"
                xalign 0.5
                action Return()


# Экран для просмотра CG на полный экран
screen thirty_five_grad_cg_viewer(cg_id):
    
    modal True
    zorder 200
    
    $ cg_item = thirty_five_grad_gallery.get(cg_id)
    
    if cg_item:
        add cg_item['filename']:
            xalign 0.5
            yalign 0.5
            at transform:
                alpha 0.0
                linear 0.3 alpha 1.0
        
        frame:
            xalign 0.5
            yalign 0.95
            xsize 800
            background Solid("#000000AA")
            padding (20, 10)
            at transform:
                alpha 0.0
                yoffset 50
                pause 0.2
                linear 0.3 alpha 1.0 yoffset 0
            
            hbox:
                spacing 20
                xalign 0.5
                
                text cg_item['title']:
                    style "thirty_five_grad_text_normal"
                    size 30
                
                if cg_item.get('description'):
                    text "—" style "thirty_five_grad_text_normal" size 30
                    text cg_item['description']:
                        style "thirty_five_grad_text_small"
                        size 24
        
        key "game_menu" action Hide("thirty_five_grad_cg_viewer", transition=Dissolve(0.3))
        key "K_ESCAPE" action Hide("thirty_five_grad_cg_viewer", transition=Dissolve(0.3))
        
        button:
            xfill True
            yfill True
            action Hide("thirty_five_grad_cg_viewer", transition=Dissolve(0.3))
            style "empty_button"
    else:
        frame:
            xalign 0.5
            yalign 0.5
            background Solid("#000000")
            padding (50, 30)
            at transform:
                alpha 0.0
                linear 0.3 alpha 1.0
            
            text "Изображение не найдено":
                style "thirty_five_grad_text_normal"
                size 40
        
        key "game_menu" action Hide("thirty_five_grad_cg_viewer", transition=Dissolve(0.3))
        key "K_ESCAPE" action Hide("thirty_five_grad_cg_viewer", transition=Dissolve(0.3))


style empty_button:
    background None
    hover_background None
    selected_background None