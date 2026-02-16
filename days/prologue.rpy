# label thirty_five_grad_prologue:
#     $ _game_menu_screen = 'game_menu_selector'
#     scene bg thirty_five_grad_prolog_glitch_epil
#     stop music
#     stop sound_loop
#     stop ambience
#     stop sound
# #     play sound thirty_five_grad_glitch_transition_1
# #     $ renpy.pause(1.0, hard=True)
# #     show thirty_five_grad_transition_prolog_words at thirty_five_grad_words_anim
# #     $ renpy.pause(4.0, hard=True)
# #     stop music fadeout 1
#     $ renpy.movie_cutscene("video/prologue.webm")
#     $ persistent.sprite_time = 'day'
#     scene bg black with dissolve
#     $ renpy.pause(1, hard=True)
#     play music thirty_five_grad_the_city_in_the_sky fadein 3.0
#     python:
#         config.hard_rollback_limit = 0
#         config.rollback_enabled = False
#         thirty_five_grad_unlock_cg('cg_transition_prolog')
#     $ renpy.display_notify('Сейчас играет:\nNatus – City In The Sky')
#     $ set_mode_nvl()
#     nvl show dissolve
#     $ _skipping = True
#     '' # я знаю про \n и что можно изменить точку начала текста по оси y, но мне как то пофек
#     python:
#         config.hard_rollback_limit = 1000
#         config.rollback_enabled = True
#         _game_menu_screen = 'game_menu_selector'
#         save_name = ('35°. Пролог')

label thirty_five_grad_prologue:
    scene bg black with dissolve
    stop music fadeout 0.5
    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    stop sound fadeout 0.5
    $ renpy.pause(1.2, hard=True)
    $ renpy.display.screen.screens[("main_menu", None)] = renpy.display.screen.screens[("thirty_five_grad_main_menu", None)] 
    $ _game_menu_screen = 'game_menu_selector'
    scene bg thirty_five_grad_prolog_glitch_epil
    play sound thirty_five_grad_glitch_transition_1
    $ renpy.pause(1.0, hard=True)
    show thirty_five_grad_transition_prolog_words at thirty_five_grad_words_anim
    $ renpy.pause(4.0, hard=True)
    $ persistent.sprite_time = 'day'
    stop music fadeout 1
    scene bg black with dissolve
    $ renpy.pause(1, hard=True)
    play music  thirty_five_grad_the_city_in_the_sky fadein 3.0
    python:
        config.hard_rollback_limit = 0
        config.rollback_enabled = False
    $ renpy.display_notify('Сейчас играет:\nNatus – City In The Sky')
    $ set_mode_nvl()
    nvl show dissolve
    $ _skipping = True
    '' # я знаю про \n и что можно изменить точку начала текста по оси y, но мне как то пофек
    python:
        config.hard_rollback_limit = 1000
        config.rollback_enabled = True
        _game_menu_screen = 'game_menu_selector'
        save_name = ('35°. Пролог')
    'Мне нравится моя жизнь. Со всеми благами и недостатками. Проблемами и взлётами. В целом, мне нравится жить - как бы странно это ни звучало.'
    'Родители, к счастью, живы и здоровы. {w}А вот друзей, к сожалению, я так и не нашёл.'
    nvl hide dissolve
    nvl clear
    $ renpy.pause(0.1, hard=True)
    nvl show dissolve
    '{nw}'
    'Недавно мне исполнилось 23 года. Сейчас возвращаюсь в съёмный дом, что в пригородной зоне, после тяжёлого учебного дня в одном небольшом провинциальном ВУЗе города К.'
    'Да, у меня были знакомые в ВУЗе, с которыми можно было перекинуться парой слов. Но назвать их "друзьями" - язык не поворачивается.'
    nvl hide dissolve
    nvl clear
    $ renpy.pause(0.1, hard=True)
    nvl show dissolve
    '{nw}'
    'А ещё больше всего на свете я люблю музыку. Любую - вне зависимости от жанра и эпохи. Главное - чтобы трогала душу.'
    'Хотя есть особый тип мелодий, которые будто спицами для вязания вшиваются прямо в сердце. Это - гитарная музыка.'
    'Я и сам пытался раньше играть хоть на чём-то, но толком ничего не вышло. Зато я нашёл дело, в котором хоть немного, но получается - ремонт техники.'
    'Я не мастер, а так, радиолюбитель. Но копеечку заработать всё же удаётся.'
    nvl hide dissolve
    nvl clear
    $ renpy.pause(0.1, hard=True)
    nvl show dissolve
    '{nw}'
    play sound thirty_five_grad_low_battery_headphones
    'Наушники жалобно сообщили о разряженном аккумуляторе.'
    '{nw}'
    th "И так до остановки почти доковылял, доживу без наушников."
    nvl hide dissolve
    nvl clear
    $ renpy.pause(0.1, hard=True)
    nvl show dissolve
    '{nw}'
    'Хоть на дворе и март, но в семь вечера на юге страны уже давно темно.'
    'Изредка по трассе проезжают машины - и те исчезают за горизонтом быстрее, чем я успеваю моргнуть.'
    nvl hide dissolve
    nvl clear
    play ambience ambience_camp_center_night fadein 3
    scene cg video_prolog with dissolve
    # $ renpy.pause(5.0, hard=True)
    # scene cg thirty_five_grad_alex_bus_station with fade
    $ renpy.pause(0.5, hard=True)
    nvl show dissolve
    '{nw}'
    'Вот и дошёл я до остановки.'
    'Местные вандалы её явно не пощадили, но она всё ещё стоит. Не жалуется. Мне бы у неё поучиться... Но есть у меня одна фобия.{w=0.2}.{w=0.2}.{w=0.2}'
    '{nw}'
    '.{w=0.2}.{w=0.2}.{w=0.2}Одиночество. {w}То, чего я боюсь до дрожи.'
    'Нет, это не про то, когда вокруг никого. И не про добровольное уединение. Вовсе нет.'
    '{nw}'
    '.{w=0.2}.{w=0.2}.{w=0.2}Это когда никто не придёт на помощь.'
    nvl hide dissolve
    nvl clear
    $ renpy.pause(1.2, hard=True)
    nvl show dissolve
    '{nw}'
    'Я уселся на лавку, снял рюкзак с плеч и поставил его рядом.'
    '{nw}'
    th 'Так, проверю-ка инвентарь. Мало ли что забыл:'
    th 'Пауэрбанк{w=0.4}- заряжен{nw}'
    th 'Вода - {w=0.3}на месте.{nw}'
    th 'Пара протеиновых и шоколадных батончиков - {w=0.5}тоже здесь.{nw}'
    th 'Набор инструментов – {w=0.2}на месте.{nw}'
    th "Набор 'Подлатай порез' - пластыри, йод, перекись{w=0.23} - всё на месте."
    nvl hide dissolve
    $ renpy.pause(1.3, hard=True)
    $ set_mode_adv()
    window show
    'Есть одна история из детства, что последнее время не даёт мне покоя.'
    play sound thirty_five_grad_glitch_transition_1
    show bg thirty_five_grad_eyes_forest_glitch_epil
    pause 0.246
    hide bg thirty_five_grad_eyes_forest_glitch_epil
    'Стоит вспомнить те жёлтые глаза - и бросает в дрожь.'
    'Но я забежал вперёд.'
    window hide
    stop ambience fadeout 3
    scene cg video_prolog at thirty_five_grad_blur with fade
    # scene cg thirty_five_grad_alex_bus_station blured with dissolve
    show thirty_five_grad_photo_1 at thirty_five_grad_picture_anim
    python:
        thirty_five_grad_unlock_cg('photo_1_nor')
    window show
    'Всё началось в детстве, когда мы с родителями жили в городе Д.'
    'От дома до леса было рукой подать. Он был небольшой, казалось - за десять минут можно пройти насквозь. Но родители всё равно запрещали мне туда ходить.'
    'Как оказалось - не зря.'
    'В один из, вроде бы, последних дней недели мать пошла со мной на прогулку. Было тепло, но мы оба были в лёгких куртках.'
    'Гуляли у самого леса, не заходя в него. Но вдруг что-то привлекло моё внимание, и я шагнул в лес.'
    window hide
    hide thirty_five_grad_photo_1
    $ renpy.pause(0.1, hard=True)
    play ambience ambience_forest_night fadein 3
    scene bg thirty_five_grad_ext_path night at thirty_five_grad_vhs_walk
    with dissolve
    window show
    'Не углублялся, просто перешагнул через корягу - и в ту же секунду почувствовал, как бросает в пот, стало не по себе.'
    window hide
    scene bg thirty_five_grad_ext_path2 night at thirty_five_grad_vhs
    with dissolve
    window show
    'А страшно стало чуть позже, когда обернулся - а матери уже не было видно.'
    window hide
    scene bg thirty_five_grad_ext_path night at thirty_five_grad_vhs_walk
    with dissolve
    window show
    'Обычно ребёнок бы запаниковал{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} Но я почему-то нет. Я начал звать её и двигаться вперёд. А дальше - пустота.'
    window hide
    scene bg thirty_five_grad_eyes_forest at thirty_five_grad_vhs
    with dissolve
    window show
    'Не помню ничего. Только те глаза. Жёлтые. Прожигающие насквозь.'
    'Но что странно - угрозы в них не было.'
    window hide
    scene bg black with dissolve2
    stop ambience fadeout 3
    $ renpy.pause(0.3, hard=True)
    window show
    'Наоборот. Было в них что-то{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} благостное. Успокаивающее.'
    'А что было потом - не помню.'
    'Помню лишь заплаканное лицо мамы, когда меня нашли местные охотники.'
    'Оказалось, я пропал почти на сутки.'
    'С тех пор лесов боюсь как огня. Стоит только увидеть хоть что-то, напоминающее лес, и меня сразу передёргивает.'
    window hide
    play ambience ambience_camp_center_night fadein 3
    scene bg thirty_five_grad_road night with dissolve2
    $ renpy.pause(1.2, hard=True)
    window show
    'Встав, я прислонился к стеклу остановки - после долгого дня за столом затекли ноги - и начал всматриваться в дорогу.'
    window hide
    $ renpy.pause(2.0, hard=True)
    window show
    '.{w=0.2}.{w=0.2}.{w=0.2}Машины проезжали одна за другой, но автобус так и не появлялся.'
    window hide
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_road night blured with dissolve
    show thirty_five_grad_mobile prologue at thirty_five_grad_mobile_anim
    $ renpy.pause(1.6, hard=True)
    window show
    th '65 процентов, надолго хватит.'
    window hide
    hide thirty_five_grad_mobile day1 morning
    $ renpy.pause(1.3, hard=True)
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_road night with dissolve
    $ renpy.pause(2.5, hard=True)
    window show
    th 'Наушники еще минут 20 подзаряжаться будут{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}'
    th 'Может, такси вызвать?{w=0.2}.{w=0.2}.'
    window hide
    $ renpy.pause(2.5, hard=True)
    window show
    show thirty_five_grad_vignette with dissolve
    'Всю дорогу до остановки я чувствовал, будто кто-то следит за мной.'
    'А сейчас казалось, что этот кто-то подошёл совсем близко.'
    window hide
    $ renpy.pause(2.5, hard=True)
    $ volume(0.1, 'sound')
    play sound sfx_hiding_in_bush
    window show
    stop music fadeout 4
    'В один момент я услышал шуршание в кустах близ меня.'
    'Я попытался отойти от остановки - но ноги не слушаются. Словно парализовало.'
    'Повернуть голову тоже не смог - шею будто заклинило.'
    window hide
    hide thirty_five_grad_vignette with dissolve_fast
    show thirty_five_grad_low_hp with dissolve2
    $ volume(1.5, 'sound')
    play sound_loop thirty_five_grad_head_heartbeat fadein 4
    $ renpy.pause(4, hard=True)
    window show
    'В глазах темнеет. Пульс зашкаливает. А причины - не понимаю.'
    window hide
    stop sound_loop fadeout 3
    stop ambience fadeout 3
    stop sound fadeout 3
    stop music fadeout 3
    hide thirty_five_grad_low_hp with dissolve_fast
    $ volume(0.3, 'sound')
    play sound thirty_five_grad_fall_grass
    scene bg thirty_five_grad_road night at thirty_five_grad_felt_animation
    show blink
    $ renpy.pause(1.2, hard=True)
    scene bg black at thirty_five_grad_vhs
    with dissolve
    window show
    'И вдруг{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} всё исчезает. Одним движением - покой. Пустота.'
    'Я ничего не вижу. Но здесь что-то тёплое.{w=0.2} Приятное.{w=0.2} Домашнее.{w=0.2} Беззаботное.'
    'Поддавшись этим чувствам, я окончательно отключился.'
    window hide
    $ persistent.prologue = True
    jump thirty_five_grad_day_one
    # python:
    #     config.skipping = False
    #     _skipping = False
    #     config.hard_rollback_limit = 0
    #     config.rollback_enabled = False
    #     save_name = ('re:35°')
    #     _game_menu_screen = None
    # play music  thirty_five_grad_mm_music fadein 5
    # call screen thirty_five_grad_main_menu with fade
