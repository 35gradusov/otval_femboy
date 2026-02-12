# label thirty_five_grad_day_one:
#     $ save_name = ('35°. День 1')
#     play sound thirty_five_grad_glitch_transition_1
#     scene bg thirty_five_grad_day1_glitch_epil
#     $ renpy.pause(1.0, hard=True)
#     show thirty_five_grad_transition_day_1_words at thirty_five_grad_words_anim
#     $ renpy.pause(4.0, hard=True)
#     play ambience ambience_camp_center_day fadein 6
#     play music thirty_five_grad_to_a_dark_lady fadein 3.0
#     python:
#         config.hard_rollback_limit = 0
#         config.rollback_enabled = False
#         thirty_five_grad_unlock_cg('cg_transition_day_1')
#     scene bg black with fade
#     $ renpy.display_notify('Сейчас играет:\nGraham Todd – To a dark lady')
#     window show
#     'Тёплый и насыщенный ветерок обдувает моё лицо и шею, отчего я постепенно отхожу ото сна, при этом не имея никакого желания просыпаться.'
#     window hide
#     python:
#         config.rollback_enabled = True
#         config.hard_rollback_limit = 1000
#     $ renpy.pause(2.3, hard=True)


label thirty_five_grad_day_one:
    $ save_name = ('35°. День 1')
    play sound thirty_five_grad_glitch_transition_1
    scene bg thirty_five_grad_day1_glitch_epil
    $ renpy.pause(1.0, hard=True)
    show thirty_five_grad_transition_day_1_words at thirty_five_grad_words_anim
    $ renpy.pause(4.0, hard=True)
    play ambience ambience_camp_center_day fadein 6
    $ persistent.sprite_time = 'day'
    play music thirty_five_grad_to_a_dark_lady fadein 3.0
    python:
        config.hard_rollback_limit = 0
        config.rollback_enabled = False
    scene bg black with fade
    $ renpy.display_notify('Сейчас играет:\nGraham Todd – To a dark lady')
    window show
    'Тёплый и насыщенный ветерок обдувает моё лицо и шею, отчего я постепенно отхожу ото сна, при этом не имея никакого желания просыпаться.'
    window hide
    python:
        config.rollback_enabled = True
        config.hard_rollback_limit = 1000
    $ renpy.pause(2.3, hard=True)
    window show
    'Мысли окончательно выводят меня из полусна.'
    window hide
    scene bg thirty_five_grad_ext_sky2_pizdec_anim sunset
    show thirty_five_grad_vignette
    show unblink
    $ renpy.pause(1.5, hard=True)
    window show
    thirty_five_grad_alex 'Ах-х-х.{w=0.3}.{w=0.3}.{w=0.6} Глаза{w=0.3}.{w=0.3}.{w=0.3}.'
    window hide
    $ renpy.pause(4.7, hard=True)
    window show
    th 'Ещё и голова раскалывается{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}'
    window hide
    $ renpy.pause(3, hard=True)
    window show
    th 'Всё то, что я могу вспомнить, это то, как я потерял сознание у остановки{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}'
    window hide
    $ renpy.pause(2.8, hard=True)
    window show
    th 'Но сейчас, где я?{w=0.3}.{w=0.3}.{w=0.3}.'
    window hide
    $ renpy.pause(2.4, hard=True)
    scene bg thirty_five_grad_ext_no_bus sunset
    with dissolve2
    window show
    'Встав, я решил осмотреться.'
    window hide
    $ renpy.pause(2.4, hard=True)
    window show
    'Сделав глубокий вдох, лёгкие будто впервые вдохнули: воздух чистый, свежий. А ещё немного солоноватый, будто рядом озеро или речка.'
    window hide
    scene bg thirty_five_grad_ext_no_bus sunset:
        ease 0.8 xalign 0.4 yalign 0.43
        ease 0.8 zoom 1.5
        pause 0.2
        ease 0.8 zoom 1.6 xalign 0.99 yalign 0.65
        pause 0.3
        ease 0.9 zoom 1.0
    window show
    th 'Какого{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} Чёрта?'
    window hide
    $ renpy.pause(1.4, hard=True)
    window show
    thirty_five_grad_alex 'Блять{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} Где я?'
    scene bg thirty_five_grad_ext_no_bus sunset:
        ease 0.6 xalign 0.3 yalign 0.65
        ease 0.6 zoom 1.4
    window hide dissolve
    $ renpy.pause(0.61)
    scene bg thirty_five_grad_ext_road sunset with dspr:
        zoom 1.8 xalign 0.3 yalign 0.65
        ease 0.6 zoom 1.0
    $ renpy.pause(0.61, hard=True)
    scene bg thirty_five_grad_ext_road sunset:
        pause 0.45
        ease 0.8 xalign 0.44 yalign 0.6
        ease 0.8 zoom 1.5
        pause 0.2
        ease 0.8 zoom 1.72 xalign 0.01 yalign 0.53
        pause 0.2
        ease 0.8 yalign 0.1
        pause 0.15
        ease 0.8 zoom 1.0
    window show
    'Окружающее меня пространство вовсе отличалось от запомнившегося мной: вместо леса – поляна, ещё и откуда-то взявшиеся линии электропередач.'
    window hide
    $ renpy.pause(2.0, hard=True)
    window show
    'Немного осмотревшись, я понял, что боль в голове почти прошла.'
    window hide
    $ renpy.pause(1.8, hard=True)
    window show
    th 'Сейчас сварюсь к чёрту{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} Сниму-ка куртку{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}'
    window hide
    play sound thirty_five_grad_unclothe1 fadein 1
    $ renpy.pause(1.232, hard=True) # 'renpy.music.get_duration(channel='sound')' для измерения длинны звука в консоли
    window show
    'Сняв куртку, я остался в чёрной футболке.'
    window hide
    $ renpy.pause(0.8, hard=True)
    window show

    #(по возможности сделать кинематографическую камеру. Это когда камера медленно по горизонту плывёт)
    # сделал бля

    th 'Неужели тут и цивилизация недалеко, раз ЛЭП поставили?'
    th 'Может, где-то поблизости смогут помочь до дома добраться?'
    window hide
    $ renpy.pause(0.4, hard=True)

    #(гг достаёт мобилу)
    #(музыка стоп)
    #ид нах
    stop music fadeout 2.0
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_ext_road sunset blured with dissolve
    show thirty_five_grad_mobile day1 morning at thirty_five_grad_mobile_anim
    window show
    $ renpy.pause(1.3, hard=True)
    "Я достал телефон из кармана: на часах было шесть утра."
    play music thirty_five_grad_Ihokkaido_leaves fadein 3.0
    #python:
        #config.hard_rollback_limit = 0
        #config.rollback_enabled = False
    $ renpy.display_notify('Сейчас играет:\nTo Life - Hokkaido Leaves')
    #(музыка) To Life – Hokkaido Leaves
    thirty_five_grad_alex 'Чё?{w=0.1}.{w=0.1}.{w=0.1}'
    thirty_five_grad_alex 'Какое ещё 15 августа?{w=0.1}.{w=0.1}.{w=0.1}'
    thirty_five_grad_alex 'Опять дата сбилась?{w=0.1}.{w=0.1}.{w=0.1}'
    window hide
    show thirty_five_grad_mobile day1 morning:
        subpixel True
        ease 0.9 yalign -0.07 rotate -7
        pause 0.1
        ease 0.2 zoom 0.985 yalign -0.1 xalign 1.06 rotate -6
        pause 0.1
        ease 0.2 zoom 1.0 yalign -0.07 xalign 1.0 rotate -7
    $ renpy.pause(1.21, hard=True)
    show thirty_five_grad_mobile day1_notifications morning
    with Dissolve(0.1)
    window show
    thirty_five_grad_alex 'Ещё и мама звонила{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}'
    window hide
    $ renpy.pause(0.1, hard=True)
    show thirty_five_grad_mobile day1_notifications morning:
        subpixel True
        ease 0.2 zoom 0.97 yalign -0.085 xalign 1.1
        pause 0.1
        ease 0.2 zoom 1.0 yalign -0.07 xalign 1.0
    show thirty_five_grad_mobile day1_dialer morning:
        ease 0.9 xalign 1.0 yalign 0.4 rotate 8
    with Dissolve(0.1)
    $ renpy.pause(1.15, hard=True)
    show thirty_five_grad_mobile day1_dialer morning:
        subpixel True
        ease 0.9 yalign -0.13 rotate -7.5
        pause 0.1
        ease 0.2 zoom 0.99 yalign -0.147 xalign 1.05
        pause 0.1
        ease 0.2 zoom 1.0 yalign -0.13 xalign 1.0
    with Dissolve(0.1)
    $ renpy.pause(1.51, hard=True)
    show thirty_five_grad_mobile day1_call morning:
        subpixel True
        ease 0.9 xalign 1.06 yalign 0.42 rotate 8.1
    $ renpy.pause(1.2, hard=True)
    window show
    thirty_five_grad_alex 'Сука{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1}'
    window hide
    show thirty_five_grad_mobile day1_call morning:
        ease 2.0 xalign 0.5 yalign -1.0 rotate -20
    $ renpy.pause(1.3, hard=True)
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_ext_road sunset with dissolve

    #бля как я вообще это все сука строчил
    #еще и работает бля каким то хуем

    window show
    th 'И что мне делать?{w=0.1}.{w=0.1}.{w=0.1}'
    scene bg thirty_five_grad_ext_road sunset:
        ease 0.6 xalign 0.9 yalign 0.6
        ease 0.6 zoom 1.4
    window hide dissolve
    $ renpy.pause(0.58)
    scene bg thirty_five_grad_ext_camp_entrance sunset with dspr:
        zoom 1.8 xalign 0.85 yalign 0.6
        ease 0.6 zoom 1.0
    $ renpy.pause(0.95)
    window show
    th 'Это ещё что?'
    stop music fadeout 2.0
    # "Перед моим взором красовались две статуи пионеров – первая пытается зигу кинуть, второй хуярит певко и ворота с надписью 'Совёнок'."
    # "У паренька так же был{w=0.3}.{w=0.3}.{w=0.3}. {w=0.3}Кхм{w=0.3}.{w=0.3}.{w=0.3}. {w=0.3}Стояк{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
    # почему Леха не разрешил это оставить ?((

    "Перед моим взором красовались ворота с надписями «Совёнок» и «пионер лагерь»; забор, построенный из кирпичей, а также две статуи пионеров – девушка и парень возрастом где-то 7-8 лет. Девушка тянула руку к небу, а паренёк{w=0.1}.{w=0.1}.{w=0.1}. {w=0.1}Пил что-то из бутылки."
    #ПАСХАЛКО 7-8 ПАСХАЛКО БЛЯЯЯТЬ ПАСХАЛКООООООО

    # '(музыка стоп)'
    # '(музыка) ichiko aoba – dawn in the adan (instrumental)'
    #да ты заебал каждые 10 строк текста музло менять бля
    #после немногочисленных споров с автором я могу выбирать музло))

    play music thirty_five_grad_Iframe_dawn_in_the_adan fadein 3.0
    $ renpy.display_notify('Сейчас играет:\nichiko aoba – dawn in the adan (instrumental)')
    #python:
        #config.hard_rollback_limit = 0
        #config.rollback_enabled = False
    $ renpy.display_notify('Сейчас играет: Ichiko Aoba – Dawn in the adan')

    th 'Так, нахожусь неизвестно где ~{w=0.35345}\n~ связи – нет; ~{w=0.2324}\n~ оффлайн-карты я не скачивал.'
    thirty_five_grad_alex 'Осталось надеяться, что в этом{w=0.1}.{w=0.1}.{w=0.1}. {w=0.1}Кхм{w=0.1}.{w=0.1}.{w=0.1}. {w=0.1}Пионер-лагере мне смогут помочь до дома добраться хотя бы.'
    window hide
    $ renpy.pause(1.67845, hard=True)
    show blink
    window show
    'Решив размять шею, перед тем как заходить в лагерь, я закрыл глаза.'
    window hide

    'Но вдруг послышался довольно тихий девичий голос.'
    # '(музыка стоп)'
    # '(спрайт Слави в спортивной форме, улыбается)'


    stop music fadeout 2.0

    $ renpy.pause(1.5, hard=True)
    window show
    if persistent.font_size == u'small':
        thirty_five_grad_sl_unk 'Решил разминочку устроить?'
    elif persistent.font_size == u'large':
        thirty_five_grad_sl_unk_larger 'Решил разминочку устроить?'
    $ renpy.pause(0.27489, hard=True)
    show unblink
    scene bg thirty_five_grad_ext_camp_entrance sunset with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_ext_camp_entrance sunset blured with dissolve_fast
    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting with dspr:
        xanchor 0.5 xalign 0.5

    # на этом моменте OTVaL (кодер (я)) уходит из разработки по личным обстоятельствам
    # вернусь ли я - неизвестно, если хотите связаться со мной:
    # discord:          @otv_l
    # tg:               https://t.me/otv_l
    # vk:               https://vk.com/otv_l
    # steam:            https://steamcommunity.com/profiles/76561199194787637/
    #
    # p.s. и да, я не добавлял музло во многих местах


    # Гы отвал отвалился

    thirty_five_grad_sl_unk_larger 'А? Ой, прости, я не хотела тебя пугать!'
    window hide
    # '(музыка) Sergey Eybog Timid Girl'
    play music music_list["timid_girl"]
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Timid Girl')
    window show
    'Аккуратным движением руки она взяла одну из своих косичек, после чего виновато посмотрела на меня.'
    th 'И только сейчас я заметил, что она была в обтягивающей чёрной форме. Которая, тем не менее, отлично подчёркивала все её, скажем так, природные таланты. '
    'Причём, прости господи, не малые.'
    thirty_five_grad_alex 'Эм, нет. Не напугала. Прости за суматоху, но я просто не знаю, где нахожусь.'
    th 'Всё же каким-то чудом взял себя в руки и, как можно спокойнее, ответил ей. Как бы мне сейчас не было некомфортно, я не хочу показаться странным или же ненормальным.'
    # '(Славя, удивлённая)'
    show 35grad_slavya 2 surprised sport with dspr

    thirty_five_grad_sl_unk_larger 'А? Как это, не знаешь? Тебе разве родители не говорили, куда ты едешь?'
    th 'Почему она говорит так, словно всё нормально? Хотя, чёрт возьми, это сейчас не особо важно.  '
    th 'Пока не буду сообщать ей о похищении, а то мало ли, вдруг она сейчас одна из похитителей? Нельзя давать ей повода для агрессии.'
    thirty_five_grad_alex '{w=0.1}.{w=0.1}.{w=0.1}.Нет.'

    # '(Славя, обычная)'
    show 35grad_slavya 2 normal sport with dspr
    #замена спрайта Слави при первой возможности!!!

    thirty_five_grad_sl 'Понятно. Тогда, меня зовут Славяна. Помощница вожатой, неформально – правая рука. Рада знакомству! А находимся мы в пионерлагере «Совёнок». '
    thirty_five_grad_sl 'Место очень хорошее, не первый год сюда езжу, так что думаю, тебе и тут тоже понравится.'
    th 'Так мало того, что они тут в пионеров играют, так ещё не первый год. Может, это всё дурной сон?{w} Вдохнув ранний утренний воздух, представился уже я:'
    thirty_five_grad_alex 'Я Алексей.{w} Приятно познакомиться.'
    'Мы пожали друг другу руки. Её тёплая и мягкая ладонь была меньше моей, но такой нежной и всё равно при этом сильной. А затем оба покраснели.'

    # '(Славя, покраснела)'
    show 35grad_slavya 2 shy sport with dspr

    thirty_five_grad_sl'И... мне. Кстати, не редкое имя. Например, у меня так младшего братика зовут, несносный парнишка, но добрый.'
    thirty_five_grad_alex 'Понятно. Но, а где твоя форма? Почему ты...'
    'Снова тихо рассмеялась, а потом спокойно произнесла:'

    # '(Славя, обычная)'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'На самом деле, я просто зарядку делала. Это полезно же ведь. А ты сам как? И вообще, давно приехал? Не ожидала, что автобус так рано приедет сегодня.'
    thirty_five_grad_alex 'Да так, время от времени делаю...'
    'Оглянувшись назад, словно остановка могла сбежать, я повернулся к этой девушке и заметил, что она непринуждённо, но с интересом смотрела на мою куртку.'
    # '(Славя, удивлённая)'
    show 35grad_slavya 3 surprised sport with dissolve

    thirty_five_grad_sl 'О, ты тоже с севера?'
    thirty_five_grad_alex 'А? Да, да. Можно и так сказать.'
    th 'Я произнёс то, что первым пришло в голову. Не знаю, что мне говорить в такой ситуации, поэтому буду делать всё по интуиции. Только бы не получилось хуже...'
    # '(Славя, заинтригованная)'
    show 35grad_slavya 2 smile sport with dissolve

    thirty_five_grad_sl 'Поняла. Я спрашиваю так, потому что тоже с севера, а именно с Заполярного.{w} Чудесный городок, но с экологией не очень. А ты?'
    th 'Откуда я? Вообще-то с юга. Но чёрт, сказал ведь, что с севера... Надеюсь то, что сейчас отвечу, мне потом не аукнется.'
    thirty_five_grad_alex 'Я тоже с него.{w} Точнее, с Мурманска, вот.{w} Год назад с родителями переехали.{w} По работе.'
    th 'Не люблю я врать, а точнее, ненавижу. Самое гнусное, что есть в этом мире, так это ложь и убийства. Но, к сожалению, без первого иногда никак по-другому.'
    # '(Славя, обычная)'
    show 35grad_slavya 2 normal sport with dspr

    thirty_five_grad_sl 'О, как здорово! Ладно, заболтались что-то. Прости, конечно, что я встретила тебя не по форме, но всё же хочешь, я провожу тебя до вожатой?'
    thirty_five_grad_sl 'Или можешь сам пройтись, я тебе дорогу укажу. Мне без разницы, что ты выберешь, ибо тут не так уж далеко идти. '
    th 'С учётом того, что это незнакомая для меня территория, и то, что по дороге со мной может быть всё что угодно...'
    th 'Зато я смогу обследовать этот лагерь тщательнее. А могу пойти и с ней, вдруг получится выудить что-то ещё интересное? Трудный выбор.'
    th 'Ладно, я ничего не потеряю, если пойду с ней. Тем более, может с ней получиться поговорить, и...{w} Ладно, она очень красивая, не стоит этого отрицать.'
    th 'У меня, в принципе, был уже опыт общения, но не шибко большой.{w} Чёрт, почему я сейчас вообще об этом думаю?'

    stop music fadeout 2.0
    # '(музыка стоп)'

    thirty_five_grad_alex 'Ладушки, не против, если я пойду с тобой? Всё же, я впервые здесь, и помощь мне вряд ли помешает.'

    play music thirty_five_grad_summer_day fadein 3.0
    $ renpy.display_notify('Сейчас играет:\nSummer Day – Jinsang')

    th 'Честно, я пытался быть дружелюбным. Надеюсь, что со стороны я не выгляжу как клоун. {w}Но Славя наоборот, только нежно улыбнулась мне и кивнула головой.'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'Мудрый выбор. Пойдём, Лёш, я отведу тебя к вожатой, а она уже оформит тебя, как надо.'

    th 'Это же классно! Неужели я наконец-то получу все ответы?{w} Но, если так задуматься, я рано обрадовался.{w} Возможно, меня сейчас вообще в рабство отправят и всё потом, домой не попаду.'
    th 'Но как же хорошо, что мой паспорт и все документы, которые позволяют определить личность, остались дома.'

    thirty_five_grad_alex 'Да без проблем. Делай, что должно. '
    'И, ещё раз улыбнувшись, она показала мне рукой, чтобы я последовал за ней...'
    window hide


    # '(затемнение (раньше это было обычное моргание))'
    # '(фон лагеря)'
    # scene cg thirty_five_grad_inter_day_1 with fade
    scene cg day1_slavya_animation 
    window show
    'Пройдя через ворота, я как будто оказался в другом мире: чистые здания, да настолько что чуть ли не сверкают, но при этом здесь практически мало людей.'
    'Пару-тройку ребят школьного возраста прошли мимо нас с полотенцами в руках.'

    # '(Славя, улыбка)'

    thirty_five_grad_sl 'Добро пожаловать, Алексей. Чувствуй себя как дома!{w} Тут ты проведёшь две оставшиеся недели. До конца лета, то есть. Так что... Надеюсь, тебе понравится тут.'

    th 'Закончила она предложение тихо, но я всё же мог её расслышать.{w} Неужели... {w}я тут останусь на четырнадцать суток? Но...{w} зачем и почему? Должна же быть какая-то цель, вожатая её «подери»!'

    thirty_five_grad_alex 'Да, и я надеюсь...'

    th 'Сказал я больше по инерции, чем действительно так думал.{w} И всё же, домой хочется. В свой укромный уголок, а не это вот всё.'
    th 'Но, так или иначе, мне нужно принять данную реальность. Потому что если ничего не сдвинется с мёртвой точки, я так и увязну в болоте непонимания.'


    # '(фон общих кружков)'
    if persistent.thirty_five_grad_blur_pref:
        scene bg thirty_five_grad_clubs_sunset blured with dissolve
    else:
        scene bg thirty_five_grad_clubs_sunset with dissolve


    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting with dspr:
        xanchor 0.5 xalign 0.5


    thirty_five_grad_sl 'Смотри, сейчас мы проходим возле общих кружков. По названию, я думаю, ты догадываешься. '
    thirty_five_grad_sl'Там есть всё – от кружков рукоделия, до электротехники, которым заведуют два наших научных светила! Ты ещё с ними познакомишься.'

    th 'Меня заинтересовало это место. А что, если у тех будет микроволновка, и можно будет машину времени построить?{w} Эх, мечты.'

    thirty_five_grad_alex 'Двое? Не особо популярное место, да?'
    # '(Славя, поменять эмоцию)'
    show 35grad_slavya 2 sad sport with dspr

    thirty_five_grad_sl 'Можно и так сказать. Но они просто к себе не особо кого подпускают. Любят уединение, чтобы никто не мешал.{w} Хотя, думаю, что они сделают для тебя исключение.'

    'Она хитро посмотрела на меня, отчего мне стало не по себе.'

    thirty_five_grad_alex 'Я не буду становиться мышью для опытов, не надейся.'

    th 'Хоть и сказал это полностью серьёзно, но новая знакомая приняла это видать за шутку, отчего засмеялась. Но, должен признать, её внешняя красота всё же заставила моё сердце биться чуточку быстрее.'
    # '(Славя, улыбка)'
    show 35grad_slavya 2 laugh sport with dspr

    thirty_five_grad_sl 'Лёшка, да я же пошутила! Просто парень ты с виду умелый, поэтому так и подумала. Прости, не хотела обидеть. Может, тебе вообще вышивание нравится?'

    th 'С другой стороны, во мне просто сейчас играют нервы. Я бы так взбаламутился даже на шутку старого доброго друга. '

    thirty_five_grad_alex 'Забей, всё в порядке, Славя. Пошли дальше...'

    scene bg black with fade
    $ renpy.pause(0.5, hard=True)

    # '(затемнение (раньше это было обычное моргание))'
    # '(фон музклуба)'

    scene bg thirty_five_grad_music_sunset with fade

    th 'Следующей точкой нашего мини путешествия стало небольшое здание с большой...{w}Кхм{w=0.1}.{w=0.1}.{w=0.1}. стеклянной стеной. Через него было всё хорошо видно, так что сразу стало понятно, что передо мной... «музыкальный клуб».'
    th 'А может кружок.{w} Неважно.{w} Но сколько там было инструментов! От гитар до флейт, даже пианино было! А если хорошо приглядеться, то даже и барабанная установка была!'
    th 'Выглядит богато. Хоть я музыкой и не увлекаюсь, но обожаю её слушать. Надо будет тоже сюда обязательно зайти. Но кстати, там никого не было внутри. Наверняка хозяин спит ещё.'

    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting with dissolve:
        xanchor 0.5 xalign 0.425
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_music_sunset blured with dspr

    thirty_five_grad_sl 'Теперь мы проходим возле нашего дорогого музыкального клуба, который заведует... целый один человек! Зато какая! Но я тебе не скажу, почему именно.'

    th 'Снова её эта хитрая манера речи.'

    thirty_five_grad_alex 'Это почему же ещё?'
    # '(Славя, поменять эмоцию)'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'Я не хочу портить тебе сюрприз, сам познакомишься со всеми, поверь, так интереснее. Да и она сама расскажет.'

    '{w=0.1}.{w=0.1}.{w=0.1}.Сама.'

    thirty_five_grad_alex'Странно, но ладно. А почему только один? Это же тяжело, наверно?'
    # '(Славя, поменять эмоцию)'
    show 35grad_slavya 2 sad sport with dissolve_fast

    thirty_five_grad_sl 'Она особо нелюдимая. Не знаю, почему, но вроде добрая. Видать, такое со всеми людьми, которые очень талантливые и одарённые.'

    'Когда Славя закончила говорить, я заметил, что как будто кто-то потихоньку выглядывает из-за раздвинутой шторы. '
    th 'Я даже не успел ничего толком рассмотреть, кроме кончика хвостика, который мгновенно скрылся из поля зрения. '
    'Хорошо запомнилось то, что он имел очень необычный цвет.'
    th 'Может, это из-за игры света и тени?'
    # '(Славя, поменять эмоцию)'
    show 35grad_slavya 2 worry sport with dissolve_fast

    thirty_five_grad_sl 'Алёш, давай поторопимся. А то через полчаса подъём, а мне ещё искупаться надо.'

    'Я кивнул ей, но сам при этом не мог отвести взгляда от этого здания. Было в нём что-то такое, что привлекало меня. Но я совершил грубейшую ошибку – увидел то, чего нельзя было.'

    th '{w=0.1}.{w=0.1}.{w=0.1}.За музклубом был целый, мать его, глубокий лес{w=0.1}.{w=0.1}.{w=0.1}.'
    # '(музыка стоп)'

    stop music fadeout 2.0


    # '(затемнение (раньше это было обычное моргание))'
    scene bg black
    with fade
    $ renpy.pause(0.5, hard=True)

    # '(музыка) Sergey Eybog What Do You Think Of Me?'
    # '(фон площади)'

    play music music_list["what_do_you_think_of_me"]
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - What Do You Think Of Me?')

    scene bg thirty_five_grad_ext_square_sunset with dissolve

    'Мы вышли к, похоже, площади.{w} Это было крайне очевидно, ведь больше всего оно было похоже на плац. Только отличие в том, что не было разметки для марширования.'

    show 35grad_slavya 2 smile sport at thirty_five_grad_sunset_lighting with dissolve:
        xanchor 1.5 xalign 0.425
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_square_sunset blured with dspr

    thirty_five_grad_sl 'А вот центр всего нашего лагеря! И, по сути, я тут чаще всего времени провожу, так что можешь меня всегда тут найти.'

    thirty_five_grad_alex 'Это ещё почему?'
    # '(Славя, поменять эмоцию)'
    show 35grad_slavya 2 normal sport with dspr

    thirty_five_grad_sl 'Всё просто – я тут часто порядок навожу, и других заставляю в добровольно-принудительном порядке. Но зато посмотри, какая чистота, аж блестит всё!'
    thirty_five_grad_sl 'Запомни, Алексей – порядок всегда будет доставаться через труд и может быть даже боль, но он того стоит.'

    thirty_five_grad_alex 'Не могу с тобой не согласиться.'
    # '(Славя, улыбка)'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'Рада это слышать.'

    'Хоть площадь и правда была кристально чистой, хоть живи здесь, но только сейчас я заметил, что она была полупуста. '
    'Не считая, конечно, памятника либо деятелю, либо самого основателя этого места, и одинокой пионерки с тёмными волосами цвета спелой сливы, которая притворяется, что читает книгу, «а на самом деле смотрит на нас».'
    # '(Славя, забеспокоеная)'
    show 35grad_slavya 2 worry sport with dissolve

    thirty_five_grad_sl 'Хм, снова она с утра пораньше читает свою книжку.{w} Не подумай, я не осуждаю её, но она редко делает зарядку, и я беспокоюсь за её здоровье. '

    thirty_five_grad_alex 'Какая же ты заботливая.'

    'Сказал я с иронией, но, похоже, она восприняла меня всерьёз, как я когда-то её.'
    # '(Славя, улыбка)'
    show 35grad_slavya 2 laugh sport with dspr

    thirty_five_grad_sl'Я не шучу, ведь и за тебя так же буду волноваться.'

    'Все мысли во мне приняли позу лёжа и отдали душу на тот свет.'

    thirty_five_grad_alex 'Ой, пошли уже дальше.'

    'Она засмеялась и, легонько толкнув меня в плечо, мы отправились дальше.'


    # '(Спрайт улыбающийся Алисой быстро проносится в бок на экране и останавливаеся с правой стороны)'

    stop music fadeout 3.0


    show 35grad_alice 1 normal joy reb at thirty_five_grad_sunset_lighting:
        xpos 1.5
        linear 0.5 xpos 0.0


    # '(музыка стоп)'

    'Или такое было в наших планах, так как стоило мне только снять рюкзак, чтобы размять плечо, у меня его тут же вырывают, как сумку у бабки на рынке!'
    'В ту же секунду всё моё внимание акцентируется на воре, который даже и не думает убегать!'

    # '(музыка) antony genn, martin slattery – the italians are coming'
    play music thirty_five_grad_The_Italians fadein 3.0
    $ renpy.display_notify('Сейчас играет:\nAntony Genn, Martin Slattery – The Italians Are Coming')
    # '(Славя, удивлённая)'
    show 35grad_slavya 3 surprised sport with dissolve
    # '(Алиса поменять эмоцию)'
    show 35grad_alice 2 laugh reb with dissolve

    thirty_five_grad_dv_unk 'Что-то он у тебя тяжёлый! Позволь, я помогу тебе разгрузиться, шалопай!'

    'Огненно-рыжая красавица смотрела на меня, как орлица на добычу, и хотела уже расстегнуть мой рюкзак, но вот только я попытался его выхватить!'
    'По итогу не получилось, ибо она толкнула меня в плечо.'

    thirty_five_grad_dv_unk 'Не-не! Поделись хабаром, а там посмотрим! Или не хочешь?..'

    thirty_five_grad_alex '...Чего?'

    thirty_five_grad_sl 'Лёша, не слушай её! Алиса... А?'

    'Но её уже и след простыл, так как рванула она ну уж очень быстро!'
    # '(музыка стоп)'
    stop music fadeout 2.0

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black with dissolve_fast
    $ renpy.pause(0.2, hard=True)

    # '(музыка) Between August And December ScaryTale'
    play music music_list["scarytale"]
    $ renpy.display_notify('Сейчас играет:\nBetween August And December ScaryTale')

    # '(фон жилых домиков)'
    scene bg thirty_five_grad_lager_sunset at running with dspr

    th '...Я бежал как умалишённый преследуя эту лисицу, пересекая те места, в которых уже был, и которые ещё даже не видел.'
    th 'Земельные тропы, лавки и какие-то здания, проносятся вдоль меня.'
    th 'Рыжая, её вроде Алиса зовут, сворачивает в бок на опушку леса.'
    th 'Чёрт, только не это!'
    th 'На последнем издыхании, я сворачиваю вправо от неё, чего она явно не ожидала.'
    'Она смотрит на меня, поэтому не видит дороги и спотыкается об камень, и затем кувырком падает лицом об землю. Больно!'

    # '(музыка стоп)'
    stop music fadeout 2.0
    scene bg thirty_five_grad_lager_sunset with dissolve

    'Но сейчас нужно помочь, ведь девушка упала на камни, и судя по стонам, посадка вышла не мягкой. '
    'Пока иду одновременно пытаюсь восстановить дыхание, попутно подавая ей руку, чтобы помочь встать.'

    # '(музыка) КАМАКА – Nerik Cinema'
    play music thirty_five_grad_Nerik_Cinema fadein 3.0
    $ renpy.display_notify('Сейчас играет:\nКАМАКА - Nerik-Cinema')

    'На удивление она берёт её, после чего отряхиваясь, виновато, но как-то при этом играючи, смотрит на меня. Сразу становится неловко, но пару слов из себя выдавливаю:'

    # '(Спрайт Алисы покрасневшей)'
    show 35grad_alice 2 shy reb at thirty_five_grad_sunset_lighting:
        xanchor 0.5 xalign 0.5
    with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_lager_sunset blured with dspr

    thirty_five_grad_alex 'Думаю, что не стоило тебе так ребячиться. Но в общем, как ты?'

    thirty_five_grad_dv_unk 'Пойдёт.{w} Бывало и лучше.{w} Ничего, Виола меня быстро подлатает. А тебе сноровки не хватает, но ноги быстрые. Да и чёт ты странный немного. Не по погоде одетый.'

    thirty_five_grad_alex 'Я...{w} просто приехал издалека.'

    'Поднял рюкзак с земли и повесил на плечо.'

    thirty_five_grad_alex 'Алексей, кстати. А ты Алиса?'
    show 35grad_alice 2 flirt reb with dissolve_fast

    thirty_five_grad_dv 'Верно. Но ты нос лишний раз не вешай, ещё увидимся!'

    th 'Странная, но до жути красивая девушка с приятными и мягкими чертами лица, у которой при каждом движении подпрыгивала объёмная грудь. '
    'Чуть погодя, затем и вовсе убежала так, как будто она и не падала.'
    hide 35grad_alice 2 flirt reb with dissolve
    th 'М-да, чего тут только не встретишь...'

    # '(появляется Славя)'
    # Славя появляется справа, Алиса смещается влево
    show 35grad_slavya 3 fear sport at thirty_five_grad_sunset_lighting:
        xanchor 0.5 xalign 0.5
    with dissolve

    thirty_five_grad_sl '…Фух. Еле добежала! Ты как, в порядке?'

    thirty_five_grad_alex 'А? Да, спасибо за заботу. Я думал, что ты спортсменка же.'

    'Блондинка была вся запыхавшаяся и вымотанная. Да, ей уж точно душ не помешает.'

    show 35grad_slavya 2 laugh sport with dissolve_fast

    thirty_five_grad_sl 'Ну, знаешь, я хороша не на скорость! Ладно, главное, что всё в порядке, и никто не пострадал. Пошли дальше, нужно тебя к вожатой всё-таки проводить.'

    'Я не успел ей сказать, что Алиса немного пострадала, но да ладно. Мы вместе вернулись обратно, на площадь. В это же время солнце уже начало греть.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    # '(затемнение (раньше это было обычное моргание))'
    window hide
    scene bg black at thirty_five_grad_vhs
    with dissolve
    $ renpy.pause(0.5, hard=True)


    'Мы шли мимо жилых домиков, которые долго тянулись один за другим. При этом архитектурно они все были как один, хотя декоративно многие отличались:'
    'На дверях и окнах висели флаги футбольных и хоккейных команд, а где-то даже веселый Роджер, что позабавило.'
    'Но мы внезапно резко остановились.'

    

    thirty_five_grad_sl 'Это наша конечная остановка. Да, в лагере еще много интересных мест, но ты уже сам изучишь их самостоятельно, хорошо? А то мы и так не успеваем.'
    thirty_five_grad_sl 'Столовая находится через мое плечо – поверни направо и налево, и будешь там. Запомнил?'

    thirty_five_grad_alex 'Ага.'

    thirty_five_grad_sl 'Отлично. А сейчас до домика вожатой рукой подать. Быстро дойдем.'

    if persistent.thirty_five_grad_blur_pref:
        scene bg ext_house_of_mt_sunset at thirty_five_grad_blur with dissolve
    else:
        scene bg ext_house_of_mt_sunset with dissolve

    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting:
        xanchor 0.5 xalign 0.5
    with dspr

    th 'Причём буквально, ведь стоило нам сделать с десяток шагов, как мы оказались возле ее домика, если смотреть по его внешнему виду и словам помощницы.'
    th 'Что сказать, он сильно выделялся от прочих: острая, как у ножа, треугольная крыша, общий деревянный каркас, новый на вид шезлонг, который стоит прямо под широкой кроной высокого, но тонкого дерева.'
    th 'А рядом с крыльцом и ступеньками стоит велосипед. Ржавый, конечно, но чутка подправить – и будет красавцем!'
    th 'Не как с завода, но всё же. Во мне кипит волнение. Да такое, словно собираюсь на встречу с директором. Сердце бьется, дышать немного трудно.'
    th 'Видать, сказывается еще и погода, которая с каждой минутой становится лишь жарче.'

    # '(музыка) Sergey Eybog Get To Know Me Better'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Get To Know Me Better')
    play music music_list["get_to_know_me_better"]

    'Славяна поднимается на крыльцо в два быстрых шага и стучится в деревянную дверь, которая хорошо выделяется на фоне новеньких стен.'

    # '(спрайт Ольги в пижаме)'
    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting:
        xanchor 0.5 xalign 0.8
    with move
    show 35grad_olga 3 normal paj at thirty_five_grad_sunset_lighting:
        xanchor 0.5 xalign 0.2
    with dissolve

    'Затем дверь всё же открывается, и из нее в пижаме выходит женщина моего возраста, хотя нет, на три-четыре года старше моего, но при этом она с интересом смотрит на меня.'
    th 'Интересно, о чем думает? В ее глазах агрессия не читается, но и доброта тоже. Забавно, ведь если бы меня так подняли, я б тоже не по-доброму смотрел.'

    show 35grad_slavya 2 laugh sport with dspr

    thirty_five_grad_sl 'Доброе утро, Ольга Дмитриевна! Я вам новенького привела, помочь его оформить?'

    'Радостно прощебетала девушка, но вот начальница этого жеста, похоже, не особо оценила, так как быстро ее выражение овального загорелого личика сменилось на недовольное.'
    'А изумрудные зелёные глаза и вовсе хотели съесть её:'

    show 35grad_olga 2 angry paj with dissolve_fast

    thirty_five_grad_mt 'Славяна, чтобы это я в последний раз видела, поняла? Спортивная форма одежды допускается только во время занятия физкультурой.'

    'Хотя женщина и не кричала, но её тон звучал угрожающе. Связываться с ней – плохая идея, так что...'

    # '(спрайт грустной Слави)'
    show 35grad_slavya 2 sad sport with dissolve_fast

    thirty_five_grad_sl 'Виновата, Ольга Дмитриевна, такого больше не повторится...'

    'Молниеносно её выражение лица сменилось на более мягкое и нежное, словно материнское:'

    show 35grad_olga 3 smile paj with dissolve_fast

    thirty_five_grad_mt 'Все в порядке, Славя. Не забывай, то, что ты моя помощница еще не прибавляет тебе особых привилегий, так что не стоит нарушать правила, хорошо?'

    thirty_five_grad_sl 'Хорошо.'

    show 35grad_slavya 2 worry sport with dissolve_fast

    thirty_five_grad_mt 'Вот и отлично. Спасибо, что привела его, можешь быть свободна, но до построения подойди ко мне, хорошо?'

    thirty_five_grad_sl 'Так точно!'

    hide 35grad_slavya 2 worry sport with dissolve

    th 'Когда Славя начала уходить, Ольга всё ещё провожала её тёплым взглядом. Может, все же дать этой вожатой второй шанс?'
    th 'Да, я зря погорячился, ведь сказываются эти дурацкие нервы. Но если так подумать, какой человек был бы спокойным в моей обстановке?'
    # '(спрайт улыбки ольги)'
    thirty_five_grad_mt 'Рада, что ты хорошо и спокойно доехал, хотя и так поздно, под середину смены. Но ничего страшного, еще наверстаешь упущенное. Проходи в домик, поговорим.'

    'Она указала, чтобы я прошёл внутрь домика, а я не мог отказаться, вожатая может дать ответы на все вопросы об этом проклятом месте'
    th 'И вообще отдельно удивительно то, что она меня ещё и ждала, оказывается...'

    # '(затемнение (раньше это было обычное моргание))'
    # '(музыка стоп)'
    stop music fadeout 3.0
    # '(фон внутри домика вожатой)'
    play sound sfx_open_dooor_campus_1
    $ volume(1.5, 'sound')
    scene bg thirty_five_grad_int_house_of_mt_sunset with fade
    stop ambience fadeout 3
    'В домике было очень прохладно из-за сквозняка, но с вентилятором было бы лучше. Хотя небольшой вроде стоял на её рабочем столике, который был... мягко говоря, крайне захламлён.'
    'То тут-то, там лежали рабочие тетради, какие-то папки, журналы, сверху пачка печенья и пакетики с быстрорастворимым кофе. Вот только они были странными.'
    'Я таких попросту никогда не видел, и было бы интересно изучить их.'

    show 35grad_olga 3 normal paj with dissolve:
            xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_day at thirty_five_grad_blur with dissolve

    thirty_five_grad_mt 'Так, пока можешь присесть на кровать, она всё равно ничья, а я кое-какие документы на тебя заполню. Минут пять всё займёт, не волнуйся.'

    'Расчистив кое-как стол, она взяла белый лист, затем ручку и, усевшись за обычный деревянный стул, который даже в моём доме стоял или в любом другом, и начала писать.'

    'Я в это время разглядывал домик изнутри. В принципе, не сказать, что он какой-то уникальный или выглядит богато. Обычный и простой.'
    'Массивный деревянный шкаф в углу, в котором теоретически может быть своя вселенная вещей, аккуратно заправленная кровать и антипод в виде стола.'
    'Лампочка на потолке без абажура. Несколько юмористических плакатов и один – со старым комедийным фильмом. Просто, но со вкусом и уютом.'

    # '(спрайт Ольги с улыбкой)'
    show 35grad_olga 2 smile paj with dissolve_fast


    thirty_five_grad_mt 'Вот и готово!'

    'Гордо заявила вожатая и встала со стула с характерным скрипом. Скрипом её поясницы, а не стула...'

    # '(музыка) Sergey Eybog Farewell To The Past'
    play music music_list['farewell_to_the_past_full'] fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Farewell To The Past Full')

    show 35grad_olga 3 normal paj with dissolve_fast

    thirty_five_grad_mt 'Ну что, давай знакомиться. Я – Ольга Дмитриевна, вожатая седьмого отряда и по совместительству твоя начальница.'
    thirty_five_grad_mt 'Так что, какие-либо вопросы, проблемы, конфликты – прямо ко мне.'

    thirty_five_grad_alex 'Хорошо, я вас понял. А я Алексей.'

    # '(грустный спрайт Ольги)'
    show 35grad_olga 3 surprised paj with dissolve_fast

    thirty_five_grad_mt 'Да, приятно познакомиться снова. На самом деле, я знаю тебя, по крайней мере, твоих родителей. Или... знала. Прими мои соболезнования.'

    th 'Я совру, если скажу, что у меня земля чуть из-под ног не ушла. Какие родители? Мои?! О чём эта женщина вообще говорит?! Видать, она заметила выражение моего лица, раз забеспокоилась:'

    show 35grad_olga 3 surprised paj with dissolve_fast

    thirty_five_grad_mt 'Алексей, всё хорошо? {w} Ты побледнел.'

    thirty_five_grad_alex 'Да, да. Всё в порядке. Просто забыл кое-что. Скажите, какой сейчас год на дворе? А то... запамятовал, да...'

    th 'Слова давались мне с большим трудом, но я всё же смог из себя их выдавить. М-да, с каждой минутой ситуация становится всё хуже и хуже. А что будет вечером?'

    thirty_five_grad_mt 'Хм, вроде не полдень, жара не такая сильная. Ладно, с кем не бывает, переутомился с дороги. Восемьдесят девятый год, а число и сама не помню, не особо слежу, хотя надо бы.'

    th 'Для меня мир если не буквально, то мысленно перевернулся полностью. Это же, чёрт побери, путешествие во времени! Ох, куда же я вляпался, а главное как это вообще могло произойти?!'

    # '(обычный спрайт Ольги)'
    show 35grad_olga 3 normal paj with dissolve_fast

    thirty_five_grad_mt 'Алексей, ты много в облаках витаешь, с тобой всё хорошо? Одного оставить можно хотя бы?'

    thirty_five_grad_alex 'А?'

    thirty_five_grad_mt 'Ладно, видать, ты очень сильно утомился, парень. Ох, отдыхай, а я схожу в административный корпус, посмотрю свободные домики. Правда, отдохни пока.'
    # '(её спрайт пропадает)'
    hide 35grad_olga 3 normal paj with dissolve_fast

    'Она попросила меня отвернуться, чтобы переодеться, а затем спокойно вышла из домика, как ни в чём не бывало. Но вот в чём-то она была права. '
    'Я смертельно устал. Мне нужен был отдых, как моральный, так и физический. Только стоит заметить, что меня это место не особо-то пугает. Скорее запутывает, словно жертву в сетях.'

    th 'Ладно, хватит на сегодня пространных мыслей. Я просто на секунду-другую закрою глаза. Просто ведь прикрою...'
    # '(музыка стоп) '
    stop music fadeout 2.0
    # '(закрываются глаза)'
    scene bg black at thirty_five_grad_vhs with fade
    $ renpy.pause(0.5, hard=True)

    '...Моё состояние было максимально расслабленным. Я испытал небесный покой. Мышцы не были напряжены, в голове было тихо и спокойно.'
    'Я бы проспал так ещё пару часов, если бы меня нежно, но при этом сильно не дёргали за плечо. Я медленно открываю глаза.'
    if persistent.thirty_five_grad_blur_pref:
        scene bg int_house_of_mt_day at thirty_five_grad_blur with thirty_five_grad_circle_transition
    else:
        scene bg int_house_of_mt_day with thirty_five_grad_circle_transition

    # '(музыка) Sergey Eybog Timid Girl'
    play music music_list['timid_girl']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Timid Girl')

    # '(спрайт Ольги в форме улыбается)'
    show 35grad_olga 3 normal form with dspr:
        xanchor 0.5 xalign 0.5

    thirty_five_grad_mt 'Проснулся, наконец. Ну, как себя чувствуешь?'

    'Всё тот же взрослый женский голос. Думаю, из неё вышла бы неплохая мать. А возможно и уже, кто его знает. Она нежно улыбается мне, но я, глядя на неё, отвечаю:'

    thirty_five_grad_alex 'Мм... более-менее нормально... сколько я проспал?'

    thirty_five_grad_mt 'Не знаю, минут двадцать, наверное, я не считала. Но до подъёма ещё десять минут.'

    'Затем она отвела взгляд, словно погрузившись в размышления, а после снова обернулась.'

    # '(спрайт Ольги улыбающийся)'
    show 35grad_olga 3 smile form with dspr

    thirty_five_grad_mt 'У меня для тебя новости. Будешь жить в больничке! {w} Ладно, шучу. Со мной вместе эти две недели. Считай, тебе повезло, иначе мог бы ночевать на улице!'

    show 35grad_olga 3 angry form with dspr

    thirty_five_grad_mt 'Да не делай такое лицо! Туда мы давно никого не клали. Все тут здоровые, крайне редко кто болеет.'

    th 'У меня ощущение, словно за меня решают мою судьбу, а я с этим ничего поделать не могу! Такое противное чувство, ей богу. Но что мне терять, если честно?'

    thirty_five_grad_alex 'Ладно, я согласен. Хоть у меня и выбора особо нет.'

    thirty_five_grad_mt 'Вот и хорошо, что ты из понимающих. А то обычно как скандалы и истерики начнут закатывать, что их с друзьями вместе не заселили, так хоть сама потом истери.'

    show 35grad_olga 2 normal form with dspr

    thirty_five_grad_mt 'Ладушки, сейчас я тебе форму в шкафу посмотрю, переоденешься, выдам тебе гигиенические принадлежности.'

    'А затем она перевела свой взгляд на мой рюкзак, который лежал всё это время на полу рядом со мной.'

    show 35grad_olga 2 surprised form with dspr

    thirty_five_grad_mt 'Интересный же у тебя он. Но я так думаю, ты с собой толком ничего не взял, да?'

    'Я медленно кивнул. Что есть, то есть. Всё время руки не доходили брать средства личной гигиены.'

    thirty_five_grad_alex 'Ольга Дмитриевна, а откуда у вас форма и такие вещи?'

    thirty_five_grad_mt 'Удивил ты меня подобным вопросом. Я же вожатая, у меня и не такое есть!'

    th 'Коротко и ясно. Неужели я и правда попал в Союз? Да ну нет, это же сюжет книги или фантастического рассказа! Ладно, как и всегда, просто смирюсь.'
    th 'Буду пока играть по правилам этого мира. Какое-то время. А потом – суп с котом, как говорили раньше.'

    show 35grad_olga 2 normal form with dspr

    thirty_five_grad_mt 'Какой у тебя размер?'

    thirty_five_grad_alex 'А?'

    'Её вопрос смутил меня, мягко говоря.'

    show 35grad_olga 2 angry form with dspr
    thirty_five_grad_mt 'Размер формы, говорю.'

    thirty_five_grad_alex 'А-а-а, я не помню.'

    th 'И я не солгал. Правда, не помню такую мелочь, что даже странно. Ольга смерила меня неодобрительным взглядом, но ничего не сказала. Видать, просто приметила на глаз.'
    'После пары минут копотни в шкафу, она протягивает мне чистую на вид форму. Немного помятую, но при носке быстро разгладится. При этом в другой руке была пара сандалий.'

    show 35grad_olga 3 normal form with dspr

    thirty_five_grad_mt 'Вот, держи. Носи с гордостью и честью, как любой пионер! А зубной порошок и мыло возьмёшь в коробке в шкафу.'

    play sound sfx_dinner_jingle_normal

    'И как только она закончила говорить, прозвучал очень интересный и крайне необычный звук, который сразу же узнал – горн.'
    'Мне приходилось его слышать ранее в воинской части, поэтому ностальгия потихоньку заполнила сердце.'

    thirty_five_grad_mt 'Вот. Официально теперь – с добрым утром! Скажи, Алексей, успел с кем-нибудь познакомиться?'

    thirty_five_grad_alex 'Со Славяной только.'

    thirty_five_grad_mt 'Ничего, будет ещё время узнать всех поближе. В особенности, когда вручу тебе подписной лист. Но это будет после завтрака и построения.'
    thirty_five_grad_mt 'А сейчас, переодевайся быстренько, приводи себя в порядок и дуй в столовую. Знаешь же, где она?'

    'Я мотнул головой, а Ольга лишь устало вздохнула. Точнее, направление знал, но вот путь...'

    thirty_five_grad_mt 'Действительно, откуда тебе знать. Ладно, я если успею, провожу тебя...'

    thirty_five_grad_alex 'А если нет, то попрошу кого-нибудь мне помочь.'

    thirty_five_grad_mt 'Именно! Вот и молодец. Я побежала.'

    # '(Ольга пропадает)'
    hide 35grad_olga 3 normal form with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_day with dspr

    # '(музыка стоп)'
    stop music fadeout 2.0

    th 'И снова она выпорхнула из домика как бабочка, оставив меня тут одного. Ещё ведь и правда нужно переодеваться в это, и, похоже, другого выбора у меня нет.'
    th 'Впрочем, деваться некуда. Надеюсь, я не буду выглядеть как Джокер после пьянки или чего ещё похуже.'

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black at thirty_five_grad_vhs with fade

    # '(музыка) Sergey Eybog Two Glasses Of Melancholy'
    play music music_list['two_glasses_of_melancholy']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Two Glasses Of Melancholy')

    th 'Переодевание не заняло больше минуты. Нужно будет побыстрее идти на завтрак, ибо я был безумно голоден.'
    th 'Ха, стоило мне подумать о пище, как всё прошлое постепенно забывается. Но...'

    scene bg int_house_of_mt_day with thirty_five_grad_circle_transition

    th '...Будем честны, это место не такое страшное, как казалось изначально. Меня пока не съели, не пытали, не заставили взять кредит в обмен на меня из плена.'
    th 'Да, возможно я переместился во времени, но это же не значит, что я умер, так? Жаль, что никто так и не ответит мне на этот вопрос. Хотя, ещё не вечер.'

    th 'Ну что, настало время подойти к зеркалу и посмотреть на себя. Поправить форму там, всё такое. Подхожу, закрываю дверцу шкафа, чтобы открылось зеркало, и...'
    # '(арт с тем, как Лёша смотрит в зеркало)'
    scene cg thirty_five_grad_nefor_mirror at shake with dspr

    # '(музыка резко стоп + звук скримера)'
    stop music fadeout 0.2
    play sound sfx_scary_sting

    '...Чуть не ору во всю глотку! Еле удержал себя от этой ошибки! Так что стою с открытым немым ртом и хватаю тёплый воздух губами.'
    th 'Всё же, я был прав насчёт того, что помолодел! Выгляжу на все семнадцать.'

    # '(музыка) Antony Genn, Martin Slattery – Shutdown / The Strike Begins'
    # Не забыть поменять
    play music thirty_five_grad_Nerik_Cinema fadein 3.0
    $ renpy.display_notify('Сейчас играет:\nAntony Genn, Martin Slattery – Shutdown')

    'Пропало несколько шрамов под глазами, которые появились в уличной драке, пропала некоторая сутулость в спине, испарились вечно висящие над глазами тройные мешки.'
    show blink
    $ renpy.pause(1.2, hard=True)
    scene bg black at thirty_five_grad_vhs
    'Закрыл глаза и медленно сосчитал до десяти. {w} Открыл глаза.'
    show unblink
    $ renpy.pause(1.5, hard=True)
    th 'Стало немного спокойнее, и только сейчас заметил, что в руке держу тот самый, пионерский галстук.'
    th 'Помню, как у кого-то из родителей был точно такой же на фотокарточке. Со старого полароида, который имел характерный желтоватый оттенок цвета фото.'
    th 'Интересно, а тут такие есть?'

    # поменять цг, лёша забыл
    scene bg int_house_of_mt_day with dspr

    # '(музыка стоп)'
    stop music fadeout 2.0
    play sound sfx_knocking_door_outside
    'Мои размышления прервал стук в дверь. Такой, равномерный и спокойный. Кто же это может быть? Я подхожу и аккуратно открываю дверь, как будто жду важного гостя.'

    # '(музыка) Sergey Eybog Sweet Darkness'
    play music music_list ['sweet_darkness']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog Sweet Darkness')
    # '(спрайт Слави в форме)'
    show 35grad_slavya 2 smile pio with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_day at thirty_five_grad_blur with dspr

    thirty_five_grad_sl 'Ой, Лёшка, не ожидала тебя здесь увидеть. Вижу, Ольга Дмитриевна тебе уже форму выдала. А где твой галстук? И где жить будешь?'

    'Засыпала меня вопросами Славяна, но в этот раз она уже была в форме, причём она ей даже шла! Придавала официальный вид, так сказать.'

    thirty_five_grad_alex 'Так я это, разучился его завязывать! Да, не удивляйся, я не часто им пользуюсь...'

    'Врать, а особенно такой девушке, было не очень приятно. Но говорить правду ещё неприятнее, так что выбрал из худшего.'
    'Но она только посмеялась, по-доброму так, как будто старшая сестра над младшим братиком.'

    show 35grad_slavya 2 laugh pio with dspr

    thirty_five_grad_sl 'Ой, ну ты и выдал! Ладно, я помогу тебе. Но ты так и не ответил мне на вопрос.'

    show 35grad_slavya 2 smile pio with dspr

    'А затем произошло что-то страшно приятное: девушка, которая младше меня, но в данный момент у нас с ней примерно одинаковый возраст, нежно берёт из моей руки этот красный платок, а затем подходит.'
    'Расстояние между нашими лицами всего несколько сантиметров, и... спокойно завязывает его в пару-тройку движений. Настолько ловко и быстро это было...'

    thirty_five_grad_alex 'С-спасибо...'

    'Я покраснел.'

    show 35grad_slavya 2 shy pio with dissolve

    thirty_five_grad_sl 'Да не за что. Это пустяки же. Но ты так и не ответил – а где же жить будешь? Неужели в больничке?'

    'Видно, что она пошутила, но в словах была лёгкая дрожь, так что надо сразу попытаться успокоить.'

    thirty_five_grad_alex 'Нет-нет! Ольга... Дмитриевна меня к себе поселила. Буду жить с взрослой тётей, а не с тобой, эх...'

    show 35grad_slavya 2 laugh pio with dspr

    thirty_five_grad_sl '...А? Но у меня уже есть соседка. И вообще, не волнуйся ты так, она хорошая и тихая. Ты просто не делай ничего плохого, как Алиса, например, и всё хорошо будет.'

    thirty_five_grad_alex 'Да нет, не буду, разве что с голодухи. Я есть очень хочу, сейчас хоть собаку...'

    show 35grad_slavya 2 smile pio with dspr

    thirty_five_grad_sl 'Домашних животных есть плохо, а на корейца ты не шибко похож, Лёшка.'

    'И ткнула меня легонько в плечо. Меня пробило мурашками, но они были приятными.'

    thirty_five_grad_alex 'Шучу же!'

    show 35grad_slavya 2 laugh pio with dspr

    'Мы вместе рассмеялись. Ведём себя так, как будто давние знакомые, встретившиеся недавно после долгой разлуки. Даже грустно стало немного.'
    'Эх, как бы мы общались, если встретились так не в сверхъестественном лагере, а в совершенно нормальной обстановке?'

    show 35grad_slavya 2 normal pio with dspr

    thirty_five_grad_sl 'Ладушки, давай, пошли на площадь, скоро построение, а на нём Ольга Дмитриевна тебе уже отдельно расскажет, что нужно будет делать.'

    thirty_five_grad_alex 'Тут работают?'

    'Её слова сильно удивили меня. Не то, чтобы я был лентяем, но работать неизвестно зачем и почему, не особо прельщает...'

    show 35grad_slavya 1 normal pio with dspr

    thirty_five_grad_sl 'Ну да, а ты чего ждал? Мы уже не октябрята, у нас полноценная работа! Хотя, полноценной её всё же тяжеловато назвать. Но не важно, разберёшься!'

    'Хлопнув меня по плечу, мы направились вдаль. Точнее, вглубь этого места. Что же меня ждёт в нём? В какие приключения я попаду? И стоит ли это того?'
    th 'Много вопросов, ответы на которые я вряд ли смогу найти...'

    # '(музыка стоп)'
    stop music

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black at thirty_five_grad_vhs with fade

    # '(музыка) Sergey Eybog Dailylife'
    play music music_list['my_daily_life']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Dailylife')

    # '(фон площади)'
    play sound sfx_close_door_1
    scene bg ext_square_day with thirty_five_grad_circle_transition

    th 'На площади выстроилось не меньше сотни детей разных возрастов, но что удивило меня ещё больше, только пару десятков взрослых на вид ребят стояло возле памятника.'
    th 'Что-то подсказывало мне, что среди них был и мой отряд. Как его там? Седьмой?'

    show 35grad_slavya 2 normal pio with dspr:
        xanchor 0.3 xalign 0.3

    thirty_five_grad_sl 'Лёш, видишь? Мы там строимся всегда, запоминай.'

    'В ответ несколько ребят посмотрели на меня, разглядывая с интересом и что-то обсуждая. Но среди них была одна какая-то странная.'
    'Она выделялась своими тёмно-лиловыми волосами, которая стояла боком от меня. Почему?'

    'Со Славей мы дошли до нужного места довольно быстро. Я даже не успел что-либо сообразить, как тут же со мной начали все здороваться:'

    # '(появляются Шурик и Электроник)'
    show 35grad_shuric 2 normal pio:
        xalign -0.2
    with dissolve
    show 35grad_electronnik 1 hmuri normal pio:
        xalign 1.2
    with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day at thirty_five_grad_blur with dissolve


    thirty_five_grad_sh_unk 'О, привет! Новенький, как зовут?'

    'Проговорили одновременно два парня с одинаковым цветом волос, как у Слави. Может, те самые братья? Неважно. Я протянул каждому из них по очереди руку и пожал, затем сказал:'

    thirty_five_grad_alex 'Алексей.'

    show 35grad_shuric 2 smile pio with dspr

    thirty_five_grad_sh 'Приятно, а я Саша, или Шурик, а вот этот Электроник.'

    'Имя второго удивило меня, и я что ни на есть улыбнулся.'

    thirty_five_grad_alex 'Прямо как из фильма?'

    show 35grad_electronnik 1 normal pio with dspr

    thirty_five_grad_el 'А то! Но это долгая история, потом расскажу! А ты какими судьбами вообще тут?'

    'Улыбаясь, ответил парниша.'

    show 35grad_slavya 2 angry pio with dspr

    thirty_five_grad_sl 'Мальчики, потом пообщаетесь. Сейчас наша вожатая скоро подойдёт. Стройтесь.'

    # '(появляется ещё спрайт Ольги)'
    show 35grad_olga 3 normal form pan:
        xanchor 0.7 xalign 0.7
    with dissolve

    'А она ведь не солгала, потому что стоило нам только стать ровно в шеренгу (куда я воткнулся последним, ибо не хотелось быть впереди планеты всей), то тут же пришла наша вожатая.'
    'Высокая стройная женщина. Её каштановые волосы развевались на ветру, при этом на голове белая панамка. Гордой походкой она подошла к нам, и начала считать каждого из нас.'

    thirty_five_grad_mt 'Вот и отлично, все на месте.'

    show 35grad_slavya 2 worry pio with dissolve_fast

    thirty_five_grad_sl 'Но Ольга Дмитриевна, Мику же ещё нет.'
    'Аккуратно заявила Славяна, но та лишь посмотрела на неё. Видать, девочка поняла без лишних слов, поэтому снова приняла стойку смирно.'
    th 'Мику...'
    th 'Это что же за имя такое знакомое... Где-то слышал, но не могу вспомнить.'
    # show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_mt 'Она же у нас не ходит, забыла? Эх, да что же это с ней такое... Ладно, стройся!'

    'Мне показалось это очень странным. Всё же, вожатый обязан следить за своими подопечными, а тут что? Вроде, это и не моё дело, но... неправильно это как-то всё.'
    'Но вот это имя так и не даёт мне покоя, словно бы я его знаю...'

    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with fade
    $ renpy.pause(1.0, hard=True)

    # '(пропадают все, кроме Ольги)'


    '...Шел так называемый «развод». Это когда каждому объясняют цели дня для каждого пионера. Не обошло это и наш отряд.'
    'Вот ко мне подходит Ольга, и с гордым видом протягивает мне какую-то бумажку:'

    scene bg ext_square_day with dissolve

    show 35grad_olga 3 normal form pan:
        xanchor 0.5 xalign 0.5
    with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day at thirty_five_grad_blur with dissolve

    thirty_five_grad_mt 'Алексей, держи. Это называется обходной лист. Видишь несколько пунктов?'

    thirty_five_grad_alex 'Да. И каждый из них я должен пройти?'

    show 35grad_olga 2 angry form pan with dissolve_fast

    thirty_five_grad_mt 'Верно. И обязательно записаться в один из них, понял?'

    thirty_five_grad_alex 'Так точно. Но почему я должен это сделать?'

    show 35grad_olga 2 normal form pan with dissolve_fast
    'Вожатая рассмеялась.'

    thirty_five_grad_mt 'Ну как же, это твоя прямая обязанность. Или ты хочешь полдня сидеть и учить права и обязанности пионера?'

    thirty_five_grad_alex 'Эм, нет. Я, пожалуй, откажусь от таких обязанностей. Так уж и быть, уговорили.'

    show 35grad_olga 3 normal form pan with dissolve_fast

    thirty_five_grad_mt 'Вот и отлично. Вопросы ещё есть?'

    thirty_five_grad_alex 'Два. Насколько быстро это нужно сделать? И когда завтрак?'

    th 'Она лишь пожала плечами, и только сейчас понял, насколько же тупой вопрос я задал. Идиот.'

    show 35grad_olga 3 angry form pan with dissolve_fast

    thirty_five_grad_mt 'Не знаю, как тебе удобно. Но чтобы до пяти вечера он уже был у меня на руках, понял? И завтрак будет после развода.'

    th 'Я тоже подумал, что затягивать лучше не стоит, тем более, злить её в мои планы не входило. М-да, расспросы подождут. '
    th 'Хм, а этот лагерь специально так делает? Задерживает меня, чтобы скрипт не поломал? Ладно, хоть завтрак скоро, уже радует.'

    # '(музыка стоп)'
    stop music

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black at thirty_five_grad_vhs with fade
    $ renpy.pause(1.2, hard=True)

    # '(музыка) Sergey Eybog Two Glasses Of Melancholy'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Two Glasses Of Melancholy')
    play music music_list['two_glasses_of_melancholy']


    'Все те задачи, которые Ольга раздавала другим, я пропустил мимо ушей. Они мне не были интересны, ведь думал я сейчас по большей части о том, когда я смогу поесть. '
    'И, конечно, о той девушке, которая одна вечно торчит в клубе, если верить словам вожатой и Слави.'

    scene bg ext_dining_hall_away_day with fade

    th 'Без понятия, откуда такие мысли. Словно она и есть мой ключ к разгадке, как бы это пафосно ни звучало. Но да ладно, это ж бред и, скорее всего, просто так накручиваю себя.'
    play sound sfx_dinner_jingle_normal
    th 'Снова прозвенел горн. Значит пора завтракать. В животе радостно заурчало, после чего Ольга дала команду строиться по двое. Ха! '
    th 'Прямо как в школе, и удивительно то, что мне пары-то не досталось. Ну и ладно, не думаю, что это так уж и страшно. '
    'Нас было шестеро, а со мной семеро, так что все стали друг с другом рядом. '

    'Хотя как сказать, что не страшно. Я ощущал на себе злой взгляд, тревожный. Чувство, словно проклинают меня! '
    'Источник этого было понять не так уж и трудно, если внимательно оглядеться.'

    'По итогу, внимательно посмотрев по сторонам так, чтобы особо не выделяться, я вычислил, откуда за мной шло наблюдение – со второго ряда левого края.'
    'Девушка с ярко рыжими волосами, и она по-лисичьи смотрела на меня как бы думая, в какой момент поймать свою «добычу».'

    'Я сразу же отвернулся от неё. Мгновенно понял – что она крайне неприятная особа, хоть и ничего так внешне, поэтому попытаюсь с ней не сталкиваться.'
    'Но зато ветер доносил до меня какие-то отголоски её беседы с ещё одной девочкой, той самой, тихоней с книжкой, которая одета при этом не по погоде – с распущенными рукавами.'
    'Разобрать о чём они говорят, было крайне тяжело, но явно говорили обо мне, что начинало раздражать.'

    th '...Просто оставьте меня в покое, прошу, я хочу домой...'

    'Зрительная память у меня хорошая, лучше, чем на имена, поэтому сразу же запомнил, что и где именно находится в этом лагере. Надеюсь, мне это в будущем поможет.'

    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with dissolve
    $ renpy.pause(1.2, hard=True)
    # '(фон столовой улица)'
    scene bg ext_dining_hall_near_day with dissolve
    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(спрайт Алисы)'
    show 35grad_alice 1 normal reb with dspr:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_day at thirty_five_grad_blur with dissolve

    'Столовая представляла собой огромное здание с верандой. У него интересная архитектура, прямые, но в некоторых местах косые углы плавно переходили в изящное расположение... окон?'
    'Не понимаю, что я несу... Всё что угодно, главное чтобы эта рыжая бестия отвязалась от меня!'
    show 35grad_alice 2 hmuri reb with dissolve_fast

    thirty_five_grad_dv 'Представляешь, а ведь больше не должно было никого приезжать. Колись, у тебя что, родители блатные, а? Или ты из этих, как это...'

    'Да, именно та самая девушка, которая обсуждала меня с тихоней, сейчас стоит рядом со мной и тянет заунывную беседу.'
    'Звали её Алисой, что неудивительно, ведь ей чертовски идёт это имя: за её поведение и за неприкрытую, но приятную харизму.'

    thirty_five_grad_alex 'Слушай, что тебе от меня нужно? Денег я тебе не дам, даже не проси.'
    show 35grad_alice 2 ready_to_smash_faces reb with dissolve_fast

    thirty_five_grad_dv 'О-о-о, всё же ты из этих, мажорчиков? Чего тогда не в «Артеке»?'

    th 'Заигрывает со мной, чертовка такая. Только вот что мне делать с ней?'
    th 'Нет, давать леща и ломать колени не буду (пока), а вот быть с ней мягче или погрубее? Выбор определённо не лёгкий, но промолчать же не могу...'
    show 35grad_alice 2 angry reb with dspr

    thirty_five_grad_dv 'Эй, Лёхич? Жопич? Ты чё, завис там?'

    # '(музыка) Antony Genn, Martin Slattery – The Italians Are Coming'
    $ renpy.display_notify('Сейчас играет:\nAntony Genn, Martin Slattery – The Italians Are Coming')
    play music thirty_five_grad_The_Italians fadein 1.0

    thirty_five_grad_alex 'Да вот думаю, в какой манере тебя послать. Понимаешь ли, с самого раннего утра я мало того, что не выспался, так ещё голодный, как псина.'
    thirty_five_grad_alex 'А сверху этого сего одна назойливая дама пытается мне башню пробить. Как думаешь? Подходящее у меня настроение для разговоров, или нет?'

    'Совершенно без понятия, какой эффект на неё это возымело, но мало того, что она покраснела, прижав руки к... упругой на вид груди, так её яркие, янтарные глазки забегали то туда, то сюда, словно ища пути отступления.'
    show 35grad_alice 2 sad reb with dspr

    thirty_five_grad_dv 'Н-ну и дурак же ты. Надо было тебя приложить тогда всё-таки.'

    # '(Алиса пропадает)'
    hide 35grad_alice 2 sad reb with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_day with dissolve

    'И стукнула кулаком в плечо. Легонько так, но ощутимо. А затем отвернулась говорить ещё с кем-то из толпы.'
    'Мне так и хотелось схватить её за две огненные косички на голове, чтобы проучить.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    'Воплощение идеи не показалось мне ужасной, и я даже хотел бы это проделать!'
    'Недолго думая, я оглянулся, чтобы проверить, не обращает ли на меня кто своё ненужное внимание, начал тянуть правую руку в сторону её головы, как вдруг...'

    # '(появляется спрайт Лены)'
    show 35grad_lena 2 smile pio with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_day at thirty_five_grad_blur with dissolve

    thirty_five_grad_ul 'О, эм... Прости, что беспокою, но ты же Лёша, так?'

    # '(музыка) КАМАКА – Nerik Cinema'
    $ renpy.display_notify('Сейчас играет:\nКАМАКА – Nerik Cinema')
    play music thirty_five_grad_Nerik_Cinema fadein 2.0

    'Я мог бы и вовсе не заметить такого тихого щебетания, если бы не та самая аура, которая внезапно ворвалась в моё пространство.'
    'Нет, я не верю во всякие астралы и тому подобное, но попав в такое место, чем вожатая не шутит...'

    thirty_five_grad_alex 'Да, я. А с кем имею честь?'

    'Я старался говорить с этой тихоней спокойно, которая вблизи была довольно милой, как и все девушки в этом лагере. Словно на подбор. Чую, что не к добру это.'
    'А возможно, что мне просто так "повезло".'
    show 35grad_lena 1 smile pio with dissolve_fast

    thirty_five_grad_ul 'Лена. Приятно познакомиться.'

    thirty_five_grad_alex 'Да, и мне.'

    'Над нами словно нависла туча средь бела дня. С ней не поговоришь (или подурачишься) так активно, как с Алисой.'
    'Нет той теплоты, как при общении со Славей. Может, тут вина лежит на мне? Я, в принципе, не особо хороший человек, может, она просто видит меня насквозь?'
    show 35grad_lena 1 normal pio with dspr

    thirty_five_grad_ul 'А о чём вы с Алисой говорили, если не секрет?'

    thirty_five_grad_alex 'Да обо всём и ни о чём конкретном. Так, просто бесились. А что, ревнуешь?'
    show 35grad_lena 1 crabbed pio with dspr
    th '...Черт, что ты несёшь? Девушка сильно залилась румянцем, вполне себе ожидаемый эффект. Поставь себя на её место, в конце-то концов...'

    thirty_five_grad_alex 'Прости, шутка дурацкая.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    show 35grad_lena 1 normal pio with dspr
    thirty_five_grad_ul 'Д-да, есть такое. Но не беспокойся, не ты первый. Мы просто с ней очень давние подруги, в-вот.'

    # '(музыка) Between August And December Heather'
    play music music_list['heather'] fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nBetween August And December Heather')

    # '(появляется Алиса)'
    show 35grad_lena 1 normal pio:
        xanchor 0.5 xalign 0.2
    with move

    show 35grad_alice 1 normal joy reb:
        xanchor 0.5 xalign 0.8
    with dissolve

    thirty_five_grad_dv 'Агась, очень давние. Со школьной скамьи и чуть ли не с подгузников!'

    'Неизвестно откуда вылезла Алиса, успев потрепать Лену по голове. Эта картинка была настолько странной, что я протёр глаза в результате того, что они обе пропадут из поля зрения.'
    '...Но нет. Облом.'

    show 35grad_lena 1 crabbed pio with dspr

    thirty_five_grad_ul 'Лёш, не обращай на неё внимания. У кого-то просто настроение хорошее, не так ли?'

    'Но, так или иначе, я всё равно немного улыбнулся от такой милоты. Всегда интересно наблюдать за действиями друзей, как они между собой выясняют отношения и так далее.'
    'Потому что у самого такого практически никогда не было.'

    thirty_five_grad_alex 'Да, ты права.'
    show 35grad_alice 2 hmuri reb with dissolve_fast
    thirty_five_grad_dv 'Но вообще, Лен, парень он вроде хороший. За те пять минут, мы. Только смотри мне, тронешь её хоть пальцем...'
    show 35grad_lena 1 shy pio with dissolve_fast

    'Эта угроза хоть и пролетела мимо ушей, но всё равно оставила что-то после себя.'

    thirty_five_grad_alex 'Больно уж надо.'

    'Фыркнув, я развернулся в другую сторону от них и не просто так. Я заметил, что очередь возле дверей стала рассасываться, и людей становилось всё меньше и меньше.'
    show 35grad_alice 2 shy reb with dissolve_fast
    thirty_five_grad_dv 'Ну ладно тебе, не обижайся!'

    thirty_five_grad_alex 'А кто сказал, что я обиделся? Ты лучше оглянись повыше. Может, совесть увидишь.'

    'Улыбнувшись, она ведёт под руку Лену прямо к столовой. Не имея никакого желания толпиться в самом хвосте, я подобно рыбе проскользнул вглубь людского потока. Хоть где-то пригодилась настырность!'

    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with fade
    $ renpy.pause(1.0, hard=True)
    # '(фон столовой внутри)'
    play sound sfx_open_door_1
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_full

    th 'Духота и густонаселённость. Вечные спутники столовых помещений. Этот факт не обогнул и это место. Любопытно, а вечером здесь будет чуточку спокойнее?'
    th 'Ведь утро только начинается, а я уже готов плюхнуться на раскладушке вожатой, закрыть глаза, и уснуть крепким сном.'
    th 'А потом, когда проснуться, пойти искать ответы или поделать что-нибудь полезное.'

    th 'А тем временем уже подходила моя очередь. Запах свежеприготовленной еды сносил мне крышу, но остаётся только ждать.'
    th 'А пока терпел, в голову пришла мысль, что наш отряд в основном женский. Хах. Даже не знаю, хорошо это или плохо.'

    th 'Прошло время, и вот теперь я стою с подносом, полным еды. Вопрос настал другой – куда мне садиться?'
    th 'Есть одно место рядом с окном, откуда наверняка будет дуть сквозняк, а можно ещё сесть и рядом с ребятами, а именно со Славяной, Леной и Алисой. Не зря они все махали мне.'

    'Недолго думая, я пошёл в направлении окна. Они, конечно же, люди приятные, почти все, но в данный момент я хотел относительной тишины. Тишины для мозга.'
    'Мне срочно нужен покой ото всех, даже собственных мыслей. Я сначала поставил поднос на стол, а затем сел на стул, который на вид был совершенно новым.'

    'Поедание овсяной каши с крепко заваренным чайком было делом неплохим. Я хорошо подкрепился, но этого было недостаточно, поэтому следующей моей целью для утоления голода являлась сладкая, свежеиспечённая круглая булочка.'
    'Её пряный аромат был схож как запах дорогой и любимой девушки. В плане по значимости, конечно же, я же не каннибал.'

    # '(музыка) Sergey Eybog Memories (Piano Version)'
    play music music_list['memories_piano_outdoors']
    $ renpy.display_notify('Сейчас играет: Sergey Eybog - Memories (Piano Version)')

    'Но стоило мне только поднести булку ко рту, как вдруг замечаю на себе изучающий взгляд.'
    'Такой бывает, когда обычно сталкер или типа того наблюдает за своей жертвой и ждёт подходящего момента для обнимашек.'
    'Поэтому поворачиваю голову туда, где приблизительно может находиться угроза. И вижу...'

    # '(вставить арт где Мику смотрит на Лёшу)'
    # scene cg thirty_five_grad_miku_art_stolov with fade
    scene cg day1_miku_animation
    play sound sfx_head_heartbeat
    $ volume(1.5, 'sound')
    '...девочку, которая сидит и смотрит на меня. Её руки скрещены на подбородке и мельком поглядывает на меня. Но было кое-что ещё, что захватило мой дух – её глаза.'
    'Прекрасные, циановые глазки покорили меня полностью. Чёрт возьми, я готов поклясться, что они самые живые у всех в этом таинственном месте.'
    'Отсюда, где я сижу, не очень хорошо было её видно, но я всё равно пытаюсь высмотреть хоть какую-нибудь детальку, ещё одну!'

    # '(цг пропадает)'
    scene bg int_dining_hall_people_day with dissolve
    stop music fadeout 2
    'Я уже встаю специально для того, чтобы подсесть к ней рядом, но кто-то, положив руку на плечо, садит меня обратно.'
    # '(появляется спрайт Шуры)'
    show 35grad_shuric 1 normal pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_dining_hall_people_day at thirty_five_grad_blur with dissolve

    'Им оказался Шурик, который с лёгкой грустью но при этом с улыбкой на лице сообщает:'

    thirty_five_grad_sh 'Лёх, ты уже надумал, куда вступать будешь?'

    'Я покачал головой, но в душе мне хотелось взять нож.'

    thirty_five_grad_alex 'Не, не решил пока что ещё. Мне подумать надо.'

    hide 35grad_shuric 1 normal pio with dissolve

    if persistent.thirty_five_grad_blur_pref:
        show bg int_dining_hall_people_day with dissolve
    play music music_list ['smooth_machine'] fadein 2
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Smooth Machine')
    'И тот печально закивал. На самом деле, я недосказал ему всей правды, так как глаз у меня уже был нацелен на кое-что, а именно – туда, где много музыки.'
    'Тут не нужно иметь трёхзначное айкью, чтобы догадаться, почему.'
    'Место, где не надо толком работать, а даже наоборот – сидеть на стуле и наслаждаться прекрасной (надеюсь на это) музыкой, а главное живой.'
    'А может если повезёт, получится что-то и большее, чем просто игра на гитаре.'

    'Да не, мне нужно думать, как выбраться отсюда, а чёртовы гормоны трубят обо всём остальном, ненужном. Но может быть всё-таки...'
    'Я даже не знаю. Во мне боролись чувства: как первоискателя, так и безопасности, что нужно валить отсюда. Ладушки, буду решать проблемы по мере их поступления.'

    'Перед тем как выйти из столовой, я взглянул напоследок ещё один раз на ту прекрасную аквамариновую деву, которая в этот момент потихоньку потягивала из кружки чай.'
    'Не знаю, что в ней было такого, вот только захватила она большую часть моих мыслей...'

    # '(музыка стоп)'
    stop music fadeout 2.0
    stop ambience
    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with fade
    $ renpy.pause(1.0, hard=True)
    # '(фон концертной площади)'
    scene bg ext_stage_normal_day with dissolve
    play ambience ambience_camp_center_day fadein 6
    'Погода на улице становилась всё жарче и жарче, а тем временем мои ноги вынесли меня чёрт знает куда. Этого места мне Славяна не показывала.'
    'Если вкратце, то, похоже было на небольшую концертную площадку, которая словно нависала над мной. Было в ней что-то такое, угрожающее, словно так и грозило смертью.'

    'Но это всё бурная фантазия, конечно же. Обычная площадка, где выступают музыканты и, скорее всего, она.'
    'Опустил голову вниз и увидел, как из кармана шорт торчит кусочек той самой бумажки – обходного листа.'

    'Торопиться всё равно было бесполезно, так как ещё только самое утро, все расслабленно плетутся до мест своих работ или обязанностей. А я что?'
    'Я как кочевник пока что никому и ничему не принадлежу, свободно могу ходить туда, куда вздумается.'

    'Я присел на одну из лавок, которая находится в тени и прикрыл немножко глаза. Почему? А всё просто. Тишина и покой.'
    'Нет шумных голосов, а только слабый ветерок, пение птичек да лёгкое поскрипывание лавки рядышком... {w} Так, стоп!'

    # '(музыка) Between August And December That's Our Madhouse'
    play music music_list['that_s_our_madhouse'] fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nBetween August And December - Thats Our Madhouse')

    # '(спрайт Алисы обычная эмоция)'
    show 35grad_alice 2 normal reb with dissolve_fast:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_stage_normal_day at thirty_five_grad_blur with dspr

    thirty_five_grad_dv 'Лёхич, решил спрятаться ото всех, да? Затворники долго не живут.'

    'Этот голос я узнаю из тысячи, ведь нотки лёгкой агрессии смешиваются с ванильной мягкостью самого голоса, и создаётся уникальная смесь.'

    thirty_five_grad_alex 'Да, Алис. А что, как-то тебе этим помешал?'
    show 35grad_alice 2 hmuri reb with dspr
    thirty_five_grad_dv 'Нет, дуралей.'
    'Похлопала по спине легонько, но удар чувствуется. А у неё крепкая рука.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    show 35grad_alice 2 shy reb with dspr
    thirty_five_grad_dv 'На самом деле, это моё любимое место, и тоже обычно с утра прихожу сюда. Здесь одиноко и хорошо, никто не мешает, кроме тебя.'

    # '(музыка) КАМАКА – Nerik Cinema'
    $ renpy.display_notify('Сейчас играет:\nКАМАКА – Nerik Cinema')
    play music thirty_five_grad_Nerik_Cinema fadein 2.0

    thirty_five_grad_alex 'Я могу уйти.'
    show 35grad_alice 2 sad reb with dspr
    thirty_five_grad_dv 'Да нет же, останься. Редко тут нормального парня встретишь. С виду.'

    thirty_five_grad_alex 'А кто сказал, что я нормальный? Мы знакомы минут десять от силы.'
    show 35grad_alice 2 normal reb with dspr
    thirty_five_grad_dv 'Верно, но ты уже круче этих мамкиных изобретателей.'

    thirty_five_grad_alex 'Даже не знаю, считать это как за комплимент или нет.'
    show 35grad_alice 2 smile reb with dspr
    'Девушка по хищному улыбнулась, но в этот раз угрозы я не чувствовал.'
    thirty_five_grad_dv 'А вот тут уже сам думай, оболтус! Девушке не прельщает то, чтобы она все секреты рассказывала проходимцу!'

    show 35grad_alice 2 laugh reb with dspr
    'Мы оба рассмеялись, негромко, но с душой.'
    thirty_five_grad_alex 'Эта площадка заброшена, что ли? Выглядит потрёпанной.'
    show 35grad_alice 2 normal reb with dspr
    thirty_five_grad_dv 'Нет, тут концерты да выступления обычно проводят. Только про ремонт обычно забывают почему-то. А, ещё!'

    'Она резко встала с лавки, да настолько, что чуть и вовсе не упала сама на спину. Встав в горделивую позу, как командир батальона, а то и выше, высказалась:'
    show 35grad_alice 2 smile reb with dspr
    thirty_five_grad_dv 'Перед тем, как я сделаю тебе предложение, от которого нельзя отказаться, скажи – ты умеешь играть на гитаре?'

    thirty_five_grad_alex 'Нет, была мысль ранее попробовать начать, но откладывал постоянно. А что? Хочешь предложить научить?'
    show 35grad_alice 2 sad reb with dspr
    'Теперь хитро улыбнулся уже я, а девушка мимолётно стала грустной, но тут же вернулась в прежнее расположение духа.'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'Конечно... {w}Нет! Я ж тебе не нянька. Фигово, конечно, что не умеешь, но ничего. Будешь познавать истинную культуру, значит.'
    thirty_five_grad_dv 'Я приглашаю тебя приходить сюда время от времени. Часто тут играю в одиночку.'

    thirty_five_grad_alex 'Звучит здорово, приду как-нибудь. Так, подожди. Это получается, в каком кружке ты состоишь? Музыкальном?'
    show 35grad_alice 2 normal reb with dspr
    thirty_five_grad_dv 'Не угадал, Шерлок. Не хватало ещё в том месте сидеть, а то рыбой провоняю ещё. А так, вообще ни в каком. Я сама по себе.'

    'Гордо выпятив носик, произнесла Алиса.'

    thirty_five_grad_alex 'О как. А как же Ольга, или ей всё равно?'

    thirty_five_grad_dv 'А она что? Да, боролась с этим, но потом забила пятиметровый болт. Хорошо, что не в меня.'
    thirty_five_grad_dv 'Эта дурацкая вожатая вообще делает вид, что меня не существует, от этого мне и легче.'

    'Полезная информация, но как её применить? Это как в доисторических компьютерных квестах. Сидеть с ней, конечно же, хорошо, но мне нужно двигаться отсюда подальше.'
    'Устал сидеть, да и говорить, что удивительно, было не о чем.'

    thirty_five_grad_alex 'Ладно, потопал я дальше. Мне же ещё этот дурацкий список заполнять.'

    'И, хищно посмотрев на него, ответила:'
    show 35grad_alice 2 shy reb with dspr
    thirty_five_grad_dv 'Хочешь, могу заполнить его я. Умею так, что никто не отличит без специальной аппаратуры.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    'Чертовка говорила настолько возбуждающим весь мой внутренний мир тоном, что я не мог ей отказать.'
    'Но всё-таки пересилил себя, ведь иначе упущу возможность посетить все места здесь, а это потеря нужных мне ответов.'

    thirty_five_grad_alex 'Нет, я откажусь, пожалуй.'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'Ну и иди, я припомню тебе это ещё.'

    'Взглянув через плечо, ответил:'

    thirty_five_grad_alex 'Я это запомню. До встречи, лисичка.'
    show 35grad_alice 2 shy reb with dspr
    'Даже не оборачиваясь на неё, можно было понять, что раскраснелась она под цвет волос, ну или своего дурацкого галстука. Впервые за долгое время я улыбаюсь от чистого сердца.'

    # '(затемнение (раньше это было обычное моргание))'
    show black with fade
    $ renpy.pause(1.0, hard=True)
    # '(фон площади)'
    play ambience ambience_camp_center_day fadein 6
    scene bg ext_square_day with dissolve

    'Я подошёл к центральной части этого лагеря – площади. Чувствую себя как тот самый богатырь на известной картине, который выбирает, в каком направлении ему помереть.'
    'Мрачно? Согласен. Но такие мысли посещают меня только тогда, когда я нервничаю. А почему нервничаю? Если посмотреть на площадь, легко можно понять...'

    # '(музыка) Sergey Eybog Timid Girl'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Timid Girl')
    play music music_list['timid_girl']

    'Толпа детишек занимаются своими делами. Почему их так много? Почему они ведут себя так, словно нет никаких перемещений во времени?'
    'Мой взгляд столкнулся с взглядом Славяны, которая очень старательно подметала пол простенькой метлой, а рядом с ней стояли и делали вид уборки ещё трое шалопаев.'
    'Я подошёл к девушке с желанием помочь:'

    # '(спрайт Слави обычный)'
    show 35grad_slavya 2 normal pio with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day with dissolve

    thirty_five_grad_alex 'Привет, Славяна. Помощь не требуется?'
    'Она мягко улыбнулась мне, и пот с её лба падал большими каплями.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'О, Алексей! Рада видеть тебя! Я с ребятами сама справ...'

    'И тут она поворачивается, и видит то, чего не следует. А именно – как эти пацаны просто стоят и болтают в кружке между собой.'
    # '(злой спрайт Слави)'
    show 35grad_slavya 2 angry pio with dspr

    thirty_five_grad_sl 'Я не поняла! Чего стоим?! Мётлы руки и вперёд! Обед ещё не скоро!'

    # '(спрайт Слави обычный)'
    show 35grad_slavya 2 normal pio with dspr

    'А затем снова повернулась ко мне, и вид её снова стал тёплым.'

    thirty_five_grad_sl 'Ох, извини за сцену. Просто они в кое-чём провинились, поэтому их послали ко мне на помощь. Так-то мне теперь помощь не особо нужна.'
    thirty_five_grad_sl 'А ты, куда путь держишь? Ходишь с обходным?'

    thirty_five_grad_alex 'Наказали их, говоришь? Тогда чем ты так провинилась, что тебя каждый день, наверное, заставляют так горбатиться?'

    'Похоже, она не особо оценила мою поддержку, если судить по её личику. Насупилась, как маленькое дитя.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Не понимаешь ты, глупыш. Это моя работа. Кто, если не я?'
    show 35grad_slavya 2 normal pio with dspr
    'Наступила неловкая тишина и, найдя более-менее пригодный предлог, я попытался уйти.'

    thirty_five_grad_alex 'Прости, Славяна, пойду я, доделывать уже свою обязанность. Не буду мешать.'

    thirty_five_grad_sl 'А куда первым делом пойдёшь?'

    thirty_five_grad_alex 'В музклуб, наверно. А что? Можешь куда-то посоветовать пойти первым?'
    show 35grad_slavya 2 smile pio with dspr
    'Теперь её взгляд стал хитрым, таинственным. О чём она вообще думает, блин?'

    thirty_five_grad_sl 'Хороший выбор. И знаешь, это по-своему философский вопрос. Каждый ходит туда, куда у него лежит душа.'
    thirty_five_grad_sl 'Я вот состою в общих кружках, но редко там появляюсь. Сам понимаешь, надеюсь.'

    thirty_five_grad_alex 'Ого, ты разбираешься в технике?'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Хах, нет! Я занимаюсь ри-{w}со-{w}ва-{w}ни-{w}ем! Если хочешь, могу показать потом, вечером.'

    thirty_five_grad_alex 'Да, с радостью бы глянул.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Вот и отлично! А теперь иди, мне работать надо. До скорого!'
    hide 35grad_slavya 2 smile pio with dissolve
    'Я её всё понять не могу. То она пытается со мной дружить, то резко настроена на работу. Это же нормально?'
    'Понимаю, что вопрос ушёл во вселенную, но всё же. Ладно, хватит стоять. Пора делать свою работу.'

    # '(затемнение (раньше это было обычное моргание))'
    show black with fade
    $ renpy.pause(1.0, hard=True)
    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(фон музыкального клуба)'
    scene bg ext_musclub_day with dissolve

    'Музыкальный клуб находился на примерно, среднем расстоянии от площади. Недалеко, но и не близко. Хотя, когда нужно будет идти в столовую, дорога не займёт много времени.'

    'Идти по красивой, мощёной дорожке было приятно, даже несмотря на то, что по левую сторону от меня начинался глубокий лес.'
    'Он был настолько большим, что захватывал в себя солнечный свет, как голодное животное. Или вечно жаждущий еды солдат.'
    'Понятное дело, я старался не смотреть туда, но всё же.'

    'Само здание одиноко стояло ото всех вдалеке в этой местности. Как одиночка или аутсайдер, оно словно просто хотело быть одно.'
    'Смотря и понимая это, появлялось чувство грусти и лёгкой меланхолии.'

    scene bg thirty_five_grad_ext_musclub_verandah_day with dissolve

    'Зайдя на веранду, я увидел перед собой обычную деревянную дверь с небольшим окошком. На удивление, было плохо видно что внутри из-за падающего солнечного света, но вроде, никого нет.'
    play sound sfx_knock_door7_polite
    'Я постучался, но мне никто не ответил. Может, и правда, никого? Это было бы логично, если не то, что дверь открыта. Потянул её на себя и зашёл внутрь.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(фон музклуба внутри)'
    play sound sfx_open_door_2
    $ renpy.pause(1.0, hard=True)
    scene bg int_musclub_day with dspr
    stop ambience fadeout 2.0

    'Внутри прохладно. Было даже лучше, чем в домике вожатой. Ещё так и царила атмосфера одиночества и уныния.'

    play ambience ambience_music_club_day fadein 1

    'Но и было что-то такое светлое, приятное и тёплое, словно вернулся в родной дом. А рыбой тут и не пахнет совсем, к слову.'

    'Изнутри клуб казался ещё меньше но, чёрт возьми, это даже к лучшему. Лишние пустые пространства ни к чему.'
    'Но затем мои уши услыхали чьё-то негромкое пение, но мелодичное и красивое.'

    'Я оглянулся, но так никого и не увидел. А вместо того чтобы позвать кого-нибудь, просто прошёлся чуть дальше.'
    # '(музыка) Sergey Eybog хз как та музыка называется из пошлых моментов в бл'
    play music music_list["eternal_longing"] fadein 2
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Eternal Longing')


    'Увидел рояль, а затем мой взгляд опустился, и я заметил чьи-то тоненькие, но очень аккуратные и стройные ножки в тёмных чулках до коленок в чёрно-серых туфельках.'
    'Но чуть погодя, когда мои глаза дошли до секретной, женской части...'

    # '(арт 3 с оригинальной цензурой оригинального арта из бл, где Мику под роялем)'
    scene cg thirty_five_grad_pancu_shot with fade

    '...Особо выделенной и на вид очень мягкой, как свежая булка. Времени словно не существовало вовсе, я смотрел как заворожённый.'
    'Мало того, что девчушка тихо пела про себя, так она ещё и легонько покачивала бёдрами так, словно...'

    # '(цг пропадает)'
    scene bg int_musclub_day with fade

    # '(музыка стоп)'
    stop music fadeout 2.0

    '...Внезапно даже для себя, моя нога топнула по деревянному полу достаточно громко, чтобы оглохнуть.'
    play sound thirty_five_grad_oi1
    thirty_five_grad_mi_unk 'Ой!'
    play sound sfx_piano_head_bump
    $ renpy.pause(1.0, hard=True)

    'Поэтому девушка, сидящая под роялем, крепко приложилась головой об его днище, отчего мне стало стыдно.'

    'Воскликнули я и незнакомка. Я сразу же нагнулся к ней и, взяв за очень нежную, но при том крепкую ладонь, помог девушке подняться.'

    # '(музыка) Sergey Eybog Waltz Of Doubts'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Waltz Of Doubts')
    play music music_list['waltz_of_doubts']

    # '(появляется спрайт Мику покрасневшая)'
    show 35grad_miku 3 shy pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_blur with dspr

    thirty_five_grad_mi 'Ой, спасибочки большое! Я не ожидала, что кто-то может зайти, поэтому с утра пораньше решила провести уборку!'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ах, прости, я не представилась! Меня Мику зовут, правда-правда!'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Не удивляйся, я родом из Японии, поэтому и такое имя и... внешность. Моя мама японка, она у меня актриса, а папа русский – он главный инженер!'
    thirty_five_grad_mi 'В последний раз атомную электростанцию проектировал на родине, представляешь! Правда, только пока чертежи... Но да ладно, благодарю ещё раз!'

    'Её циановые глазки полностью захватили мой разум, унося его куда-то за задвижки души, а уши, несмотря на её безумно быструю речь, ловил каждое её слово, как радар.'
    'И что удивительно, мне это нравилось.'

    thirty_five_grad_alex 'Да на здоровье, прости, что так получилось. Мне стоило позвать как-то или типа того, вот.'
    thirty_five_grad_alex 'Ты как, всё нормально? Голова не болит? А то сильно ударилась, стук громкий был.'

    'Не знаю почему, но говорить с ней было не то, что сложно, а очень волнительно. Я старался подбирать каждое её слово, ибо внутри был страх, что как-то смогу оттолкнуть её.'
    'Интересное было ощущение внутри сердца, мягко говоря...'

    show 35grad_miku 1 smile pio ponytails with dspr

    thirty_five_grad_mi 'Нет-нет! Не вини себя. По сути, это была просто случайность, не более того. О, и это у тебя что торчит из кармана? Обходной? Ты тот самый новичок?'
    thirty_five_grad_mi 'Вообще, ещё раз спасибо! Любой другой бы просто мимо прошёл! Или посмеялся...'
    show 35grad_miku 1 normal pio ponytails with dspr
    'И тут её глазки загорелись ещё сильнее, словно увидели последнюю надежду в своей жизни. Это странно, но выглядело мило. И вдруг мне как-то неловко от того, что я не представился.'

    thirty_five_grad_alex 'Прости, что сразу не сказал, но я Лёша. Приятно познакомиться.'

    'Сначала протянул руку, но потом вспомнил, откуда Мику родом, после чего попытался совершить поклон, но что-то пошло не так, и в итоге я почувствовал себя шутом.'

    'Однако девочка рассмеялась чисто и искренне, отчего и я улыбнулся.'

    show 35grad_miku 2 laughter pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Ой, прости, просто когда это делают люди из другой страны это так мило! Но я очень рада с тобой познакомиться! Редко, очень редко увидишь новые лица...'

    show 35grad_miku 2 thoughtful pio ponytails with dspr

    thirty_five_grad_mi 'Особенно когда сама нечасто появляешься на улице...'

    'Прошептала она концовку, но я всё равно всё услышал.'

    thirty_five_grad_alex 'Но почему? У тебя мало друзей?'

    'Она погрустнела, и я снова почувствовал за это вину.'
    th 'Вот же дурак, ну почему я задаю такие же тупые вопросы, как те репортёры в новостях?!'

    show 35grad_miku 1 normal pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Да... Но ничего! У меня есть чудесная музыка и лучшие инструменты, которые я знала! Хочешь, сыграю тебе на чём-нибудь?'
    thirty_five_grad_mi 'Но погоди, у меня есть идея лучше! Только скажи – ты ещё никуда не вступил?'

    'С ней мне не хотелось ёрничать или юлить, поэтому сказал совершенно честно:'

    thirty_five_grad_alex 'Нет, ещё нет. Но уже подумывал кое-куда.'

    '...А вот поиграть с ней немножко всё же решил. Почему бы и нет? Тем более, если примет, то хочется узнать её поближе, ведь...'
    'В ней мне кажется что-то смутно знакомое... Словно бы она тоже была не отсюда...'

    show 35grad_miku 1 surprise pio ponytails with dissolve_fast

    thirty_five_grad_mi 'О! {w} О-о-о! Куда-куда?!'

    'Удивлению не было предела.'

    thirty_five_grad_alex 'Сюда, если ты не против. Мне нравится музыка, так что, почему бы и нет.'

    'Я думаю, что если бы не её воспитание, то девочка напрыгнула бы прямо на меня. Она почти и хотела это сделать, только вовремя остановилась.'
    'Неловкость зашкаливала, но это всё равно было приятно.'

    show 35grad_miku 2 laughter pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Лёша, ты чего? Конечно не против, а наоборот, я только безумно рада слышать это! Потому что... я...'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ай, это не так важно! Давай свой обходной, подпишу! Не могу поверить даже в такое.'

    play sound sfx_paper_bag
    $ volume(1.5, 'sound')

    'Хоть я его и протянул ей, но всё равно оставался вопрос:'

    thirty_five_grad_alex 'Но почему?'

    show 35grad_miku 2 sad pio ponytails with dspr

    thirty_five_grad_mi 'Я просто не хочу портить сейчас настроение ни тебе, ни себе. Прости за это, но давай лучше поговорим о чём-нибудь другом?'

    thirty_five_grad_alex 'Хорошо...'

    th 'Я понимаю её, ведь кто захочет изливать свою душу каждому встречному? Мне искренне жаль её, и надеюсь, что смогу в будущем хоть как-нибудь помочь.'

    thirty_five_grad_alex 'А ты давно в Союзе живёшь?'

    play sound sfx_paper_bag
    $ volume(1.5, 'sound')
    'Она тем временем взяла с рояля ручку, а из моих рук крайне аккуратно и почти что незаметно вытянула лист.'

    show 35grad_miku 1 normal pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Можно сказать, почти десять лет.'

    thirty_five_grad_alex 'Ого, много!'

    thirty_five_grad_mi 'Да! Но я скучаю немного по родине, хотя... Не знаю. Смешанные чувства. Скорее можно сказать, что желаю снова увидеть природу. Вот её люблю! Особенно горы!'

    show 35grad_miku 1 sad pio ponytails with dspr

    'Грустно вздохнула юная пионерка и стала выводить на бумаге... нет, не слова, а целые иероглифы!'
    'Которые, тем не менее, были мне довольно знакомыми, и даже знал их примерный перевод.'

    thirty_five_grad_alex 'Ми-ку. Как мило.'

    show 35grad_miku 2 laughter pio ponytails with dissolve_fast

    'Я прочитал их вслух, отчего девица выпрямилась по стойке как солдат, и с интересом ребёнка посмотрела мне прямо в глаза.'

    thirty_five_grad_mi 'Как здорово! Ты ещё и язык мой знаешь?! А что ещё умеешь? Как долго учил? Где? Пригодились ли тебе знания?! А может, вообще уехать из этой страны хочешь?!'

    'Её словесный пулемёт М134 калибра 7,62 всё обстреливал меня, не давая и шанса что-либо произнести, но я даже был рад этому. Мне просто приятно находиться в её компании.'

    thirty_five_grad_alex 'Нет-нет, совсем капельку. На самом деле я ведь только начал, и просто нашёл твоё имя немного ироничным. – «Первый звук будущего».'

    show 35grad_miku 3 shy pio ponytails with dissolve_fast

    'Она раскраснелась так, словно я признался ей в любви.'

    show 35grad_miku 3 normal pio ponytails with dspr

    thirty_five_grad_mi 'Лёша. Лё-ё-ёша! Я никогда не встречала в своей жизни людей, которые обращали внимания на такие мелочи, даже у себя на родине.'
    thirty_five_grad_mi 'Хотя, я и там немного прожила, но не важно! Если хочешь, можем в будущем заняться самообучением, я его хорошо знаю! Ну, помимо музыки, конечно.'

    thirty_five_grad_alex 'А что ты ещё знаешь? Или умеешь?'

    show 35grad_miku 2 laughter pio ponytails with dissolve_fast

    'Она стала с гордым видом всё объяснять, мило прикрыв глаза:'

    thirty_five_grad_mi 'Готовить блюда обеих стран, играть на всех музыкальных инструментах, которые ты тут видишь, а также плавать не на «отлично», но всё же.'
    thirty_five_grad_mi 'И люблю ухаживать за детьми! А ты детей любишь?'

    'Я не знал, как ответить ей на такой вопрос, ибо у меня такого никогда и не спрашивали.'

    thirty_five_grad_alex 'Даже не знаю, но не отношусь к ним плохо. Всё зависит от ребёнка, наверное.'

    thirty_five_grad_mi 'О, я тоже так думаю! Рада, что мы сошлись во мнениях! Ой! Прости, я печать не поставила! {w} Вот, готово!'

    thirty_five_grad_alex 'Хорошо, спасибо.'

    show 35grad_miku 2 normal pio ponytails with dissolve
    play sound sfx_head_heartbeat
    $ renpy.pause(1.0, hard=True)

    'А затем мы уставились друг на дружку. Словно хотели что-то сказать, но не могли. Это было тяжело, но по-своему мило и... Приятно. На душе было медово.'

    show 35grad_miku 3 shy pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Я хотела сказать, что благодарю! Благодарю, что ты вступил в мой... наш клуб! Приходи когда захочешь, я буду всегда тебя ждать! В любое время дня и даже ночи!'
    thirty_five_grad_mi 'Хотя, глубоко ночью не надо, я же тоже спать хочу! В общем, рада была познакомиться с тобой... Лёша.'

    'Её щёчки горели очень и очень сильно, и я совру, если скажу, что мои нет. Мне хотелось её немного приобнять, по-дружески прижать к себе, но это было бы очень уж странно, ведь пять минут только как знакомы.'
    'Так что я просто кивнул ей, постарался как можно красивее улыбнуться, и вышел из клуба, помахав на прощанье. Вышел с неприятной пустотой в душе, но зато она была лёгкой...'

    play sound sfx_close_door_campus_1
    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(затемнение (раньше это было обычное моргание))'
    scene bg black with fade
    $ renpy.pause(1.0, hard=True)
    # '(фон библиотеки)'
    scene bg ext_library_day with fade

    th '...Следующим моим пунктом (из четырёх) была библиотека. На самом деле, можно было бы сначала дойти до общих кружков, но тогда нужно совершить крюк.'
    th 'В такую невыносимую жару делать это не хочется от слова совсем.'

    th 'Да, насчёт неё. Время тоже идёт в своём верном направлении; часы и минуты летят как угорелые. Поэтому, чем выше солнце – тем жарче становится на улице.'
    th 'Эх, ещё и кепки нет, а ту, которая была, осталась дома...'

    th 'Вот я и стою возле длинного и вытянутого вдоль горизонта здания. Старое на вид, но всё равно ухоженное и приятное. Судя по табличке возле двери, я в нужном мне месте.'

    'Потихоньку открыл дверь и вошёл. Да, наверное, после музклуба необходимо было постучаться, но мог потом получить нагоняя от библиотекаря.'
    th 'Что тоже было бы нежелательно.'

    # '(музыка) Flawed Mangoes – Tunnel Vision'
    play music thirty_five_grad_flawed_mangoes fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nFlawed Mangoes – Tunnel Vision')
    # '(фон библиотеки внутри)'
    scene bg int_library_day with dissolve
    play sound sfx_open_cabinet_1
    'Внутри было свежо. Не как у Мику, конечно, но тоже по-своему приятно. На стойке гудел маленький вентилятор, а за столом, между прочим, спала библиотекарша.'
    'А точнее, храпела как раненый олень или медведь.'

    'Улыбнувшись от такого поведения, ведь это буквально означало то, что я тут царь и бог (пока девчонка не проснулась, конечно), могу ходить и трогать тут всё, что хочу.'
    'Так, мысли нужно оставить при себе...'

    'Я прошёлся вдоль ближайшей полки, осматривая её содержимое. Обидно, что художественной литературы было мало.'
    'В основном масса из политических высказываний, трактатов философии, а также учебников не только для школы, но и техникумов и вузов!'

    'Вытащив случайный учебник, я ужаснулся в приятном смысле: это же редкий экземпляр по моей специальности!'
    'Чтоб достать его в моём времени, нужно было бы выложить за него немаленькие деньги!'

    '...Но я поставил его обратно. Не то время сейчас, чтобы читать такое. Зато моя рука нырнула на полку выше и вытащила оттуда... Сборник стихов Владимира Маяковского.'
    'Я люблю его творчество, но интересно, какой стих мне попадётся, если я сейчас открою книгу на случайной странице? Вроде, гадание есть такое, но я в это не верю.'

    # '(режм нвл вкл)'
    $ set_mode_nvl()
    nvl show dissolve

    # Стихотворение
    "«Послушайте! Ведь, если звезды зажигают -"
    "значит - это кому-нибудь нужно?"
    "Значит - кто-то хочет, чтобы они были?"
    "Значит - кто-то называет эти плевочки жемчужиной?"
    "И, надрываясь в метелях полуденной пыли,"
    "врывается к богу,"
    "боится, что опоздал,"
    "плачет,"
    "целует ему жилистую руку,"
    "просит -"
    "чтоб обязательно была звезда! -"
    "клянется -"
    "не перенесет эту беззвездную муку!"
    nvl hide dissolve
    nvl clear
    $ renpy.pause(0.27, hard=True)
    nvl show dspr
    "А после"
    "ходит тревожный,"
    "но спокойный наружно."
    "Говорит кому-то:"
    "«Ведь теперь тебе ничего?"
    "Не страшно?"
    "Да?!»"
    "Послушайте!"
    "Ведь, если звезды"
    "зажигают -"
    "значит - это кому-нибудь нужно?"
    "Значит - это необходимо,"
    "чтобы каждый вечер над крышами"
    "загоралась хоть одна звезда?!»"

    # Выключение NVL-режима
    nvl hide dissolve
    $ set_mode_adv()

    '...Забавно очень даже для простого совпадения. Ненавижу намёки! Но стих, между тем, любопытный, как и всё то, о чём писал этот экстравагантный автор.'
    'За своё любопытство за чтением я поплатился тем, что чуть не отдал Богу душу.'

    # '(музыка резко стоп + звук скримера)'
    stop music
    play sound sfx_scary_sting

    thirty_five_grad_alex 'Вожатую побери! Девушка, нельзя же так пугать честного человека!'

    # '(музыка) Between August And December Doomed to be Defeated'
    $ renpy.display_notify('Сейчас играет:\nBetween August And December - Doomed to be Defeated')
    play music music_list['doomed_to_be_defeated']

    # '(спрайт Жени недовольный)'
    show 35grad_zhenya 1 normal angry pio with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg int_library_day at thirty_five_grad_blur with dspr

    '...Слева от меня, в слепой зоне, появляется та самая библиотекарша, у которой вид сменился с милого на «уничтожающего-всё-живое».'
    'Её очки сидели прямо на носу, а жёлтые глаза, как у настоящего орла, словно выдирали из меня всё мясо.'

    thirty_five_grad_mz_unk 'В библиотеке орать запрещено, дубина ты стоеросовая. Мог бы меня разбудить, прежде чем ходить и тыкать во всё вокруг, как макака.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    thirty_five_grad_alex 'А, извините. Смерд просто увидел, что вы наверняка очень важным делом занимаетесь, поэтому не захотел вас беспокоить, простите.'

    'Да, театрал из меня фиговый, но я надеюсь, что девушка не помрёт от испанского стыда. Пускай и зануда, но довольно милая.'
    show 35grad_zhenya 1 normal hmuri pio with dspr
    thirty_five_grad_mz_unk 'Ещё раз так не смешно пошутишь, и вход в моё помещение будет тебе закрыт навсегда, усёк? Зачем пришёл?'

    thirty_five_grad_alex 'Мне это, обходной...'

    'Не успел я договорить, как она выхватывает из рук листок, в три шага сажается за столик, после чего подписывает аккуратным почерком и ставит печать.'
    show 35grad_zhenya 1 normal pio with dspr
    thirty_five_grad_mz_unk 'Вот. Брать будешь что? И побыстрее, пожалуйста, дело не ждёт.'

    'Я решил не играться с Судьбой, поэтому просто махнул рукой.'

    thirty_five_grad_mz_unk 'Ну и слава партии. Вали отсюда и больше не приходи. А может и приходи, мне всё равно.'

    'Какой чудесный и милый сервис! Аж сердечко ёкнуло!'

    thirty_five_grad_alex 'Спокойного сна.'

    'Сказал я ей напоследок, а она, что-то пробурчав в ответ, снова заснула.'

    # '(затемнение (раньше это было обычное моргание))'

    # '(фон библиотеки)'
    play sound sfx_close_door_1
    scene bg ext_library_day with fade

    'Я вышел из библиотеки и снова попал в геенну огненную. Жаркий ветер обдул меня, и я тут же вспотел, как псина сутулая.'
    'Эх, душ принять сейчас не помешало бы! Вот разделаюсь с этим листом и сразу на разведку пойду искать, где же тут душевые.'

    # '(музыка) MIKUMYLOVE'
    play music  thirty_five_grad_mikumylove fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nMIKUMYLOVE')

    'Но не успел я сделать и пары шагов от здания в сторону медпункта, как вдруг меня останавливает пускай и запыхавшийся, но столь милый и знакомый мне голос:'

    # '(спрайт Мику)'
    show 35grad_miku 2 laughter pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_library_day at thirty_five_grad_blur with dspr
    thirty_five_grad_mi 'Лёша! Ух, еле нашла тебя... Сейчас, дай отдышаться...'

    'Я отвёл Мику в тенёк, чтобы она не стояла на солнышке, и не дай бог, получила тепловой удар.'
    'А то она такая хрупкая, словно хрустальная. Хотя и цвет кожи соответствующий...'
    show 35grad_miku 2 sad pio ponytails with dspr

    thirty_five_grad_mi 'Ой, спасибо. В общем, я, правда, тебя еле нашла. Но не просто так! Прости, если отвлекаю тебя...'

    'С ней мне хочется только улыбаться.'

    thirty_five_grad_alex 'Да не переживай, всё хорошо же. Ты что-то хотела? Или просто поболтать?'
    show 35grad_miku 1 smile pio ponytails with dissolve_fast
    'Теперь уже она мне улыбнулась.'
    th 'Если этот лагерь хочет заманить меня в ловушку, используя такого ангелочка как она, то... у него это, блин, получится.'
    th 'И если будет возможность, то заберу её с собой домой. М-да. Прозвучало так, словно она какой-то магнитик. Зато зарубежный!'
    th 'И, где-то на закоулке здравого смысла, шепчет голосок:«Очнись, олух».'

    thirty_five_grad_mi 'Ну да и нет! Просто там, в клубе, я забыла дать тебе ключ от него! Вот видишь, как я тебе доверяю? Так что, Лёша, поздравляю! Ты новый член кружка!'

    'Совершенно играючи протянула девочка.'

    thirty_five_grad_alex 'Даю слово, что не подведу, Мику-сан.'
    show 35grad_miku 3 shy pio ponytails with dissolve_fast
    'Хрен его знает, откуда у меня вырвалось это, но она покраснела. Приятно, однако.'

    thirty_five_grad_mi 'Ха-х! Лёшка, ну ты чего это. Мы же не в Японии. Но всё равно это очень мило так! Словно взрослой себя почувствовала.'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'То есть я уже и взрослая, но не так, как моя ока-сан, например. Ой, прости, «ока-сан» это как по-русски «мама»!'

    'Мы негромко рассмеялись. И правда, с ней не соскучишься!'

    thirty_five_grad_alex 'Спасибо за объяснение, Мику. Но я это и так знал. Как и слово «отец», к слову.'

    # '(спрайт Мику улыбается)'
    show 35grad_miku 3 smile pio ponytails with dissolve_fast

    'А затем её милая мордашка приняла хитрющий вид:'

    thirty_five_grad_mi 'И как же оно будет звучать?'

    'Подловила! Вроде и знаю, но вслух никогда не произносил. Придётся поднапрячься, поэтому собрал все свои мозги в кучку, и выдал следующее:'

    thirty_five_grad_alex 'Эм... Ото-сан?'

    'Последовало пару быстрых кивков. В точку!'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Вот какой мне умный член попался! Теперь-то я уж точно тебя не отпущу никуда!'

    '...Гы, член...'

    # '(спрайт Мику удивлённый)'
    show 35grad_miku 2 surprise pio ponytails with dspr

    thirty_five_grad_mi 'А? Что смешного?'

    thirty_five_grad_alex 'Прости, но я даже играть-то ни на чём не умею, какой же из меня... член.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ой, ну это же дело поправимое! Не волнуйся, со временем придёт. Я тоже не сразу научилась играть на всём. Хотя бы на гитаре, но до конца смены научишься!'

    'А затем её взгляд упал на листок в моей руке. Будь он неладен.'

    # '(спрайт Мику грустный)'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Ох, прости, Лёшенька. Ты тоже беги давай, а то и так тебя задержала...'

    'Девочка резко погрустнела из-за какой-то мелочи.'

    thirty_five_grad_alex 'Мику, я же пообещал, что зайду к тебе, так что вскоре встретимся. И не волнуйся, ничего ты мне не мешаешь. Если хочешь, можем вместе пройтись.'

    '...И, как всегда, последовал отказ. Он совсем меня не ранил, нет. Я привык к такому раскладу. Привык.'

    thirty_five_grad_mi 'Прости-прости, просто у меня самой дела, прости!'

    # '(спрайт Мику пропадает)'
    show 35grad_miku 1 sad pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_library_day with dspr

    # '(музыка стоп)'
    stop music fadeout 2.0
    'Она развернулась, и стремглав бросилась к своему клубу. По крайней мере, я так думаю. Единственное, что я успел ей сказать в дорогу:'

    thirty_five_grad_alex 'Не беги ты так по жаре. Будь осторожней.'

    '...Но она навряд ли услышала мои слова...'

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black with dissolve_fast
    # '(фон медпункта)'
    scene bg ext_aidpost_day with fade

    '...Медпункт. Мне тоже нужно туда. Точно. Совершенно забыл. Может, там мне дадут синюю таблетку.'
    'Дойти до него не составило особого труда, так как он был расположен в сотне метров от библиотеки. Мысли мои были пусты, особенно от того, что произошло пару минут назад.'

    th 'Всё произошло так быстро... Наверняка в отказе виноват я сам, так как, скорее всего, со стороны выглядел полным тупицей.'
    th 'Но я же хотел как лучше! Надеюсь, что это не подпортит наши начавшиеся отношения.'

    'Здание, где лечат травмы, располагалось в гордой позе, если это распространяемо по отношению к вещам и помещению.'
    play sound sfx_knock_door7_polite
    'Пришлось подняться по небольшой лестнице, чтобы оказаться возле входа. В этот раз я уж точно постучался, а то мало ли.'

    thirty_five_grad_cs_unk 'Войдите!'
    'Произнёс женский голос вполне взрослой особы то ли с усталым, то ли измученным тоном. Это сразу говорит мне о том, что меня тут не будут рады видеть.'

    # '(фон внутри медпункта, + спрайт Виолы)'
    play sound sfx_open_cabinet_1
    scene bg int_aidpost_day with dissolve
    show 35grad_viola 1 normal reb with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_aidpost_day at thirty_five_grad_blur

    thirty_five_grad_alex 'Здравствуйте.'

    'Тихо произнёс я, ибо в такой ситуации важен даже тон голоса.'

    thirty_five_grad_cs_unk 'Жалобы? Негодования? Проблемы? Если неприятности душевные – прости, помочь не могу, не психолог, а водку тебе ещё рано.'

    # '(музыка) Between August And December Gentle Predator'
    play music music_list['gentle_predator']
    $ renpy.display_notify('Сейчас играет:\nBetween August And December Gentle Predator')

    'Высокая даже в сидячем положении женщина около двадцати восьми-тридцати лет обладала изысканной статью. Даже сидя ее фигура могла соревноваться с обложками модных журналов.'
    'В особенности она отличалась ото всех своей аурой и... немаленькой груди, а также гетерохромии. Уникальный человек, сразу видно.'

    thirty_five_grad_alex 'Да не, вроде, нету такого.'

    '...Не считая того, что я переместился во времени чуть ли не по щелчку пальцев.'
    show 35grad_viola 2 flirt reb with dspr
    thirty_five_grad_cs_unk 'Тогда тебе нужно подписать обходной, верно? Или ты специально пришёл ко мне, к такой одинокой женщине?'

    'Она легонько прикусила одну из оправы очков. Я охренел, мягко говоря. Всё моё нутро сжалось, как будто на внутренности капнули сока лимона.'

    thirty_five_grad_alex 'Е-если бы я знал, что тут работает такая прекрасная дама, как вы, то и просто так бы зашёл. Но у меня и правда, есть дело, уж простите.'

    'Говорил я хоть и с лёгким заиканием, но лучше уж так, чем промолчать.'
    'А вот вместо ответа она встала, подошла ближе ко мне, очень близко, я мог почуять запах её тела и духов, а затем спокойно вытянула из моих штанов листок...'
    show 35grad_viola 2 sly reb with dspr
    thirty_five_grad_cs_unk 'Пионер, что-то ты не очень расторопный. Хочешь, витаминчиков прописать могу. Б12, например.'

    'Её рука спустилась уже в свой карман халата и достала неоткрытую пачку со шприцом и положила на стол.'
    'Надо валить отсюда, а то вскоре эта сумасшедшая ещё и опыты будет надо мной ставить!'

    thirty_five_grad_alex 'Уж простите, но я откажусь от витаминов, оно того не стоит. Просто поставьте мне уже печать, и это, пойду я, пожалуй...'
    show 35grad_viola 2 angry reb with dissolve_fast
    'Её взгляд резко погрустнел и, после откровенно разочарованного вздоха она одним ловким движением поставила эту роспись и штамп.'
    show 35grad_viola 2 normal reb with dissolve_fast
    thirty_five_grad_cs_unk 'Вот, держи, пионер. Если чего нужно будет, меня тут можешь найти. И вообще – ты же знаешь, куда попал?'

    'Вопрос был с подвохом, но я уже понял, к чему она клонит. Или думал, что понял.'

    thirty_five_grad_alex 'В большой женский коллектив, где нет толком парней?'
    show 35grad_viola 2 hitry reb with dissolve_fast
    thirty_five_grad_cs_unk 'Бинго! И ты же в курсе, что это означает?'

    thirty_five_grad_alex 'Что меня могут с лёгкостью сожрать, если я не покажу, кто здесь мужчина?'

    thirty_five_grad_cs_unk 'Это тоже. Но не исключай варианта, что могут быть склоки, ревности и обиды. Старайся в это не вляпываться, понял? Проведи эти две недели спокойно.'

    thirty_five_grad_alex 'Понял. Мне проблемы не нужны.'

    thirty_five_grad_cs_unk 'Вот и хорошо. Извини уж за мои нестандартные шутки, но ты вроде парень неплохой. Так что ступай теперь и дай мне... отдохнуть.'
    thirty_five_grad_cs 'Кстати, меня Виолетта Церновна зовут. Но можешь и просто Виолой.'

    thirty_five_grad_alex 'А я Алексей. Приятно.'

    # '(музыка стоп)'
    stop music fadeout 1.0
    # '(фон медпункта)'
    play sound sfx_close_door_1
    scene bg ext_aidpost_day with dissolve

    'Не сказав больше ни единого слова, я вышел из медпункта.'
    'Что-то было в ней не так, словно она тоже пришелец или наоборот, самый главный злодей здесь, который и засунул меня сюда.'
    'Не удивлюсь, если у неё под помещением есть секретная лаборатория, где выращивают мутантов. Или прекрасных кошкодевочек...'

    th '...О чём я думаю, чёрт подери?..'

    # '(затемнение (раньше это было обычное моргание))'
    show blink with dissolve
    # '(музыка) Goodbye Home Shores'
    $ renpy.pause(1.0, hard=True)
    play music music_list['goodbye_home_shores']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog Goodbye Home Shores')
    show unblink with dissolve
    scene bg ext_aidpost_day with dissolve
    # '(спрайт Лены улыбающийся)'
    show 35grad_lena 1 smile pio with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_aidpost_day at thirty_five_grad_blur

    thirty_five_grad_ul 'Ой, Лёша! Ты лист заполнял или с тобой что-то случилось?'

    'Не успел я сойти с лестницы, как вдруг натолкнулся, или, скорее всего, это она столкнулась со мной, на Лену.'

    thirty_five_grad_alex 'Нет-нет, не волнуйся. Я по поводу обходного листа приходил. А ты зачем сюда идёшь? Всё в порядке?'
    show 35grad_lena 1 shy pio with dissolve_fast
    'Она немного покраснела. Не так, как Мику, но тоже прилично. Иногда, мне хочется заиметь ту способность Мела Гибсона, когда тот мог читать мысли женщин.'
    'Вот если бы лагерь дал мне её, тогда и всё супер было!'

    thirty_five_grad_ul 'Ой! Да нет, я Виоле помогаю на самом деле. Точнее, нарабатываю навыки медсестры, ведь после лагеря пойду учиться на медицинский, вот...'
    thirty_five_grad_ul 'Но, Лёш, если будет желание – приходи всегда. Рада только буду.'

    'Вот так уж поворотец. Неожиданно. Хотя, если так задуматься, то они не выглядят как голограмма, иллюзия или что-то в этом роде.'
    'Пускай я и знаю их не так уж и много по времени, но они не выглядят как пришельцы.'
    '...Мику уж тем более...'

    # '(спрайт Лены серьёзный)'
    show 35grad_lena 1 crabbed pio with dissolve_fast

    thirty_five_grad_ul 'Алексей, всё хорошо?'

    'Внезапно строго спросила Елена.'

    thirty_five_grad_alex 'А? Да-да, задумался просто.'
    show 35grad_lena 1 normal pio with dspr
    thirty_five_grad_ul 'Ты так аккуратнее, хорошо? Ладно, давай, до обеда.'

    thirty_five_grad_alex 'Давай...'

    hide 35grad_lena 1 normal pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_aidpost_day at thirty_five_grad_deblur

    'И куда делся тот застенчивый вид прошлой Лены? Удивительно... А теперь, последняя контрольная точка и я могу быть свободным!'
    'Наверное. Хочется надеяться на это...'

    # '(затемнение (раньше это было обычное моргание))'
    show black with dissolve
    $ renpy.pause(1.0, hard=True)
    # '(фон общих кружков)'
    scene bg ext_clubs_day with dissolve
    'Идти до общих кружков было тяжело морально: ведь последний бой всегда самый трудный. Вот и у меня сейчас та же ситуация...'

    'Хоть я и недавно здесь, но чёртова жара меня уже достала. Точно, нужно будет достать панамку где-нибудь, иначе без неё чокнуться можно.'

    'А тем временем я уже успел подойти к зданиям общих кружков, мимо которых мы со Славей проходили с самого утра.'
    'В отличие от остальных помещений, это выглядело потрёпанным и старым. Видимо, оно повидало многое на своём веку.'

    'Слева от двери висит табличка со стёртыми надписями, которые невозможно прочитать. То есть, местным жителям абсолютно всё равно на то, что происходит с этим местом?'
    'Странно, хотя это и придаёт лагерю некой «живости».'
    'Что это не просто место вне времени и пространства, а действительно одно из мест нашей большой страны, просто в другом временном отрезке.'

    'Я заметил, что чем больше времени нахожусь здесь, то тем меньше мне страшно за самого себя. Все ужасы отходят на второй план, хотя... Рановато.'
    'Ведь, а что будет, когда эта смена подойдёт к своему финалу? Меня просто выкинет обратно, в свой мир и на этом всё?'

    # '(фон внутри клуба)'
    play sound sfx_open_door_clubs
    scene int_clubs_male_day with dissolve

    'Внезапно обнаружил себя, находящимся внутри клуба. Да-а-а, не побоюсь этого выражения: «технический рай»!'
    'Множество всяких инструментов, разобранных и собранных механизмов, какие-то наработки, а над потолком и вовсе склеенные модели самолётов.'
    'Припоминаю, что у меня в детстве были похожие вещи. Как мило.'

    # '(спрайт Эла)'
    if persistent.thirty_five_grad_blur_pref:
        show bg int_clubs_male_day at thirty_five_grad_blur
    show 35grad_electronnik 1 normal pio:
        xanchor 0.5 xalign 0.2
    with dissolve

    thirty_five_grad_el 'О-о-о, кто к нам пожаловал!'

    'Радостно заявил Электроник, выходя, скорее всего, из подсобки.'

    thirty_five_grad_alex 'Да, да. Неужели ждал?'

    # '(спрайт Шуры)'
    show 35grad_shuric 2 smile pio:
        xanchor 0.5 xalign 0.8
    with dissolve

    thirty_five_grad_sh 'Ждали. Так будет вернее сказать.'

    'Высказался уже Александр более-менее спокойно, тоже выходя из подсобки.'

    thirty_five_grad_el 'Как видишь, Алексей, мы в технике разной копаемся. Что хочешь, отремонтируем. Правда, с такой просьбой к нам почти не обращались.'
    thirty_five_grad_el 'Так что если у тебя что-то сломается, тащи сюда сразу. А если ты хочешь присоединиться к нам, то мы будем рады видеть тебя на наших общих кружках!'

    'Уверенно заявил Электроник. Повисло неловкое молчание.'
    show 35grad_electronnik 1 hmuri normal pio with dspr
    thirty_five_grad_el 'Ну, ты к нам по делу или просто так? Извини, мы сейчас сильно заняты, поболтать пока что не можем.'

    thirty_five_grad_alex 'Грустно, конечно, но и правда, по делу. Подписать нужно.'
    show 35grad_shuric 2 normal pio with dspr
    thirty_five_grad_sh 'Только ответь на вопрос: ты уже...'

    'И я перебил его:'

    thirty_five_grad_alex 'Да. Уже в музклубе. Простите ребят, там была просто одна особа, которой я уж не мог отказать.'

    thirty_five_grad_el 'Любитель редкости.'

    'Пробурчал Эл. Честно говоря, мне эта его клоунская манера не очень понравилась.'

    thirty_five_grad_alex 'Что ты сказал?'

    thirty_five_grad_sh 'Тебе показалось. Давай листок, подпишу. Но ты всё равно заглядывай иногда.'

    'Хоть Саня и встал на защиту друга, но я и сам тут же остыл. Не стоит нарываться на неприятности с самого начала знакомства, хотя за Мику и было обидно до чёртиков, что её сравнили с вещью.'

    thirty_five_grad_el 'А, Лёх, погоди.'

    thirty_five_grad_alex 'Чего тебе?'

    thirty_five_grad_el 'А ты умеешь паять там, собирать, чертить? Да и с мелкой моторикой как?'

    thirty_five_grad_alex 'Умею всё то, что ты перечислил, вдобавок к этому ещё работать с электричеством и, если необходимо, проложить дома проводку.'

    'Парни остолбенели на секунду-другую, но тут же пришли в норму. Их выражение лиц было печально-радостным...'

    thirty_five_grad_sh 'Эх, жалко, такие руки пропадают...'

    # '(фон кружков на улице)'
    play sound sfx_close_door_1
    scene bg ext_clubs_day with dissolve

    'Я попрощался с ними, после чего вышел отсюда. Вроде и парни неплохие, но всё же рад, что не попал к ним.'
    'Хотя, может, я зря записался к Мику в музклуб? Поторопился и тому подобное...'

    'Вспоминая её круглое милое личико, которое буквально искрилось от счастья, я понял, что записался всё же не зря.'
    'Пускай для меня это много и не значило, но зато для неё – чуть ли ни счастье всего мира.'

    'Надо будет зайти к ней ещё сегодня, а сейчас вернуться к домику и отдать этот листок. Времени прошло уже много, заодно стоит спросить, когда наступает обед и ужин.'
    'Поднял голову наверх – облака медленно плыли по небосклону, а бледно-синяя поверхность примеряла на себе голубоватые цвета...'

    # '(музыка стоп)'
    stop music fadeout 1.0
    # '(фон домика вожатой)'
    scene bg ext_house_of_mt_day with dissolve

    'Ещё не подходя к домику, можно было увидеть, как хорошо «трудится» Ольга Дмитриевна на шезлонге с книжкой в руках. Везёт же некоторым!'
    'Хотя, честно сказать, у всех есть свои трудности, и если сейчас человек отдыхает, то это значит, что он это заслужил.'

    'Я подошёл к ней аккуратно, но она всё равно заметила меня, после чего и вовсе поднялась с лежанки, поправила свою форму, которая помялась на уровне бёдер и груди, после чего спросила:'

    # '(спрайт Ольги обычный)'
    show 35grad_olga 2 normal form with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_blur

    thirty_five_grad_mt 'О, Алексей, а ты не особо торопился? Ладно, не переживай, всё хорошо. Рада, что ты вернулся на самом деле, ведь обычно ребята сильно затягивают с этим.'

    thirty_five_grad_alex 'Да всё хорошо, Ольга Дмитриевна. Просто заодно по лагерю погулял, изучал местность, с людьми знакомился. Вот...'

    thirty_five_grad_mt 'А записался ли куда-нибудь?'

    'И, как назло, моя покрасневшая рожа лица прекрасно выдала.'
    show 35grad_olga 3 normal form with dissolve_fast
    thirty_five_grad_mt 'Ла-а-адно, в данном случае можешь и не говорить, так как сама поняла, куда.'

    thirty_five_grad_alex 'Но... как?'

    thirty_five_grad_mt 'Да легко. У нас, в лагере, всего одно место, где сидит очень красивая, одинокая пионерка, жаждущая внимания и мужского плеча. Только прошу тебя, не увлекайся.'

    thirty_five_grad_alex 'То есть?'
    thirty_five_grad_mt 'Не играйся с её чувствами. Если понял, что разлюбил, то просто тихо расстаньтесь, а не тяните до последнего. Хуже будет.'

    thirty_five_grad_alex 'Но кто вам вообще сказал, что у меня к ней есть чувства? Тем более что мы с ней несколько часов знакомы.'

    'Этот диалог надо было быстрее кончать, чтобы он не принял неправильные повороты.'
    'У меня к ней нет вообще чувств, кроме как чувства общения и... маленького огонька сердечного любопытства.'
    show 35grad_olga 3 angry form with dissolve_fast
    thirty_five_grad_mt 'Лёша, поверь мне. Я работаю здесь не первый год и много чего повидала. Конечно, вы знакомы недавно, но и пирамиды не строились за пару дней.'
    thirty_five_grad_mt 'Подростковые отношения, они такие. Глазом не успеешь моргнуть, а уже страстно целуетесь на фоне красивого заката. Просто позволишь дать маленький совет?'

    thirty_five_grad_alex '...Да, конечно.'

    thirty_five_grad_mt 'Девочка молода и наивна, так что не пользуйся этим. Будь мужчиной. Защищай и оберегай, хорошо? Я надеюсь на тебя.'

    # '(музыка) Sergey Eybog что-то из спокойной'
    play music music_list['take_me_beautifully'] fadein 2.0
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog Take Me Beautifully')

    'Я хитро улыбнулся.'

    thirty_five_grad_alex 'Но на самом деле просто вам проблемы с бумажками не нужны, так?'

    # '(спрайт улыбающийся Ольги)'
    show 35grad_olga 3 normal form with dspr

    thirty_five_grad_mt 'Это тоже верно, но и всё равно я забочусь о ней так же, как и обо всех своих подопечных.'

    thirty_five_grad_alex 'Хорошо, я обещаю.'

    thirty_five_grad_mt 'Вот и отлично.'

    thirty_five_grad_alex 'Тогда я спрошу: а во сколько у нас обед и ужин?'

    thirty_five_grad_mt 'Пионер, как и солдат, всегда голоден, не так ли? В двенадцать дня и шесть вечера. А для детей и полдник есть.'

    thirty_five_grad_alex 'А я тоже ребёнок в какой-то степени!'
    show 35grad_olga 3 smile form with dspr
    'На что мы рассмеялись.'

    thirty_five_grad_mt 'Ребёнок не может быть почти что выше своей вожатой! Ладно, меньше слов больше дела! Готовься к обеду и отдохни.'

    'Она снова легла на шезлонг, а я зашёл в домик.'

    # '(фон домика вожатой внутри)'
    play sound sfx_open_dooor_campus_2
    scene bg int_house_of_mt_day

    'Не знаю, права ли Ольга, но сердце моё говорит мне, что да. А может, так сыграл нежный тембр голоса вожатой?'
    'Всё может быть. Через пару мгновений, открывается дверь.'

    # '(спрайт Ольги)'
    show 35grad_olga 2 angry form with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_day at thirty_five_grad_blur

    thirty_five_grad_mt 'Алексей, всё то, что я сказала, относится не только к Мику, но и ко всем девушкам нашего отряда. Ты же это понял, надеюсь?'

    thirty_five_grad_alex 'А, то есть, с девушками из других отрядов я могу играть?'

    thirty_five_grad_mt 'Ещё одно слово, и ночевать будешь в больничке. А там уж я не знаю, что с тобой будет делать Виола...'

    'Ласково, но в то же время, – угрожающе произнесла вожатая.'

    thirty_five_grad_alex 'Хорошо, молчу, не дурак. Дурак бы не понял.'
    show 35grad_olga 3 normal form with dissolve_fast
    thirty_five_grad_mt 'Вот и замечательно!'

    # '(музыка стоп)'
    stop music fadeout 2.0

    'И снова закрыла за собой дверь. Боже, хотя бы в этом домике будет минута спокойствия?'

    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with fade

    'Судя по времени на телефоне, до обеда оставалось примерно десять минут. Лучше заранее дойду до столовки, пока не прозвучал горн.'
    # '(фон домика вожатой снаружи)'
    play sound sfx_close_door_1
    scene bg ext_house_of_mt_day with dspr

    'Когда вышел из домика, то понял одну деталь: в отличие от завтрака, на обед и, скорее всего на ужин тоже никто не ходит строем.'

    'А это только мне на руку! Буду добираться в тишине и спокойствии. Но зато вот думаю, а вообще, стоит ли идти туда?'
    'Я не очень-то и голоден, лучше бы поваляться на кровати, пока есть возможность.'

    # '(музыка) Sergey Eybog Timid Girl'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Timid Girl')
    play music music_list['timid_girl'] fadein 2.0
    # '(спрайт обычной Слави)'
    show 35grad_slavya 2 normal pio with dissolve:
        xalign 0.5 xanchor 0.5

    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_blur

    thirty_five_grad_sl 'О чём думаешь, если не секрет?'

    'Внезапный голос Славяны прервал меня из раздумий.'

    thirty_five_grad_alex 'Да так, мелочи.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Да кались. Мне же интересно. Или совсем личное?'

    thirty_five_grad_alex '... Ну, стоит ли идти на обед. Я лично полежать хочу, полдня на ногах.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'А-а-а.'

    'Девушка забавно фыркнула, после чего мило мне улыбнулась. Всё же, и в ней было что-то такое, что запало мне в душу, словно чернила в воде.'

    thirty_five_grad_sl 'Стоит. Ещё как. Человек, а в особенности парень, будущий защитник родины, не должен голодать, а отдохнуть всегда успеешь.'
    thirty_five_grad_sl 'Не волнуйся, Ольга Дмитриевна не будет тебя гонять после обеда. Всё же ты пока у нас первый день.'

    thirty_five_grad_alex 'Слушай, а ты к вожатой всегда так, на имя-отчество? А то она-то мне ро...'

    'Дурак! Чуть не проговорился!'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'А? Ты это о чём?'

    thirty_five_grad_alex 'Не обращай внимания, язык заплёлся.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Бывает, не переживай. Давай вместе пройдёмся до столовой. Ты не желаешь составить мне компанию?'

    thirty_five_grad_alex 'Конечно да. После вас.'

    # '(затемнение (раньше это было обычное моргание))'
    show black with dissolve
    # '(фон домиков + спрайт Слави)'
    scene bg ext_houses_day with dissolve

    show 35grad_slavya 2 normal pio with dissolve:
        xalign 0.5 xanchor 0.5

    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_day at thirty_five_grad_blur

    thirty_five_grad_sl 'Лёш, я слышала, что ты уже успел кой-куда записаться.'

    'Сказала блондинка не без интереса.'

    thirty_five_grad_alex 'Ну, да. А что? Нельзя? Просто вот парни этим недовольны были особо.'

    'На что помощница лишь пожала плечами.'

    thirty_five_grad_sl 'Да мне всё равно как-то. Просто поинтересовалась, а то, что ребята так отреагировали – они просто завидуют тебе! Я тебе так скажу.'
    thirty_five_grad_sl 'Мику – очень интересный человек. Хоть сама с ней не особо долго общаюсь, при этом знакомы года два, но она очень хорошая. И... {w} по секрету...'

    # '(спрайт Слави смущённый)'
    show 35grad_slavya 2 shy pio with dissolve

    'Девушка вновь покраснела. Провайдером клянусь, я в жизни не видел столько краснеющих девушек, как за сегодняшний день.'

    thirty_five_grad_sl 'Я думаю, что из вас получилась хорошая пара... друзей.'

    'И опять она спешит. Точно уж младшая копия вожатой!'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_alex 'Славяна, и ты туда же! Да, она очень приятная, но и ты тоже... Вообще, я знаю её полдня-то.'

    'Затем, девушка подошла ко мне ближе, склонилась над ухом и прошептала:'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Всему. {w} Своё. {w} Время.'

    'И подмигнула.'

    thirty_five_grad_alex 'Хорошо, я понял тебя.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Вот и славненько! А ещё, скажу кое-что. Зови меня Славей. А то полное моё имя немного... раздражает.'

    thirty_five_grad_alex 'Ух ты. Это ещё почему?'
    show 35grad_slavya 2 surprised pio with dspr
    thirty_five_grad_sl 'Слишком уж официальное.'

    thirty_five_grad_alex 'Даже так, не ожидал. Ладно, Славя, буду знать.'

    thirty_five_grad_sl 'Ловишь на лету, мне это нравится. О-о-о, смотри, кто там идёт.'

    'Девушка внезапно дёрнула меня за край рукава. Часть её руки коснулась моей руки, вызвав приятную дрожь на месте касания.'

    thirty_five_grad_alex 'Куда?'

    'А вместо ответа она указала аккуратно так, пальчиком чуть поодаль нас, с левой стороны. И там стояла Мику, но она была не одна, а с Алисой.'
    'Они вроде не спорили, но их разговор не был особо приятным.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    thirty_five_grad_alex 'Ты же это тоже заметила, да?'
    show 35grad_slavya 2 worry pio with dspr
    thirty_five_grad_sl 'А то.'

    thirty_five_grad_alex 'Пойду-ка я посмотрю, что у них там происходит. Вдруг, помощь нужна будет.'

    thirty_five_grad_sl 'Хорошая идея, но пойду с тобой, а то мало ли.'

    'Мне было всё равно, ведь медлить я не хотел от слова совсем. Если я смогу помочь предотвратить скандал или спор, то сделаю это.'

    # '(музыка) вставь какую-нибудь нагнетающую музыку из оригинального бл'
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Just Think')
    play music music_list ['just_think'] fadein 2.0
    # '(спрайты на экране Мику (испуганной), Алисы (хитрой) и Слави)'
    show 35grad_miku 2 fear pio ponytails:
        xanchor 0.0 xalign 0.0 yalign 1.0 # Слева
    with dissolve_fast
    show 35grad_alice 2 tricky reb:
        xanchor 0.5 xalign 0.5   # В центре
    with dissolve_fast
    show 35grad_slavya 2 worry pio:
        xanchor 1.0 xalign 1.0  # Справа
    with dspr

    thirty_five_grad_dv 'Мику, ну и каким же способом ты заманила его к себе? Всё тем же способом? Или что-то новенькое придумала? Признавайся, а то я ж любопытная, ты знаешь.'

    'Хорошо было видно, как противоположной девочке был крайне неприятен этот разговор.'
    'Словно всё её нутро сейчас борется, чтобы она не сорвалась, но при этом, смотря на Алису, нельзя точно сказать, говорит она со злостью или же нет.'
    'Вроде, спокойно, хоть и не без ехидства, интересуется.'

    thirty_five_grad_mi 'Алиса, ну хватит, прошу тебя. Лёша просто пришёл. Ему первому понравился мой клуб. Я что, должна была ему отказать?'
    thirty_five_grad_mi 'Когда год назад ты также приходила ко мне, то и я тебе предлагала, но ты отказалась! Да и что говорить, я предложила тебе ещё две недели назад, с начала смены, но ты тоже рога упёрла!'
    thirty_five_grad_mi 'Зато вот как гитару свою заносить, так без колебаний, пожалуйста!'
    show 35grad_alice 2 laugh reb with dspr
    thirty_five_grad_dv 'Не понимаешь что ли того, что я не могу вступать в клубы, потому как это накладывает обязательства? А мне этого ой как не надо.'

    # '(спрайт Мику пропадает)'
    hide 35grad_miku 2 fear pio ponytails with dissolve
    # '(музыка стоп)'
    stop music fadeout 2.0

    'А затем Мику и вовсе развернулась на 180 градусов и ушла, скорее всего, в столовую. А может и в клуб.'
    'Мне стало жаль её, ведь я такой же одиночка, как и она, и поэтому прекрасно понимаю эту боль. Вздохнув, направился к Алисе.'

    thirty_five_grad_alex 'Ну что, довольна? Довела девочку?'
    show 35grad_alice 2 fear reb with dspr
    thirty_five_grad_dv 'А? Блин, Лёх, Славя, зачем так из-за спины-то подходить? А если б у меня бита была?'
    show 35grad_slavya 2 angry pio with dspr
    thirty_five_grad_sl 'Не была бы. Тебе и тяпку опасно доверять, не то, что холодное оружие.'
    show 35grad_alice 2 sad reb with dspr
    'Недовольно высказалась Славя, а Алиса лишь тяжело вздохнула.'

    thirty_five_grad_alex 'Алиса, я не думаю, что стоит быть такой грубой с Мику. Она не ровня тебе в этом плане.'
    show 35grad_alice 2 thinking reb with dspr
    thirty_five_grad_dv 'Ох, ну ты хотя бы не нуди, Лёх. Не разочаровывай меня.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Вообще-то, он дело говорит. Не всегда стоит искать себе соперников. А теперь, хватит болтать, я есть хочу. Пойдёмте все в столовую.'

    thirty_five_grad_dv 'Хорошо сказано, госпожа вожатая!'

    # '(спрайт Слави смущённый)'
    show 35grad_slavya 2 shy pio with dspr

    'Сказала Алиса, на что Славя смутилась в алую краску.'

    thirty_five_grad_sl 'Ой, да куда мне до неё!'

    'Вот так вот и была разрешена небольшая, но печальная ситуация. Теперь хорошо понимаю, почему Мику одна.'
    'Редко кто за неё заступается и понимает её чувства, а это значит, что я должен буду стать для неё той самой стеной и поддержкой.'
    'Да и, в общем, не буду противиться этому, так как отчасти приятно, когда ты о ком-то заботишься, не так ли?'

    # '(затемнение (раньше это было обычное моргание))'
    show black with dissolve
    # '(фон столовой внутри)'
    play sound sfx_open_cabinet_1
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_camp_center_day

    'Оказывается, во время обеда в столовой не так уж и шумно, как на завтраке.'
    'Неужели детишки за день успевают настолько уставать, что им тоже хочется тишины и спокойствия? Никогда не думал об этом.'

    'Я стою с подносом в руках и ищу свою цель, ведь я должен с ней пообщаться насчёт того, что произошло недавно.'
    'Хоть это и может подождать после приёма пищи, но я не смогу иначе успокоить своё... любопытство.'

    'А искать долго не пришлось, ибо нет такой девушки в этом месте, которая настолько ярко выделяется цветом волос.'
    'Сидела она на самом дальнем конце столовой, но уже не была такой грустной, как с утра.'

    'Сделал шаг вперёд, но не успеваю сделать и второй, как вдруг меня окликают сзади. Негромко, но всё равно хорошо слышно:'

    # '(появляется спрайт Слави, Алисы и Лены)'
    show 35grad_lena 1 normal pio:
        xanchor 0.5 xalign 0.5 yalign 0.5
    with dissolve
    show 35grad_alice 1 normal reb:
        xanchor 0.0 xalign 0.0 yalign 0.5
    with dissolve
    show 35grad_slavya 1 normal pio:
        xanchor 1.0 xalign 1.0 yalign 0.5   # В центре
    with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_dining_hall_people_day at thirty_five_grad_blur

    thirty_five_grad_sl 'Лёш, идём с нами.'

    'Это была Славя, Алиса и, на удивление, Лена. Затем снова перевёл взгляд на Мику. Меня разрывает чёртово противоречие!'
    'Ведь хочется посидеть как и с ними, так и с той красавицей...'

    # '(музыка) Ейбог – Two Glasses Of Melancholy'
    $ renpy.display_notify('Сейчас играет:\nЕйбог – Two Glasses Of Melancholy')
    play music music_list ['two_glasses_of_melancholy']

    'Я снова повернулся к ней. Она меня как будто и не замечает вовсе, а может и делает вид, что не смотрит. Может, дать ей побыть одной?'

    thirty_five_grad_alex 'Ладно, с вами так с вами.'

    'Я уселся между Славей и Леной. Все вокруг взяли как первое, так и второе блюда, а я отличился и взял только второе.'
    'Не хотелось мне есть сейчас горячий борщ в такую жару.'

    # '(по возможности сделать так, чтобы спрайты "как бы сидели" за столом)'
    thirty_five_grad_dv 'А я слышала, что тебя к вожатой поселили. Теперь шестёрочкой её будешь?'

    'Съязвила без злости Алиса.'
    show 35grad_slavya 2 hmuri pio with dissolve_fast
    show 35grad_lena 1 crabbed pio with dissolve_fast
    thirty_five_grad_sl 'Алиса!'

    'Подали своё недовольство Лена и Славя. Но я проигнорировал этот выпад. Мне было без разницы, о чём она говорит.'
    show 35grad_alice 2 sad reb with dissolve_fast
    thirty_five_grad_dv 'А что я? Просто общаюсь с новичком, не более. И то, он игнорирует меня.'

    'Обида в её голосе звучала горько, как тёмный шоколад.'

    thirty_five_grad_sl 'И правильно делает. Вообще ума не приложу – у тебя же мама милиционер, так почему такая дочка...'
    show 35grad_alice 2 hmuri reb with dspr
    thirty_five_grad_dv 'Так, а теперь ты помолчи, ладно? Безотцовщина.'
    $ renpy.pause(1.0, hard=True)
    show 35grad_alice 1 normal reb with dspr
    show 35grad_slavya 2 normal pio with dspr
    'Наступила резкая, томная тишина. Она не была приятной, а наоборот, острой и больной. Зря сел с ними, нужно было идти до той японки.'
    show 35grad_lena 1 normal pio with dspr
    thirty_five_grad_ul 'Лёш, о чём думаешь?'

    'Спросила меня Лена, отчего я задал ей вопрос с подвохом:'

    thirty_five_grad_alex 'А что бы ты делала, узнай, что переместилась во времени эдак лет на тридцать назад? И не знаешь, сможешь ли вернуться или же нет.'

    thirty_five_grad_sl 'Странный вопрос, Алексей. Видать, кто-то научной фантастики перечитался.'

    'Сказала Славя вместо Лены, но и та тоже не заставила себя долго ждать:'
    show 35grad_lena 1 shy pio with dissolve_fast
    thirty_five_grad_ul 'Продолжила бы жить, как ни в чём не бывало. Ведь даже попав в такую ситуацию, то жизнь не обрывается. А ещё попробовала найти родителей. Почему?'
    thirty_five_grad_ul 'Не знаю. Просто идея такая возникла. Представила их, что они, как я сейчас, такие же молодые первооткрыватели, которые исследуют мир и открывают новые для себя возможности.'
    thirty_five_grad_ul 'Переступают порог от беззаботного детства к суровой и серьёзной взрослой жизни.'
    show 35grad_lena 1 normal pio with dspr
    'Мечтательно высказалась Лена. Хм... А ведь она таким способом подала мне неплохую идею.'
    'Тем более я помню, что и Ольга говорила, что меня сюда отправили мои родители, и она сама лично знает их! Лена, ты гений!'

    'Но, с другой стороны, в этот период времени мои родители были примерно такими же, как и мои одногодки сейчас. Что-то здесь не сходится...'

    thirty_five_grad_dv 'Лёхич, всё хорошо?'

    'Внезапно спросила Алиса.'

    thirty_five_grad_dv 'Что-то ты бледный, может попросить Виолу укольчик тебе сделать?'

    thirty_five_grad_alex 'Э-э-э как-нибудь без этого обойдусь. Со мной всё хорошо. Лучше не бывает!'

    'Я встал со стула и, допивая «кофе», от которого было лишь одно название, стал уходить. Всё равно я уже всё доел, а делать мне тут больше нечего.'

    thirty_five_grad_sl 'Что это с ним?'

    thirty_five_grad_dv 'Не знаю, странный какой-то.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    'Послышалось мне. Да и было всё равно на это. А вот кто конкретно это говорил я понять не смог, но зато осознал одно – аквамариновая девочка столовую уже покинула...'

    # '(затемнение (раньше это было обычное моргание))'
    show black with dissolve
    # '(музыка) Ейбог – Trapped In Dreams'
    $ renpy.display_notify('Сейчас играет:\nЕйбог – Trapped In Dreams')
    play music music_list ['trapped_in_dreams']
    # '(фон столовой снаружи)'
    scene bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_day fadein 6
    'Выйдя на свежий воздух, я почувствовал, как стало легче дышать. Эх, когда же этот день закончится? Я устал, и это вполне логично. Стресс сказывается. Огромное потрясение.'
    'Ощущаю себя так, словно меня выкинули на остров, как Робинзона Крузо. Только я здесь не одиночка. И всё это происходит в прошлом.'
    'Если это вообще ещё можно назвать прошлым моего мира. Да чёрт его знает. Всё, что угодно может произойти здесь.'

    'Странно то, что делает японка здесь, если отношения Японии с Советским Союзом были крайне натянуты? Или она может быть из семьи крайне богатых и влиятельных людей?'
    'Но кто-то вывел меня из раздумий. Аккуратно, нежно и внезапно похлопав меня по плечу.'

    # '(появляется Мику)'
    show 35grad_miku 2 laughter pio ponytails at thirty_five_grad_sunset_lighting_revers with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_sunset at thirty_five_grad_blur

    thirty_five_grad_mi 'Ой, Лёша. Это всё же ты. Рада видеть!'

    'Прощебетала девушка. Её стройная и аккуратная фигура, без изъянов хорошо подчёркивали длинные-предлинные хвостики, которые тянулись, как две реки, а её небольшая грудь приподнималась с каждым произнесённым словом.'

    thirty_five_grad_alex 'И я тебе рад. Как ты?'

    'А я и не солгал. На самом деле, если бы на её месте была, допустим, Славя или Алиса, то сказал бы то же самое.'
    'Но на Мику это произвело более сильный эффект, чем я мог подумать.'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ой, да я уже в порядке. Точнее, с утра и была в норме, просто всегда случаются разного рода неприятности... И вот, представляешь!'
    thirty_five_grad_mi 'Я сегодня пыталась колонки подключить, проверить, работают ли, а розетка... {w} Она чуть не загорелась! Задымилась, почернела! Мне стало... {w} страшно...'

    'Совершенно откровенно и даже по-детски объяснялась она мне. Со стороны выглядело это очень и очень мило, и я бы в любом случае не смог ей отказать.'
    'Это не только из-за того, что я член клуба, а и просто чисто по-человечески.'

    thirty_five_grad_alex 'Не переживай, главное, что ты не поранилась, так ведь?'
    show 35grad_miku 1 sad pio ponytails with dspr
    thirty_five_grad_mi 'А-ага. Но это же надо к кибернетикам идти...'

    'Нет-нет, я не допущу их до моей сферы работы. Тем более что это отчасти моя обязанность. Особенно после тех его слов.'

    thirty_five_grad_alex 'Нет необходимости, Мику. Я сам всё сделаю. Главное, чтобы запасная розетка имелась, а всё остальное – дело техники!'
    show 35grad_miku 2 laughter pio ponytails with dspr
    'Девчушка смотрела на меня, как на героя, что смутило меня.'

    # '(спрайт Мику радостный)'
    thirty_five_grad_mi 'Лёшенька, ты просто чудо! О боги, как же мне повезло, что я встретила тебя! А за розетку эту не беспокойся, тебе её не нужно искать!'
    thirty_five_grad_mi 'Представляешь, в начале смены приезжал грузовик, и кибернетики долго-долго разгружали его!'
    thirty_five_grad_mi 'А потом у них на складе места не хватило, и они решили из моей подсобки сделать склад! Но зато пригодилось. Видишь, как всё подвернулось то!'

    'И рассмеялась. Её звонкий смех давал надежду на то, что в будущем всё будет хорошо. Не знаю, как это работает, да и знать не хочу. Так что, просто улыбнулся.'

    thirty_five_grad_alex 'Ну что, Мику, пойдём в музклуб? Только давай сначала до моего домика дойдём, я все необходимые инструменты возьму.'

    # '(Мику удивлённая)'
    show 35grad_miku 2 surprise pio ponytails with dspr
    thirty_five_grad_mi 'Ого! А ты что, с собой и такое привёз?'

    th 'Эх, теперь придётся выкручиваться...'

    thirty_five_grad_alex 'Представляешь, я их взял, а зубную пасту нет! Ну, на самом деле, их ношу для всяких несчастных случаев, наподобие того, с чем сейчас придётся иметь дело.'

    thirty_five_grad_mi 'А-а-а! Но мне кажется, что это не очень практично... Тяжёлые, наверно.'

    # '(спрайт Мику обычный)'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast

    thirty_five_grad_alex 'Не переживай. У меня спина крепкая!'
    show 35grad_miku 3 shy pio ponytails with dissolve_fast
    'Девочка покраснела, а затем спустилась с лестницы, что сделал и я, а затем вместе зашагали вперёд.'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ну что, веди, мой драгоценный товарищ!'

    'Произнесла она с кристально-чистой и честной улыбкой.'

    thirty_five_grad_alex 'Вау, а когда я это успел стать драгоценным?'
    $ renpy.display_notify('Перевод с японского - Спасибо больше тебе за это.')
    thirty_five_grad_mi 'Тогда, когда ты искренне захотел присоединиться в мой кружок.{font=NotoSansJP-Medium.ttf}もっとありがとう。{/font}'
    # '(перевод для редактора и кодера, вставить в игру)'

    thirty_five_grad_alex 'Хм, да на здоровье, Мику. Я... не смог бы тебе отказать.'

    thirty_five_grad_mi 'Почему?'

    thirty_five_grad_alex 'Не знаю. А этому вопросу так уж и нужен ответ?'
    show 35grad_miku 2 thoughtful pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Думаю, что нет.'

    'Легкомысленно протянула музыкальная девочка.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    show black at thirty_five_grad_vhs with thirty_five_grad_timeskip_transition

    'Остальной путь до домика мы провели в полной тишине, наслаждаясь этими тихими мгновениями, когда вокруг тебя только звонкий свистящий ветер, вдалеке поют редкие птицы, а под ногами раздаётся противный скрежет цикад.'

    # '(затемнение (раньше это было обычное моргание))'

    # '(фон домика вожатой)'
    scene bg ext_house_of_mt_sunset with thirty_five_grad_timeskip_transition

    show 35grad_miku 1 normal pio ponytails at thirty_five_grad_sunset_lighting with dspr:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_blur

    'Я уже подошёл к двери, чтобы открыть её, как вдруг Мику говорит:'

    thirty_five_grad_mi 'Повезло же тебе, прямо у Ольги Дмитриевны под крылышком живёшь.'

    thirty_five_grad_alex 'И что это значит?'

    thirty_five_grad_mi 'То, что ты будешь в безопасности от Алисы. Тебя могли бы и к ней подселить.'

    'А вот это поменяло моё мнение об Ольге.'

    thirty_five_grad_alex 'Значит, я должен буду сказать ей «спасибо»?'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Да я же пошутила!'

    # '(фон внутри домика вожатой)'
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_sunset with fade

    'Хихикнув и помотав головой, я зашёл внутрь, в натуральную свободу от жары.'
    'Внутри сидела моя вожатая уже за убранным столом, который выглядел намного больше, когда был прибран, и что-то писала в журнале, пока тихо работало радио.'
    'Что оно играло, непонятно, ибо речь диктора была мне не слышна. Поэтому, не став отвлекать её от важного дела, я потянулся к своему рюкзаку.'
    'Только вот та всё равно обернулась, заметила меня и легонько улыбнулась.'

    # '(спрайт Ольги обычный)'
    show 35grad_olga 3 normal form at thirty_five_grad_sunset_lighting_revers with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_sunset at thirty_five_grad_blur

    thirty_five_grad_mt 'О, Алексей, какая встреча. Что делаем?'

    'Из собственного опыта знаю, что когда так говорят, то хотят загрузить тебя работой с ног до головы. Но мне не страшно, так как уже есть задание!'

    thirty_five_grad_alex 'Сейчас только инструменты возьму и буду ремонтировать розетку в музклубе.'

    'Она серьёзно удивилась.'

    # '(спрайт Ольги удивлённый)'
    show 35grad_olga 3 surprised form with dissolve_fast

    thirty_five_grad_mt 'Ого, ты и такое умеешь?'

    thirty_five_grad_alex 'Да. Поэтому, если у вас будут какие-то проблемы, то можете обращаться ко мне.'

    '...Вот чёрт, угораздило же меня такое ляпнуть! Буквально наступил на те же грабли, что и тогда в армии, когда вызывали перед строем и спрашивали, кто что умеет делать.'
    'Да, хотя, я и жил несколько месяцев в доме одного из офицеров, но работы (в основном, по ремонту дома) было выше крыши! Чуть ли не в буквальном смысле.'
    thirty_five_grad_mt 'Буду знать, Лёша. А ты молодец, на самом деле. Сам же выручился помогать, так?'

    thirty_five_grad_alex 'Ну да. Я не брошу друга без помощи.'

    '...Друга. Сильное слово для человека, которого я знаю полдня. А может, она вообще маньяк какой? Специально глазками меня заманила в своё логово, как паучиха, а потом...'
    'Да не, вот Алиса – та ещё лисица, спокойно может на такое пойти. А вот Мику... {w} Нет. Она не такая, нутром чую! Хотя, в тихом омуте, как говорится...'
    show 35grad_olga 2 normal form with dissolve_fast

    thirty_five_grad_mt 'Рада такое слышать. Главное смотри, чтоб твой запал также быстро не пропал. А, кстати! Вспомнила.'
    hide 35grad_olga 2 normal form with dissolve_fast

    'После того, как вожатая нырнула в один из ящиков стола, она достала из него небольшой латунный ключик.'
    'Он был примерно похож как клубный, только более потрёпанный. Видать, прошёл через не одну пару рук.'
    show 35grad_olga 3 normal form at thirty_five_grad_sunset_lighting_revers with dspr:
        xanchor 0.5 xalign 0.5

    thirty_five_grad_mt 'Это от нашего домика. А то я же не всегда тут сижу.'

    thirty_five_grad_alex 'Спасибо, сохраню.'

    thirty_five_grad_mt 'Ты уж постарайся, больше такого у меня нет.'

    thirty_five_grad_alex 'А ещё я хотел бы спросить у вас кое-что.'

    thirty_five_grad_mt 'Я слушаю.'

    'И тут у меня язык исчез чуть ли не по щелчку пальцев. Я не знаю, почему так, но не мог подобрать ни единого слова, чтобы вопрос смотрелся адекватно и разумно.'

    thirty_five_grad_alex 'Простите, запамятовал что-то. Потом спрошу.'

    thirty_five_grad_mt 'Ну, ладно. Подходи в любое время.'

    # '(спрайт Ольги пропадает)'
    hide 35grad_olga 3 normal form with dissolve

    'А теперь инструменты. Засунув ключик от домика в задний карман шорт, туда же, куда и клубный, я вытащил из рюкзака плоскогубцы, кусачки и изоленты порядка «ЖЗК», в простонародье: жёлтый, зелёный, красный.'
    'Так удобнее работать с проводами и кабелями, чтобы не было путаницы. Но и не только, конечно же.'

    'В карман это всё дело, к сожалению, не положишь, поэтому придётся нести в руках. Эх, только бы по пути никто из знакомых не встретился!'
    'Но как только я вышел из домика, то моей спутницы почему-то не было рядом...'

    # '(затемнение (раньше это было обычное моргание))'
    play sound sfx_close_door_1
    show bg black with fade
    # '(музыка) КАМАКА – Nerik Cinema'
    $ renpy.display_notify('Сейчас играет:\nКАМАКА – Nerik Cinema')
    play music thirty_five_grad_Nerik_Cinema fadein 2.0
    # '(фон музклуба снаружи)'
    scene bg thirty_five_grad_music_sunset with dissolve

    '...Так действительно и было. По пути никто не встретился из знакомых, а дорога заняла, по ощущению, чутка меньше времени, чем необходимо.'
    'Смотря в чужие лица, я не находил в них непонимания, словно перед ними не типичный попаданец, а самый обычный ровесник. Ладно, всё равно.'
    'И вот теперь я снова стою тут, прямо как с утра. Главное, чтобы на такую же картину не натолкнуться, гы.'
    scene bg thirty_five_grad_ext_musclub_verandah_sunset with dissolve

    'Но не отрицаю, что событие с мужской стороны было приятным. Голубые в белую полосочку нижнее бельё не каждый день увидишь, особенно на такой округлой части тела...'
    'Господи, куда меня понесло! Я прямо ощущаю, как горит моя голова и щёки!'
    'Стук.'

    thirty_five_grad_mi 'Лёша, если это ты, то можешь спокойно входить!'

    'Пожав плечами, я взялся за ручку двери и потянул на себя.'
    # '(фон музклуба внутри)'
    play sound sfx_open_cabinet_1
    scene bg thirty_five_grad_int_music_club_sunset with dissolve

    'Только в этот раз клуб меня не встретил арктической прохладой, а наоборот – жарким зноем. Всё из-за этого панорамного окна.'

    # '(спрайт Мику улыбающийся)'
    show 35grad_miku 1 smile pio ponytails at thirty_five_grad_sunset_lighting_revers with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_music_club_sunset at thirty_five_grad_blur

    thirty_five_grad_mi 'О, Лёшка! Наконец-то ты пришёл! Прости, что я покинула тебя. Правда, прости! Но... что-то в душе было неспокойно за музклуб.'
    thirty_five_grad_mi 'Когда вернулась, то всё оказалось в норме...'

    th 'Что-то она мне явно недоговаривала. Нет, не врала, а просто пыталась уйти от ответа. Ну и ладно.'
    th 'У каждого есть свои тараканы в голове. Ведь я тоже отчасти странный.'

    thirty_five_grad_alex 'Ладно. Ничего страшного, думаю. Просто сначала показалось, будто ты хотела избежать обратной дороги вместе или типа того.'

    # '(спрайт Мику грустной)'
    show 35grad_miku 1 sad pio ponytails with dspr

    'Но её лицо изображало реальное смущение и грусть. Отчего решил, что давить на Мику – не лучшая идея.'

    # '(спрайт Мику обычный)'
    show 35grad_miku 1 normal pio ponytails with dspr

    thirty_five_grad_mi 'Нет-нет-нет! Ни в коем случае! Просто я серьёзно... Ой, точно! Розетка же! Давай покажу тебе её! Надеюсь, там ничего страшного. Но всё равно будь осторожен.'

    'Только в этом не было необходимости, так как её было хорошо видно и так. Всю чёрную, сморщенную и воняющую горелым пластиком.'
    th 'Как только тут не случился пожар? Вопрос не шуточный.'

    'Подойдя ближе, в нос ударил характерный запах электрической вони.'
    'Профессиональная деформация, грубо говоря, когда ты можешь чуять, был ли коротыш в сети или нет. Тут был.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    thirty_five_grad_alex 'Мику, где у тебя тут электрический щиток?'

    # '(музыка) Сергей Ейбог – Sweet Darkness'
    $ renpy.display_notify('Сейчас играет:\nСергей Ейбог – Sweet Darkness')
    play music music_list['sweet_darkness']
    show 35grad_miku 2 surprise pio ponytails with dissolve_fast

    thirty_five_grad_mi 'А?'
    show 35grad_miku 2 normal pio ponytails with dissolve_fast
    thirty_five_grad_alex 'Ну это коробочка небольшая такая на стене, обычно чёрного или серого цвета с множеством проводов и переключателей.'

    th 'Если мне не изменяет память, то в конце восьмидесятых были распространены допотопные СО-1-5. Они же счётчики однофазные.'
    th 'Я в них никогда не ковырялся, так что это мой первый опыт! Почти как с девушкой. Хех.'

    thirty_five_grad_mi 'Ой, он в подсобке как раз! Давай, я покажу тебе.'

    'И она поманила меня рукой. Словно и правда загоняет в ловушку. Но то, как она это сделала...'
    'Как её чудесные хвостики, подобно Млечному пути, закрутили в воздухе, то, каким взглядом она смотрит на меня... С интересом и доброжелательностью... Чистой искренностью!'
    'Да я только «за» попасть в такую ловушку.'

    # '(фон склада + спрайт Мику обычный)'
    scene bg thirty_five_grad_int_wardrobe with fade
    play sound sfx_open_cabinet_1
    show 35grad_miku 2 thoughtful pio ponytails at thirty_five_grad_night_lighting with dissolve_fast:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_wardrobe at thirty_five_grad_blur

    thirty_five_grad_mi 'Лёшенька, ты уж прости за такой беспорядок. Тут раньше было тоже красиво, когда не было столько... хлама.'

    'Обычный совершенно склад, который набит всякой строительной мелочёвкой и... кроватью с сеткой рабица. А ещё и матрас на ней сверху.'
    'Словно это подарок от самой Судьбы. Такой тонкий от неё намёк. Ага.'
    show 35grad_miku 2 normal pio ponytails with dissolve
    thirty_five_grad_mi 'Ой, а я уже и сама не помню, что она тут делает... Ладно, неважно! Вот та коробочка, да?'

    # '(музыка стоп)'
    stop music fadeout 2.0

    '...И Мику совершила самую очевидную, но, тем не менее, глупую ошибку любого совершенно обычного человека.'
    'Тотчас, – она потянулась пальцем к источнику опасности.'

    # '(музыка) Сергей Ейбог – Glimmering Coals'
    play music music_list['glimmering_coals']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog – Glimmering Coals')

    thirty_five_grad_alex 'Стой!'

    # '(спрайт Мику испуганный)'
    show 35grad_miku 2 fear pio ponytails with dspr

    thirty_five_grad_mi 'Ай! Лёша! Зачем так кричать-то? Я чуть Аматерасу душу не отдала! Фух, блин...'

    'То, как она взволновалась, пытаясь отдышаться, выглядит мило. Хотя и совестно теперь немного. Ведь я хотел как лучше...'

    thirty_five_grad_alex 'Прости.'

    # '(спрайт Мику улыбающийся)'
    show 35grad_miku 2 laughter pio ponytails with dspr

    'Грустно протянул я. Но на её личике отразилась тёплая улыбка.'

    thirty_five_grad_mi 'За что, глупышка? Ты мне жизнь спас!'

    thirty_five_grad_alex 'Ну... Всё же не хотелось, чтобы ты пострадала. Короче, можешь выйти пока? А то тут места не очень много.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Хорошо, конечно. Если что – зови!'
    hide 35grad_miku 2 normal pio ponytails with dissolve
    'Я выгнал её специально, чтобы не мешалась мне своими бесконечными речами. На самом деле, в обычной жизни мне это даже начало нравится, но не сейчас, когда я работаю с этой штукой.'
    'Впервые в жизни, между прочим. Надеюсь, что и не в последний.'

    th 'Так... {w} Что тут у нас... {w} Серьёзно? Настолько легко? Тут словно для самых маленьких написано, что и зачем каждая кнопочка нужна.'
    th 'Это меня даже разочаровало. Так теперь, по идее, везде должен был пропасть свет.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    thirty_five_grad_alex 'Мику!'

    # '(музыка) MIKUMYLOVE (как и в прошлый раз эта музык есть в архиве который я кидал)'
    play music thirty_five_grad_mikumylove
    $ renpy.display_notify('Сейчас играет:\nMIKUMYLOVE')
    show 35grad_miku 1 normal pio ponytails at thirty_five_grad_night_lighting with dissolve:
        xanchor 0.5 xalign 0.5
    thirty_five_grad_mi 'Я к твоим услугам!'

    'Меня эти её слова лишили на секунду-другую дара речи, отчего мой рот был похож на рыбий: хлоб-плоб.'

    thirty_five_grad_alex 'М-мику! Ну что ты смущаешь меня. Мне нельзя!'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    'Её кристальный смех было слышно даже здесь.'

    thirty_five_grad_mi 'Ну, Лёшка! Даёшь ты. Чего хотел?'

    thirty_five_grad_alex 'Попробуй включить свет.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'А меня не ударит?'

    thirty_five_grad_alex 'Не должно.'
    show 35grad_miku 2 fear pio ponytails with dspr
    thirty_five_grad_mi 'То есть может?!'

    thirty_five_grad_alex 'Шанс всегда есть. Но ты не бойся. Пока я рядом, тебе это не грозит.'
    # (sound)
    play sound thirty_five_grad_light_on_off
    'Помедлив секунду, она всё же нажала на кнопку. Раздался глухой щелчок.'

    thirty_five_grad_mi 'А! Сработало!'

    thirty_five_grad_alex 'Вот-вот. Полдела сделано. А теперь за работу!'

    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(затемнение (раньше это было обычное моргание))'
    show black with dissolve
    # '(фон музклуба внутри)'
    play sound sfx_open_cabinet_1
    scene bg thirty_five_grad_int_music_club_sunset with thirty_five_grad_timeskip_transition
    play music thirty_five_grad_svet_urodi
    $ renpy.display_notify('Сейчас играет:\nЧёЗаУродыНаСцене - Свет')
    'Мику всё ходила да бегала вокруг меня, спрашивая постоянно о том, нужна ли мне помощь. Да и какая тут помощь напрашивается?'
    'Делов-то: открутить испорченную розетку, переизолировать провода (проблема была в них, так как изоляция вся сошла на нет) и вкрутить новую розетку, которую заранее принесла Мику.'

    thirty_five_grad_alex 'По сути, всё готово. Надо лишь снова включить счётчик, и...'
    # ('sound')
    play sound thirty_five_grad_light_on_off
    '...Прозвучал глухой щелчок...'

    thirty_five_grad_alex '...Мику?!'
    show 35grad_miku 2 normal pio ponytails at thirty_five_grad_sunset_lighting_revers with dspr:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_music_club_sunset at thirty_five_grad_blur
    thirty_five_grad_mi 'Да-да? Я просто видела, как ты это делал, вот и решила также сделать!'

    thirty_five_grad_alex '...А тебя разве папа не учил, что электричество – это опасно? Чёрт побери, предупреждать надо! Меня и убить могло!'

    # '(спрайт Мику грустная)'
    show 35grad_miku 2 sad pio ponytails with dspr

    thirty_five_grad_mi 'Учил, конечно! И мне было страшно по началу, но всё же решила попробовать... {w} Прости... {w} Прости, пожалуйста!'

    'Хоть она и выглядела со стороны как ребёнок, но смелости ей не занимать.'
    'Серьёзно. Даже я не сразу осмелился, а она... Одним словом, девочка-секрет. Да и злиться на неё совершенно не хотелось.'

    thirty_five_grad_alex 'Глупышка теперь ты. Тебе не за что просить прощения. Просто... Я переживаю за тебя немного. Вот... Да и сам испугался.'
    thirty_five_grad_alex 'Но ты молодец, хорошо справилась! Осталось только теперь проверить...'

    'Я подключил вилку от динамика в розетку и... Всё работает! Динамик издал писк, знаменуя помещение о том, что он проснулся и готов к работе.'
    'А мне оставалось только ловить слова благодарности от девочки оркестра, если верить на слово, об её способностях.'

    # '(спрайт Мику улыбается)'
    show 35grad_miku 2 laughter pio ponytails with dspr

    thirty_five_grad_mi 'Лёша, скажу ещё раз: ты просто чудо! Я благодарю всех богов о том, что встретила именно тебя! Но теперь, я думаю, тебе положена награда!'
    thirty_five_grad_mi 'И не сопротивляйся! Кружку горячего свежего чая ты уж точно заслужил!'

    thirty_five_grad_alex 'Думаю, хорошая награда. Хотя я и помог тебе не ради неё.'
    show 35grad_miku 2 normal pio ponytails with dspr

    thirty_five_grad_mi 'Я знаю. Но чай будет вечером. Ты не против подождать? Просто ему нужно немного настояться. Вот, так что... Давай я тебе сыграю что-нибудь?'
    thirty_five_grad_mi 'А завтра приступим к первому этапу твоего обучения! Поверь, я хоть сама и обучалась в музыкальной школе, но ты будешь моим первым учеником!'

    thirty_five_grad_alex 'Как мило. А кто будет вторым?'
    show 35grad_miku 3 dreamy pio ponytails with dissolve_fast

    'Закусив губу и приняв задумчивый вид, эта юная дама выдала следующее:'

    thirty_five_grad_mi 'А вот не знаю! Говорю тебе это честно, так как считаю тебя моим другом. Другому человеку соврала бы.'

    thirty_five_grad_alex 'О? Ты считаешь меня другом?'
    show 35grad_miku 3 shy pio ponytails with dspr
    thirty_five_grad_mi 'Да почему бы и нет? В общем, ты хочешь слушать или нет?'
    'Она была краснее, чем икра на хлебе в новогоднюю ночь, и тараторила так быстро, что даже я еле поспевал воспринимать её речь. Друг... так... приятно слышать это.'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_alex 'Мику, успокойся. Отдышись.'
    show 35grad_miku 3 normal pio ponytails with dissolve_fast
    'Она взяла в руку совершенно обычную на вид акустическую гитару. Но даже так вокруг неё начала расти как будто аура музыкального превосходства и эпатажа.'
    'Словно перед тобой снизошла с небес сама Богиня Музыки, чтобы одарить жалкого крестьянина своей частичкой красоты.'

    # '(спрайт Мику обычная)'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Что будем играть?'

    thirty_five_grad_alex 'Ну... Давай на твой вкус. А то, смотря на тебя и твою небесную красоту, я не смог выбрать.'

    'Хоть я и прошептал конец предложения крайне тихо (я старался), но её щёчки выдали все мои старания. После чего уже она прошептала:'
    show 35grad_miku 3 shy pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Спасибо. Мне никто раньше этого никогда не говорил...'
    show 35grad_miku 3 normal pio ponytails with dspr
    'Наступила секундная тишина, после чего её пальцы медленно застучали по струнам, как капли дождя по черепице.'
    'Пока играла музыка, я был словно околдован. Мне не хотелось даже дышать, настолько был погружён в её дивный дар.'

    # '(музыка стоп)'
    stop music fadeout 2.0
    # '(затемнение (раньше это было обычное моргание))'
    show black at thirty_five_grad_vhs with thirty_five_grad_star_falling_transition
    # '(музыка) Сергей Ейбог – Memories'
    play music music_list['memories']

    '...Песня шла за песней, лаконично сменяя друг дружку, пока небо не принялось окрашиваться в нежно-жёлтый цвет. Как долго я здесь сижу? Ай, неважно.'
    'Главное, что я получил именно то, чего и хотел: прекрасную музыку и хороший отдых.'

    scene bg thirty_five_grad_int_music_club_sunset with thirty_five_grad_star_falling_transition

    show 35grad_miku 1 normal pio ponytails at thirty_five_grad_sunset_lighting_revers with dissolve_fast:
        xalign 0.5 xanchor 0.5

    thirty_five_grad_mi 'Фу-х. Устала.'

    'Девушка отложила гитару на специальную стойку, а затем подсела на стул рядом со мной.'

    thirty_five_grad_alex 'Мику, это было прекрасно. У тебя и вправду талант! Был бы твоим отцом, то я гордился тобой. Хотя даже без него бы радовался такому прекрасному человеку.'
    show 35grad_miku 3 shy pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёшка! Бака! Не смущай меня! Я же сейчас... Но спасибо, мне так приятно! Он и так гордится мной. Честно-честно! Хотя и скуп на эмоции...'
    thirty_five_grad_mi 'А вообще, я рада, что понравилось и...'

    'Она резко остановилась. Мне это не понравилось.'

    # '(спрайт Мику грустная)'
    show 35grad_miku 1 thoughtful pio ponytails with dissolve_fast

    thirty_five_grad_alex 'Мику? Всё хорошо?'

    thirty_five_grad_mi 'Д-да. Просто сейчас ужин будет, и я на него не пойду.'

    thirty_five_grad_alex 'Почему?'
    show 35grad_miku 1 sad pio ponytails with dspr
    thirty_five_grad_mi 'Есть свои кое-какие дела. И ты же не обидишься, если чай подождёт до завтра?'

    'Что-то она резко сдала. Погрустнела, опустились плечи и вообще, как будто выкачали жизнь.'
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_alex 'Мику, с тобой точно всё хорошо? Вижу же, что тебя что-то беспокоит. Да и стала мрачнее тучи.'

    'Она медленно вдохнула и выдохнула. На уголках глаз собирались небольшие, но в свете уходящего солнца яркие капельки слёз.'

    thirty_five_grad_mi 'Да. Прости, просто я хочу побыть одна. Вот...'
    # ('sound')
    play sound sfx_dinner_jingle_normal
    'Прозвучал горн, который отбил у меня всё желание есть.'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёша, пожалуйста. Просто у меня сегодня за день произошло столько, сколько и за пару лет не было. Так что...'
    thirty_five_grad_mi 'Всё в порядке, правда. Но прошу тебя, сходи на ужин, развейся. Тем более, что устал за сегодня наверняка.'

    thirty_five_grad_alex 'А ты сама всё же не пойдёшь?'

    thirty_five_grad_mi 'Нет.'

    thirty_five_grad_alex 'Тогда и я нет.'

    # '(фон музклуба снаружи)'
    play sound sfx_close_door_1
    scene bg thirty_five_grad_music_sunset with dissolve
    'Она что-то пыталась сказать, но я её уже не слушал. Точнее, не услышал, ведь к этому времени как раз закрыл дверь. Подошёл к веранде и облокотился об неё.'

    th 'Вот дурёха, а! На кой чёрт она себя так ведёт? И я не лучше: «Тогда и я нет». Клоун. Только цирк уехал, а меня тут оставили.'
    th 'И смотря на ситуацию, этот вариант не такой уж и тупой.'

    # '(музыка стоп)'
    stop music fadeout 2.0

    'Я медленно двинулся прочь от клуба. Да, правда, не пойду на ужин. Не было желания ни есть, ни встречаться с кем-то из знакомых.'
    'Я устал. Как физически, так и морально.'
    th '...А ещё этот чёртов лес, который стоит недалеко от меня. Так и давит, зараза.'

    # '(затемнение (раньше это было обычное моргание))'
    scene bg black with dissolve
    $ renpy.pause(0.5,hard=True)
    # '(музыка, а точнее звук моря)'
    play ambience ambience_boat_station_night fadein 2
    # '(фон пирса ночь)'
    scene bg ext_boathouse_night with dissolve

    th '...Что? Как я тут очутился? И сколько времени прошло? Почему я стою на пирсе и смотрю вдаль синей реки? Я шёл сюда, словно в дымке. Не помню, как оказался здесь.'
    'Красивый, тёмно-жёлтый из-за ночи пляж с ракушками, старенький, но надёжный деревянный пирс, на котором я сейчас стою, а неподалёку – самый настоящий причал.'
    th 'Как красиво-то на самом деле!'

    'А в особенности яркое звёздное небо, которое было утыкано мириадами звёзд, практически без пустого места.'
    'Я присел на пирс, свесив ноги. Вода не доходила даже до стоп, так что я не боялся их промочить.'

    'Тишина, не считая звука волн, окутывала меня с головы до пят, а уходящая вдаль река напоминала хвостики моей новой аквамариновой подруги.'
    'Интересно, в чём суть её такого поведения? Внезапный голос немного испугал меня, но я тут же пришёл в норму.'

    # '(спрайт Слави обычный)'
    show 35grad_slavya 2 normal pio at thirty_five_grad_night_lighting with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_boathouse_night at thirty_five_grad_blur

    thirty_five_grad_sl 'Алёш, а почему тебя на ужине не было? Всё хорошо?'

    'Крайне заботливо спросила Славя, после чего спокойно села со мной рядышком. Мы были сейчас настолько близки, что наши плечи касались друг друга.'

    thirty_five_grad_alex 'Да всё просто прекрасно, не переживай.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Увы, не могу. Всё же ты тоже под моей ответственностью. Так что...'
    show 35grad_slavya 2 normal pio with dspr
    'Диалог слегка не клеился...'

    thirty_five_grad_alex 'Знаешь, что эти звёзды мне напоминают?'

    thirty_five_grad_sl 'И что же?'

    thirty_five_grad_alex 'Твои глаза сейчас. Настолько яркие и живые... Я никогда раньше не был в подобных местах, никогда не встречал людей, похожих на вас.'
    thirty_five_grad_alex 'Все уникальные, яркие, незабываемые.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Благодарю. Давно не слышала ничего подобного. Но почему ты так внезапно решил открыть мне душу? И как это: не был?'

    thirty_five_grad_alex 'Сам не знаю почему. Ты вроде неплохая, добрая. А я... {w} я не знаю. Уже ничего не знаю.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Алёш, вся твоя хандра сейчас от усталости и перенасыщения новыми чувствами. Я очень рада, что ты за сегодня смог найти столько новых знакомых.'
    thirty_five_grad_sl 'Но у тебя ещё тринадцать дней, понимаешь? Спешить некуда! Расслабься и отдыхай.'

    thirty_five_grad_alex 'Ты вроде и верно говоришь, но...'

    th '...Ты никогда меня не поймёшь, что всё на самом деле куда как страшнее и даже опаснее, наверное... И лучше бы не понимала, никому такого не пожелаю.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'А, поняла! Голод – это такая злая штука, что... Айда в столовую! Там наверняка что-то осталось ещё.'

    thirty_five_grad_alex 'У тебя что, и ключи от всех помещений есть?'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Почти. Только от администрации, домиков и технических помещений нет. Да оно мне и не нужно. Вставай, а то уже холодный ветер подул. Простудишься...'

    'Но вставать не было сил. Хотелось разлечься и отдать всего себя этому морскому ветру. Так вот откуда я чуял тогда солёный запах на остановке.'
    th 'Кстати, насчёт неё. Нужно будет сходить и проверить её. Вдруг что-то там появилось...'

    # '(спрайт Слави улыбающийся)'
    show 35grad_slavya 2 smile pio with dspr

    thirty_five_grad_sl 'Лёш, я на руках тебя не понесу. Я всё же дама.'

    thirty_five_grad_alex 'Ха, а если б я без сознания валялся? Ты бы так и оставила?'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Какой же ты врединой иногда бываешь!'

    'Она рассмеялась. Это сделал и я. После чего всё же встал, отчего почувствовал некоторую ломку в спине.'

    thirty_five_grad_alex 'Ух! Старость не радость...'
    show 35grad_slavya 2 smile pio with dspr
    'Нам предстоит с ней долгий путь до столовой. Не такой длинный, конечно, как от Тибета до Китая, но всё же...'

    # '(затемнение (раньше это было обычное моргание))'
    # '(фон домиков ночью)'
    play music music_list['sweet_darkness']
    $ renpy.display_notify('Сейчас играет:\nSergey Eybog - Sweet Darkness')
    stop ambience fadeout 2
    scene bg thirty_five_grad_ext_houses_night with fade

    show 35grad_slavya 2 laugh pio at thirty_five_grad_night_lighting with dspr:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_houses_night at thirty_five_grad_blur

    thirty_five_grad_sl '...А потом Лена такая: «Ой! Кто мне жука в тарелку подложил?!» И как закричит!'

    'Славя по пути рассказывала мне всякие интересные истории из этого места: Как Алиса чуть памятник не взорвала, как Мику одна выступила на сцене в первый раз...'

    thirty_five_grad_alex 'Слушай, а получается, я тут не с самого начала смены, верно?'

    thirty_five_grad_sl 'Ага. Ровно с её половины. И как у тебя вообще так получилось?'

    'Надо что-то придумать. Да такое, чтобы звучало и реалистично, и правдиво.'

    thirty_five_grad_alex 'Понимаешь... Это вообще моя первая поездка в лагерь. Я... постоянно болел и меня никуда не пускали. Вот.'

    'По лицу Слави и не скажешь, что она мне особо-то и поверила, но другого выхода у меня нет.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Ну... Ладно. Только одно не сходится. А именно...'

    'Я остановил её рукой. И нет, не только потому, что слышать её не хочу, а ещё из-за того, что со стороны столовой доносились странные звуки копошения и дёрганья за ручку двери.'
    'Кто уже пытается тут что-то взламывать?'

    thirty_five_grad_alex 'Тс-с. Ты слышишь это?'
    show 35grad_slavya 2 worry pio with dspr
    thirty_five_grad_sl 'Ага... Но что это?'

    thirty_five_grad_alex 'Мне-то откуда знать? Стой здесь, а я на разведку.'

    thirty_five_grad_sl 'Ишь, смелый какой. А если там разбойник не один?'

    thirty_five_grad_alex 'Ха! Разбойник. Скажешь тоже. Не волнуйся, со мной всё хорошо будет. Ты, главное тут постой, а я тебя позову, если что.'

    'Девушка постояла немного в раздумьях, после чего грустно вздохнула.'
    show 35grad_slavya 2 sad pio with dspr
    thirty_five_grad_sl 'Ладно, иди. Я постою на стрёме. Но бездействовать не буду!'

    'Я улыбнулся и кивнул ей. Переживает она за меня. Как это мило. Но зато это придало мне некоторой уверенности в том, что я, собственно, и делаю.'
    # '(фон столовой снаружи)'
    scene bg ext_dining_hall_near_night with dissolve
    stop music fadeout 2
    'Обогнув здание и подкрадываясь сбоку, как в какой-нибудь игре, я увидел нашего злоумышленника. Им оказалась...'

    # '(музыка) Сергей Ейбог – Heather'
    play music music_list['heather'] fadein 3

    thirty_five_grad_alex '...Алиса? Ты ещё чего тут делаешь?'

    # '(спрайт Алисы испуганной)'
    show 35grad_alice 2 fear reb at thirty_five_grad_night_lighting with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_night at thirty_five_grad_blur

    'Девушка прильнула спиной к двери, пытаясь скрыть следы преступления. Но тут и сыщиком быть не нужно, чтобы понять это.'
    'На её прямом и слегка угловатом личике, (что, всё равно придавало некоторой красоты) читался откровенный страх, перерождающийся в непонимание.'
    # show 35grad_alice 2 angry reb at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_dv 'А т-ты что тут делаешь?! Время позднее, спать иди!'

    'Я скрестил руки на груди и серьёзно глянул на неудавшуюся преступницу:'

    thirty_five_grad_alex 'Вот и не уйду, пока не скажешь, что ты делала тут. Не волнуйся, я не позову ни Славю, ни тем более Ольгу, если со мной поделятся планами.'

    # '(спрайт Алисы обычная)'
    show 35grad_alice 2 normal reb with dspr

    'А вот теперь узнаю прошлую её! Хитрая, как лиса, глаза загорелись, и даже горделивая поза выдавала её с потрохами.'

    thirty_five_grad_dv 'Ты что, решил тоже встать на скользкую дорожку? Первый день тут, а уже. Вот. Дверь взломать хочешь?'

    thirty_five_grad_alex 'Наоборот. Хочу отговорить тебя от этого. Оно того не стоит. Только проблем у нас у всех будет выше крыши.'
    show 35grad_alice 2 tricky reb with dspr
    thirty_five_grad_dv 'Это почему ещё? Я скажу, что это была твоя идея.'

    thirty_five_grad_alex 'А ты разве не слышала про такое понятие, как «коллективная ответственность»?'
    show 35grad_alice 2 thinking reb with dspr
    th 'Девушка глубоко задумалась. Впервые вижу её такой... Неужели и она умеет мыслить?'

    # '(музыка стоп)'
    stop music fadeout 2.0
    show 35grad_alice 2 normal reb with dspr
    thirty_five_grad_dv 'Ладно, думаю, ты прав. Вообще-то мне плевать на остальных, но есть человек, который не должен пострадать.'

    thirty_five_grad_alex 'И кто это?'
    show 35grad_alice 2 laugh reb with dspr
    thirty_five_grad_dv 'А вот это уже секрет. Обалдуй!'

    thirty_five_grad_alex 'Хватит обзываться!'

    thirty_five_grad_dv 'А ты прекращай орать, а то услышат. Ты и так меня голодной оставил, а теперь...'

    # '(спрайт Алисы пропадает)'
    hide 35grad_alice 2 laugh reb at thirty_five_grad_night_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_night at thirty_five_grad_deblur

    th 'Она спустилась с лестницы и, отойдя на приличное расстояние, подмигнула мне. Странная она какая-то, но вряд ли плохая.'
    th 'Бывают такие люди, которые внешне пытаются показаться агрессивными, но внутри... Интересно, а у Алисы какая история жизни?'
    th 'Хотелось бы с ней поговорить просто по душам...'

    # '(поялвяется спрайт Слави обычный. Медленно)'
    show 35grad_slavya 1 normal pio at thirty_five_grad_night_lighting with dissolve2:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_night at thirty_five_grad_blur

    'Медленно подошла Славя и начала подниматься по лестнице. Её косички мило разлетались в стороны, а большая... гм... естественная часть тела поднималась в такт дыхания.'
    'Но больше всех мне нравилась её кожа. Естественный загар придавал ей уникальную черту и натуральность.'
    show 35grad_slavya 2 worry pio with dspr
    thirty_five_grad_sl 'Ну, как всё прошло?'

    'Обеспокоенно спросила девушка.'

    thirty_five_grad_alex 'Всё спокойно на удивление. Поговорили, решили проблему на месте. Можно идти по домам.'
    show 35grad_slavya 2 hmuri pio with dspr
    thirty_five_grad_sl 'Правда?'

    'В её голосе звучало подозрение, которое мне ой как не понравилось...'

    thirty_five_grad_sl 'Алёш, я прекрасно знаю, кто там был.'

    thirty_five_grad_alex 'Как?'

    # '(спрайт Слави печальный)'
    show 35grad_slavya 2 sad pio with dspr

    thirty_five_grad_sl 'По голосу догадалась. Я понимаю, что ты прикрыл своего товарища, и это, к слову, очень похвально. Но, Лёш, она пыталась взломать замок. Это плохо.'

    thirty_five_grad_alex 'Я понимаю. Но каждый имеет в своей жизни право на ошибку. Я не знаю историю Алисы. Кто она, как жила.'
    thirty_five_grad_alex 'Наверняка, не очень хорошо, раз для неё это в порядке вещей.'

    thirty_five_grad_sl 'И что же ты предлагаешь?'

    thirty_five_grad_alex 'Понять её. И попытаться по возможности решить кой какие проблемы, чтобы сделать из неё лучшую версию себя.'

    thirty_five_grad_sl 'Говоришь красиво. Но как это реализовать на практике?'

    thirty_five_grad_alex 'Добродетелью и разговором по душам, Славя. А теперь пойду я, пожалуй, баиньки.'

    # '(спрайт Слави обычный)'
    show 35grad_slavya 2 normal pio with dspr

    thirty_five_grad_sl 'Но до отбоя ещё полчаса.'

    thirty_five_grad_alex 'Хорошо. Спокойной ночи.'

    thirty_five_grad_sl 'Вот же ж... Спокойной, Алёш. Погоди!'

    thirty_five_grad_alex 'Чего?'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'А перекусить не желаешь?'

    thirty_five_grad_alex 'Не, я не голоден.'

    thirty_five_grad_sl 'Как хочешь. Придётся есть одной, эх.'

    # '(пропадает спрайт Слави)'
    hide 35grad_slavya 2 smile pio at thirty_five_grad_night_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_night at thirty_five_grad_deblur
    'Я развернулся и начал идти в сторону остановки... Впервые после последней встречи с Мику на душе было приятно.'
    'Но теперь немного и совестно, ведь я соврал ей, так как иду далеко не в дом. А к остановке...'

    # '(затемнение (раньше это было обычное моргание))'
    # '(фон ночных ворот)'
    scene bg ext_camp_entrance_night with fade
    # '(музыка) Goodbye Home Shores'
    $ renpy.display_notify('Сейчас играет:\nGoodbye Home Shores')
    play music music_list ['goodbye_home_shores']

    'Дорога была мрачной, тёмной и тягучей, как воск. Освещения толком не было, а какое и есть, то слабое.'
    th 'Надеюсь, что увижу хотя бы табличку с адресом! Как странно, что здесь нет КПП. Хоть какая-то должна же быть охрана.'

    'Дрязг-дрязг. Даже ворота не закрыты. Ну что за беспорядок! Я открыл их и вышел на свободу, если её можно таковой назвать.'
    'А затем, оглянувшись вокруг своей оси ещё раз и ещё несколько, обомлел...'

    '...Грёбанной... {w} Остановки... {w} Не было...'

    'Как будто её, блин, там никогда и не стояло!'
    'Долго я там не стоял, а в панике закрыл ворота и отбежал к ближайшему фонарю, словно он может спасти меня в случае чего. Да что же здесь происходит?!'

    'Всё. Хватит с меня на сегодня мистики и прочего сверхъестественного дерьма. Сыт по уши. Быстрым шагом, чуть ли не бегом, я отправился к домику...'

    # '(затемнение (раньше это было обычное моргание))'
    # '(фон ночного домика вожатой)'
    scene bg ext_house_of_mt_night with fade

    '...Перед тем, как войти, я постучался, а то мало ли. Сейчас ещё бы эротических казусов не хватало мне. Но вожатая крикнула «входите!».'

    # '(фон внутри домика вожатой ночью)'
    play sound sfx_open_dooor_campus_1
    scene bg int_house_of_mt_night with dissolve

    show 35grad_olga 3 normal paj at thirty_five_grad_night_lighting with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_house_of_mt_night at thirty_five_grad_blur

    thirty_five_grad_mt 'А это ты, Алексей. Мог бы не стучаться.'

    'Встретила меня Ольга в бабушкином халате. Хотя в это время он, скорее всего, в пике моды.'

    thirty_five_grad_alex 'Вдруг вы бы переодевались там или ещё чего.'
    show 35grad_olga 3 surprised paj with dspr
    thirty_five_grad_mt 'А что, звучит логично.'

    'Не то с шуткой, не то с иронией пробурчала она.'
    'А я тем временем разулся, снял рубашку с шортами и повесил на стул, а затем лёг на мягкую, даже слегка прохладную кроватку. Я бы тут же уснул, если не она...'
    show 35grad_olga 3 normal paj with dspr
    thirty_five_grad_mt 'Рассказывай, Алексей.'

    thirty_five_grad_alex 'Что именно?'

    thirty_five_grad_mt 'Как тебе первый день у нас? Подружился с кем-нибудь?'

    th 'Хороший вопрос. Удивительно, чем больше я здесь нахожусь, тем... обычнее кажется это место. Не считая треклятой остановки, конечно.'
    th 'Да и местные девчата... Особенные. Все красивы, умны... Хитры. И относятся ко мне как, чёрт возьми, к личности, а не на «принеси-подай-иди-нахер-не-мешай». Так что...'

    thirty_five_grad_alex 'Хорошо здесь. Пляж с музклубом понравились. И девушки все... {w} хорошие...'
    show 35grad_olga 2 normal paj with dspr
    thirty_five_grad_mt 'Но одна особенно?'

    'Мои щёки выдали меня всего. Всё моё чёртово нутро.'
    show 35grad_olga 3 shy paj with dspr
    thirty_five_grad_mt 'Эх, как это мило. Где же мои шестнадцать...'

    thirty_five_grad_alex 'А вам зачем? Вы и так выглядите на восемнадцать.'
    show 35grad_olga 3 normal paj with dspr
    thirty_five_grad_mt 'Теперь я понимаю, почему ты с моими девчатами быстро сдружился. Но я хочу дать тебе два предупреждения.'

    th '...Началось...'
    show 35grad_olga 2 angry paj with dissolve_fast
    thirty_five_grad_mt 'Первое: ты как мужчина, держи себя в руках.'

    th 'Дальше, пожалуйста.'
    thirty_five_grad_mt 'И второе: будь осторожнее с Алисой. Она у нас немного с... Ну, ты понял. Не хочу, чтобы с вами произошло что-то плохое, хорошо?'

    th 'А вот это было интересно. Но не так, как моя будущая встреча с подушкой.'

    thirty_five_grad_alex 'По рукам.'
    show 35grad_olga 3 normal paj with dspr
    thirty_five_grad_mt 'Вот и отлично. Спокойной ночи. И знай, в случае чего – идёшь сразу ко мне.'

    hide 35grad_olga 3 normal paj at thirty_five_grad_night_lighting with dissolve
    # ('sound')
    play sound thirty_five_grad_light_on_off
    scene bg int_house_of_mt_night2 with dspr

    'Я кивнул, а затем вожатая выключила свет.' 
    th 'Неужели этот день закончился? Хотя Ольга права. Мне нужно... Нет!'
    th 'Необходимо следить как за своими словами, так и действиями. А ещё нужно будет узнать завтра, как дела у Мику, ведь вела она себя странно, и потом разобраться с Леной.'
    th 'Вдруг ей тоже нужна будет помощь.'
    th '...А теперь другой вопрос. Кто поможет мне?'
    # '(музыка стоп)'
    stop music fadeout 2.0
    scene bg black at thirty_five_grad_vhs with fade
    $ persistent.day1 = True
    $ renpy.pause(1.0, hard=True)
    jump thirty_five_grad_day_two

    # stop music fadeout 2.0
    # python:
    #     config.skipping = False
    #     _skipping = False
    #     config.hard_rollback_limit = 0
    #     config.rollback_enabled = False
    #     save_name = ('re:35°')
    #     _game_menu_screen = None
    # play music thirty_five_grad_mm_music fadein 5
    # call screen thirty_five_grad_main_menu with fade
