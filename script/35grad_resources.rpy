init -1:
    python:
        import os
        mods["thirty_five_grad_init"]                           = u"{font=SonySketch.ttf}{color=#5F9EA8}{size=40}re:35° code{/size}{/color}{/font}"
        user = os.environ.get('username')

        #персонажи
        thirty_five_grad_alex                                   = Character(u'Алексей', color="627388", what_color="FFFFFF")
        thirty_five_grad_sl_unk                                 = Character(u'{glitch=0.55}{color=#DBAB00}{font=SonySketch.ttf}{size=28}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_sl_unk_larger                          = Character(u'{glitch=0.55}{color=#DBAB00}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_sl                                     = Character(u'{glitch=0.55}{color=#DBAB00}{font=SonySketch.ttf}{size=35}Славя{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_dv_unk                                 = Character(u'{glitch=0.55}{color=#FF8C00}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_dv                                     = Character(u'{glitch=0.55}{color=#FF8C00}{font=SonySketch.ttf}{size=35}Алиса{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_ul                                     = Character(u'{glitch=0.55}{color=#9527F5}{font=SonySketch.ttf}{size=35}Лена{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_ul_unk                                 = Character(u'{glitch=0.55}{color=#9527F5}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mt                                     = Character(u'{glitch=0.55}{color=#2BFF46}{font=SonySketch.ttf}{size=35}Ольга Дмитриевна{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mt_unk                                 = Character(u'{glitch=0.55}{color=#2BFF46}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_sh_unk                                 = Character(u'{glitch=0.55}{color=#E8F000}{font=SonySketch.ttf}{size=35}Неизвестный{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_sh                                     = Character(u'{glitch=0.55}{color=#E8F000}{font=SonySketch.ttf}{size=35}Шурик{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_el_unk                                 = Character(u'{glitch=0.55}{color=#F7FF0F}{font=SonySketch.ttf}{size=35}Неизвестный{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_el                                     = Character(u'{glitch=0.55}{color=#F7FF0F}{font=SonySketch.ttf}{size=35}Электроник{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mz_unk                                 = Character(u'{glitch=0.55}{color=#534FFF}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mz                                     = Character(u'{glitch=0.55}{color=#534FFF}{font=SonySketch.ttf}{size=35}Женя{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_cs                                     = Character(u'{glitch=0.55}{color=#B891FF}{font=SonySketch.ttf}{size=35}Виола{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_cs_unk                                 = Character(u'{glitch=0.55}{color=#B891FF}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mi                                     = Character(u'{glitch=0.55}{color=#00ddc0}{font=SonySketch.ttf}{size=35}Мику{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mi_unk                                 = Character(u'{glitch=0.55}{color=#00ddc0}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_uv                                     = Character(u'{glitch=0.55}{color=#00ddc0}{font=SonySketch.ttf}{size=35}Юля{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_uv_unk                                 = Character(u'{glitch=0.55}{color=#00ddc0}{font=SonySketch.ttf}{size=35}Неизвестная{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_vz_unk                                 = Character(u'{glitch=0.55}{color=#2BFF46}{font=SonySketch.ttf}{size=35}Вожатый{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_mi_alex                                = Character(u'{glitch=0.55}{color=#00ddc0}{font=SonySketch.ttf}{size=35}Мику/Алексей{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")
        thirty_five_grad_pi                                     = Character(u'{glitch=0.55}{color=#FF0000}{font=SonySketch.ttf}{size=35}Пионер{/size}{/color}{/font}{/glitch}', what_color="FFFFFF")


        #директории
        thirty_five_grad_main_menu_directory                    = 'images/gui/main_menu/'
        thirty_five_grad_coming_soon_directory                  = 'images/gui/in_development/'
        thirty_five_grad_sounds_directory                       = 'sounds/'
        thirty_five_grad_music_directory                        = 'music/'
        thirty_five_grad_cg_directory                           = 'images/cg/'
        thirty_five_grad_bg_directory                           = 'images/bg/'
        thirty_five_grad_textbox_directory                      = 'images/gui/textbox/'
        thirty_five_grad_qm_directory                           = 'images/gui/quick_menu/'
        thirty_five_grad_save_load_pref_directory               = 'images/gui/save_load_pref/'
        thirty_five_grad_exit_directory                         = 'images/gui/exit/'
        thirty_five_grad_mobile_directory                       = 'images/mobile/'
        thirty_five_grad_etc_directory                          = 'images/etc/'
        thirty_five_grad_transitions                            = 'images/transitions/'


        #звуки
        thirty_five_grad_button_hover_sound                     = thirty_five_grad_sounds_directory+'button_hover.wav'
        thirty_five_grad_button_release_sound                   = thirty_five_grad_sounds_directory+'button_release.wav'
        thirty_five_grad_button_page_sound                      = thirty_five_grad_sounds_directory+'repl_page_turning_5_7dl.ogg'
        thirty_five_grad_low_battery_headphones                 = thirty_five_grad_sounds_directory+'low_battery_headphones.mp3'
        thirty_five_grad_glitch_transition_1                    = thirty_five_grad_sounds_directory+'glitch_transition.mp3'
        thirty_five_grad_head_heartbeat                         = thirty_five_grad_sounds_directory+'head_heartbeat.ogg'
        thirty_five_grad_fall_grass                             = thirty_five_grad_sounds_directory+'fall_grass.ogg'
        thirty_five_grad_old_desktop_pc_booting_up              = thirty_five_grad_sounds_directory+"old_desktop_pc_booting_up.mp3"
        thirty_five_grad_unclothe1                              = thirty_five_grad_sounds_directory+"unclothe1.mp3"
        thirty_five_grad_scream                                 = thirty_five_grad_sounds_directory+"myinstants.ogg"
        thirty_five_grad_light_on_off                           = thirty_five_grad_sounds_directory+"light_on_off.ogg"
        thirty_five_grad_2                                      = thirty_five_grad_sounds_directory+"2.mp3"
        thirty_five_grad_3                                      = thirty_five_grad_sounds_directory+"3.mp3"
        thirty_five_grad_666                                    = thirty_five_grad_sounds_directory+"666.mp3"


        #музыка
        thirty_five_grad_mm_music                               = thirty_five_grad_music_directory+'ill_be_waiting.ogg'
        thirty_five_grad_the_city_in_the_sky                    = thirty_five_grad_music_directory+'natus_city_in_the_sky_end.ogg'
        thirty_five_grad_to_a_dark_lady                         = thirty_five_grad_music_directory+'to_a_dark_lady.ogg'
        thirty_five_grad_Ihokkaido_leaves                       = thirty_five_grad_music_directory+'Ihokkaido_leaves.ogg'
        thirty_five_grad_Iframe_dawn_in_the_adan                = thirty_five_grad_music_directory+'Iframe_dawn_in_the_adan.ogg'
        thirty_five_grad_summer_day                             = thirty_five_grad_music_directory+'summer_day.ogg'
        thirty_five_grad_The_Italians                           = thirty_five_grad_music_directory+'The_Italians.ogg'
        thirty_five_grad_Nerik_Cinema                           = thirty_five_grad_music_directory+'КАМАКА-—-Nerik-Cinema.ogg'
        thirty_five_grad_drive                                  = thirty_five_grad_music_directory+'drive.ogg'
        thirty_five_grad_flawed_mangoes                         = thirty_five_grad_music_directory+'Flawed_Mangoes_Tunnel_Vision.ogg'
        thirty_five_grad_mikumylove                             = thirty_five_grad_music_directory+'mikumylove.ogg'
        thirty_five_grad_svet_urodi                             = thirty_five_grad_music_directory+'ЧёЗаУродыНаСцене_Свет_Домашняя_версия.ogg'
        thirty_five_grad_sfl1                                   = thirty_five_grad_music_directory+'sfl1.mp3'
        thirty_five_grad_misshome2                              = thirty_five_grad_music_directory+'misshome2.mp3'
        thirty_five_grad_excited_happiness                      = thirty_five_grad_music_directory+'Excited_Happiness.ogg'
        thirty_five_grad_feeling_good                           = thirty_five_grad_music_directory+'everlasting_summer_12 - Feeling Good.mp3'


        # переходы
        thirty_five_grad_timeskip_transition                    = ImageDissolve( thirty_five_grad_transitions + 'timeskip.png', 1.0, ramplen=0, reverse=False, alpha=True)
        thirty_five_grad_blinds_h_transition                    = ImageDissolve( thirty_five_grad_transitions + 'blinds_h.png', 1.0, ramplen=0, reverse=False, alpha=True)
        thirty_five_grad_blinds_v_transition                    = ImageDissolve( thirty_five_grad_transitions + 'blinds_v.png', 1.0, ramplen=0, reverse=False, alpha=True)
        thirty_five_grad_circle_transition                      = ImageDissolve( thirty_five_grad_transitions + 'circle.png', 1.0, ramplen=0, reverse=False, alpha=True)
        thirty_five_grad_star_falling_transition                = ImageDissolve( thirty_five_grad_transitions + 'star_falling.png', 1.0, ramplen=0, reverse=False, alpha=True)



        
init 1:

    #бг
    image bg thirty_five_grad_eyes_forest                       = thirty_five_grad_bg_directory+'eyes_forest.png'
    image bg thirty_five_grad_eyes_forest_glitch_epil:  
        contains:
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_1.png')
            pause 0.016
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_2.png')
            pause 0.0341
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_3.png')
            pause 0.02618
            thirty_five_grad_get_image('anim/eyes_forest_glitch/eyes_forest1.png')
            pause 0.0156
            thirty_five_grad_get_image('anim/eyes_forest_glitch/eyes_forest2.png')
            pause 0.0065
            thirty_five_grad_get_image('anim/eyes_forest_glitch/eyes_forest3.png')
            pause 0.009056
            thirty_five_grad_get_image('anim/eyes_forest_glitch/eyes_forest4.png')
            pause 0.04549
            thirty_five_grad_get_image('anim/eyes_forest_glitch/eyes_forest5.png')
            pause 0.0564
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_3.png')
            pause 0.016
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_1.png')
            pause 0.00265
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_3.png')
            pause 0.0185
            thirty_five_grad_get_image('anim/eyes_forest_glitch/cg_bus_station_4.png')

    image bg thirty_five_grad_prolog_glitch_epil:
        contains:
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_1.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_2.jpg')
            pause 0.0341
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_3.jpg')
            pause 0.02618
            thirty_five_grad_get_image('anim/prolog_glitch/eyes_forest1.png')
            pause 0.0156
            thirty_five_grad_get_image('anim/prolog_glitch/eyes_forest2.png')
            pause 0.0065
            thirty_five_grad_get_image('anim/prolog_glitch/eyes_forest3.png')
            pause 0.009056
            thirty_five_grad_get_image('anim/prolog_glitch/eyes_forest4.png')
            pause 0.04549
            thirty_five_grad_get_image('anim/prolog_glitch/eyes_forest5.png')
            pause 0.0564
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_3.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_1.jpg')
            pause 0.00265
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_3.jpg')
            pause 0.0185
            thirty_five_grad_get_image('anim/prolog_glitch/transition_prolog_main_4.png')

    image bg thirty_five_grad_day1_glitch_epil:
        contains:
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_1.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_2.jpg')
            pause 0.0341
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_3.jpg')
            pause 0.02618
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_1.jpg')
            pause 0.0156
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_2.jpg')
            pause 0.0065
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_3.jpg')
            pause 0.009056
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_4.png')
            pause 0.04549
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_2.jpg')
            pause 0.0564
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_3.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_1.jpg')
            pause 0.00265
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_3.jpg')
            pause 0.0185
            thirty_five_grad_get_image('anim/day1_trans/transition_day1_4.png')

    image bg thirty_five_grad_day2_glitch_epil:
        contains:
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_1.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_2.jpg')
            pause 0.0341
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_3.jpg')
            pause 0.02618
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_1.jpg')
            pause 0.0156
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_2.jpg')
            pause 0.0065
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_3.jpg')
            pause 0.009056
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_4.jpg')
            pause 0.04549
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_2.jpg')
            pause 0.0564
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_3.jpg')
            pause 0.016
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_1.jpg')
            pause 0.00265
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_3.jpg')
            pause 0.0185
            thirty_five_grad_get_image('anim/day2_trans/transition_day2_5.png')


    image bg thirty_five_grad_ext_path night                    = thirty_five_grad_bg_directory+'ext_path_night.png'
    image bg thirty_five_grad_ext_path2 night                   = thirty_five_grad_bg_directory+'ext_path2_night.png'
    image bg thirty_five_grad_road night                        = thirty_five_grad_bg_directory+'ext_road2_night_7dl.png'
    image bg thirty_five_grad_road night blured                 = im.Blur(thirty_five_grad_bg_directory+'ext_road2_night_7dl.png', 2.0)
    image bg thirty_five_grad_ext_path2 sunset                  = thirty_five_grad_bg_directory+'ext_path2_sunset.png'
    image bg thirty_five_grad_ext_square sunset                 = thirty_five_grad_bg_directory+'ext_square_sunset.png'
    image bg thirty_five_grad_ext_road sunset                   = thirty_five_grad_bg_directory+'ext_road_sunset.png'
    image bg thirty_five_grad_ext_road sunset blured            = im.Blur(thirty_five_grad_bg_directory+'ext_road_sunset.png', 2.0)
    image bg thirty_five_grad_ext_camp_entrance sunset          = thirty_five_grad_bg_directory+'ext_camp_entrance_sunet.png'
    image bg thirty_five_grad_ext_camp_entrance sunset blured   = im.Blur(thirty_five_grad_bg_directory+'ext_camp_entrance_sunet.png', 2.0)
    image bg thirty_five_grad_ext_no_bus sunset                 = thirty_five_grad_bg_directory+'ext_no_bus_sunset.png'

    image bg thirty_five_grad_ext_sky2_pizdec_anim sunset:
        contains:
            thirty_five_grad_get_image('bg/ext_sky2_7dl_pizdec.png') 
            thirty_five_grad_get_image('bg/ext_sky2_7dl.png') with hell_dissolve
    
    image bg thirty_five_grad_clubs_sunset                                        = thirty_five_grad_bg_directory+'clubs_sunset.png'
    image bg thirty_five_grad_clubs_sunset blured                                 = im.Blur(thirty_five_grad_bg_directory+'clubs_sunset.png', 2.0)
    image bg thirty_five_grad_lager_sunset                                        = thirty_five_grad_bg_directory+'lager_sunset.png'
    image bg thirty_five_grad_lager_sunset blured                                 = im.Blur(thirty_five_grad_bg_directory+'lager_sunset.png', 2.0)
    image bg thirty_five_grad_music_sunset                                        = thirty_five_grad_bg_directory+'music_sunset.png'
    image bg thirty_five_grad_music_sunset blured                                 = im.Blur(thirty_five_grad_bg_directory+'music_sunset.png', 2.0)
    image bg thirty_five_grad_ext_square_sunset                                   = thirty_five_grad_bg_directory+'ext_square_sunset.png'
    image bg thirty_five_grad_ext_square_sunset blured                            = im.Blur(thirty_five_grad_bg_directory+'ext_square_sunset.png', 2.0)
    image bg thirty_five_grad_hata_vojatoi                                        = thirty_five_grad_bg_directory+'hata_vojatoi.jpg'
    image bg thirty_five_grad_int_music_club_sunset                               = thirty_five_grad_bg_directory+'int_musclub_sunset.jpg'
    image bg thirty_five_grad_ext_warehouse_day                                   = thirty_five_grad_bg_directory+'ext_warehouse_day.jpg'
    image bg thirty_five_grad_ext_warehouse_sunset                                = thirty_five_grad_bg_directory+'ext_warehouse_sunset.jpg'
    image bg thirty_five_grad_ext_musclub_verandah_day                            = thirty_five_grad_bg_directory+'ext_musclub_verandah_day.jpg'
    image bg thirty_five_grad_ext_musclub_verandah_sunset                         = thirty_five_grad_bg_directory+'obs_ext_musclub_verandah_sunset.png'
    image bg thirty_five_grad_int_wardrobe                                        = thirty_five_grad_bg_directory+'int_wardrobe.jpg'
    image bg thirty_five_grad_int_musclub_night_nolight                           = thirty_five_grad_bg_directory+'int_musclub_night_nolight_7dl.jpg'
    image bg thirty_five_grad_ext_musclub_verandah_night                          = thirty_five_grad_bg_directory+'ext_musclub_verandah_night_7dl.jpg'
    image bg thirty_five_grad_ext_musclub_night                                   = thirty_five_grad_bg_directory+'ext_musclub_night_7dl.jpg'
    image bg thirty_five_grad_ext_houses_night                                    = thirty_five_grad_bg_directory+'ext_houses_night_7dl.jpg'
    image bg thirty_five_grad_int_house_of_mt_sunset                              = thirty_five_grad_bg_directory+'int_house_of_mt_sunset.jpg'
    image bg thirty_five_grad_ext_playground_sunset                               = thirty_five_grad_bg_directory+'ext_playground_sunset.jpg'
    image bg thirty_five_grad_ext_washstand_sunset                                = thirty_five_grad_bg_directory+'ext_washstand_sunset_7dl.jpg'
    image bg thirty_five_grad_ext_aidpost_sunset                                  = thirty_five_grad_bg_directory+'ext_aidpost_sunset_7dl.jpg'
    image bg thirty_five_grad_ext_house_of_un_night                               = thirty_five_grad_bg_directory+'ext_house_of_un_night_7dl.jpg'



    #цг
    # Пролог
    image cg thirty_five_grad_transition_prolog_main            = thirty_five_grad_cg_directory+'transition_prolog_main.png'
    image cg thirty_five_grad_alex_bus_station                  = thirty_five_grad_cg_directory+'cg_bus_station.png'
    image cg thirty_five_grad_alex_bus_station blured           = im.Blur(thirty_five_grad_cg_directory+'cg_bus_station.png', 2.0)

    # день 1
    image cg thirty_five_grad_pancu_shot                        = thirty_five_grad_cg_directory+'cg_day1_pshot.png'
    image cg thirty_five_grad_nefor_mirror                      = thirty_five_grad_cg_directory+'cg_day1_mirror.png'
    image cg thirty_five_grad_miku_art_stolov                   = thirty_five_grad_cg_directory+'cg_day1_miku.png'
    image cg thirty_five_grad_miku_art_stolov_2                 = thirty_five_grad_cg_directory+'miku_1488.jpg'
    image cg thirty_five_grad_inter_day_1                       = thirty_five_grad_cg_directory+'cg_day1_slavya.jpg'
    image cg thirty_five_grad_transition_day_1_main             = thirty_five_grad_cg_directory+'transition_day_1_main.png'
    
    # день 2
    image cg thirty_five_grad_alice_day_2                       = thirty_five_grad_cg_directory+'cg_day2_alice.png'
    image cg thirty_five_grad_day2_miku                         = thirty_five_grad_cg_directory+'cg_day2_miku.png'
    image cg thirty_five_grad_transition_day_2_main             = thirty_five_grad_cg_directory+'transition_day_2_main.png'

    # день 3
    image cg thirty_five_grad_day3_miku                         = thirty_five_grad_cg_directory+'cg_day3_musclub.png'
    image cg thirty_five_grad_day3_miku_dinner                  = thirty_five_grad_cg_directory+'cg_day3_dinner.png'
    image cg thirty_five_grad_day3_musclub2                     = thirty_five_grad_cg_directory+'cg_day3_musclub2.png'
    image cg thirty_five_grad_transition_day_3_main             = thirty_five_grad_cg_directory+'transition_day_3_main.png'
    
    # день 4
    image cg thirty_five_grad_day4_kiss                         = thirty_five_grad_cg_directory+'cg_day4_kiss.png'
    image cg thirty_five_grad_day4_valyna                       = thirty_five_grad_cg_directory+'cg_day4_valyna.png'
    image cg thirty_five_grad_day4_one-punch                    = thirty_five_grad_cg_directory+'cg_day4_one-punch.png'
    image cg thirty_five_grad_day4_1_podval                     = thirty_five_grad_cg_directory+'cg_day4_1_podval.png'
    image cg thirty_five_grad_day4_2_podval                     = thirty_five_grad_cg_directory+'cg_day4_2_podval.png'
    image cg thirty_five_grad_day4_3_podval                     = thirty_five_grad_cg_directory+'cg_day4_3_podval.png'
    image cg thirty_five_grad_day4_4_podval                     = thirty_five_grad_cg_directory+'cg_day4_4_podval.png'
    image cg thirty_five_grad_day4_5_podval                     = thirty_five_grad_cg_directory+'cg_day4_5_podval.png'
    image cg thirty_five_grad_transition_day_4_main             = thirty_five_grad_cg_directory+'transition_day_4_main.png'

    # день 5
    image cg thirty_five_grad_day5_miku                         = thirty_five_grad_cg_directory+'cg_day5_miku.png'
    image cg thirty_five_grad_day5_alice                        = thirty_five_grad_cg_directory+'cg_day5_alice.png'
    image cg thirty_five_grad_transition_day_5_main             = thirty_five_grad_cg_directory+'transition_day_5_main.png'




    # анимации
    # Пролог
    image cg video_prolog                                       = Movie(play="video/alex_prologe.webm", loop=True)

    # день 1
    image cg day1_miku_animation                                = Movie(play="video/cg_day1_miku_animation.webm", loop=True)
    image cg day1_slavya_animation                              = Movie(play="video/cg_day1_slavya_animation.webm", loop=True)

    # день 2
    image cg day2_alice_animation                               = Movie(play="video/alice_animation.webm", loop=True)







    #прочее
    image thirty_five_grad_time                                 = DynamicDisplayable(thirty_five_grad_time_def)
    image thirty_five_grad_date                                 = DynamicDisplayable(thirty_five_grad_date_def)
    image thirty_five_grad_day                                  = DynamicDisplayable(thirty_five_grad_day_def)

    image thirty_five_grad_photo_1                              = thirty_five_grad_cg_directory+'photo_1.png'
    image thirty_five_grad_transition_day_1_words               = thirty_five_grad_cg_directory+'transition_day1_words.png'
    image thirty_five_grad_transition_day_2_words               = thirty_five_grad_cg_directory+'transition_day2_words.png'
    image thirty_five_grad_transition_day_3_words               = thirty_five_grad_cg_directory+'transition_day3_words.png'
    image thirty_five_grad_transition_day_4_words               = thirty_five_grad_cg_directory+'transition_day4_words.png'
    image thirty_five_grad_transition_prolog_words              = thirty_five_grad_cg_directory+'transition_prolog_words.png'


    image thirty_five_grad_mobile black                         = thirty_five_grad_mobile_directory+'mobile_black.png'
    image thirty_five_grad_mobile prologue                      = thirty_five_grad_mobile_directory+'mobile_prologue.png'
    image thirty_five_grad_mobile day1 morning                  = thirty_five_grad_mobile_directory+'d1_morning.png'
    image thirty_five_grad_mobile day1_notifications morning    = thirty_five_grad_mobile_directory+'d1_morning_notifications.png'
    image thirty_five_grad_mobile day1_dialer morning           = thirty_five_grad_mobile_directory+'d1_morning_dialer.png'
    image thirty_five_grad_mobile day1_call morning             = thirty_five_grad_mobile_directory+'d1_morning_call.png'
    
    image thirty_five_grad_logo_startup:    
        contains:
            thirty_five_grad_get_image('gui/logo_startup/part1.png')
            
    # image thirty_five_grad_text_logo_startup:
    #     xpos 0.7
    #     contains:
    #         thirty_five_grad_get_image('gui/logo_startup/part2.png')

    image thirty_five_grad_low_hp:
        thirty_five_grad_get_image("anim/low_hp/low_hp.png") with dissolve
        pause 0.62
        thirty_five_grad_get_image("anim/low_hp/low_hp1.png") with dissolve
        pause 0.62
        repeat


    image thirty_five_grad_after_seven_day_image_part1:
        thirty_five_grad_get_image('anim/after_seven_day/1.png')
    image thirty_five_grad_after_seven_day_image_part2:
        thirty_five_grad_get_image('anim/after_seven_day/2.png')
    image thirty_five_grad_after_seven_day_image_part3:
        thirty_five_grad_get_image('anim/after_seven_day/3.png')
    image thirty_five_grad_after_seven_day_image_part4:
        thirty_five_grad_get_image('anim/after_seven_day/4.png')
    image thirty_five_grad_after_seven_day_image_part5:
        thirty_five_grad_get_image('anim/after_seven_day/5.png')
    image thirty_five_grad_after_seven_day_image_part6:
        thirty_five_grad_get_image('anim/after_seven_day/6.png')
    image thirty_five_grad_after_seven_day_image_part7:
        thirty_five_grad_get_image('anim/after_seven_day/7.png')
    image thirty_five_grad_after_seven_day_image_part8:
        thirty_five_grad_get_image('anim/after_seven_day/8.png')
    
    image thirty_five_grad_after_seven_day_hes_here:
        contains:
            thirty_five_grad_get_image('anim/after_seven_day/9.png')
            pause 0.015
            thirty_five_grad_get_image('anim/after_seven_day/10.png')
            pause 0.0954
            thirty_five_grad_get_image('anim/after_seven_day/11.png')
            pause 0.05784
            thirty_five_grad_get_image('anim/after_seven_day/12.png')
            pause 0.15641
            thirty_five_grad_get_image('anim/after_seven_day/13.png')
            pause 0.04564
            thirty_five_grad_get_image('anim/after_seven_day/14.png')
            pause 0.04788
            thirty_five_grad_get_image('anim/after_seven_day/15.png')
            pause 0.04156865
            thirty_five_grad_get_image('anim/after_seven_day/16.png')



    image thirty_five_grad_vignette                             = thirty_five_grad_etc_directory+'vignette.png'

    