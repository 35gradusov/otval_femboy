init 1:

    image menu_bg_video = Movie(play="video/menu_animation.webm")

    screen thirty_five_grad_main_menu:
        tag menu modal True

        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)

        #я ужал пнг кнопок до 997х561

        # Видео фон на заднем плане
        add "menu_bg_video":
            xysize (1920, 1080)
            xpos 0 ypos 0
            xanchor 0 yanchor 0

        frame:
            background None
            xfill True
            yfill True

            text ['{font=SonySketch.ttf}{color=#494949}{size=110}{alpha=195}re:35°{/alpha}{/size}{/color}{/font}'] outlines [(1,"#000000",2,2)] at thirty_five_grad_name_0

            area(0.0, 0.0, 1.0, 1.0)

            imagebutton:        #играть
                at thirty_five_grad_button_1_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"start_game_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_start_game_mm")]
                unhovered [Hide("thirty_five_grad_hover_start_game_mm")]
                action [Hide("thirty_five_grad_hover_start_game_mm"), Start('thirty_five_grad_start')]

            imagebutton:        #загрузить
                at thirty_five_grad_button_2_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"load_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_load_mm")]
                unhovered [Hide("thirty_five_grad_hover_load_mm")]
                action [Hide("thirty_five_grad_hover_load_mm"), ShowMenu('load')]

            imagebutton:        #муз-шкатулка
                at thirty_five_grad_button_3_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"mus_box_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_mus_box_mm")]
                unhovered [Hide("thirty_five_grad_hover_mus_box_mm")]
                action [Hide("thirty_five_grad_hover_mus_box_mm"), ShowMenu('thirty_five_grad_musicroom')]

            imagebutton:        #альбом
                at thirty_five_grad_button_4_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"gallery_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_gallery_mm")]
                unhovered [Hide("thirty_five_grad_hover_gallery_mm")]
                action [Hide("thirty_five_grad_hover_gallery_mm"), ShowMenu('thirty_five_grad_gallery_screen')]




            imagebutton:        #бусти
                at thirty_five_grad_button_boosty_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"boosty_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_boosty_mm")]
                unhovered [Hide("thirty_five_grad_hover_boosty_mm")]
                action [Hide("thirty_five_grad_hover_boosty_mm"), OpenURL('https://boosty.to/35andnotonlythat')]

            imagebutton:        #телега
                at thirty_five_grad_button_telegram_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"tg_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_telegram_mm")]
                unhovered [Hide("thirty_five_grad_hover_telegram_mm")]
                action [Hide("thirty_five_grad_hover_telegram_mm"), OpenURL('https://t.me/YinYanTeam')]

            imagebutton:        #вк
                at thirty_five_grad_button_vk_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"vk_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_vk_mm")]
                unhovered [Hide("thirty_five_grad_hover_vk_mm")]
                action [Hide("thirty_five_grad_hover_vk_mm"), OpenURL('https://vk.com/yinyangteam')]

            imagebutton:        #стим
                at thirty_five_grad_button_steam_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"steam_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_steam_mm")]
                unhovered [Hide("thirty_five_grad_hover_steam_mm")]
                action [Hide("thirty_five_grad_hover_steam_mm"), OpenURL('https://steamcommunity.com/sharedfiles/filedetails/?id=3567909002&searchtext=')]


            imagebutton:        #выход
                at thirty_five_grad_button_5_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"exit_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_exit_mm")]
                unhovered [Hide("thirty_five_grad_hover_exit_mm")]
                action [Hide("thirty_five_grad_hover_exit_mm"), ShowMenu('quit')]
                yoffset -2

        add thirty_five_grad_dust_anim



    screen thirty_five_grad_coming_soon_mus_box:
        tag menu modal True

        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)

        frame:

            area(0.0, 0.0, 1.0, 1.0)

            background thirty_five_grad_main_menu_directory+"background.png"
            
            add thirty_five_grad_coming_soon_directory+"coming_soon.png" at thirty_five_grad_button_3_menu

            imagebutton:        #назад
                at thirty_five_grad_button_4_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_coming_soon_directory+"back_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_back")]
                unhovered [Hide("thirty_five_grad_hover_back")]
                action [Hide('thirty_five_grad_hover_back'), Return()]
                yoffset 1

        add thirty_five_grad_dust_anim


    
    screen thirty_five_grad_coming_soon_gallery:
        tag menu modal True
        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)

        frame:

            area(0.0, 0.0, 1.0, 1.0)

            background thirty_five_grad_main_menu_directory+"background.png"
            
            add thirty_five_grad_coming_soon_directory+"coming_soon.png" at thirty_five_grad_button_3_menu

            imagebutton:        #назад
                at thirty_five_grad_button_4_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_coming_soon_directory+"back_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_back")]
                unhovered [Hide("thirty_five_grad_hover_back")]
                action [Hide('thirty_five_grad_hover_back'), Return()]
                yoffset 1



    screen thirty_five_grad_adv:

        window id "window":       

            if persistent.font_size == "small":

                background thirty_five_grad_textbox_directory+'background.png'

                text what id "what" xpos 156 ypos 900 xmaximum 1536 size 28 line_spacing 1 color "#ffffff" font "Storopia.ttf" 
                if who:
                    text who id "who" xpos 157 ypos 869 size 32 line_spacing 1 color "#ffffff" font "SonySketch.ttf" 
                
                imagebutton:            # реверс
                    xpos 55
                    ypos 927
                    idle thirty_five_grad_textbox_directory+"reverse_button_idle.png"
                    hovered [Show('thirty_five_grad_reverse_textbox_hover_small')]
                    unhovered [Hide('thirty_five_grad_reverse_textbox_hover_small')]
                    action [Hide('thirty_five_grad_reverse_textbox_hover_small'), ShowMenu("text_history")]

                if persistent.thirty_five_grad_save_hint != True:

                    imagebutton:        # сохранить
                        focus_mask None
                        xpos 158
                        ypos 1022
                        idle thirty_five_grad_textbox_directory+"save_small_normal.png"
                        hovered [Show('thirty_five_grad_save_textbox_hover_small'), Show('thirty_five_grad_save_fuckingstick_textbox_hover_small')]
                        unhovered [Hide('thirty_five_grad_save_textbox_hover_small'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_small')]
                        action [Hide('thirty_five_grad_save_textbox_hover_small'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_small'), ShowMenu("thirty_five_grad_save_hint_sc")]

                if persistent.thirty_five_grad_save_hint:

                    imagebutton:        # сохранить
                        focus_mask None
                        xpos 158
                        ypos 1022
                        idle thirty_five_grad_textbox_directory+"save_small_normal.png"
                        hovered [Show('thirty_five_grad_save_textbox_hover_small'), Show('thirty_five_grad_save_fuckingstick_textbox_hover_small')]
                        unhovered [Hide('thirty_five_grad_save_textbox_hover_small'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_small')]
                        action [Hide('thirty_five_grad_save_textbox_hover_small'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_small'), ShowMenu("save")]

                imagebutton:            # загрузить
                    xpos 535
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"load_small_normal.png" 
                    hovered [Show('thirty_five_grad_load_textbox_hover_small'), Show('thirty_five_grad_load_fuckingstick_textbox_hover_small')]
                    unhovered [Hide('thirty_five_grad_load_textbox_hover_small'), Hide('thirty_five_grad_load_fuckingstick_textbox_hover_small')]
                    action [Hide('thirty_five_grad_load_textbox_hover_small'), Hide('thirty_five_grad_load_fuckingstick_textbox_hover_small'), ShowMenu("load")]

                if persistent.thirty_five_grad_hide_hint != True:
                    
                    imagebutton:        # спрятать
                        xpos 910
                        ypos 1022 
                        idle thirty_five_grad_textbox_directory+"hide_small_normal.png" 
                        hovered [Show('thirty_five_grad_hide_textbox_hover_small'), Show('thirty_five_grad_hide_fuckingstick_textbox_hover_small')]
                        unhovered [Hide('thirty_five_grad_hide_textbox_hover_small'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_small')]
                        action [Hide('thirty_five_grad_adv'), Hide('thirty_five_grad_hide_textbox_hover_small'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_small'), ShowMenu('thirty_five_grad_screen_skip_hint')]
                    
                elif persistent.thirty_five_grad_hide_hint:
                    
                    imagebutton:        # спрятать
                        xpos 910
                        ypos 1022 
                        idle thirty_five_grad_textbox_directory+"hide_small_normal.png" 
                        hovered [Show('thirty_five_grad_hide_textbox_hover_small'), Show('thirty_five_grad_hide_fuckingstick_textbox_hover_small')]
                        unhovered [Hide('thirty_five_grad_hide_textbox_hover_small'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_small')]
                        action [Hide('thirty_five_grad_hide_textbox_hover_small'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_small'), Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')]

                imagebutton:            # настройки
                    xpos 1285
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"settings_small_normal.png" 
                    hovered [Show('thirty_five_grad_preferences_hover_small'), Show('thirty_five_grad_preferences_fuckingstick_textbox_hover_small')]
                    unhovered [Hide('thirty_five_grad_preferences_hover_small'), Hide('thirty_five_grad_preferences_fuckingstick_textbox_hover_small')]
                    action [Hide('thirty_five_grad_preferences_hover_small'), Hide('thirty_five_grad_preferences_fuckingstick_textbox_hover_small'), ShowMenu("preferences")]

                imagebutton:            # менюха
                    xpos 1660 
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"menu_small_normal.png" 
                    hovered [Show('thirty_five_grad_qm_hover_small'), Show('thirty_five_grad_qm_fuckingstick_textbox_hover_small')]
                    unhovered [Hide('thirty_five_grad_qm_hover_small'), Hide('thirty_five_grad_qm_fuckingstick_textbox_hover_small')]
                    action [Hide('thirty_five_grad_qm_hover_small'), Hide('thirty_five_grad_qm_fuckingstick_textbox_hover_small'), ShowMenu("game_menu_selector")]                

                if not config.skipping:
                    
                    key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button'), thirty_five_grad_stop_skip()]

                    imagebutton:        # скип
                        xpos 1821
                        ypos 927
                        idle thirty_five_grad_textbox_directory+"skip_button_idle.png" 
                        hovered [Show('thirty_five_grad_skip_textbox_hover_small')]
                        unhovered [Hide('thirty_five_grad_skip_textbox_hover_small')]
                        action Skip()

                else:

                    key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')] 

                    imagebutton:        # скип
                        xpos 1821 
                        ypos 927
                        idle thirty_five_grad_textbox_directory+"skip_button_idle.png"
                        action Skip()


            elif persistent.font_size == "large":

                background thirty_five_grad_textbox_directory+'large/background.png'

                text what id "what" xpos 156 ypos 873 xmaximum 1536 size 35 line_spacing 1 color "#ffffff" font "Storopia.ttf"
                if who:
                    text who id "who" xpos 157 ypos 837 size 39 line_spacing 1 color "#ffffff" font "SonySketch.ttf"

                imagebutton:            # реверс
                    xpos 55
                    ypos 919
                    idle thirty_five_grad_textbox_directory+"reverse_button_idle.png"
                    hovered [Show('thirty_five_grad_reverse_textbox_hover_large')]
                    unhovered [Hide('thirty_five_grad_reverse_textbox_hover_large')]
                    action [Hide('thirty_five_grad_reverse_textbox_hover_large'), ShowMenu("text_history")]

                if persistent.thirty_five_grad_save_hint != True:

                    imagebutton:        # сохранить
                        focus_mask None
                        xpos 158
                        ypos 1022
                        idle thirty_five_grad_textbox_directory+"large/save_normal.png"
                        hovered [Show('thirty_five_grad_save_textbox_hover_large'), Show('thirty_five_grad_save_fuckingstick_textbox_hover_large')]
                        unhovered [Hide('thirty_five_grad_save_textbox_hover_large'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_large')]
                        action [Hide('thirty_five_grad_save_textbox_hover_large'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_large'), ShowMenu("thirty_five_grad_save_hint_sc")]

                if persistent.thirty_five_grad_save_hint:

                    imagebutton:        # сохранить
                        focus_mask None
                        xpos 158
                        ypos 1022
                        idle thirty_five_grad_textbox_directory+"large/save_normal.png"
                        hovered [Show('thirty_five_grad_save_textbox_hover_large'), Show('thirty_five_grad_save_fuckingstick_textbox_hover_large')]
                        unhovered [Hide('thirty_five_grad_save_textbox_hover_large'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_large')]
                        action [Hide('thirty_five_grad_save_textbox_hover_large'), Hide('thirty_five_grad_save_fuckingstick_textbox_hover_large'), ShowMenu("save")]

                imagebutton:            # загрузить
                    xpos 535
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"large/load_normal.png"
                    hovered [Show('thirty_five_grad_load_textbox_hover_large'), Show('thirty_five_grad_load_fuckingstick_textbox_hover_large')]
                    unhovered [Hide('thirty_five_grad_load_textbox_hover_large'), Hide('thirty_five_grad_load_fuckingstick_textbox_hover_large')]
                    action [Hide('thirty_five_grad_load_textbox_hover_large'), Hide('thirty_five_grad_load_fuckingstick_textbox_hover_large'), ShowMenu("load")]

                if persistent.thirty_five_grad_hide_hint != True:
                    
                    imagebutton:        # спрятать
                        xpos 910
                        ypos 1022 
                        idle thirty_five_grad_textbox_directory+"large/hide_normal.png" 
                        hovered [Show('thirty_five_grad_hide_textbox_hover_large'), Show('thirty_five_grad_hide_fuckingstick_textbox_hover_large')]
                        unhovered [Hide('thirty_five_grad_hide_textbox_hover_large'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_large')]
                        action [Hide('thirty_five_grad_adv'), Hide('thirty_five_grad_hide_textbox_hover_large'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_large'), ShowMenu('thirty_five_grad_screen_skip_hint')]
                    
                elif persistent.thirty_five_grad_hide_hint:
                    
                    imagebutton:        # спрятать
                        xpos 910
                        ypos 1022 
                        idle thirty_five_grad_textbox_directory+"large/hide_normal.png" 
                        hovered [Show('thirty_five_grad_hide_textbox_hover_large'), Show('thirty_five_grad_hide_fuckingstick_textbox_hover_large')]
                        unhovered [Hide('thirty_five_grad_hide_textbox_hover_large'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_large')]
                        action [Hide('thirty_five_grad_hide_textbox_hover_large'), Hide('thirty_five_grad_hide_fuckingstick_textbox_hover_large'), Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')]

                imagebutton:            # настройки
                    xpos 1285
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"large/preferences_normal.png" 
                    hovered [Show('thirty_five_grad_preferences_hover_large'), Show('thirty_five_grad_preferences_fuckingstick_textbox_hover_large')]
                    unhovered [Hide('thirty_five_grad_preferences_hover_large'), Hide('thirty_five_grad_preferences_fuckingstick_textbox_hover_large')]
                    action [Hide('thirty_five_grad_preferences_hover_large'), Hide('thirty_five_grad_preferences_fuckingstick_textbox_hover_large'), ShowMenu("preferences")]

                imagebutton:            # менюха
                    xpos 1660 
                    ypos 1022 
                    idle thirty_five_grad_textbox_directory+"large/menu_normal.png" 
                    hovered [Show('thirty_five_grad_qm_hover_large'), Show('thirty_five_grad_qm_fuckingstick_textbox_hover_large')]
                    unhovered [Hide('thirty_five_grad_qm_hover_large'), Hide('thirty_five_grad_qm_fuckingstick_textbox_hover_large')]
                    action [Hide('thirty_five_grad_qm_hover_large'), Hide('thirty_five_grad_qm_fuckingstick_textbox_hover_large'), ShowMenu("game_menu_selector")]
                    
                if not config.skipping:

                    key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button'), thirty_five_grad_stop_skip()]

                    imagebutton:        # скип
                        xpos 1821
                        ypos 919
                        idle thirty_five_grad_textbox_directory+"skip_button_idle.png" 
                        hovered [Show('thirty_five_grad_skip_textbox_hover_large')]
                        unhovered [Hide('thirty_five_grad_skip_textbox_hover_large')]
                        action Skip()

                else:

                    key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')] 

                    imagebutton:        # скип
                        xpos 1821 
                        ypos 919
                        idle thirty_five_grad_textbox_directory+"skip_button_idle.png"
                        action Skip()



    screen thirty_five_grad_nvl(dialogue, items=None):

        key "hide_windows" action [Hide('thirty_five_grad_nvl')] 
        
        if persistent.font_size == "large":

            window background Frame(thirty_five_grad_textbox_directory+"nvl.png",50,50) at thirty_five_grad_bg_zoom_nvl_text_history
            imagebutton:        # реверс
                xpos 55
                ypos 919
                idle thirty_five_grad_textbox_directory+"reverse_button_idle.png"
                hovered [Show('thirty_five_grad_reverse_textbox_hover_large')]
                unhovered [Hide('thirty_five_grad_reverse_textbox_hover_large')]
                action [Hide('thirty_five_grad_reverse_textbox_hover_large'), ShowMenu("text_history")]
                xoffset 6 yoffset 6

            if not config.skipping:

                key "hide_windows" action [thirty_five_grad_stop_skip(), Hide('thirty_five_grad_nvl')]

                imagebutton:    # скип
                    xpos 1821
                    ypos 919
                    idle thirty_five_grad_textbox_directory+"skip_button_idle.png" 
                    hovered [Show('thirty_five_grad_skip_textbox_hover_large')]
                    unhovered [Hide('thirty_five_grad_skip_textbox_hover_large')]
                    action Skip()
                    xoffset 6 yoffset 6

            else:

                key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')] 

                imagebutton:    # скип
                    xpos 1821 
                    ypos 919
                    idle thirty_five_grad_textbox_directory+"skip_button_idle.png"
                    action Skip()
                    xoffset 6 yoffset 6

            vbox:
                for d in dialogue:
                    window:
                        id d.window_id
                        has hbox:
                            spacing 10

                        if d.who is not None:
                            text d.who id d.who_id xpos 220 ypos 128 xmaximum 1500 color "#FFFFFF" size 35 font "SonySketch.ttf" 
                        text d.what id d.what_id xpos 220 ypos 124 xmaximum 1500 color "#FFFFFF" size 35 font "Storopia.ttf"
        

            

    
        elif persistent.font_size == "small":
            window background Frame(thirty_five_grad_textbox_directory+"nvl.png",50,50) at thirty_five_grad_bg_zoom_nvl_text_history
            imagebutton:        # реверс
                xpos 55
                ypos 927
                idle thirty_five_grad_textbox_directory+"reverse_button_idle.png"
                hovered [Show('thirty_five_grad_reverse_textbox_hover_small')]
                unhovered [Hide('thirty_five_grad_reverse_textbox_hover_small')]
                action [Hide('thirty_five_grad_reverse_textbox_hover_small'), ShowMenu("text_history")]
                xoffset 6 yoffset 6

            if not config.skipping:

                key "hide_windows" action [thirty_five_grad_stop_skip(), Hide('thirty_five_grad_nvl')]

                imagebutton:    # скип
                    xpos 1821
                    ypos 927
                    idle thirty_five_grad_textbox_directory+"skip_button_idle.png" 
                    hovered [Show('thirty_five_grad_skip_textbox_hover_small')]
                    unhovered [Hide('thirty_five_grad_skip_textbox_hover_small')]
                    action Skip()
                    xoffset 6 yoffset 6

            else:

                key "hide_windows" action [Hide('thirty_five_grad_adv'), ShowMenu('thirty_five_grad_show_adv_button')] 

                imagebutton:    # скип
                    xpos 1821 
                    ypos 927
                    idle thirty_five_grad_textbox_directory+"skip_button_idle.png"
                    action Skip()
                    xoffset 6 yoffset 6

            vbox:
                for d in dialogue:
                    window:
                        id d.window_id
                        has hbox:
                            spacing 10
                        if d.who is not None:
                            text d.who id d.who_id xpos 220 ypos 128 xmaximum 1400 color "#FFFFFF" size 28 font "SonySketch.ttf"
                        text d.what id d.what_id xpos 220 ypos 124 xmaximum 1500 color "#FFFFFF" size 28 font "Storopia.ttf"



    screen thirty_five_grad_screen_skip_hint:
        tag menu modal True
        
        frame background im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0)
        text 'Чтобы отобразить интерфейс, нажмите на ПКМ или кнопку в левом нижнем углу.' xalign 0.5 yalign 0.47 style 'thirty_five_grad_text_storopia' at screen_thirty_five_grad_hint_anim
        text 'Она будет невидимой.' xalign 0.5 yalign 0.51 style 'thirty_five_grad_text_storopia' at screen_thirty_five_grad_hint_anim

                
        add thirty_five_grad_textbox_directory+'hidden_hovered.png' at screen_thirty_five_grad_hide_hint_button_anim

        imagebutton:
            xalign 0.5
            yalign 0.6 
            idle thirty_five_grad_textbox_directory+"clearly_hide_tip_idle.png"
            hovered [Show('thirty_five_grad_clearly_hover'), Show('thirty_five_grad_clearly_fuckingstick_hover')]
            unhovered [Hide('thirty_five_grad_clearly_hover'), Hide('thirty_five_grad_clearly_fuckingstick_hover')]
            action [Hide('thirty_five_grad_clearly_hover'), Hide('thirty_five_grad_clearly_fuckingstick_hover'), Hide('thirty_five_grad_screen_skip_hint', transition=Dissolve(0.15)), Show('thirty_five_grad_show_adv_button', transition=Dissolve(0.15)), thirty_five_grad_hide_hint_appeared]



    screen thirty_five_grad_show_adv_button:
        key "hide_windows" action [Return(value=None)]
        imagebutton:
            idle thirty_five_grad_textbox_directory+'hidden_idle.png'
            xalign 0.017 yalign 0.97
            hovered [Show('thirty_five_grad_showtextbox_hover_small')]
            unhovered [Hide('thirty_five_grad_showtextbox_hover_small')]
            action [Hide('thirty_five_grad_show_adv_button'), Hide('thirty_five_grad_showtextbox_hover_small'), Return()]



    screen thirty_five_grad_text_history:
        
        tag menu
        predict False
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
        window background Frame("images/gui/textbox/nvl.png",50,50) top_padding 33 bottom_padding 40 at thirty_five_grad_bg_zoom_nvl_text_history:

            viewport id "thirty_five_grad_text_history":
                
                draggable True
                mousewheel True
                scrollbars None
                yinitial 1.0
                has vbox

                for history in _history_list:
                    if history.who:
                        text history.who:
                            font thirty_five_grad_sonysketch
                            pos (50, 0)
                            size (37 if persistent.font_size == "large" else 30)
                            if "color" in history.who_args:
                                color history.who_args["color"]

                    textbutton history.what:
                        style 'thirty_five_grad_text_storopia_th'
                        text_font thirty_five_grad_storopia
                        text_style "thirty_five_grad_text_storopia_th"
                        text_size (35 if persistent.font_size == "large" else 28)
                        xmaximum 1550
                        xpos 50
                        text_hover_color "#808080" 
                        action RollbackToIdentifier(history.rollback_identifier)



    screen thirty_five_grad_save_hint_sc:
        tag menu modal True
        frame background im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0) 
        text 'Сохранения можно загрузить только из главного и быстрого меню мода.' xalign 0.5 yalign 0.47 style 'thirty_five_grad_text_storopia' at screen_thirty_five_grad_hint_anim
        text 'Не волнуйтесь, если они не отображаются в загрузках основной игры и других модификациях.' xalign 0.5 yalign 0.51 style 'thirty_five_grad_text_storopia' at screen_thirty_five_grad_hint_anim

        imagebutton:
            xalign 0.5
            yalign 0.6
            idle thirty_five_grad_textbox_directory+"clearly_hide_tip_idle.png"
            hovered [Show('thirty_five_grad_clearly_hover'), Show('thirty_five_grad_clearly_fuckingstick_hover')]
            unhovered [Hide('thirty_five_grad_clearly_hover'), Hide('thirty_five_grad_clearly_fuckingstick_hover')]
            action [Hide('thirty_five_grad_clearly_hover'), Hide('thirty_five_grad_clearly_fuckingstick_hover'), thirty_five_grad_save_hint_appeared, ShowMenu('save')]



    screen thirty_five_grad_quick_menu:
        tag menu modal True

        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)

        key "game_menu" action [Hide('game_menu_selector', transition=Dissolve(0.5)), Return()]

        
     
        frame:
            area(0.0, 0.0, 1.0, 1.0)

            background thirty_five_grad_qm_directory+"background_blur.png"

            text ['{font=SonySketch.ttf}{color=#494949}{size=110}{alpha=195}re:35°{/alpha}{/size}{/color}{/font}'] outlines [(1,"#000000",2,2)] at thirty_five_grad_name_0

            add thirty_five_grad_qm_directory+"clock_bg.png" at thirty_five_grad_time_bg

            add ["thirty_five_grad_time"] at thirty_five_grad_time_1
            add ['thirty_five_grad_date'] at thirty_five_grad_time_2
            add ['thirty_five_grad_day'] at thirty_five_grad_time_3

            if persistent.thirty_five_grad_save_hint != True:

                imagebutton:        # сохранить
                    at thirty_five_grad_button_0_menu
                    focus_mask None
                    sensitive True
                    idle thirty_five_grad_qm_directory+"save_normal.png"
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    hovered [Show("thirty_five_grad_quick_menu_save")]
                    unhovered [Hide("thirty_five_grad_quick_menu_save")]
                    action [Hide("thirty_five_grad_quick_menu_save"), ShowMenu('thirty_five_grad_save_hint_sc')]

            if persistent.thirty_five_grad_save_hint:

                imagebutton:        # сохранить
                    at thirty_five_grad_button_0_menu
                    focus_mask None
                    sensitive True
                    idle thirty_five_grad_qm_directory+"save_normal.png"
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    hovered [Show("thirty_five_grad_quick_menu_save")]
                    unhovered [Hide("thirty_five_grad_quick_menu_save")]
                    action [Hide("thirty_five_grad_quick_menu_save"), ShowMenu('save')]
            

            imagebutton:        # загрузить
                at thirty_five_grad_button_1_menu
                yoffset 2
                focus_mask None
                sensitive True
                idle thirty_five_grad_qm_directory+"load_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_quick_menu_load")]
                unhovered [Hide("thirty_five_grad_quick_menu_load")]
                action [Hide("thirty_five_grad_quick_menu_load"), ShowMenu('load')]

            imagebutton:        # параметры
                at thirty_five_grad_button_2_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_qm_directory+"settings_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_quick_menu_pref")]
                unhovered [Hide("thirty_five_grad_quick_menu_pref")]
                action [Hide("thirty_five_grad_quick_menu_pref"), ShowMenu('preferences')]

            imagebutton:        #выход
                at thirty_five_grad_button_3_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_main_menu_directory+"exit_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_exit_qm")]
                unhovered [Hide("thirty_five_grad_hover_exit_qm")]
                action [Hide("thirty_five_grad_hover_exit_qm"), ShowMenu('quit')]


            imagebutton:        #назад
                at thirty_five_grad_button_5_menu
                focus_mask None
                sensitive True
                idle thirty_five_grad_coming_soon_directory+"back_normal.png"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                hovered [Show("thirty_five_grad_hover_back_qm")]
                unhovered [Hide("thirty_five_grad_hover_back_qm")]
                action [Hide('game_menu_selector', transition=Dissolve(0.3)), Return()]
                yoffset -1

        
        add thirty_five_grad_dust_anim


        
    screen thirty_five_grad_load:
        tag menu modal True
        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)
        frame background im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0) 
        key "game_menu" action (Hide('load', transition=Dissolve(0.3)), Return(value=None)) 
        vbox spacing 20 align(0.8,0.92):
            text FileTime(selected_slot,format='{font=SonySketch.ttf}{size=42}{color=#808080}%d.%m.%y, %H:%M{/size}{/color}{/font}',empty=""):
                xalign 0.5 xanchor 0.5
                style "thirty_five_grad_text_normal"
                outlines [(1,"#000000",2,2)]
            null height 180

        hbox spacing 20 align(0.8,0.8):
            textbutton "Загрузить":
                text_outlines [(1,"#000000",2,2)]
                text_insensitive_color "#FFFFFF"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                action [Hide('load', transition=Dissolve(0.3)), thirty_five_grad_FunctionCallback(thirty_five_grad_on_load_callback, selected_slot),FileLoad(selected_slot,confirm=False), ShowMenu('load'), ]

            textbutton "Удалить":
                text_outlines [(1,"#000000",2,2)]
                text_insensitive_color "#FFFFFF"
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                action [Hide('load', transition=Dissolve(0.3)), FileDelete(selected_slot,confirm=False), ShowMenu('load')]

        vbox spacing 50 align(0.1,0.5):
            hbox spacing 20 xalign 0.5:
                textbutton "Ручные":
                    text_outlines [(1,"#000000",2,2)]
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                    action [Hide('load', transition=Dissolve(0.3)), FilePage("thirty_five_grad_FilePage_game"),SetVariable("selected_slot",""),SelectedIf(persistent._file_page == "thirty_five_grad_FilePage_game"), ShowMenu('load')]

                textbutton "Авто":
                    text_outlines [(1,"#000000",2,2)]
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                    action [Hide('load', transition=Dissolve(0.3)), FilePage("thirty_five_grad_FilePage_auto"),SetVariable("selected_slot",""),SelectedIf(persistent._file_page == "thirty_five_grad_FilePage_auto"), ShowMenu('load')]
            hbox spacing 30 xalign 0.5:
                vbox spacing 10:
                    for item in range(1,6):
                        textbutton (FileSaveName(item) if FileSaveName(item) else "Пустой слот"):
                            text_outlines [(1,"#000000",2,2)]
                            hover_sound thirty_five_grad_button_hover_sound
                            activate_sound thirty_five_grad_button_release_sound
                            style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                            text_align 0.0
                            xalign 0.0
                            action [Hide('load', transition=Dissolve(0.3)), SetVariable("selected_slot", item), ShowMenu('load')]

        textbutton "Назад":
            xpos 0.06 ypos 0.87
            text_outlines [(1,"#000000",2,2)]
            hover_sound thirty_five_grad_button_hover_sound
            activate_sound thirty_five_grad_button_release_sound
            style "thirty_five_grad_text_small_menu" text_style "thirty_five_grad_text_small_menu"
            action [Return(value=None)]
            yoffset -1

        add thirty_five_grad_dust_anim



    screen thirty_five_grad_save:
        tag menu modal True
        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)
        frame background im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0) 
        key "game_menu" action (Hide('thirty_five_grad_save', transition=Dissolve(0.3)), Return(value=None)) 
        vbox spacing 20 align(0.8,0.92):
            text FileTime(selected_slot,format='{font=SonySketch.ttf}{size=42}{color=#808080}%d.%m.%y, %H:%M{/size}{/color}{/font}',empty=""):
                xalign 0.5 xanchor 0.5
                style "thirty_five_grad_text_normal"
                outlines [(1,"#000000",2,2)]
            null height 180

        hbox spacing 20 align(0.8,0.8):
            textbutton "Сохранить":
                text_insensitive_color "#FFFFFF"
                text_outlines [(1,"#000000",2,2)]
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal"
                action [Hide('save', transition=Dissolve(0.3)), thirty_five_grad_FunctionCallback(thirty_five_grad_on_save_callback, selected_slot),FileSave(selected_slot,confirm=False), SensitiveIf(persistent._file_page != "thirty_five_grad_FilePage_auto"), ShowMenu('save')]

            textbutton "Удалить":
                text_insensitive_color "#FFFFFF"
                text_outlines [(1,"#000000",2,2)]
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal"
                action [Hide('save', transition=Dissolve(0.3)), FileDelete(selected_slot,confirm=False), ShowMenu('thirty_five_grad_save')]

        vbox spacing 50 align(0.1,0.5):
            hbox spacing 20 xalign 0.5:
                textbutton "Ручные":
                    text_outlines [(1,"#000000",2,2)]
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal"
                    action [Hide('save', transition=Dissolve(0.3)), FilePage("thirty_five_grad_FilePage_game"),SetVariable("selected_slot",""),SelectedIf(persistent._file_page == "thirty_five_grad_FilePage_game"), ShowMenu('save')]

                textbutton "Авто":
                    text_outlines [(1,"#000000",2,2)]
                    hover_sound thirty_five_grad_button_hover_sound
                    activate_sound thirty_five_grad_button_release_sound
                    style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal"
                    action [Hide('save', transition=Dissolve(0.3)), FilePage("thirty_five_grad_FilePage_auto"),SetVariable("selected_slot",""),SelectedIf(persistent._file_page == "thirty_five_grad_FilePage_auto"), ShowMenu('save')]

            hbox spacing 30 xalign 0.5:
                vbox spacing 10:
                    for item in range(1,6):
                        textbutton (FileSaveName(item) if FileSaveName(item) else "Пустой слот"):
                            hover_sound thirty_five_grad_button_hover_sound
                            activate_sound thirty_five_grad_button_release_sound
                            style "thirty_five_grad_text_normal" text_style "thirty_five_grad_text_normal" 
                            text_align 0.0
                            xalign 0.0
                            text_outlines [(1,"#000000",2,2)]
                            action [Hide('save', transition=Dissolve(0.3)), SetVariable("selected_slot", item), ShowMenu('save')]
        
            
        textbutton "Назад":
            hover_sound thirty_five_grad_button_hover_sound
            activate_sound thirty_five_grad_button_release_sound
            text_outlines [(1,"#000000",2,2)]
            xpos 0.06 ypos 0.87
            style "thirty_five_grad_text_small_menu" text_style "thirty_five_grad_text_small_menu"
            action [Return()]
            yoffset -1
        add thirty_five_grad_dust_anim



    screen thirty_five_grad_preferences:
        tag menu modal True
        default thirty_five_grad_dust_anim = CustomParticles("images/gui/main_menu/dust_partic.png", 150)
        frame background im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0) 
        key "game_menu" action (Hide('preferences', transition=Dissolve(0.3)), Return(value=None)) 
        vbox spacing 80 align(0.5,0.5):
            hbox xalign 0.5 spacing 50:
                vbox xalign 0.5 spacing 20:
                    text "Режим экрана" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    hbox xalign 0.5 spacing 20:
                        if not _preferences.fullscreen:
                            textbutton "Оконный":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] text_color '#666666'

                            textbutton "Полноэкранный":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                action [Hide('preferences', transition=Dissolve(0.3)), Preference("display", "fullscreen"), ShowMenu('preferences')]

                        if _preferences.fullscreen:
                            textbutton "Оконный":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] 
                                action [Hide('preferences', transition=Dissolve(0.3)), Preference("display", "window"), ShowMenu('preferences')]

                            textbutton "Полноэкранный":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] text_color '#666666'


                vbox xalign 0.5 spacing 20:
                        text "Режим пропуска" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                        hbox xalign 0.5 spacing 20:

                            if not _preferences.skip_unseen:
                                textbutton "Весь текст":
                                    hover_sound thirty_five_grad_button_hover_sound
                                    activate_sound thirty_five_grad_button_release_sound
                                    style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                    action [Hide('preferences', transition=Dissolve(0.3)), Preference("skip","all"), ShowMenu('preferences')]

                                textbutton "Прочитанное":
                                    style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] text_color '#666666'

                            if _preferences.skip_unseen:
                                textbutton "Весь текст":
                                    style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] text_color '#666666'


                                textbutton "Прочитанное":
                                    hover_sound thirty_five_grad_button_hover_sound
                                    activate_sound thirty_five_grad_button_release_sound
                                    style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)] 
                                    action [Hide('preferences', transition=Dissolve(0.3)), Preference("skip","seen"), ShowMenu('preferences')]

                vbox xalign 0.5 spacing 20:
                    text "Размер шрифта" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    hbox xalign 0.5 spacing 20:
                        if persistent.font_size == "small":
                            textbutton "Обычный":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]  text_color '#666666'


                            textbutton "Большой":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                action [Hide('preferences', transition=Dissolve(0.3)), SetField(persistent,"font_size","large"), ShowMenu('preferences')]

                        if persistent.font_size == "large":
                            textbutton "Обычный":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                action [Hide('preferences', transition=Dissolve(0.3)), SetField(persistent,"font_size","small"), ShowMenu('preferences')]

                            textbutton "Большой":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]  text_color '#666666'

                
                vbox xalign 0.5 spacing 20:
                    text "Размытие фона" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    hbox xalign 0.5 spacing 20:
                        if persistent.thirty_five_grad_blur_pref == True:
                            textbutton "Вкл.":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]  text_color '#666666'


                            textbutton "Выкл.":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                action [Hide('preferences', transition=Dissolve(0.3)), thirty_five_grad_blur_disable_def, ShowMenu('preferences')]

                        if persistent.thirty_five_grad_blur_pref != True:
                            textbutton "Вкл.":
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]
                                action [Hide('preferences', transition=Dissolve(0.3)), thirty_five_grad_blur_enable_def, ShowMenu('preferences')]

                            textbutton "Выкл.":
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 30 xalign 0.5 text_outlines [(1,"#000000",2,2)]  text_color '#666666'





            hbox xalign 0.5 spacing 50:
                vbox xalign 0.5 spacing 20:
                    text "Музыка" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    bar value Preference("music volume") xalign 0.5 maximum(264,22):
                        right_bar thirty_five_grad_save_load_pref_directory+"volume_right.png"
                        left_bar thirty_five_grad_save_load_pref_directory+"volume_left.png"
                        thumb thirty_five_grad_save_load_pref_directory+"volume_dot.png"

                vbox xalign 0.5 spacing 20:
                    text "Звуки" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    bar value Preference("sound volume") xalign 0.5 maximum(264,22):
                        right_bar thirty_five_grad_save_load_pref_directory+"volume_right.png"
                        left_bar thirty_five_grad_save_load_pref_directory+"volume_left.png"
                        thumb thirty_five_grad_save_load_pref_directory+"volume_dot.png"

                vbox xalign 0.5 spacing 20:
                    text "Эмбиент" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    bar value Preference("voice volume") xalign 0.5 maximum(264,22):
                        right_bar thirty_five_grad_save_load_pref_directory+"volume_right.png"
                        left_bar thirty_five_grad_save_load_pref_directory+"volume_left.png"
                        thumb thirty_five_grad_save_load_pref_directory+"volume_dot.png"

                vbox xalign 0.5 spacing 20:
                    text "Скорость текста" size 30 font thirty_five_grad_storopia outlines [(1,"#000000",2,2)] xalign 0.5
                    bar value Preference("text speed") xalign 0.5 maximum(264,22):
                        right_bar thirty_five_grad_save_load_pref_directory+"volume_right.png"
                        left_bar thirty_five_grad_save_load_pref_directory+"volume_left.png"
                        thumb thirty_five_grad_save_load_pref_directory+"volume_dot.png"

        textbutton "Назад":
            hover_sound thirty_five_grad_button_hover_sound
            activate_sound thirty_five_grad_button_release_sound
            xpos 0.06 ypos 0.87
            text_outlines [(1,"#000000",2,2)]
            style "thirty_five_grad_text_small_menu" text_style "thirty_five_grad_text_small_menu"
            action [Return()]
            yoffset -1

        add thirty_five_grad_dust_anim



    screen thirty_five_grad_skip_indicator:
        zorder 100
        style_prefix "skip"
        text 'Пропуск' style 'thirty_five_grad_text_small' size 50 color "#ffffff" outlines [(1,"#000000",2,2)] at thirty_five_grad_skip_anim



    screen thirty_five_grad_notify(message):
        modal False
        zorder 100
        
        if not config.skipping:
            text message font thirty_five_grad_storopia size 30 color "#FFFFFF" xmaximum 0.4 text_align 1.0 outlines [(1,"#000000",2,2)] at thirty_five_grad_notify_anim

        else:
            timer 0.01 action Hide('notify')

        key "dismiss" action (Hide('notify'), Return())
        key "toggle_skip" action (Hide('notify'), Return())
        key "skip" action (Hide('notify'), Return())
        key "rollforward" action (Hide('notify'), Return())



    screen thirty_five_grad_exit: # анимки глючат, как фиксить - хз
        tag menu modal True

        frame:
            background thirty_five_grad_exit_directory+"bg.png"
            key "game_menu" action (Hide('thirty_five_grad_exit', transition=Dissolve(0.5)), Return(value=None)) 
            add thirty_five_grad_exit_directory+"mi_blur_dark.png"
        
            vbox xpos 0.075 ypos 0.2:

                text 'Хочешь уйти?' style "thirty_five_grad_text_storopia" size 96 outlines [(1,"#000000",2,2)] color '#696969' at thirty_five_grad_exit_text_anim
                vbox ypos 0.8 spacing 10:
                    textbutton '{glitch=0.45}{outlinecolor=#000000}{font=Storopia.ttf}{color=#665050}{size=36}Да{/size}{/color}{/font}{/outlinecolor}{/glitch}': 
                        # особенности глитча для текста:
                        # 1. не работает с длинными путями файлов (я в корневую папку мода поэтому их и закадываю)
                        # 2. надо переуказывать шрифты и параметры стиля, тк они с глитчем не применяются (хз поч)
                        # 3. всегда {glitch} и {/glitch} надо ставить ПЕРЕД ВСЕМИ ДРУГИМИ ТЕГАМИ (напр - text '{glitch=1.0}{font=Storopia.ttf}{size=28}пиво{/size}{/font}{/glitch}', а не text '{font=Storopia.ttf}{glitch=1.0}{size=28}пиво{/size}{/glitch}{font=/font}' или text '{font=Storopia.ttf}{size=28}{glitch=1.0}пиво{/font}{/size}{/glitch}') 
                        # 4. это отдельная библиотека (в addons лежит, 35grad_glitch_tag.rpy и 35grad_kinetic_text_tags.rpy нужны, чтобы все работало, только когда будете к себе в код перетаскивать - переименуйте файлы под свой мод, чтобы конфликтов имён не было
                        hover_sound thirty_five_grad_button_hover_sound
                        activate_sound thirty_five_grad_button_release_sound
                        style "thirty_five_grad_text_storopia"
                        action [Start('thirty_five_grad_exit_label')]
                        at thirty_five_grad_exit_yes_anim

                    textbutton 'Нет':
                        hover_sound thirty_five_grad_button_hover_sound
                        activate_sound thirty_five_grad_button_release_sound
                        style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" text_size 36 text_color '#696969' text_outlines [(1,"#000000",2,2)]
                        action [Return()] 
                        at thirty_five_grad_exit_no_anim
 


    screen thirty_five_grad_start_blur_sc:
        tag menu modal True
        frame:
            
            if persistent.thirty_five_grad_blur_pref:
                background im.Blur(thirty_five_grad_bg_directory+'ext_road2_night_7dl.png', 2.0)
                add 'images/sprites/normal/pioneer/miku/1/miku_1_smile_pio_ponytails.png' xalign 0.7  at thirty_five_grad_night_lighting
                vbox spacing 80 align(0.175,0.2):
                    vbox xalign 0.2 yalign 0.2 spacing 20:
                        text 'Размытие фона': 
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]

                        text 'Фон будет размываться\nпри появлении персонажей\nи телефона': 
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]
                        text 'Этот параметр можно изменить\nв настройках':
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]
                        hbox yalign 0.3 spacing 10:
                            textbutton ['Вкл.']:
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" 
                                text_style "thirty_five_grad_text_storopia" 
                                text_size 36 
                                text_color '#696969' 
                                text_outlines [(1,"#000000",2,2)]


                            textbutton ['Выкл.']:
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" 
                                text_size 36 
                                text_outlines [(1,"#000000",2,2)]
                                action [Hide('thirty_five_grad_start_blur_sc', transition=Dissolve(0.5)), thirty_five_grad_blur_disable_def, ShowMenu('thirty_five_grad_start_blur_sc')] 



            if not persistent.thirty_five_grad_blur_pref:
                background thirty_five_grad_bg_directory+'ext_road2_night_7dl.png'
                add 'images/sprites/normal/pioneer/miku/1/miku_1_smile_pio_ponytails.png' xalign 0.7 at thirty_five_grad_night_lighting
                vbox spacing 80 align(0.175,0.2):
                    vbox xalign 0.2 yalign 0.7 spacing 20:
                        text 'Размытие фона': 
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]

                        text 'Фон будет размываться\nпри появлении персонажей\nи телефона': 
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]
                        text 'Этот параметр можно изменить\nв настройках':
                            size 36
                            font thirty_five_grad_storopia 
                            outlines [(1,"#000000",2,2)]
                        hbox yalign 0.7 spacing 10:
                            textbutton ['Вкл.']:
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" 
                                text_style "thirty_five_grad_text_storopia" 
                                text_size 36 
                                action [Hide('thirty_five_grad_start_blur_sc', transition=Dissolve(0.5)), thirty_five_grad_blur_enable_def, ShowMenu('thirty_five_grad_start_blur_sc')] 
                                text_outlines [(1,"#000000",2,2)]


                            textbutton ['Выкл.']:
                                hover_sound thirty_five_grad_button_hover_sound
                                activate_sound thirty_five_grad_button_release_sound
                                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" 
                                text_size 36 
                                text_color '#696969' 
                                text_outlines [(1,"#000000",2,2)]



            textbutton ['Далее']:
                xalign 0.9 yalign 0.9
                hover_sound thirty_five_grad_button_hover_sound
                activate_sound thirty_five_grad_button_release_sound
                style "thirty_five_grad_text_storopia" text_style "thirty_five_grad_text_storopia" 
                text_size 36 
                text_color '#FFFFFF' 
                text_outlines [(1,"#000000",2,2)]
                action [Start('thirty_five_grad_prologue')] 








init -1: # я в душе не чаю, че я тут написал

    screen thirty_five_grad_hover_start_game_mm:
        add thirty_five_grad_main_menu_directory+"start_game_hover.png" at thirty_five_grad_button_1_hover_menu

    screen thirty_five_grad_hover_load_mm:
        add thirty_five_grad_main_menu_directory+"load_hover.png" at thirty_five_grad_button_2_hover_menu

    screen thirty_five_grad_hover_mus_box_mm:
        add thirty_five_grad_main_menu_directory+"mus_box_hover.png" at thirty_five_grad_button_3_hover_menu

    screen thirty_five_grad_hover_gallery_mm:
        add thirty_five_grad_main_menu_directory+"gallery_hover.png" at thirty_five_grad_button_4_hover_menu

    screen thirty_five_grad_hover_boosty_mm:
        add thirty_five_grad_main_menu_directory+"boosty_hover.png" at thirty_five_grad_button_boosty_hover_menu

    screen thirty_five_grad_hover_telegram_mm:
        add thirty_five_grad_main_menu_directory+"tg_hover.png" at thirty_five_grad_button_telegram_hover_menu

    screen thirty_five_grad_hover_vk_mm:
        add thirty_five_grad_main_menu_directory+"vk_hover.png" at thirty_five_grad_button_vk_hover_menu

    screen thirty_five_grad_hover_steam_mm:
        add thirty_five_grad_main_menu_directory+"steam_hover.png" at thirty_five_grad_button_steam_hover_menu

    screen thirty_five_grad_hover_exit_mm:
        add thirty_five_grad_main_menu_directory+"exit_hover.png" at thirty_five_grad_button_5_hover_menu

    screen thirty_five_grad_hover_back:
        add thirty_five_grad_coming_soon_directory+"back_hover.png" at thirty_five_grad_button_4_hover_menu


    screen thirty_five_grad_save_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"save_small_hovered.png" at thirty_five_grad_save_button_hover_anim
    
    screen thirty_five_grad_save_fuckingstick_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"save_button_hover_small.png" at thirty_five_grad_save_button_fuckingstick_anim


    screen thirty_five_grad_load_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"load_small_hovered.png" at thirty_five_grad_load_button_hover_anim
    
    screen thirty_five_grad_load_fuckingstick_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"load_button_hover_small.png" at thirty_five_grad_load_button_fuckingstick_anim


    screen thirty_five_grad_hide_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"hide_small_hovered.png" at thirty_five_grad_hide_button_hover_anim
    
    screen thirty_five_grad_hide_fuckingstick_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"hide_button_hover_small.png" at thirty_five_grad_hide_button_fuckingstick_anim


    screen thirty_five_grad_skip_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"skip_button_hover_part1.png" at thirty_five_grad_skip_button_hover_small_anim_part1
        add thirty_five_grad_textbox_directory+"skip_button_hover_part2.png" at thirty_five_grad_skip_button_hover_small_anim_part2


    screen thirty_five_grad_clearly_hover:
        add thirty_five_grad_textbox_directory+"clearly_hide_tip_hover.png" at thirty_five_grad_clearly_button_hover_anim

    screen thirty_five_grad_clearly_fuckingstick_hover:
        add thirty_five_grad_textbox_directory+"clearly_button_hover.png" at thirty_five_grad_clearly_button_fuckingstick_anim


    screen thirty_five_grad_continue_hover:
        add "images/gui/a_few_moments/continue_hover.png" at thirty_five_grad_clearly_button_hover_anim

    screen thirty_five_grad_continue_fuckingstick_hover:
        add "images/gui/a_few_moments/continue_fuckingstick.png" at thirty_five_grad_continue_button_fuckingstick_anim


    screen thirty_five_grad_showtextbox_hover_small:
        add thirty_five_grad_textbox_directory+"hidden_hovered.png" at thirty_five_grad_show_textbox_button_hover_anim


    screen thirty_five_grad_preferences_hover_small:
        add thirty_five_grad_textbox_directory+"settings_small_hover.png" at thirty_five_grad_preferences_button_hover_anim

    screen thirty_five_grad_preferences_fuckingstick_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"settings_button_hover_small.png" at thirty_five_grad_preferences_button_fuckingstick_anim


    screen thirty_five_grad_qm_hover_small:
        add thirty_five_grad_textbox_directory+"menu_small_hovered.png" at thirty_five_grad_qm_button_hover_anim

    screen thirty_five_grad_qm_fuckingstick_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"menu_button_hover_small.png" at thirty_five_grad_qm_button_fuckingstick_anim


    # screen thirty_five_grad_qm_hover_small:
    #     add thirty_five_grad_textbox_directory+"menu_small_hovered.png" at thirty_five_grad_preferences_button_hover_anim

    # screen thirty_five_grad_qm_fuckingstick_textbox_hover_small:
    #     add thirty_five_grad_textbox_directory+"menu_button_hover_small.png" at thirty_five_grad_preferences_button_fuckingstick_anim


    screen thirty_five_grad_reverse_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"reverse_button_hover_part1.png" at thirty_five_grad_reverse_button_hover_large_anim_part1
        add thirty_five_grad_textbox_directory+"reverse_button_hover_part2.png" at thirty_five_grad_reverse_button_hover_large_anim_part2

        
    screen thirty_five_grad_save_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/save_hover.png" at thirty_five_grad_save_button_hover_anim
    
    screen thirty_five_grad_save_fuckingstick_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/save_fuckingstick.png" at thirty_five_grad_save_button_fuckingstick_anim


    screen thirty_five_grad_load_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/load_hover.png" at thirty_five_grad_load_button_hover_anim
    
    screen thirty_five_grad_load_fuckingstick_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/load_fuckingstick.png" at thirty_five_grad_load_button_fuckingstick_anim


    screen thirty_five_grad_hide_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/hide_hover.png" at thirty_five_grad_hide_button_hover_anim
    
    screen thirty_five_grad_hide_fuckingstick_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/hide_fuckingstick.png" at thirty_five_grad_hide_button_fuckingstick_anim

    screen thirty_five_grad_preferences_hover_large:
        add thirty_five_grad_textbox_directory+"large/preferences_hover.png" at thirty_five_grad_preferences_button_hover_anim

    screen thirty_five_grad_preferences_fuckingstick_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/preferences_fuckingstick.png" at thirty_five_grad_preferences_button_fuckingstick_anim


    screen thirty_five_grad_skip_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"skip_button_hover_part1.png" at thirty_five_grad_skip_button_hover_large_anim_part1
        add thirty_five_grad_textbox_directory+"skip_button_hover_part2.png" at thirty_five_grad_skip_button_hover_large_anim_part2
 


    screen thirty_five_grad_qm_hover_large:
        add thirty_five_grad_textbox_directory+"large/menu_hover.png" at thirty_five_grad_qm_button_hover_anim

    screen thirty_five_grad_qm_fuckingstick_textbox_hover_large:
        add thirty_five_grad_textbox_directory+"large/menu_fuckingstick.png" at thirty_five_grad_qm_button_fuckingstick_anim


    screen thirty_five_grad_quick_menu_pref:
        add thirty_five_grad_qm_directory+"settings_hover.png" at thirty_five_grad_button_2_hover_menu

    screen thirty_five_grad_quick_menu_load:
        add thirty_five_grad_qm_directory+"load_hover.png" at thirty_five_grad_button_1_hover_menu

    screen thirty_five_grad_hover_exit_qm:
        add thirty_five_grad_main_menu_directory+"exit_hover.png" at thirty_five_grad_button_3_hover_menu

    screen thirty_five_grad_hover_back_qm:
        add thirty_five_grad_coming_soon_directory+"back_hover.png" at thirty_five_grad_button_5_hover_menu

    screen thirty_five_grad_quick_menu_save:
        add thirty_five_grad_qm_directory+"save_hover.png" at thirty_five_grad_button_0_hover_menu

    screen thirty_five_grad_back_save_load_pref:
        add thirty_five_grad_save_load_pref_directory+"back_hover.png" at thirty_five_grad_button_5_back_load_pref_hover


    screen thirty_five_grad_reverse_textbox_hover_small:
        add thirty_five_grad_textbox_directory+"reverse_button_hover_part1.png" at thirty_five_grad_reverse_button_hover_small_anim_part1
        add thirty_five_grad_textbox_directory+"reverse_button_hover_part2.png" at thirty_five_grad_reverse_button_hover_small_anim_part2


