init 1:
    transform thirty_five_grad_vhs:
        mesh True
        shader "MakeVisualNovels.VHS"
        u_color (1.0, 1.0, 1.0, 1.0)

    # Манга-стиль: классический чёрно-белый
    transform thirty_five_grad_manga_bw:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.5           # Порог яркости (0.0-1.0). Чем выше - тем больше чёрного
        u_color (1.0, 1.0, 1.0, 1.0)  # Цвет светлых участков (белый)

    # Манга-стиль: с цветным контуром (синий)
    transform thirty_five_grad_manga_blue:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.45
        u_color (0.6, 0.8, 1.0, 1.0)  # Светло-голубой

    # Манга-стиль: сепия
    transform thirty_five_grad_manga_sepia:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.5
        u_color (0.9, 0.85, 0.7, 1.0)  # Сепия/бежевый

    # Манга-стиль: тёплый (воспоминания)
    transform thirty_five_grad_manga_memory:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.55
        u_color (1.0, 0.95, 0.85, 1.0)  # Тёплый бежевый

    # Манга-стиль: холодный (мрачные сцены)
    transform thirty_five_grad_manga_cold:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.4
        u_color (0.85, 0.9, 1.0, 1.0)  # Холодный голубоватый

    # Манга-стиль: контрастный (для драматических сцен)
    transform thirty_five_grad_manga_dramatic:
        mesh True
        shader "MakeVisualNovels.Manga"
        u_intensity 0.3           # Низкий порог = больше белого, контрастнее
        u_color (1.0, 1.0, 1.0, 1.0)

    transform thirty_five_grad_crt:
        subpixel True
        mesh True
        shader "akumo.crt"
        zoom 1.42
        truecenter
        u_renpy_factor 0.3 u_renpy_scanlines 0.35 u_renpy_border 5.0 u_renpy_bcolor Color("#000").rgb



    transform thirty_five_grad_night_lighting:
        mesh True
        shader "MakeVisualNovels.SimulatedLighting"
        u_rim_light_color (1.0, 1.0, 1.0)  
        u_key_light_color (0.7, 0.7, 0.9)   
        u_fill_light_color (1.0, 1.0, 1.0) # This is typically SUBTRACTED from the sprite since sprites are usually 100% lit.
        # The size of the rim light relative to the size of the graphic you're putting this on.
        u_rim_light_radius (0.5)
        # Positions the effect of the rimlight
        u_rim_light_position (0.5, 0.2)  
        # This will be, on average, pretty close to most sprites' faces
        # assuming they're nearly centered in their images and are about 20% down from the top
        u_key_light_position (0.45, 0.2)  
        u_key_light_radius (0.8)        # This is relative to the thing you're lighting. 0.5 is half the size of the thing.  
        u_fill_light_direction (-1.0, 0.0)   # Direction of the rim light (from the side and behind)
        u_rim_light_intensity (0.2)             # Intensity of the rim light
        u_key_light_intensity (0.5)              # Intensity of the key light
        # This is really a fill shadow, because light works differently on screens.
        u_fill_light_intensity (-0.8)  


    transform thirty_five_grad_night_lighting_lamp:
        mesh True
        shader "MakeVisualNovels.SimulatedLighting"
        u_rim_light_color (1.0, 1.0, 1.0)  
        u_key_light_color (0.7, 0.7, 0.9)   
        u_fill_light_color (1.0, 1.0, 1.0) # This is typically SUBTRACTED from the sprite since sprites are usually 100% lit.
        # The size of the rim light relative to the size of the graphic you're putting this on.
        u_rim_light_radius (0.5)
        # Positions the effect of the rimlight
        u_rim_light_position (0.5, 0.2)  
        # This will be, on average, pretty close to most sprites' faces
        # assuming they're nearly centered in their images and are about 20% down from the top
        u_key_light_position (0.45, 0.2)  
        u_key_light_radius (0.8)        # This is relative to the thing you're lighting. 0.5 is half the size of the thing.  
        u_fill_light_direction (-1.0, 0.0)   # Direction of the rim light (from the side and behind)
        u_rim_light_intensity (0.2)             # Intensity of the rim light
        u_key_light_intensity (0.5)              # Intensity of the key light
        # This is really a fill shadow, because light works differently on screens.
        u_fill_light_intensity (-0.8)  

    # transform thirty_five_grad_sunset_lighting:
    #     mesh True
    #     shader "MakeVisualNovels.SimulatedLighting"
    #     u_rim_light_color (0.9, 0.7, 0.4)  
    #     u_key_light_color (0.9, 0.7, 0.4)
    #     u_fill_light_color (0.4, 0.9, 0.9)  
    #     u_rim_light_radius (0.4)
    #     u_key_light_position (0.1,0.182)
    #     u_rim_light_position (0.1,0.182)
    #     u_key_light_radius (0.6)    
    #     u_fill_light_direction (-1.0, 0.0)  
    #     u_rim_light_intensity (2.0)
    #     u_key_light_intensity (0.8)
    #     u_fill_light_intensity (-0.42)
    #     pause 0
    #     repeat
    
    transform thirty_five_grad_sunset_lighting:
        mesh True
        shader "MakeVisualNovels.SimulatedLighting"
        u_rim_light_color (1.0, 0.784, 0.471)  
        u_key_light_color (1.0, 0.706, 0.4)
        u_fill_light_color (0.4, 0.9, 0.9)  
        u_rim_light_radius (0.4)
        u_key_light_position (0.1,0.182)
        u_rim_light_position (0.1,0.182)
        u_key_light_radius (0.6)    
        u_fill_light_direction (-1.0, 0.0)  
        u_rim_light_intensity (0.2)
        u_key_light_intensity (0.8)
        u_fill_light_intensity (-0.42)
        pause 0
        repeat
    
    transform thirty_five_grad_sunset_lighting_revers:
        mesh True
        shader "MakeVisualNovels.SimulatedLighting"
        u_rim_light_color (0.9, 0.7, 0.4)
        u_key_light_color (0.9, 0.7, 0.4)
        u_fill_light_color (0.4, 0.9, 0.9)
        u_rim_light_radius (0.4)
        u_key_light_position (0.9,0.182)
        u_rim_light_position (0.9,0.182)
        u_key_light_radius (0.6)
        u_fill_light_direction (0.0, -1.0)
        u_rim_light_intensity (0.2)
        u_key_light_intensity (0.8)
        u_fill_light_intensity (-0.42)
        pause 0
        repeat

    transform thirty_five_grad_day_lighting:
        mesh True
        shader "MakeVisualNovels.SimulatedLighting"
        u_rim_light_color (0.8, 0.6, 0.3)
        u_key_light_color (0.9, 0.7, 0.4)
        u_fill_light_color (0.4, 0.9, 0.9)
        u_rim_light_radius (0.4)
        u_key_light_position (0.5,0.182)
        u_rim_light_position (0.5,0.182)
        u_key_light_radius (0.6)
        u_fill_light_direction (-1.0, 0.0)
        u_rim_light_intensity (1.0)
        u_key_light_intensity (0.4)
        u_fill_light_intensity (-0.42)
        pause 0
        repeat


    transform thirty_five_grad_picture_anim:
        subpixel True
        zoom 0.5 rotate -30  xalign -2.1 yalign 0.4 
        on show:
            ease 2 rotate 10 xalign 0.5 yalign 0.5
        on hide:
            ease 2 rotate 40  xalign 3.1 yalign 0.4 

    transform thirty_five_grad_words_anim:
        subpixel True
        xalign -2.1 yalign 0.4
        on show:
            ease 2 xalign 0.5 yalign 0.5
        on hide:
            ease 2 xalign 3.1 yalign 0.4

                
    transform thirty_five_grad_vhs_walk:
        parallel:
            mesh True
            shader "MakeVisualNovels.VHS"
            u_color (1.0, 1.0, 1.0, 1.0)
        parallel:
            zoom 1.05 anchor (48,27)     
            subpixel True
            ease 0.6 pos (0, 0)
            ease 0.6 pos (15,15)
            ease 0.6 pos (0, 0)
            ease 0.6 pos (-15,15)
            repeat

    transform thirty_five_grad_mobile_anim:
        subpixel True
        xanchor 0.0 yanchor 0.0
        xalign 0.5 yalign -1.0 rotate -20 
        on show:
            ease 2.0 xalign 1.0 yalign 0.47 rotate 8
        on hide:
            ease 2.0 xalign 0.5 yalign -1.0 rotate -20 

    transform thirty_five_grad_felt_animation:
        subpixel True
        truecenter
        parallel:
            ease 0.9 zoom 1.5 rotate -15
        parallel:
            ease 1 ypos 0.5
            ease 1 ypos 0.5

    transform running:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat



    transform shake:
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 10
        linear 0.05 xoffset 0
        linear 0.00 xoffset 0

    transform thirty_five_grad_blur:
        blur 0
        linear 1 blur 5

    transform thirty_five_grad_deblur:
        blur 5
        linear 1 blur 0







init -1:

    transform thirty_five_grad_sprite_blur_text_anim:
        xoffset -100 alpha 0.0
        ease 0.5 xoffset 0.0 alpha 1.0


    transform thirty_five_grad_blur_on_anim:
        xoffset -100 alpha 0.0
        pause(0.05)
        ease 0.5 xoffset 0.0 alpha 1.0

    transform thirty_five_grad_blur_off_anim:
        xoffset -100 alpha 0.0
        pause(0.1)
        ease 0.5 xoffset 0.0 alpha 1.0


    transform thirty_five_grad_sprite_blur_next_anim:
        pause(0.15)
        xoffset +100 alpha 0.0
        ease 0.5 xoffset 0.0 alpha 1.0







    
    transform thirty_five_grad_logo_startup_anim_old(y=0.5, x=0.5, xx=0.0):
        subpixel True
        on show:
            xalign x yalign y xoffset xx alpha 0.0
            xalign x yalign y xoffset-600 alpha 0.0
            pause(0.15)
            ease 1.2 xalign x xoffset xx yalign y alpha 1.0
        on hide:
            ease 0.5 alpha 0.0

    
    transform thirty_five_grad_logo_startup_anim:
        subpixel True
        truecenter
        on show:
            alpha 0.0
            pause(0.15)
            ease 1.2 alpha 1.0
        on hide:
            ease 0.5 alpha 0.



    transform thirty_five_grad_text_logo_startup_anim(y=0.24, x=0.9, xx=0.0):
        subpixel True
        on show:
            xalign x yalign y xoffset xx alpha 0.0
            xalign x yalign y xoffset+600 alpha 0.0
            pause(0.15)
            ease 1.2 xalign x xoffset xx yalign y alpha 1.0 
        on hide:
            ease 0.5 alpha 0.0



    transform thirty_five_grad_name_0(y=0.1, x=0.97, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset+500 alpha 0.0
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0


    transform thirty_five_grad_time_bg(y=0.4075, x=1.01, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset+500 alpha 0.0
        pause(0.15)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0


    transform thirty_five_grad_time_1(y=0.36, x=0.9875, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset+500 alpha 0.0
        pause(0.15)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_time_2(y=0.42, x=0.985, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset+500 alpha 0.0
        pause(0.2)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    
    transform thirty_five_grad_time_3(y=0.48, x=0.9825, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset+500 alpha 0.0
        pause(0.25)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0







    transform thirty_five_grad_button_0_menu(y=0.28, x=0.017, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.1)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_1_menu(y=0.4, x=0.02, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.15)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_2_menu(y=0.52, x=0.023, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.2)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_3_menu(y=0.64, x=0.026, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.25)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_4_menu(y=0.76, x=0.032, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.3)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_boosty_menu(y=0.98, x=0.998, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.3)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_telegram_menu(y=0.98, x=0.958, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.3)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_vk_menu(y=0.98, x=0.918, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.3)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_steam_menu(y=0.98, x=0.878, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.3)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0

    transform thirty_five_grad_button_5_menu(y=0.88, x=0.038, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.35)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0


    transform thirty_five_grad_button_5_menu_nolat(y=0.88, x=0.038, xx=0.0):
        subpixel True
        xalign x yalign y xoffset xx alpha 0.0
        xalign x yalign y xoffset-500 alpha 0.0
        pause(0.35)
        ease 0.75 xalign x xoffset xx yalign y alpha 1.0




    transform thirty_five_grad_button_5_back_load_pref_hover(y=0.88, x=0.038, xx=0.0):
        subpixel True
        alpha 0.0 ypos y xpos x yoffset -20 xoffset 5
        on show:
            ease 0.2 alpha 1.0 yoffset 3
        on hide:
            ease 0.2 alpha 0.0 yoffset -20
    





    transform thirty_five_grad_button_0_hover_menu(y=0.28, x=0.017,xx=6, yy=3):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0


    transform thirty_five_grad_button_1_hover_menu(y=0.4, x=0.02, xx=6, yy=3):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        
    transform thirty_five_grad_button_2_hover_menu(y=0.52, x=0.023, xx=7, yy=-1):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        
    transform thirty_five_grad_button_3_hover_menu(y=0.64, x=0.026, xx=6, yy=-2):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0

    transform thirty_five_grad_button_4_hover_menu(y=0.76, x=0.032, xx=6, yy=-4):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0

    transform thirty_five_grad_button_boosty_hover_menu(y=0.98, x=0.998, xx=-6, yy=-5.3):
        subpixel True
        xalign x yalign y xoffset xx yoffset 500 alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset xx yoffset 500 alpha 0.0

    transform thirty_five_grad_button_telegram_hover_menu(y=0.98, x=0.958, xx=-6, yy=-5.3):
        subpixel True
        xalign x yalign y xoffset xx yoffset 500 alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset xx yoffset 500 alpha 0.0

    transform thirty_five_grad_button_vk_hover_menu(y=0.98, x=0.918, xx=-6, yy=-5.3):
        subpixel True
        xalign x yalign y xoffset xx yoffset 500 alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset xx yoffset 500 alpha 0.0

    transform thirty_five_grad_button_steam_hover_menu(y=0.98, x=0.878, xx=-6, yy=-5.3):
        subpixel True
        xalign x yalign y xoffset xx yoffset 500 alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset xx yoffset 500 alpha 0.0

    transform thirty_five_grad_button_5_hover_menu(y=0.88, x=0.038, xx=7, yy=-9):
        subpixel True
        xalign x yalign y xoffset-500 yoffset yy alpha 0.0
        on show:
            ease 0.5 xalign x xoffset xx yoffset yy yalign y alpha 1.0
        on hide:
            ease 0.5 xalign x yalign y xoffset-500 yoffset yy alpha 0.0







    


    transform thirty_five_grad_reverse_button_hover_small_anim_part1:
        subpixel True
        alpha 0.0 ypos 929 xpos 55 yoffset -20 xoffset 6
        on show:
            ease 0.2 alpha 1.0 yoffset 3
        on hide:
            ease 0.2 alpha 0.0 yoffset -20
            

    transform thirty_five_grad_reverse_button_hover_small_anim_part2:
        subpixel True
        alpha 0.0 ypos 958 xpos 55 yoffset 20 xoffset 6
        on show:
            ease 0.2 alpha 1.0 yoffset 4
        on hide:
            ease 0.2 alpha 0.0 yoffset 20

            

    transform thirty_five_grad_skip_button_hover_small_anim_part1:
        subpixel True
        alpha 0.0 ypos 929 xpos 1821 yoffset -20 xoffset 5
        on show:
            ease 0.2 alpha 1.0 yoffset 3
        on hide:
            ease 0.2 alpha 0.0 yoffset -20

            
    transform thirty_five_grad_skip_button_hover_small_anim_part2:
        subpixel True
        alpha 0.0 ypos 958 xpos 1821 yoffset 20 xoffset 5
        on show:
            ease 0.2 alpha 1.0 yoffset 4
        on hide:
            ease 0.2 alpha 0.0 yoffset 20

        


    transform thirty_five_grad_save_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 158 xoffset 6 yoffset 20
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    transform thirty_five_grad_save_button_hover_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 158 xoffset 6 yoffset -19
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0
        

    transform thirty_five_grad_load_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 535 yoffset 20 xoffset 6
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    transform thirty_five_grad_load_button_hover_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 535 yoffset -19 xoffset 6
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0

    
    transform thirty_five_grad_preferences_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 ypos 1048 xpos 1285 yoffset 20 xoffset 6
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    transform thirty_five_grad_preferences_button_hover_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 1285 xoffset 6 yoffset -19
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0


    transform thirty_five_grad_hide_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 910 yoffset 20 xoffset 6
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    transform thirty_five_grad_hide_button_hover_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 910 xoffset 6 yoffset -19
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0

    
    transform thirty_five_grad_qm_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 1660 yoffset 20 xoffset 6
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    transform thirty_five_grad_qm_button_hover_anim:
        subpixel True
        alpha 0.0 ypos 1047 xpos 1660 xoffset 6 yoffset -19
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0






    transform thirty_five_grad_reverse_button_hover_large_anim_part1:
        subpixel True
        alpha 0.0 ypos 923 xpos 55 yoffset -20 xoffset 6
        on show:
            ease 0.2 alpha 1.0 yoffset 3
        on hide:
            ease 0.2 alpha 0.0 yoffset -20
            

    transform thirty_five_grad_reverse_button_hover_large_anim_part2:
        subpixel True
        alpha 0.0 ypos 952 xpos 55 yoffset 20 xoffset 6
        on show:
            ease 0.2 alpha 1.0 yoffset 4
        on hide:
            ease 0.2 alpha 0.0 yoffset 20



            
    transform thirty_five_grad_skip_button_hover_large_anim_part1:
        subpixel True
        alpha 0.0 ypos 923 xpos 1821 yoffset -20 xoffset 5
        on show:
            ease 0.2 alpha 1.0 yoffset 3
        on hide:
            ease 0.2 alpha 0.0 yoffset -20

    transform thirty_five_grad_skip_button_hover_large_anim_part2:
        subpixel True
        alpha 0.0 ypos 952 xpos 1821 yoffset 20 xoffset 5
        on show:
            ease 0.2 alpha 1.0 yoffset 4
        on hide:
            ease 0.2 alpha 0.0 yoffset 20




    transform screen_thirty_five_grad_hint_anim:
        on show:
            ease 0.15 alpha 1.0 yoffset 14
        on hide:
            ease 0.15 alpha 0.0 yoffset 30

    transform screen_thirty_five_grad_hide_hint_button_anim:
        subpixel True
        yalign 0.97 xalign 0.017 alpha 0.0
        on show:
            ease 1.0 alpha 0.3
            pause 1.5
            ease 1.0 alpha 0.05
            repeat
        on hide:
            ease 0.15 alpha 0.0

    transform thirty_five_grad_clearly_button_hover_anim:
        subpixel True
        alpha 0.0 yalign 0.6 xalign 0.5
        on show:
            ease 0.15 alpha 1.0
        on hide:
            ease 0.15 alpha 0.0

    transform thirty_five_grad_clearly_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 yalign 0.62 xalign 0.5
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20


    transform thirty_five_grad_continue_button_fuckingstick_anim:
        subpixel True
        alpha 0.0 yalign 0.615 xalign 0.5
        on show:
            ease 0.15 alpha 1.0 yoffset 4
        on hide:
            ease 0.15 alpha 0.0 yoffset 20

    
    transform thirty_five_grad_show_textbox_button_hover_anim:
        subpixel True
        alpha 0.0 yalign 0.97 xalign 0.017 
        on show:
            ease 0.3 alpha 0.5
        on hide:
            ease 0.3 alpha 0.0

    transform thirty_five_grad_bg_zoom_nvl_text_history(z=0.92, x=0.5,  y=0.5, a=1.0):
        zoom z xalign x yalign y alpha a


    transform  thirty_five_grad_skip_anim(y=0.05, x=0.05, xx=0.0):
        xalign x yalign y xoffset xx alpha 0.0
        on show:
            xalign x yalign y xoffset-100 alpha 0.0
            ease 0.25 xalign x xoffset xx yalign y alpha 1.0
        on hide:
            ease 0.25 xalign x yalign y xoffset-100 alpha 0.0



    transform thirty_five_grad_notify_anim(y=0.05, x=0.95, xx=0.0):
        xalign x yalign y xoffset xx alpha 0.0
        on show:
            xalign x yalign y xoffset+100 alpha 0.0
            ease 0.25 xalign x xoffset xx yalign y alpha 1.0
        on hide:
            ease 0.25 xalign x yalign y xoffset+100 alpha 0.0


    transform thirty_five_grad_exit_text_anim:
        xoffset -100 alpha 0.0
        ease 0.5 xoffset 0.0 alpha 1.0

    transform thirty_five_grad_exit_yes_anim:
        xoffset -100 alpha 0.0
        pause(0.05)
        ease 0.5 xoffset 0.0 alpha 1.0

    transform thirty_five_grad_exit_no_anim:
        xoffset -100 alpha 0.0
        pause(0.1)
        ease 0.5 xoffset 0.0 alpha 1.0

