label thirty_five_grad_day_two:
    $ save_name = ('35°. День 2')
    play sound thirty_five_grad_666
    $ renpy.pause(0.42, hard=True)
    scene bg thirty_five_grad_day2_glitch_epil
    show thirty_five_grad_transition_day_2_words at thirty_five_grad_words_anim    
    $ renpy.pause(2.0, hard=True)
    python:
        config.hard_rollback_limit = 0
        config.rollback_enabled = False

    # (фон домика вожатой утро)
    scene bg int_house_of_mt_sunset with flash
    play ambience ambience_camp_center_day fadein 6

    'Проснулся я тогда, когда только начало вставать солнце, а на часах было что-то около шести утра. То, что проснулся вообще не в своём доме, меня это не смутило.'
    python:
        config.rollback_enabled = True
        config.hard_rollback_limit = 1000
        thirty_five_grad_unlock_cg('cg_day2_miku_transition')
    'Так как понял, что это место не отпустит меня просто так. Хоть я и надеялся на быстрый исход.'
    'Ольга ещё спала, по самый лоб укутавшись в тонкое одеяло. Только смотря на неё, мне становится как-то не по себе, отчего зубы начинают ныть, а тело чесаться.'
    'Так что, забрал всё самое необходимое, а именно - полотенце, зубной порошок и мыло, я вышел на улицу в одних шортах, стараясь при этом не скрипеть половицами.'
    # (затемнение (раньше это было обычное моргание))
    # (фон возле домика вожатой с утра)
    play sound sfx_open_dooor_campus_1
    scene bg ext_house_of_mt_sunset with fade

    'Утро встретило меня самой радостной и лучшей погодой, которую я видал за последнюю пару лет.'
    th 'Не жарко, хотя градусник на двери показывает 20 градусов тепла, и это в тени. Слегка прохладный колющий ветерок с нотками морской соли забивался мне в ноздри.'
    # (музыка) Сергей Ейбог - So Good To Be Careless
    play music music_list['so_good_to_be_careless'] fadein 3

    th 'На улице никого не было, за исключением этих вечных птиц да сверчков.'
    th 'Хотя, если встать и хорошенько прислушаться, то можно приметить вдалеке чей-то равномерно быстрый топот, который, тем не менее, приближался.'
    th 'Хм, в голову приходят вчерашние слова Слави:'
    thirty_five_grad_sl '«А я тут зарядкой занималась!»'

    th 'Тогда всё объясняет. Хотя далеко не факт. Ведь вдруг тут есть и другие фанаты зарядки по утрам.'
    th 'Но я всё равно не решился уходить. Ведь попросту... не знаю дорогу до этих самых умывальников.'

    'На горизонте начал появляться силуэт в чёрной спортивной форме. При этом длинная коса на голове бегунье явно не мешала.'

    # (появляется спрайт Слави в чёрной форме)
    show 35grad_slavya 2 normal sport at thirty_five_grad_sunset_lighting with dissolve:
        xanchor 0.5 xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_blur
    'Девушка по пути увидала меня и сразу же, улыбаясь, остановилась. Никак к этому не привыкну. К улыбкам, то есть.'
    'Но на моё удивление, Славяна вообще не выглядела запыхавшейся.'
    show 35grad_slavya 2 smile sport with dspr
    thirty_five_grad_sl 'Доброе утро, Алёш. Смотрю, решил встать пораньше?'
    thirty_five_grad_alex 'То же утречка. Сам не знаю, как так получилось. Видать, природа и хорошая погода так подействовали.'
    show 35grad_slavya 2 laugh sport with dspr
    thirty_five_grad_sl 'А то! Ты мне не поверишь, но до первого приезда сюда я и сама часто спала чуть ли не до восьми часов. Только зарядка помогает мне оставаться бодрой в течение дня.'

    thirty_five_grad_alex 'В первый раз? То есть, ты сюда не первый год ездишь?'
    show 35grad_slavya 2 normal sport with dspr
    thirty_five_grad_sl 'Ну да. Этот уже третий так-то. Любимый лагерь! А, в общем-то, какие у тебя планы на утро? До подъёма прилично времени ещё.'

    thirty_five_grad_alex 'Я вообще хочу умывальники найти, а если повезёт, то и душевые.'
    show 35grad_slavya 2 smile sport with dspr
    thirty_five_grad_sl 'Это хорошо, а потом?'

    thirty_five_grad_alex 'Не понял, это какой-то допрос?'

    'Я хоть и спросил с улыбкой, но внутри себя чуял некий подвох.'
    show 35grad_slavya 2 normal sport with dspr
    thirty_five_grad_sl 'Тьфу ты, не волнуйся, я всё обязательно тебе покажу, но!'

    thirty_five_grad_alex '...Ничего не бывает задаром.'
    show 35grad_slavya 2 laugh sport with dspr
    thirty_five_grad_sl 'А вот нетушки! Мы с тобой живём в социалистической стране, где деньги на последнем месте, товарищ мой.'
    thirty_five_grad_sl 'Но всё же услуга есть услуга. Пускай она пойдёт также и ТЕБЕ на пользу.'

    'Меня это смутило, но я примерно догадывался, о чём она имеет в виду.'

    thirty_five_grad_alex 'Ты хочешь, чтобы я...'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'Верно. Чтобы занялся со мной спортом. Или же это слишком сложно для тебя?'

    'Она смотрела. Нет, пожирала меня взглядом, и если я скажу «нет» - мне конец.'
    'Хотя и не сказать, что я так уж против... Кхм, «спорта», ведь вместе с работой приходят светлые и умные мысли. Иногда.'

    thirty_five_grad_alex 'Ладно, хорошо. Я согласен.'
    show 35grad_slavya 2 shy sport with dissolve
    # (Славя в форме покраснела)
    'Девушка покраснела и, похоже, ей самой это было приятно.'
    show 35grad_slavya 2 laugh sport with dspr
    thirty_five_grad_sl 'Вот и славненько! Так что, когда закончим, вместе в душевые и пройдём. И, это... А где твоя форма?'

    # (Славя в форме обычная)
    show 35grad_slavya 2 normal sport with dspr
    thirty_five_grad_alex 'Я её как-то не брал с собой.'

    'Что было правдой, ведь у меня в тот день даже не было пары по физкультуре. Чёрт возьми, меня же теперь ещё и с университета отчислят...'
    'Как будто это сейчас вообще важно.'
    show 35grad_slavya 2 smile sport with dspr
    thirty_five_grad_sl 'Ладно, бег тогда отменяется. Но ничего! До пола доставать и в шортах можно.'

    # (затемнение (раньше это было обычное моргание))
    # (фон спортплощадки)
    scene bg thirty_five_grad_ext_playground_sunset with fade
    show 35grad_slavya 2 smile sport at thirty_five_grad_sunset_lighting with dspr:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_playground_sunset at thirty_five_grad_blur
    'Прошло не меньше часа, пока мы со Славей занимались... зарядкой на местной спортплощадке.'
    'Место крайне колоритное, так как сильно напоминало мне о моём детстве, когда ещё был активным и в принципе весёлым мальчуганом. Эх, времена...'

    show 35grad_slavya 2 laugh sport with dspr
    thirty_five_grad_sl 'И раз! И два! И три!'

    '...Оказывается, давно я дома зарядку не делал. Спину ломит, а коленки и вовсе помрут. Чёрт, как же болит шея теперь...'
    show 35grad_slavya 2 smile sport with dspr
    thirty_five_grad_sl 'Всё, Алёш, остановись. С тебя на сегодня хватит. На самом деле хорошо постарался. Для новичка!'

    'И тихо рассмеялась, но так мило. На самом деле мне с ней было тепло и уютно, прямо как с Мику.'
    'Движение её рук, её яркие, звёздные глаза... Было в ней что-то, дающее ту самую домашнюю атмосферу.'
    show 35grad_slavya 2 normal sport with dspr

    thirty_five_grad_sl 'О чём задумался?'

    thirty_five_grad_alex 'Да так, что форма тебе идёт. Где купила?'
    show 35grad_slavya 2 smile sport with dspr

    thirty_five_grad_sl 'Ой, спасибочки. Но она вроде обычная, даже не заграничная. Помню только, что это отец мне подарил, когда я на первый год сюда приехала.'
    thirty_five_grad_sl 'А почему спрашиваешь?'

    'Но я не стал ей отвечать. Иначе это будет... да никак это не будет.'

    thirty_five_grad_alex 'Я выполнил часть своей сделки.'
    show 35grad_slavya 2 laugh sport with dspr

    thirty_five_grad_sl 'Алёша, не разочаровывай. Говоришь как капиталист.'

    thirty_five_grad_alex 'И будь добра, прекрати меня так называть. Я давным-давно вырос из этого детского имени.'

    # (спрайт Слави в форме грустный)
    show 35grad_slavya 2 sad sport with dissolve_fast
    stop music fadeout 5
    'Неожиданно грубо даже для себя объявил я. Неприятно, надо извиниться.'

    thirty_five_grad_alex 'Славь, я...'

    thirty_five_grad_sl 'Ничего, это ты прости. Иди за мной.'
    hide 35grad_slavya 2 sad sport at thirty_five_grad_sunset_lighting with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_playground_sunset at thirty_five_grad_deblur
    'Ожидаемо холодно. Нужно научиться держать себя в руках. Не маленький уже...'

    # (затемнение (раньше это было обычное моргание))
    # (фон умывальников)
    # (музыка) Сергей Ейбог - Dance Of Fireflies
    play music music_list['dance_of_fireflies'] fadein 3
    scene bg thirty_five_grad_ext_washstand_sunset with fade
    'Оказывается, умывальники с душевыми кабинками были рядом с моим домиком! Вполне удобно, так что путь я запомнил. Но какой ценой...'
    show 35grad_slavya 2 sad sport at thirty_five_grad_sunset_lighting with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_washstand_sunset at thirty_five_grad_blur

    thirty_five_grad_alex 'Славь, прошу, прости. Я не специально! Не знаю, что нашло на меня.'

    thirty_five_grad_sl 'Да всё в порядке, со всеми же бывает. Ты лучше это, долго под едва тёплой водой не стой, заболеешь ещё.'
    hide 35grad_slavya 2 sad sport at thirty_five_grad_sunset_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_washstand_sunset at thirty_five_grad_deblur
    'Затем она скрылась в другой части умывальников, называемых «женскими». Ладно, сейчас она и слушать меня не хочет, а значит, нужно будет подойти чуть позже.'
    'Точно! Угощу батончиком и возможно, её сердце оттает. Хотя, она же не самая злая девушка на свете, поэтому должна принять угощение...'

    'Ну вот, мне осталось только помыться. Зубы с горем пополам почистил, поэтому отложил сложное дело на потом.'
    'Раздевшись догола, я зашёл в одну из ближайших ко мне душевых. Внешне он не казался старым, а наоборот, словно его сделали недавно!'
    play sound sfx_close_water_sink
    $ renpy.pause(0.5)
    play sound sfx_water_sink_stream loop
    'Но всё-таки кое-где иногда проступала ржавчина. Да это и не страшно. Заранее отойдя так, чтобы меня не задела возможная ледяная струя воды, я повернул ручку крана...'
    'Видать, вода успела хорошо прогреться за вчерашний день, потому что была довольно-таки тёплой.'
    'Далеко не кипяток, но всё же помыться в ней спокойно смог. Тщательно вытерся, оделся в форму и отправился в домик, чтобы отдохнуть перед разводом...'
    play sound sfx_close_water_sink
    # (затемнение (раньше это было обычное моргание))
    # (фон домика вожатой + она сама в ночнушке)
    stop ambience fadeout 3
    scene bg ext_house_of_mt_sunset with fade 
    $ renpy.pause(1.0)
    scene bg thirty_five_grad_int_house_of_mt_sunset with dissolve
    play sound sfx_open_door_1

    'Как только зашёл, то сразу заприметил Ольгу. От её обычного, строгого вида осталось только одно название.'
    'Она сидела в обнимку с подушкой, ведя жестокий бой с остатками сна. Я не стал ей мешать, поэтому, как только дошёл до кровати...'
    show 35grad_olga 2 angry paj at thirty_five_grad_sunset_lighting with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_house_of_mt_sunset at thirty_five_grad_blur
    thirty_five_grad_mt 'Алексей, выйди, пожалуйста. Погуляй. А то я...'
    hide 35grad_olga 2 angry paj at thirty_five_grad_sunset_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_house_of_mt_sunset at thirty_five_grad_deblur
    '...Уснула. Ну что за женщина! А ещё строит из себя... Хотя, когда она так спит, то выглядит очень уж милой.'
    'Ладно, она права. Не стоит ей сейчас мешать. Пускай поспит, вдруг и правда вчера устала.'

    # (фон домика вожатой снаружи)
    scene bg ext_house_of_mt_sunset with dissolve
    play sound sfx_open_door_1
    play ambience ambience_camp_center_day fadein 3
    'Я тихо вышел из домика, даже ни разу не скрипнув половицей! А посидеть и отдохнуть можно на лежанке.'
    'Правда, я без верха, в одних шортах. Так что надеюсь, девушек будет немного...'

    # (музыка стоп)
    show blink
    stop music fadeout 3
    '...И, как всегда, сглазил. Вдали виден ещё один силуэт в белом халате. Но принадлежал он явно не пионерке.'
    'Большой рост, стройное, как у модели тело и распущенные волосы вместе с поведением. А глаза – отдельное достижение этого человека.'
    'Как её звали? Виола, вроде. Да, точно.'
    'Цоканье каблуков раздавалось всё ближе и ближе, а в это время, пока она полностью не подошла, я притворился спящим. Вдруг она меня не заметит?'

    'Похоже, заметила. Так как цоканье полностью прекратилось, я ощутил, как кто-то стоит рядом со мной, и атмосфера происходящего стала... не очень хорошей.'
    # (музыка) Gentle Predator
    # (появляется спрайт Виолы)
    play music music_list['gentle_predator'] fadein 3
    thirty_five_grad_cs 'О-о-о, так-так-так. И что же у нас за пионер такой, который позволяет сидеть в общественном месте... без верха?'

    'Если бы это говорила Ольга, то звучала она максимально злобно, и её при этом можно было бы понять, но Виола...'
    'Словно она поймала сладкий кусок халявного пирога в воздухе. Да и тон голоса был соответствующим.'

    'Я потихоньку открыл глаза:'
    scene bg ext_house_of_mt_sunset
    show 35grad_viola 2 sly reb at thirty_five_grad_sunset_lighting with dspr:
        xalign 0.5 xanchor 0.5
    show unblink
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_blur

    thirty_five_grad_cs 'Ах, он ещё спал, оказывается. Батюшки, вы только гляньте на это.'

    'Её розовые щёки смущали меня. Неужели она так заигрывает со мной?'

    thirty_five_grad_alex 'В-виола? И вам... доброе утро.'

    show 35grad_viola 2 normal reb at thirty_five_grad_sunset_lighting with dissolve_fast
    thirty_five_grad_cs 'Утра, утра. Парень, а чего ты тут сидишь-то? Да без одежды?'

    'Теперь её голос сменился на нормальный, серьёзный. Я её когда-нибудь пойму?'

    thirty_five_grad_alex 'Вот, Ольга Дмитриевна всё ещё спит, поэтому не стал ей мешать.'
    show 35grad_viola 2 shy reb at thirty_five_grad_sunset_lighting with dissolve_fast
    thirty_five_grad_cs 'Ну, у меня она быстро проснётся, тем более что вставать уже надо.'
    
    'Но её вид снова сменился на розовый и смущённый? Я не знаю, как описать это!'
    show 35grad_viola 2 normal reb at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_cs 'И больше так не сиди! А то сам провоцируешь на такие шутки.'
    

    # (спрайт Виолы пропадает)
    hide 35grad_viola 2 normal reb at thirty_five_grad_sunset_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_deblur
    play sound sfx_close_door_1
    'И зашла внутрь домика. Да что с ней не так? Блин, а утро только начинается...'    
    show blink
    # (затемнение (раньше это было обычное моргание))
    'Просидели они там недолго, пару минут максимум. Зато Ольга вышла довольной и сразу в халате.'
    show unblink
    scene bg ext_house_of_mt_sunset with fade
    # (появляется спрайт Ольги и Виолы)
    show 35grad_olga 2 surprised paj at thirty_five_grad_sunset_lighting with dissolve:
        xalign 0.2 xanchor 0.2
    show 35grad_viola 2 normal reb at thirty_five_grad_sunset_lighting with dissolve:
        xalign 0.8 xanchor 0.8
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_blur
    thirty_five_grad_mt 'О, Алексей. А чего ты тут без одежд как попрошайка?'
    
    thirty_five_grad_alex 'А всё потому что вы меня в домик не пустили.'
    show 35grad_viola 2 shy reb at thirty_five_grad_sunset_lighting with dspr

    thirty_five_grad_cs 'Ай-ай-ай, Ольга-Ольга. Хорошо, что я его первым заметила, а не другая пионерка. Шуму-то было! Считай, я тебя и во второй раз спасла. За тобой должок.'
    show 35grad_olga 2 angry paj at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_mt 'В-виола! Так, Лёша, не слушай её. Заходи и переодевайся. Умыться не забудь!'
    'Перед тем, как зайти, ответил:'

    thirty_five_grad_alex 'Я это уже сделал.'

    # (музыка стоп)
    # (затемнение (раньше это было обычное моргание))
    # (фон домика вожатой внутри)
    scene bg thirty_five_grad_int_house_of_mt_sunset with fade
    play sound sfx_open_door_1
    stop music fadeout 3
    'Кровать была всё такой же мягкой и удобной. Я прилёг всего лишь на секундочку, но вставать уже так не хочется!'
    'Может, ну его, разводы там всякие, столовки... Но дверь против моей воли всё же открылась.'

    # (спрайт Ольги в халате)
    show 35grad_olga 2 normal paj at thirty_five_grad_sunset_lighting with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_sunset at thirty_five_grad_deblur
    thirty_five_grad_mt 'Алексей, хватит лежать, успеешь ещё. Давай, иди на площадь. Я догоню.'

    'Без лишних слов я встал, быстро натянул рубашку и галстук, с пятой попытки и нервного взгляда вожатой всё же получилось, и потопал на площадь.'
    'Ведь чем раньше приду, тем... А хотя, нет. Ольгу же нужно будет ждать.'

    # (фон площади)
    scene bg ext_square_day with fade
    play sound sfx_close_door_1
    # (музыка) Сергей Ейбог - Timid Girl
    play music music_list['timid_girl']

    'По пути мне так никто из знакомых не попался. Даже Мику. Всё же, переживаю я за неё как-то, сам даже не понимаю, почему.'
    'Вроде, мне здесь все девушки приятны, но она... словно заняла премиум место в моём сердце. Странно как-то. Знакомы же только сутки...'

    'На площади было уже полно пионеров и октябрят. Любопытно всё же, как они все такой гурьбой помещаются на такой небольшой площадке...'
    'Но к своим ребятам я всё же смог попасть, никого не растолкав по пути.'

    'Затем, со мной поздоровались ребята. В принципе, я их всех даже был рад видеть в какой-то степени. Господи, только день прошёл с моего прибытия, а я как будто домой попал.'
    'Да и вообще ничего не произошло странного... Но да ладно, я обратился сразу к Славяне:'

    # (спрайт Слави в форме)
    show 35grad_slavya 2 normal pio with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day at thirty_five_grad_blur
    thirty_five_grad_alex 'Славя, прошу, прости меня ещё раз! Я не специально, честно!'

    'Но она лишь легонько отмахнулась, а на мордашке была та же улыбка, с которой она впервые меня встретила.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Алёшка, кончай уже. Всё в порядке, я про то в принципе уже забыла, и тебе стоит. Вообще, хочешь совет?'

    thirty_five_grad_alex 'Давай, почему нет.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Рада, что ты умеешь слушать людей. Не бери в голову всё то, о чём тебе говорят или пытаются тебя как-то задеть.'
    thirty_five_grad_sl 'Вообще не стоит переживать такие темы из раза в раз, ибо оно сгрызёт человека изнутри. Так что просто будь налегке как... Мику!'
    show 35grad_slavya 2 shy pio with dspr
    thirty_five_grad_sl 'Ну, или я.'

    'Она снова схватилась за свою косу как за спасательный жилет и покраснела.'

    thirty_five_grad_alex 'Хорошо, спасибо. Кстати, насчёт её. Почему она не посещает утренние мероприятия?'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Тут... всё сложно. Она у нас не очень людимая. Как только не пытались её вытащить оттуда, так вечно там сидит.'
    thirty_five_grad_sl 'Пока кое-кто не приехал. Ты первый, кому она более-менее открылась за всё это время.'

    thirty_five_grad_alex '...А ты откуда знаешь?'

    # (спрайт Слави смущённой)
    show 35grad_slavya 3 shy pio with dissolve_fast
    'И снова покраснела.'

    thirty_five_grad_sl 'Ну я же тоже по лагерю хожу, и слышала то, что вы делали вчера. Такой радостной я её никогда лично не слышала.'

    thirty_five_grad_alex 'Я... Просто не знаю, что она думает обо мне.'

    thirty_five_grad_sl 'А?'

    thirty_five_grad_alex 'Ну, вчера перед ужином... Она просто выгнала меня. Сказала, что срочные дела или типа того.'

    # (Славя улыбается)
    show 35grad_slavya 2 laugh pio with dspr
    'Славя рассмеялась в кулачок, что поставило меня в тупик.'

    thirty_five_grad_alex 'Чего смешного?'

    thirty_five_grad_sl 'Так это же элементарно, Ватсон. Как ты сам не догадался? Она просто волнуется. Я б на её месте себя вела точно так же.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Поэтому тебе не о чём переживать. Просто поговори с ней сегодня, вот и всё.'

    thirty_five_grad_alex 'Хорошо, благодарю. Как камень с души.'

    thirty_five_grad_sl 'Да это мелочи. Лёш, ты парень хороший, просто... с самооценкой что-то делать надо. И физкультура в этом как раз поможет. Намёк понятен?'
    show 35grad_slavya 2 normal pio with dspr
    'Я кивнул.'

    thirty_five_grad_sl 'А с формой я разберусь, не переживай. На складе должно что-то свежее остаться, просто назови свой размер.'

    'И снова те же грабли!'

    thirty_five_grad_alex 'Да я как-то и не задумывался.'
    show 35grad_slavya 2 surprised pio with dspr
    thirty_five_grad_sl 'Тебе что, родители одежду покупают?'

    '...Я готов был провалиться сквозь землю...'

    thirty_five_grad_alex '...'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Да я же шучу! Ладно, прости. Ничего страшного! Глаз у меня меткий. Так.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'На вид ты метр восемьдесят пять, в плечах широкий, в талии узкий. Как по стандарту.'

    thirty_five_grad_alex 'Да тебе либо в модельеры, либо в снайперы, Славь.'
    show 35grad_slavya 2 smile pio with dspr 
    thirty_five_grad_sl 'У меня отец охотником раньше был, так что... наследственное!'

    'А затем она оглянулась мне через плечо.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Всё. Вставай в строй.'

    'Послушался её.'
    show black with fade
    pause 1.0
    thirty_five_grad_sl 'Все в строй, ребята. Вожатая идёт. Лёш, ты самый высокий из нас. Становись первым.'
    hide black
    # (спрайты всех, кроме Мику)
    show 35grad_electronnik 1 normal pio with dissolve:
        xalign -0.2 
    show 35grad_slavya 2 normal pio:
        xalign 0.3
    show 35grad_alice 2 normal reb:
        xalign 0.7
    show 35grad_lena 1 normal pio:
        xalign 1.2

    'Ненавижу в линейках быть первым, но зато это открыло для меня что-то новенькое! Информация эта не очень полезная, но просто занятная.'
    'Рядом со мной по росту встали парни, за ними Славя, потом Алиса, Лена и в конце концов та самая... библиотекарша... Внезапно.'
    
    hide 35grad_electronnik 1 normal pio
    hide 35grad_slavya 2 normal pio
    hide 35grad_alice 2 normal reb
    hide 35grad_lena 1 normal pio with fade

    # (спрайт Ольги)
    show 35grad_olga 2 normal form pan with dissolve:
        xalign 0.5 xanchor 0.5
    thirty_five_grad_mt 'Всем доброе утро.'

    'Мы протянули все то же самое.'

    thirty_five_grad_mt 'Наступает новый день, а с ним – новые обязанности, заботы, и конечно же – задания!'

    thirty_five_grad_alex 'А отдыхать когда?'

    'Я совершил попытку шуткануть. Надеюсь, не обернётся для меня чем-то плохим...'
    show 35grad_olga 2 angry form pan with dspr
    thirty_five_grad_mt 'Так, Алексей. Перебивать не нужно, пожалуйста. Когда скажу, тогда и будем! Ладно, давайте начинать!'

    'И добавила полушёпотом:'

    # (музыка стоп)
    stop music fadeout 3
    thirty_five_grad_mt 'Чтобы это всё закончилось, наконец...'

    'Впервые с самого утра я был с ней согласен.'

    # (затемнение (раньше это было обычное моргание))
    scene black at thirty_five_grad_vhs with fade
    # (музыка) Сергей Ейбог - Goodbye Home Shores
    play music music_list['goodbye_home_shores'] fadein 3
    'Почему-то Ольга начала с конца строя.'
    'Первой под натиском заданий пала та библиотекарша по имени Женя. Хотя, по её виду и не скажешь, что она против сидеть в библиотеке.'
    'Затем Лена, которую отправили в медпункт разгружать новую поставку лекарств.'
    'Алису почему-то проигнорировала, просто кивнув ей, и та ушла.'
    'Славе так же, что вызывало ещё больше подозрений.'
    'Парней попросила остаться, чтобы подробнее рассказать суть их задач.'
    'И, наконец, добралась до меня:'
    scene bg ext_square_day with fade
    show 35grad_olga 2 normal form pan with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day at thirty_five_grad_blur
    thirty_five_grad_mt 'Алексей, у тебя будет много работы, но я уверена, что ты с ними справишься.'
    thirty_five_grad_mt 'Смотри, я тебе сейчас дам три задачи: помочь Лене с коробками. Поверь, они тяжёлые.'
    thirty_five_grad_mt 'Помочь Алисе с обновлением стадиона, ведь зная её она одна будет делать это целый день.'
    thirty_five_grad_mt 'И помочь Славе, но она сама тебе всё расскажет. Выполнять можешь в любом порядке, главное, чтобы ты это всё сделал за сегодня. Ты меня понял?'

    thirty_five_grad_alex 'Да, Ольга Дмитриевна, услышал. Но можно отпроситься сходить кое-куда?'
    show 35grad_olga 2 angry form pan with dspr
    thirty_five_grad_mt 'Не поняла.'

    thirty_five_grad_alex 'Я хочу сходить к Мику. Проверить, как у неё дела.'
    show 35grad_olga 2 smile form pan with dspr
    'Мило улыбается мне, а сказать не может.'

    thirty_five_grad_mt 'Хорошо, сходи. Но потом сразу иди, помогай. Девочки тебе этого не забудут, если ты не придёшь.'

    'А нет, лучше бы молчала.'

    # (пропадает спрайт Ольги)
    hide 35grad_olga 2 smile form pan with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_square_day at thirty_five_grad_deblur
    'Я кивнул ей и, сунув руки в карманы, двинулся сначала в столовую, где не было ничего интересного от слова совсем, ведь я поел в тишине и спокойствии.'
    'А затем пошёл уже к первоначальной по важности цели. Ждать остальных не имело смысла, так как они уже все и так разошлись, кроме кибернетиков. И почему их так все называют?'

    # (музыка стоп)
    # (фон музыкального клуба снаружи)
    # (музыка) Sergey Eybog - My Daily Life
    play music music_list['my_daily_life'] fadein 3
    scene bg ext_musclub_day with fade
    'Солнце уже давало о себе знать тем, что даже земля начала греться у меня под ногами. Но хуже жары была только духота!'
    'Кстати, тут же есть пляж! Что мешает мне пригласить сейчас ту же Мику или Славю туда?'
    'Но вторая, зная о том, какая она пчёлка трудолюбивая, вряд ли согласится, да и осудит, что с утра её дёргаю отдыхать...'

    'Как раз уже подошёл к клубу, только уже со стороны панорамного окна, откуда было хорошо видно, что внутри происходит.'
    'Но я всё равно не сдержался от любопытства, поэтому пристроился к окну.'

    'Мику сидела на небольшом стульчике перед роялем и с задумчивым видом нажимала на его клавиши. Неужели придумывает новую песню?'
    'Я тихонько отстранился. Обычным шагом направился сразу к двери. При этом, не стучась, как и просила аквамариновая красавица.'

    # (фон внутри музклуба)
    scene bg int_musclub_day with fade
    stop ambience fadeout 3
    play sound sfx_open_door_1
    # (спрайт Мику обычный)
    show 35grad_miku 1 normal pio ponytails with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_blur
    thirty_five_grad_mi 'Кто там? А, Лёшка, это ты. Доброе утро.'

    thirty_five_grad_alex 'И тебе.'

    'Наступила проклятая неловкая тишина. Словно злая колдунья забрала все необходимые для разговора слова. Так, успокойся.'
    'Судя по её настрою, она сейчас в таком же положении. Вот, как её циановые глазки бегают туда-сюда. Но затем она отворачивается...'

    thirty_five_grad_alex 'Мику. Я хотел узнать, как ты.'
    thirty_five_grad_mi 'А? Я хорошо. Благодаря тебе, конечно. Но ты что-то хотел?'

    thirty_five_grad_alex 'Да. Проведать тебя. Ведь ты вчера так повела себя и подумал, что виноват перед тобой. Ты и на ужин не пришла, между прочим.'

    show 35grad_miku 1 sad pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Прости.'

    'Мне это надоело. Я хочу, чтобы она была чуточку смелее, чтобы поверила в себя!'

    thirty_five_grad_alex 'Микусь, я с утра тут пляж видел. Давай вместе сходим? Необязательно даже купаться. Просто прогуляться.'

    # (Мику улыбается)
    show 35grad_miku 2 normal pio ponytails with dissolve
    'Девушка помедлила, приняла лёгкий задумчивый вид. Затем уголки её губ легонько приподнялись, и она закивала. Победа!'
    show 35grad_miku 2 laughter pio ponytails with dspr
    thirty_five_grad_mi 'Хорошо, я согласна! Гулять, так гулять. А то сначала даже подумала о чём-то нехорошем, но потом... В общем, пошли уже.'

    'Она сильно покраснела и прикусила губу. Но внутри себя чувствовал только всё разгорающийся жар, как в доменной печи.'
    'А может, это всё из-за погоды чёрт его поймёт.'

    # (музыка) Sergey Eybog - I Tried To Bring It Back
    play music music_list['tried_to_bring_it_back'] fadein 3
    thirty_five_grad_alex 'Можно вопрос?'

    thirty_five_grad_mi 'Да, конечно!'

    thirty_five_grad_alex 'Чего ты стесняешься?'

    # (спрайт Мику грустный)
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Можно я не буду на него отвечать? Я прекрасно знаю, что веду себя странно, но тому есть причина, которую я никому не расскажу. {w} Даже тебе. {w} Пока.'
    thirty_five_grad_mi 'Пока что. Просто... я всю жизнь была одна. Даже ни на секунду не преувеличиваю.'
    thirty_five_grad_mi 'Давай лучше расскажу тебе на пляже? Ветер унесёт плохие слова и память. Так будет проще.'

    thirty_five_grad_alex '...Хорошо. Пошли?'

    'Её слова были для меня... Я даже не знаю. Видать, у неё много горя за плечами. Но что с ней такое произошло? Что она думает и чувствует?'
    'И самое главное, почему у меня такое чувство, что я обязан разобраться со всем этим, чтобы ей помочь?'

    # (затемнение (раньше это было обычное моргание))
    # (фон домиков)
    scene bg ext_houses_day with fade
    'Мы шли тихим и размеренным шагом, никуда не спеша и никого не боясь. Пока я рядом, нас никто не побеспокоит. Чувствую это, наверное.'
    'Мику тем временем вела себя вроде чуточку спокойнее. Слегка открыто, но всё равно была немного зажата.'
    show 35grad_miku 1 sad pio ponytails with dissolve:
        xalign 0.5 xanchor 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_day at thirty_five_grad_blur
    thirty_five_grad_alex 'Тебя что-то беспокоит прямо сейчас?'

    thirty_five_grad_mi 'Нет. Просто наслаждаюсь погодой! Скажи же, как хорошо сейчас! Я редко выхожу на улицу, но на пляже... По сути, вообще не была.'

    thirty_five_grad_alex 'Но почему? Та же Славя говорила, что ты сама отказалась.'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'И она не солгала. Просто... Я не знаю. Боюсь, наверное. Хотя нет. В школе боялась, да. А сейчас... Не доверяю?'
    show 35grad_miku 1 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ай, не загоняйся. У меня просто нет на это времени.'

    # (музыка стоп) звуки природы
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    'Я остановился. Что-то мне не нравилось в её словах, но снова продолжаю путь. А она этого даже и не заметила. Оно и к лучшему.'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ох, как солнышко-то печёт! Только-только же сказала, что не так уж и жарко.'

    thirty_five_grad_alex 'Верно. Всегда так бывает, что понадеешься... Эм, Мику.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Да?'

    thirty_five_grad_alex 'Ты доверяешь мне?'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Может быть. То есть да. Просто мы с тобой хоть и знакомы второй день, но состоим в одном клубе.'
    thirty_five_grad_mi 'А ты, наверно, знаешь, что в школах Японии тоже есть клубы? Я была в одном из них. Угадай, в каком?'

    thirty_five_grad_alex 'В музыкальном?'
    show 35grad_miku 2 laughter pio ponytails with dspr
    thirty_five_grad_mi 'Почти! Я хотела туда, но не успела. Места были заняты. Так что попала в кружок готовки.'
    thirty_five_grad_mi 'Но пробыла там тоже недолго. Год почти как я потом с родителями переехала в Союз. А потом снова пошла в школу. И как было обидно, когда узнала, что здесь не было клубов!'
    thirty_five_grad_mi 'Но только перед первым днём школы узнала, что она всё-таки была музыкальной! Представляешь, ока-сан мне рассказала об этом! Я была тогда так счастлива!'

    'Поток её мыслей был в радость для меня. Слышать её счастливый голос как услада для ушей и мёд для души.'
    'Даже если она просто притворяется счастливой, то всё равно рад этому.'
    show 35grad_miku 2 sad pio ponytails with dspr
    thirty_five_grad_mi 'Ой, прости. Иногда, когда волнуюсь, я бываю такой говорливой!'

    thirty_five_grad_alex 'Знаешь что?'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Лёшка, не томи!'

    'Я хитро улыбнулся.'

    thirty_five_grad_alex 'Мне даже нравится твоя эта черта. Она делает тебя милой, хотя ты и без неё очень красива и симпатична. Мне нравится.'

    'Мне стоило много усилий, чтобы сказать это вслух. Не, я не соврал ей, а по правде так считаю. Просто на это необходима определённая... смелость.'

    # (спрайт Мику грустный)
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'За эти два дня я столько приятных слов услышала...'

    'В этот раз она даже не покраснела, а даже наоборот, ещё больше погрустнела. Что я сделал не так?'

    thirty_five_grad_mi 'Понимаешь меня...'

    # (фон пристани)
    play ambience ambience_lake_shore_day
    scene bg ext_boathouse_day with fade
    '...Только девочка не успела договорить, так как увидела голубого мастодонта в виде реки, которая словно в вечность уходила в бесконечность.'
    'Вдалеке видна железная дорога, по которой проезжает товарный поезд, а дальше видны сельскохозяйственные угодья.'
    show 35grad_miku 1 surprise pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_boathouse_day at thirty_five_grad_blur
    thirty_five_grad_mi_alex 'Как тут красиво!'

    'Одновременно произнесли мы, отчего немного смутились. Почему бы и нет. Это было мило.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ох, оно напоминает мне о доме...'

    'Мы пошли по пляжу. Ближе к воде.'

    thirty_five_grad_alex 'Ты о Японии?'
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Не. Просто так... показалось. Я ведь сама живу недалеко от реки.'

    thirty_five_grad_alex 'Ясно.'

    'Где-то в небе над нами пролетело несколько чаек.'

    thirty_five_grad_alex 'Мику, можно вопрос?'
    show 35grad_miku 2 serious pio ponytails with dspr
    thirty_five_grad_mi 'Конечно! Если он не пошлый, конечно. А-то мальчики, сам понимаешь, опасными могут быть...'

    'Теперь смутился уже я.'

    thirty_five_grad_alex 'Эй!'
    show 35grad_miku 2 laughter pio ponytails with dspr
    thirty_five_grad_mi 'Я тоже люблю играться!'

    'Весело произнёс ходячий оркестр.'

    # (музыка) Sergey Eybog - Memories (Piano Version)
    play music music_list['memories'] fadein 3
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_alex 'Ну ты! Ладно. Но... прости заранее, если тебе вопрос этот не понравится, можешь не отвечать. В общем...'
    thirty_five_grad_alex 'Почему тебя обижали в школе? Из-за чего тебе так страшно проявлять доверие?'
    show 35grad_miku 3 smile pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ты такой заботливый, и я понимаю твоё любопытство, но... Я обязательно тебе расскажу про это, но поделись и о себе.'
    thirty_five_grad_mi 'Тоже хочется знать, вообще-то, с кем общаюсь. Точнее знаю, но по-дро-бно-сти!'

    'Мне хотелось её приобнять, но я боюсь, что спугну её. Да и со стороны странно смотрелось бы.'
    show 35grad_miku 2 normal pio ponytails with dissolve_fast
    thirty_five_grad_alex 'А... Что я. Обычный парень, который окончил школу кое-как, при этом уже успевший поработать электриком.'
    thirty_five_grad_alex 'Люблю читать и слушать музыку. Даже собираюсь учиться у тебя этому!'

    'Я поднял небольшой камушек с песка, чтобы сделать пару «блинчиков». Не получилось.'

    thirty_five_grad_alex 'А так... Тоже друзей нет. Я не особо из разговорчивых, как видишь.'

    'Мику последовала моему примеру. Но у неё один раз получилось даже!'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ва! Ты видел-видел?!'

    thirty_five_grad_alex 'Ага, молодец.'
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёш... Вот чего-чего, но я не ожидала этого услышать...'

    thirty_five_grad_alex 'Чего?'

    thirty_five_grad_mi 'Ну что, у тебя друзей нет и ты работал на такой опасной... Ух.'

    thirty_five_grad_alex 'Это ты так думаешь. Но... во всём этом моя вина.'
    show 35grad_miku 2 fear pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Почему? Почему ты говоришь такое?'

    thirty_five_grad_alex 'Ты говоришь, что я хороший, но... Просто плохо знаешь меня. Я зануда и параноик.'

    'Говорил и говорил спокойным, рассудительным голосом, но внутри меня была целая буря противоречий.'
    'Я не могу им всем сказать правду, особенно Мику. От этого и больно.'
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёша, хватит. Не стоило поднимать эту тему.'

    'Как всегда. Я всё испортил.'

    thirty_five_grad_alex 'Прости.'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'А знаешь, мы даже ведь похожи. На моей родине говорят, что людей, которые ты встретил на своём жизненном пути, появляются не зря.'

    thirty_five_grad_alex 'Как романтично.'
    show 35grad_miku 1 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Ага. Ты очень хороший, просто знай это, слышишь? Я встречала много плохих людей, но ты далеко не такой. И я не хочу, чтобы ты думал о себе так.'

    'Её слова согрели меня изнутри, и в них даже хочется верить. Ха, как забавно! Я привёл её сюда для того, чтобы помочь ей, а в итоге она исцеляет мою душу.'
    'Интересно, а в моём времени такое вообще было бы возможно?'

    thirty_five_grad_alex 'Ладно, пойдём отсюда. Не хочу, чтобы ты на жаре стояла.'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Эх, Лёшка, какой же ты милый! Но я тебе и свою историю не рассказала. Обещала ведь. Не волнуйся, она будет короткой.'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast
    'Она медленно вдохнула и выдохнула, словно приготовилась терпеть боль.'

    # (музыка) ARTERRIA - Excited Happiness
    play music thirty_five_grad_excited_happiness fadein 3.0
    $ renpy.display_notify('Японское определение, обозначающее людей полуяпонского происхождения, то есть имеющих одного родителя неяпонца.')
    show 35grad_miku 1 sad pio ponytails with dspr
    thirty_five_grad_mi 'Я *Хафу, Лёша. Полукровка. Поэтому мне в школе жизни не было. Практически все дразнили, а те, кто нет, игнорировали. Меня считали грязью, но хотя бы не били.'
    show 35grad_miku 1 normal pio ponytails with dspr
    thirty_five_grad_mi 'Вот и вся история, почему я никому не доверяю. Зато эта страна многонациональная. Тут ко всем одинаково относятся, но...'

    'Меня это тронуло. Пускай я и не знаю, каково это, но наверняка очень и очень больно.'
    'Поэтому специально перешёл на шёпот, чтобы маленькая чудная девочка внутри Мику успокоилась, чтобы дать ей понять, что она в безопасности.'

    thirty_five_grad_alex 'Мику. Не мне это говорить, но всё хорошо. Тебя больше никто обижать не будет. Я клянусь тебе в этом.'
    thirty_five_grad_alex 'Мне без разницы, какой ты нации и какого рода. Для меня ты тоже прекрасный человек, который достоин всего лучшего.'
    thirty_five_grad_alex 'Ха! Я не люблю громкие слова, но сейчас без них никуда.'
    show 35grad_miku 3 smile pio ponytails with dissolve_fast
    'Она смотрела на меня с большим... любопытством и с искренней радостью! Такой взгляд невозможно подделать, даже имея актёрский талант.'
    'Её глаза говорили всё и много в данный момент. Она была счастлива.'

    thirty_five_grad_mi 'Я... Лёша. Спасибо. Благодарю, что ты сводил меня сюда за наш разговор. Что открылись друг другу. Я очень это ценю. А теперь...'

    thirty_five_grad_alex 'Мне проводить тебя?'
    show 35grad_miku 2 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Нет. Прости меня, прошу! Но мне нужно побыть одной. Хорошо?'

    thirty_five_grad_alex 'Да, конечно. Как скажешь, Мику. Если что, ты знаешь, я рядом.'

    thirty_five_grad_mi 'Агась. Но я не понимаю, почему? Почему ты так добр ко мне?'

    'Хороший вопрос, дамочка. Я и сам его себе задаю.'

    thirty_five_grad_alex 'Не знаю. Просто считаю, что так нужно. Вот и всё...'
    show 35grad_miku 1 sad pio ponytails with dissolve_fast
    'Она резко погрустнела...'

    thirty_five_grad_mi 'А... Ты хочешь что-то попросить в будущем?'

    thirty_five_grad_alex 'Нет. О чём ты вообще?'

    thirty_five_grad_mi 'Ну ты же сам так сказал...'

    thirty_five_grad_alex 'Я про то, что стараюсь не совершать необдуманные поступки. Так и живу.'
    show 35grad_miku 3 smile pio ponytails with dissolve_fast
    'Её нежные на вид губы улыбнулись, отчего стало немного теплее на сердце.'

    # (музыка стоп)
    stop music fadeout 3.0
    thirty_five_grad_mi 'Хорошо! Я запомню это! До встречи, Лёша!'

    thirty_five_grad_alex 'Ещё увидимся.'
    hide 35grad_miku 3 smile pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_boathouse_day at thirty_five_grad_deblur
    'На душе осталось приятное нечто. Оно как газ, обволакивает изнутри и обтекает, защищая от плохого. Эх, Мику. Девушка-секрет. Девушка-загадка.'

    # (музыка) Between August And December - Glimmering Coals
    # (появляется спрайт Виолы в купальнике)
    play music music_list['glimmering_coals'] fadein 3
    show 35grad_viola 2 normal bikini glasses
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_boathouse_day at thirty_five_grad_blur
    thirty_five_grad_cs 'Да она уж точно та ещё загадка.'

    'Сладко протянула... Виола?!'

    thirty_five_grad_alex 'ЧЕГО?!'

    'Женщина в купальнике с горячими во всех смыслах узорами на белье стояла возле меня и смотрела сверху вниз, как будто на своего сабмиссива. Мне резко поплохело...'
    show 35grad_viola 2 angry bikini glasses with dissolve
    thirty_five_grad_cs 'Не кричи так, пионер. Привлечёшь ненужное внимание.'

    thirty_five_grad_alex 'Я-я что последнее про неё вслух сказал?!'
    show 35grad_viola 2 normal bikini glasses with dspr
    thirty_five_grad_cs 'Да, есть такое. Это нормально. В твоём-то возрасте. И почему ты это смотришь на меня таким взглядом?'

    thirty_five_grad_alex 'А?'

    thirty_five_grad_cs 'Похоже, солнце и на тебя плохо влияет. Ладно, забей. Будешь купаться или как?'

    thirty_five_grad_alex 'Да у меня это, работа есть...'
    show 35grad_viola 2 normal bikini with dspr
    thirty_five_grad_cs 'Я в курсе, что ты Лене помочь должен. Но знаешь... Я была бы не прочь искупаться вдвоём.'

    'Она обошла меня по часовой стрелке, словно суккуб. И что мне прикажете делать?'

    thirty_five_grad_alex 'И-именно мне нужно ей помочь. Коробки тяжёлые, все дела...'

    'Она была чуть выше меня. Не как мы с Мику, где я был её выше на целую голову... Но всё же метр девяносто спокойно ей дашь.'
    'Её грудь так сладко летала возле моего лица, что мне кажется, будто сейчас так и упаду на землю... То есть на песок.'

    thirty_five_grad_cs 'Елена ещё десять минут подождёт. Ей физический труд только на пользу. Ведь сидит целыми днями за своими книжками и даже... сверстников не видит.'

    'То, что она совершает сейчас, в моём времени называется как «харасмент», если не ошибаюсь. Но тут не сказать, что я был так уж и против этого...'

    thirty_five_grad_alex 'Вы правы, но... А если нас застукают?'
    show 35grad_viola 2 normal bikini glasses with dissolve
    thirty_five_grad_cs 'И что? Мы же не делаем ничего такого. Подумаешь, двое взрослых людей купаются.'

    '...Взрослых? Неужели она... Да быть того не может. Нет! Не правда!'

    thirty_five_grad_alex 'Виола, я понимаю, что вы дама красивая и обворожительная, но я уже дал обещание одной девушке, так что...'

    thirty_five_grad_cs 'Я в курсе. Ну и что? Вы же не встречаетесь?'

    thirty_five_grad_alex '...Нет.'

    'Затем она, подобно гадюке, посмотрела мне прямо в глаза.'
    show 35grad_viola 2 angry bikini glasses with dspr
    thirty_five_grad_cs 'Так что чего тебе стесняться, мой юный во всех отношениях друг?'

    'Но, вожатая возьми! Я бы солгал, если сказал, что её глаза мне не нравятся.'
    '...А фары уж тем более... Это... они натуральные же, да?'

    thirty_five_grad_alex 'В плане?'
    show 35grad_viola 2 normal bikini glasses with dspr
    thirty_five_grad_cs 'Парня, не видавшего всю свою жизнь девушек, умудрённой женщине видно как минимум за километр. И что подтверждает мои слова...'
    thirty_five_grad_cs 'Ты же сейчас не на мои глаза смотришь, верно?'

    'Я хочу сейчас же закопаться в песок с головой, как делает та самая птица, чтобы спрятать все следы стыда и чтобы поскорее это всё закончилось...'

    thirty_five_grad_alex 'П-простите...'

    'И снова румянец. И снова прикусила нижнюю губу. Да что с ней не так?! Почему я себя чувствую каким-то... грязным?'
    'И что ещё более странно, так это то, что и мне самому это не так уж и противно. Господи, что со мной не так?!'

    thirty_five_grad_cs 'Искала золото, а нашла алмаз. Ладно, не хочешь купаться, значит, можешь настоять на своём. Мне это нравится. Так уж и быть, иди до Елены и помоги ей.'

    thirty_five_grad_alex 'Что? Вы так просто меня отпускаете?'

    show 35grad_viola 2 shy bikini glasses with dspr
    thirty_five_grad_cs 'А я похожа на рабовладелицу? Ты мне и не был подчинённым. А всё то, что сейчас произошло...'

    # (музыка стоп)
    stop music fadeout 3
    'Развратница приторно простонала. Негромко. Но мне и этого хватило. Нужно будет снова душ принимать...'

    thirty_five_grad_cs 'И, пока ты не ушёл, скажу. Приходи в мой кабинет как-нибудь. Я не против твоей компании. Даже при входе стучаться не обязательно.'

    thirty_five_grad_alex 'Ладно... До свидания...'

    'Всё, что мог выдавить из себя я.'

    thirty_five_grad_cs 'До встречи... пионер.'
    hide 35grad_viola 2 shy bikini glasses with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_boathouse_day at thirty_five_grad_deblur
    'Она аккуратно обогнула меня, и след её духов остался со мной. Сладкий, нежный. И что ещё удивительнее, она ни разу за всё это действие не прикоснулась к моему телу.'
    'Так, пора мне валить отсюда. Пускай купается сама по себе.'
    'Мне совсем не интересны ни её прекрасное, словно на подбор, тело, ни её до безумия красивые глаза разных цветов, ни даже её чудесный взрослый тембр.'
    'Вообще не интересует...'

    # (затемнение (раньше это было обычное моргание))
    # (фон медпункта снаружи)
    scene bg ext_aidpost_day with fade
    'Я и сам не заметил, как дошёл до медпункта, возле которого было пару десятков коробок. Они на вид и не были большими.'
    'Тогда почему Лена с ними не справляется? Попытался приподнять одну из них...'

    '...Ядрёна вошь! Они туда что положили совесть Виолы? Какого хера она такая тяжёлая-то?! Ладно, Лене действительно нужна будет моя помощь.'
    'Хотя мне к ней даже идти больше не надо, так как она и сама вышла ко мне. Вид её был удивлённый:'

    # (музыка) Sergey Eybog - Let's Be Friends (Lena Theme)
    # (появляется спрайт Лены)
    play music music_list['lets_be_friends'] fadein 3
    show 35grad_lena 1 shy pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_aidpost_day at thirty_five_grad_blur
    thirty_five_grad_ul 'О, Лёша, рада видеть тебя. А ты что тут делаешь? Случилось что-то? Поранился?'

    'Такого потока слов я ждал от Мику, но никак не от неё. Забавно.'

    thirty_five_grad_alex 'Что удивительно – нет. Я пришёл к тебе на помощь, если ты не против.'

    'На что она радостно мне закивала.'
    show 35grad_lena 1 laugh pio with dspr
    thirty_five_grad_ul 'Конечно! Они ж тяжёлые, как не знаю что! Прости, конечно, что я, может быть, заставляю тебя работать. Мне правда неловко.'

    thirty_five_grad_alex 'Ты вовсе не заставляешь. Тем более, что мне и самому разминка не помешает. Просто скажи, куда перенести надо.'

    'Она была счастлива. Не как Мику, конечно, когда я ей пообещал о важной вещи в мире, но всё же. Лена это показывала искренне, и даже как будто черепок на её груди мне улыбнулся. Жутко.'
    show 35grad_lena 1 smile pio with dspr
    thirty_five_grad_ul 'Нужно будет просто в сам медпункт отнести, а разбирать уже сама буду. И Лёш, а ты Виолу саму не видел? Она просто ушла, а куда – не сказала.'

    thirty_five_grad_alex 'Виола... по делам ушла. Сказала, что скоро придёт.'

    'Походу, в этом лагере я стану тем ещё вруном. Но куда деваться? Не правду же говорить? Хотя мне, по сути, какое дело. Это их разборки, не мои.'
    'Но ведь это я стану тем самым катализатором проблем... Ай, пофиг.'
    show 35grad_lena 1 crabbed pio with dissolve_fast
    thirty_five_grad_ul 'Ладно. Снова придётся одной всё делать...'

    'Я взял одну из тридцати коробок. И куда их столько, этому маленькому лагерю?!'

    thirty_five_grad_alex 'А что... она часто тебя покидает?'

    'Поднял одну из коробок и понёс по лестнице.'
    show 35grad_lena 1 normal pio with dissolve_fast
    thirty_five_grad_ul 'Бывает временами, но не так уж и долго, как сейчас.'

    'Теперь уже Лена спустилась с лестницы, чтобы взять одну из коробок.'

    # (затемнение (раньше это было обычное моргание))
    show black at thirty_five_grad_vhs with dissolve
    
    'Прошло уже некоторое время. Руки ноют, но в тишине работать ещё хуже.'
    scene bg ext_aidpost_day with dissolve
    thirty_five_grad_alex 'Лен, можно тебя спросить?'
    show 35grad_lena 1 normal pio with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_aidpost_day at thirty_five_grad_blur

    thirty_five_grad_ul 'Да, конечно.'

    thirty_five_grad_alex 'Расскажи о себе. Чтоб в молчании не работать.'
    show 35grad_lena 1 laugh pio with dspr
    'Она тихо рассмеялась.'

    thirty_five_grad_ul 'Даже не знаю. Живу в местном райцентре, точнее на окраине. Хорошо учусь. После лагеря хочу поступать в медицинский, а именно на хирургию.'

    thirty_five_grad_alex 'Любишь резать людей?'
    show 35grad_lena 1 crabbed pio with dspr
    thirty_five_grad_ul 'Только тех, кто задаёт слишком много вопросов.'
    show 35grad_lena 1 laugh pio with dspr
    'Смех был довольно громким, но мне было от этого хорошо. Оказывается, Лена тоже не лишена чего-то человеческого. С её внешним видом уж точно.'

    thirty_five_grad_alex 'Ну уж извини. Ещё два вопросика. Это эдакая цена за помощь.'
    show 35grad_lena 2 normal pio
    thirty_five_grad_ul 'Уговорил. А-то правда. Прости. Я бы сама всё, но старшие настояли.'

    thirty_five_grad_alex 'Понимаю. Так что ты можешь мне рассказать о... Мику?'

    'Она остановилась. Как и я.'
    show 35grad_lena 1 smile pio with dspr
    thirty_five_grad_ul 'О. Многое. Во-первых, она моя соседка по домику. Во-вторых, она много говорила о тебе вчера вечером. И, в-третьих, она никогда не злится.'
    show 35grad_lena 1 laugh pio with dspr
    thirty_five_grad_ul 'Всегда такой весь одуванчик!'

    # (музыка стоп)
    stop music fadeout 3    
    thirty_five_grad_alex '...А что она говорила обо мне?'
    show 35grad_lena 1 normal pio with dspr
    thirty_five_grad_ul 'Самые базовые вещи, которые я пропустила мимо ушей. Вроде что, какой ты хороший и добрый, все дела. Уж прости, но мы с ней не особо подруги.'

    'Она мне не очень нравится, хотя меня считает другом. Странно, не правда ли?'

    thirty_five_grad_alex 'А почему бы тебе и правда с ней не дружить? Она очень хорошая.'
    show 35grad_lena 1 crabbed pio with dissolve_fast
    thirty_five_grad_ul 'Говоришь в точности как Мику. И мне не хочется говорить об этом.'

    thirty_five_grad_alex 'Ладно, забей. А что ты скажешь о Виоле?'
    show 35grad_lena 1 normal pio with dspr
    thirty_five_grad_ul 'Она моя начальница и друг. Больше тебе ничего не скажу.'

    thirty_five_grad_alex 'Вот как. А почему?'
    show 35grad_lena 1 crabbed pio with dspr
    thirty_five_grad_ul 'Потому что не хочу. Вопросы?'

    thirty_five_grad_alex 'Больше нет.'
    show 35grad_lena 1 smile pio with dspr
    thirty_five_grad_ul 'Замечательно.'
    show 35grad_lena 1 normal pio with dspr
    'Хреново. Вот и поговорили, называется. В принципе, разговор был даже бесполезным. Ибо нового для себя ничего не открыл.'
    'Сзади раздаётся шум спокойных шагов. Кто же это идёт? Точно не Виола, она на каблуках.'

    # (музыка) Between August And December - Heather
    # (появляется спрайт Алисы)
    play music music_list['heather'] fadein 3
    show 35grad_alice 1 normal reb with dissolve:
        xalign 0.2 
    show 35grad_lena 1 normal pio with move:
        xalign 0.8 
    thirty_five_grad_dv 'Привет всем работягам, и отдельно тебе.'

    thirty_five_grad_alex 'Ого, а чего это я такой чести удостоился?'
    show 35grad_alice 1 normal joy reb with dspr
    thirty_five_grad_dv 'А почему бы и нет? Я слышала, что ты будешь обязан мне в кое-чём помочь. Вот и располагаю тебя к себе. Кстати, пришла я не просто так. {w} Ле-на!'
    show 35grad_lena 1 crabbed pio with dissolve_fast
    thirty_five_grad_ul 'Чего ты кричишь? Здесь же я стою!'
    show 35grad_alice 2 normal reb with dissolve_fast
    thirty_five_grad_dv 'Дай мне зелёнки и спиртяги. Второе не обязательно, но было бы не плохо.'

    thirty_five_grad_ul 'Сейчас принесу.'

    # (Лена пропадает)
    hide 35grad_lena 1 crabbed pio with dissolve_fast
    thirty_five_grad_alex 'А что случилось?'
    show 35grad_alice 2 sad with dspr
    thirty_five_grad_dv 'Да ничего такого. Пару пальцев поранила. А ты что делаешь? Почему не со мной на спортплощадке?'

    'И только сейчас, когда взглянул в её яркие глаза, заметил. Что-то было в них не так. Что-то неправильное, словно потухшее. Как старая лампочка.'

    thirty_five_grad_alex 'Алис, с тобой точно всё хорошо?'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'А что, не похоже?'

    thirty_five_grad_alex 'Да чёрт тебя знает. В обморок недавно не падала?'
    show 35grad_alice 2 ready_to_smash_faces with dspr
    thirty_five_grad_dv 'Других тем для разговора у тебя нет?'

    thirty_five_grad_alex 'Ну, когда ты рядом, я лучше промолчу, чтобы не буркнуть что-нибудь опасное. А то ты дама боевая, как та валькирия.'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'Скажешь ещё что-то такое – язык вырву.'

    thirty_five_grad_alex 'Только перед этим я тебе сначала глаза выдавлю.'

    'В эту омерзительную игру могут играть двое. Не знаю, что она задумала про себя там, но у меня нет теперь особого желания помогать ей.'

    # (появляется Лена недовольная)]
    show 35grad_lena 1 crabbed pio with dspr
    thirty_five_grad_ul 'Что у вас тут происходит? Что за резню вы хотите совершить?'

    'Лене явно не нравилось то, что мы тут обсуждали. Оно и понятно почему.'
    'В руках она несла баночку зелёнки, по виду новая, из коробки, и кусок ваты, намотанный то ли на спичку, то ли на палочку.'
    show 35grad_alice 2 laugh reb with dissolve_fast
    thirty_five_grad_dv 'Да мы просто играемся, Лен. Или он и тебя заразил? Тоже в зануду превращаешься.'
    show 35grad_lena 2 normal pio with dspr
    thirty_five_grad_ul 'Алиса, с тобой точно всё хорошо? А то с утра ты такой не была.'

    'Лена старалась говорить заботливо, но даже она почуяла какой-то подвох в ней.'

    thirty_five_grad_dv 'Всё просто замечательно! Ладно, возможно это и я палку перегнула. Забейте. Спасибо, Лена. До встречи всем.'

    # (Алиса пропадает)
    hide 35grad_alice 2 laugh reb with dissolve_fast
    thirty_five_grad_ul 'Пока...'

    'Ответила Елена, а я промолчал. Всё равно же ещё встретимся. Хотя надеюсь, что нет.'
    'А тем временем на земле осталось ещё коробок пять. Времени много это не займёт. Надеюсь.'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон медпункта внутри + спрайт Лены)
    scene bg int_aidpost_day with fade
    show 35grad_lena 1 normal pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_aidpost_day at thirty_five_grad_blur
    'И правда, не заняло. Я сижу на мягкой кушетке, попивая уже успевший остыть чай. Вкусный такой, ароматный и мягкий, но на языке оставляет след, похожий на плёнку.'
    show 35grad_lena 1 smile pio with dspr
    thirty_five_grad_ul 'Спасибо тебе ещё раз за помощь, Алексей. Мне очень приятно, что ты помог мне первой.'

    'Вообще-то нет. Но какая кому разница, верно?'

    thirty_five_grad_alex 'А есть различия, кому я должен помогать?'
    show 35grad_lena 1 normal pio with dissolve_fast
    thirty_five_grad_ul 'Не, просто... забей. Сказала, не подумав. Как Алиса сегодня.'
    show 35grad_lena 1 laugh pio with dspr
    'И снова рассмеялись. Хотя и было не над чем.'
    show 35grad_lena 1 normal pio with dissolve_fast
    thirty_five_grad_ul 'Лёш, внезапный вопрос. А кто ты? В плане, какая у тебя мечта?'

    '...Выбраться отсюда. Хм...'

    thirty_five_grad_alex 'Даже не знаю. Особо не задумывался. Наверно, обрести покой, умиротворение. Знать, что тебе незачем переживать о завтрашнем дне.'

    thirty_five_grad_ul 'Звучит романтично, хотя это и не мечта особо.'

    thirty_five_grad_alex 'А. Тогда что?'
    show 35grad_lena 1 shy pio with dspr
    thirty_five_grad_ul 'Желание. Это то, чего тебе сейчас как раз-таки не хватает. Беспокоит что-то?'

    thirty_five_grad_alex 'Можно и так сказать.'
    show 35grad_lena 2 smile pio with dspr
    thirty_five_grad_ul 'А что, если не секрет? Я постараюсь помочь.'

    'Сидел и думал. Думал и сидел. Говорить ли ей. Тогда начнутся новые расспросы и тому подобное, которые мне сейчас не нужны вовсе.'

    thirty_five_grad_alex 'Прости, не могу. Не хочу сейчас нам обоим мозги нагружать. Спасибо за чай, он был вкусным.'
    show 35grad_lena 1 sad pio with dissolve_fast
    'На её личике застыла грустная ухмылка. Это из-за того, что я не хотел с ней делиться о моей проблеме?'

    thirty_five_grad_ul 'И тебе спасибо. За помощь. Если что, приходи. Двери всегда открыты гостям.'

    # (фон медпункта снаружи)
    scene bg ext_aidpost_day with fade
    'Я кивнул и вышел. На улице уже стоял зной, и было трудно дышать. Сейчас идти помогать Алисе смысла нет.'
    'Она, скорее всего, сама отдыхает где-нибудь, а вот Славяна одна. Наверное. И почему я вообще забочусь о них так, как будто они для меня родные?'

    'Хотя чего я теряю, проявляя заботу? Наоборот, даже получаю больше и лучше.'
    'Что-то вроде друзей, которые потом мне также помогут в будущем. По крайне мере, я надеюсь на это.'

    'Мой путь сейчас лежит на пляж. А почему бы и нет? Вдруг, пока никого нет, получится искупаться. Отдохну по-человечески!'
    'В конце концов-то, люди за такой отдых сотни тысяч рублей отдают, а я бесплатно! Но, как и всегда, с одним малюсеньким условием...'

    # (затемнение (раньше это было обычное моргание))
    # (музыка) Sergey Eybog - Feeling Good
    # (фон пляжа)
    play music thirty_five_grad_feeling_good fadein 3
    scene bg ext_beach_day with fade
    'Когда я подошёл к пляжу, то меня накрыло одно большое разочарование, словно одеялом. Место было полным-полно детей с их вожатыми.'
    'Они все веселились, и им явно было хорошо. Не могу их за это винить, ведь вёл бы себя точно так же. Да и дети это. Не хочется забирать у них кусочек радости.'

    'Зато словно сама Судьба сделала мне небольшой презент в виде Слави, которая в белом купальнике выглядела просто сногсшибательно!'
    'Он хорошо сидел на ней, вычерчивая каждую чёрточку груди и фигурки. Сама она хоть и стояла на фронтовой стороне, но не видела меня.'
    'Но что она здесь делает? Надеюсь, она не будет против, если я подойду к ней.'

    # (спрайт Слави в купальнике)
    show 35grad_slavya 2 normal bikini with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_beach_day at thirty_five_grad_blur
    thirty_five_grad_alex 'Здрав будь!'
    show 35grad_slavya 2 laugh bikini with dspr
    thirty_five_grad_sl 'О. Лёша! Рада видеть! Неужели ты искупаться пришёл? Но не получится, прости. Приходи вечером!'

    thirty_five_grad_alex 'Вообще-то, я ради тебя пришёл.'
    show 35grad_slavya 2 shy bikini with dspr
    '...И только сейчас понял, что я ляпнул. М-да.'
    'Язык у меня точно резиновый. Девушка сильно покраснела (из-за жары, видимо, точно), но смотрела своими голубыми глазами чуть ли мне не в душу.'
    'Не сказать, что это было неприятно.'
    show 35grad_slavya 2 smile bikini with dspr
    thirty_five_grad_sl 'Ой, ну ты скажешь тоже. Но стоит признать, комплименты ты делать умеешь. А если серьёзно, просто так пришёл?'

    thirty_five_grad_alex 'Я и не шутил. Мне Ольга... Дмитриевна задание дала, чтобы я кое-кому помог. Но я и не против.'
    show 35grad_slavya 2 laugh bikini with dspr
    thirty_five_grad_sl 'Молодец! Но мне помощь не особо-то нужна. Разве что от скукоты! Ведь... ты не против, если присядем?'
    # (Возможно стоит нарисовать цг)
    show 35grad_slavya 2 normal bikini with dspr
    'Мы сели на небольшую деревянную лавку, которая стояла в самой густой тени. Ноги меня тут же отблагодарили, и лёгкость растеклась по мышцам.'
    show 35grad_slavya 2 smile bikini with dspr
    thirty_five_grad_sl 'Я хоть и люблю работу, но тут та-а-ак скучно. И знаешь? Я даже этому рада.'

    thirty_five_grad_alex 'Почему? В чём вообще заключается твоя обязанность?'

    thirty_five_grad_sl 'Следить за безопасностью, чтобы никто не утонул. Смотри, на будущее. По утрам всегда ходят дети. А мы как старшие, по вечерам.'
    thirty_five_grad_sl 'Так что если хочешь искупаться, то добро пожаловать. В часиков семь вечера.'

    thirty_five_grad_alex 'Спасибо, я запомню.'
    show 35grad_slavya 2 normal bikini with dspr
    'Но она отмахнулась.'

    thirty_five_grad_sl 'Не стоит, Лёш.'

    'Прошло некоторое количество времени, как мы сидели и смотрели за происходящим.'
    'Как в реке купались дети, веселились, кто-то на берегу играл в мяч, а вожатые и вовсе перекидывались в картишки. Лепота!'
    
    thirty_five_grad_alex 'Славя, а у тебя... молодой человек есть? В плане более близкий друг. Ну, ты понимаешь.'
    show 35grad_slavya 2 smile bikini with dspr
    'Сам не понимаю, почему задал именно такой вопрос. Но, скорее всего, чтобы узнать её реакцию.'
    'Но она среагировала совершенно нормально, даже не смущаясь.'
    
    thirty_five_grad_sl 'Да как-то даже и не планировала этого. Учёба, работа по дому, помощь семье. Жизнь идёт своим чередом, поэтому и времени на любовь нет.'
    thirty_five_grad_sl 'А почему ты так спросил?'
    thirty_five_grad_alex 'Покажи писю'

    thirty_five_grad_alex 'Жаль это слышать, Славя. Хотя я тоже такой же. Абсолютно. Дом, учёба, работа и семья.'
    thirty_five_grad_alex 'Но иногда всё же нужно что-то менять в жизни, не так ли? Да и спросил чисто из интереса. Извини, если задел как-то.'
    show 35grad_slavya 2 laugh bikini with dspr
    thirty_five_grad_sl 'Всё хорошо. Иногда приятно вот так открыться, чем в себе держать.'

    'И, подобно пуле, в голову влетела ещё одна «офигенная» мысль.'

    thirty_five_grad_alex 'Славя. А как ты смотришь на то, чтобы вместе со мной пойти сегодня вечером на пляж искупаться?'

    'На это девочка тоже отреагировала совершенно спокойно.'

    # (Славя улыбается)
    show 35grad_slavya 2 smile bikini with dspr
    thirty_five_grad_sl 'Без проблем! Я даже рада, что ты меня пригласил. Ой, я имела в виду, что не против сходить развеяться. Отдых ещё никому не мешал.'

    thirty_five_grad_alex 'Тогда встречаемся тут же? На этом месте?'

    thirty_five_grad_sl 'Ага. Давай в... семь? Как раз все дела переделаю.'

    thirty_five_grad_alex 'Отлично, я тоже. Договорились.'

    'Мы пожали друг другу руки. Она у неё мягкая, но в то же время немного шершавая и сильная. Чувствовалось её усердие и уверенность.'
    show 35grad_slavya 3 shy bikini with dissolve
    thirty_five_grad_sl 'А ещё знаешь...'

    # (музыка) Between August And December - Pile
    play music music_list['pile'] fadein 3
    show 35grad_slavya 3 fear bikini with dspr
    '...Внезапный крик на воде прервал Славяну, отчего мы оба посмотрели в ту сторону, откуда, собственно, голос и раздался.'
    # (спрайт Слави пропадает)
    hide 35grad_slavya 3 fear bikini with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_beach_day at thirty_five_grad_deblur
    'Только рядом со мной Слави уже не было.'

    thirty_five_grad_sl 'Освободите дорогу!'

    'Кричала она, и все её слушались. Мне было плохо видно, что там происходит, но я не стал стоять в стороне и тоже побежал за девушкой.'
    'Кто-то тонул, и он находился довольно далеко от берега, практически рядом с теми красными буйками!'
    'В это же время, Славя уже была на середине реки. Быстро, однако!'

    thirty_five_grad_vz_unk 'Что... Что там происходит?!'

    'Ошарашенно спросил вожатый мужчина. Я пригляделся. И испугался.'

    'Славяна не могла вытащить бедолагу оттуда, так как сама уже боролась за жизнь. Мои руки снимают рубашку и бросают куда-то на песок.'
    'Я не отдаю себе отчёта, что делает моё тело, но вот уже и сам бросаюсь в воду. Тёплая вода обволакивает меня всего и словно даёт энергию.'
    'Я стараюсь плыть всё быстрее и быстрее, но мышцы уже отдаются колючей болью. А я всё плыву и плыву.'
    'В поле зрения показываются два человека уже на таком расстоянии, что можно протянуть руку и забрать их. Что и делаю! Славю хватаю за руку и поднимаю наверх.'
    'Она дышит, она жива. А парниша поднимается сам. Тоже живой, но в глазах страх.'

    'Затем я чувствую небывалую лёгкость в теле, расслабление и с тем же вязкость, как в киселе.'
    'Я моргаю, но после этого не открываю глаза, так как что-то чёрное, как смоль, топит меня с головой.'

    # (затемнение (раньше это было обычное моргание))
    show black at thirty_five_grad_vhs with fade
    # (музыка стоп)
    'Темнота. Приятная, прохладная, спасительная чернота, которая, тем не менее, не продлилась долго. Вдали раздавались чьи-то растерянные голоса.'
    'Они были грустными и даже немного злыми. Не знаю, сколько я так пролежал, но сознание всё же возвращалось ко мне, а с ним солнце. С жаром. Жаром в груди.'
    'Воздух сотрясся моим кашлем. А затем кто-то подбегает прямо ко мне и тянет, тянет вдаль...'
    scene bg ext_beach_day with flash
    show 35grad_slavya 2 angry bikini with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_beach_day at thirty_five_grad_blur
    thirty_five_grad_sl 'Эй, вы двое! Хватит стоять столбом! Помогите же! Ну!'

    'Женский сильный голос заполнил всю голову, но слышал я его кристально ярко и чисто, отчего сразу стало ясно, кому он принадлежал.'

    # (музыка) Sergey Eybog - Confession
    play music music_list['confession_oboe'] fadein 3
    thirty_five_grad_alex '...Славя... {w} Пусти, я сам могу идти.'

    'Не солгал. Она сначала сопротивлялась, но всё же я хоть и легонько, но смог вырваться и встать на собственные ноги.'
    'Ощущать землю своими стопами намного приятнее, скажу так.'
    'Но у всего есть своя цена. Лёгкие и нос горели так, словно подожгли изнутри, а в голове стоял дикий белый шум.'

    # (спрайт Слави грустный в купальнике)
    show 35grad_slavya 2 sad bikini with dspr
    thirty_five_grad_sl 'Лёша... {w} Как ты?'

    'Заботливо спросила эта чудная блондинка. Интересно, а она ко всем такая заботливая? Или только мне так повезло?'

    thirty_five_grad_alex 'Да нормально я, нормально. Просто не каждый день тонешь в воде.'

    thirty_five_grad_sl 'Давай сходим в медпункт, а? А то мало ли...'

    'И только сейчас стал замечать, насколько много здесь людей! Притом все смотрят на нас так, как будто среди них стоит второй Мессия.'
    'Мне это категорически не нравится, так как не хочу привлекать к себе лишнего внимания. Это того не стоит.'

    thirty_five_grad_alex 'Нет, Славя! А вот тебе нужно. Мне нужно идти.'
    show 35grad_slavya 2 shy bikini with dspr
    'Но Славяна лишь схватила меня за локоть и, поняв то, что сделала, покраснев, сразу же отпустила.'
    show 35grad_slavya 2 sad bikini with dspr
    thirty_five_grad_sl 'Почему? Лучше, думаю, сходить нам обоим.'

    'А затем она берёт из рук какой-то девчонки мою рубашку, которая вся тем временем в ярко-жёлтом песке.'
    'Потом против ветра вытряхивает её и передаёт мне.'
    show 35grad_slavya 2 normal bikini with dspr
    thirty_five_grad_sl 'Вот, держи. Её лучше постирать, конечно, но...'

    thirty_five_grad_alex 'А это нормально? Что мы стоим тут и разговариваем так, как будто ничего не произошло?'

    'Мы с ней оглядываемся и узнаём, что все уже занимаются своими делами.'
    'Да, конечно, обстановка стала менее радостной, и кто-то даже вообще уже собирается уходить, но всё же.'
    show 35grad_slavya 2 smile bikini with dspr
    thirty_five_grad_sl 'Алёш, ещё раз спасибо тебе. Ты спас двум людям жизни. Ой, прости, ты же просил...'

    thirty_five_grad_alex 'Забудь, ничего страшного. Да и сказал же, что сделал то, что должен. Меня не было бы, сделал кто-то другой.'
    show 35grad_slavya 2 laugh bikini with dspr
    'Но она лишь усмехнулась.'

    thirty_five_grad_sl 'М-да уж. Кому-то явно стоит поработать с самооценкой. Но ничего, отряд должен знать героя дня. А вообще, подождёшь меня? Я быстро переоденусь.'
    show 35grad_slavya 2 smile bikini with dissolve
    'Я кивнул. На самом деле мне не хотелось ждать её от слова совсем, так как нуждался совершенно в другом – в отдыхе и покое, желательно даже в коротком сне.'
    'Поэтому, подождав, пока Славя отойдёт в кабинку для переодеваний, я пошёл к своему (как странно), домику, молясь ангелу-хранителю о том, чтобы Ольги в нём не было...'

    # (музыка стоп)
    stop music fadeout 3
    # (фон домика вожатой снаружи)
    scene bg ext_house_of_mt_day with fade
    'Жизнь в лагере продолжалась так, как будто ничего и не было. И, наверное, оно и к лучшему. Мне не нужны были тонны благодарностей.'
    'Нет, безусловно, это было приятно. И возможно, что так я останусь у этой замечательной блондинки в сердечке. Но не за этим я здесь.'

    # (музыка) Sergey Eybog - Meet Me There
    play music music_list['meet_me_there'] fadein 3
    'В конце концов, я думаю, что я здесь не только ради романтики. Может быть, чтобы спасти кого-то или... Убить? Да не. Бред какой-то.'

    'Мысли так и роились, а возможно, что вовсе прожрали бы мой мозг, если не долгожданная лежанка!'
    'Она так гордо и красиво стояла, так манила меня к себе, как любовника! А я беру и не заставляю её долго ждать, ложусь прямо на неё.'
    'Для чего и была, собственно, создана.'

    'Мышцы сразу же «сказали» мне «спасибо».'
    'Приятная мягкость растеклась по моему телу, а тенёк из-за большого крона над моей головой придавал прохладу, хотя это и делал ветер, остужая до костей мокрую кожу.'

    'А затем в закрытых глазах выросла, словно гора, большая тень. Но кто это, чёрт бы вас драл?! Ольга? Нет, она бы сразу орала.'
    'Да и зачем долго гадать, открываю глаза.'

    # (спрайт Слави в форме)
    show 35grad_slavya 2 normal pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_blur
    thirty_five_grad_sl 'Лёша, я же просила тебя по-человечески подождать меня! Ладно, не волнуйся. Прощаю, так уж быть.'

    'Говорила девушка всё мягко и приятно. Отчего не знаю, как реагировать.'

    thirty_five_grad_alex 'Да, извини. Просто нужен отдых.'

    thirty_five_grad_sl 'Понимаю. Но вот со мной такое не получится. Нужно сначала Ольге Дмитриевне доложить о случившемся, а потом она мне новую работу назначит.'
    thirty_five_grad_sl 'Отдыхать только вечером буду.'

    thirty_five_grad_alex 'Так не докладывай прямо сейчас. Какая разница-то? Могу уступить. Шезлонг тебе нужнее, наверно.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Нет уж, спасибо. Не хочу ещё большего нагоняя получить. Ведь на нём может только она лежать.'

    thirty_five_grad_alex 'Как это ещё большего?'
    show 35grad_slavya 2 sad pio with dspr
    thirty_five_grad_sl 'За то, что чуть мальчишку не угробила, да ещё и себя. Да не вставай. Она на тебя кричать не будет. Правда, когда узнает...'

    thirty_five_grad_alex 'А может, вообще лучше не говорить? Меньше проблем будет как мне, так и тебе.'

    # (спрайт Слави серьёзная)
    show 35grad_slavya 2 hmuri pio with dspr
    thirty_five_grad_sl 'Лёш, прошу, хватит. Нужно принимать ответственность не только за себя, но и за других людей, которые тебя окружают. Всё будет хорошо, уверяю тебя.'

    thirty_five_grad_alex '...Ладно, так уж и быть, доверюсь.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Вот и славненько! А теперь... Она в домике?'

    thirty_five_grad_alex 'Да мне откуда знать? Я туда даже не заходил ещё.'
    play sound sfx_knock_door2
    'Девушка постучалась. Но в ответ ей была только глухая тишина.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Ну и ладно. Значит, она либо у Виолы Церновны, либо в административном корпусе. А теперь до скорого! Точнее, до обеда! И это... я горжусь тобой, правда.'

    thirty_five_grad_alex 'Спасибо, но думаю, тебе пора идти. Вдруг другие вожатые ей доложат первыми.'

    # (спрайт Слави удивлённой)
    show 35grad_slavya 3 surprised pio with dspr
    'И тут на её лице возникло такое удивление, будто она великое открытие совершила.'

    thirty_five_grad_sl 'Точно! Как я сразу-то не подумала!'

    # (спрайт Слави пропадает)
    hide 35grad_slavya 3 surprised pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_deblur
    '...И убежала прочь. Вроде и взрослая девушка, но... Хотя, чего ещё ожидать от человека, у которого номенклатура и политика на первом месте?'
    'Впрочем, эти мысли я отложил на долгий и глубокий ящик и попытался всё же поспать. Хоть бы немного...'
    play sound sfx_open_dooor_campus_1
    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    show black at thirty_five_grad_vhs with fade
    '...Во сне ощущал, словно меня за щеку аккуратно и медленно тягает краб. Это не было больно, а неприятно.'
    'Тягучесть надоедала мне, и я открыл глаза. В итоге это не оказалось сном...'

    # (музыка) Between August And December - Gentle Predator
    # (появляется арт с видом на грудь Алисы от первого лица)
    play music music_list['gentle_predator'] fadein 3
    # scene cg thirty_five_grad_alice_day_2 with flash
    scene cg day2_alice_animation 
    thirty_five_grad_dv 'Ути-пути, а кто это у нас проснулся? А кто это нарушает негласный закон о лежанке? Да и вообще, какого чёрта у тебя вся рубашка в песке?'

    'Рыжая чертовка наседала возле меня, закрывая собой солнце. И благодаря этому я вижу два высоких холмика, которые чуть ли тыкаются мне в лицо.'
    'Приятно, конечно, но от возможных последствий мне страшно.'

    thirty_five_grad_alex 'А тебе какое дело? Не трогай честного человека, женщина, и он тебя трогать за приличные места не будет. Если они у тебя ещё остались.'

    thirty_five_grad_dv 'Смотрю, смелости тебе не занимать. Это даже хорошо. Пытать тебя дольше придётся.'

    'Её янтарные глазища загорелись чуть ли не натуральным пламенем.'
    'Меньше всего мне сейчас хотелось испытывать сексуальное напряжение, поэтому нужно постараться отстраниться от неё.'

    thirty_five_grad_alex 'Слушай, давай прекращай со всем этим. Не до тебя сейчас. Мне Виолы с утра хватило.'

    'Теперь её пыл сменился на такой же серьёзный, как и мой. Я не понимаю её, и меня это напрягает.'

    thirty_five_grad_dv 'Да, хорошо, что ты про это сказал. Странная она, не так ли?'

    thirty_five_grad_alex 'Но и ты себя не совсем адекватно ведёшь.'

    thirty_five_grad_dv 'Не занудствуй. И кстати! Спасибо, что напомнил. Зачем ты Мику дал такое обещание?'

    'А вот это было очень внезапно! Я ощущаю себя рыбой, которую выкинули на берег. На всякий случай встал с шезлонга.'

    # (цг пропадает)
    scene bg ext_house_of_mt_day with dissolve
    # (Алиса обычная)
    show 35grad_alice 2 normal reb with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_blur
    thirty_five_grad_alex 'А тебе-то что? Я сделал то, что посчитал нужным. Девочке нужна была поддержка, и оказал её. Что тебе не нравится?'
    show 35grad_alice 2 sad reb with dspr
    thirty_five_grad_dv 'Тебе не следовало этого делать.'

    'Обиженно произнесла она. И что мне сейчас говорить?'

    thirty_five_grad_alex 'Алиса! Неужели ревнуешь?'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'Вот ещё! Не хватало мне этого. Не стыдно?'

    thirty_five_grad_alex 'За что?'

    thirty_five_grad_dv 'Взял и всё настроение мне испортил, козлина.'

    thirty_five_grad_alex 'Но ты первая на меня наезжать начала!'

    # (Алиса пропадает)
    hide 35grad_alice 2 angry reb with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_house_of_mt_day at thirty_five_grad_deblur
    'Девушка фыркнула и на прощанье залепила хорошего такого щелбана. Что с ней не так? Вчера же нормально себя вела! Относительно, конечно.'
    'Ладно, всё равно отдыхать мне вряд ли дадут. Схожу-ка я к Мику, время за музыкой скоротаю. Зато, быть может, Ольге на глаза не попадусь...'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон музклуба снаружи)
    # Фиксануть баг бг
    scene bg ext_musclub_day with fade
    $ renpy.pause(1.0) 
    scene bg thirty_five_grad_ext_musclub_verandah_day with dissolve
    'Стоило мне подойти к музыкальному зданию, как моё сердце ёкнуло. Ещё не знаю, что происходит там внутри, но явно ничего хорошего.'
    'Я медленно подхожу к двери и прикладываю к ней ухо. Благо, дверь не такая уж и толстая, как могла бы быть. Но всё равно не услышал весь их разговор:'

    # (музыка) antony genn, martin slattery - the italians are coming
    play music thirty_five_grad_The_Italians fadein 3
    thirty_five_grad_dv '...ку, думаешь, этот парень уже твой?'

    thirty_five_grad_mi 'А? О чём ты говоришь, Алиса?'

    thirty_five_grad_dv 'Не прикидывайся дурочкой. Я прекрасно слышала, о чём ты с ним на пляже говорила.'
    thirty_five_grad_dv 'Так ему глазки строила, словно настоящий ангелочек. Самой не стыдно, стерва?'

    thirty_five_grad_mi 'П-почему ты такое говоришь? Что я тебе сделала?'

    thirty_five_grad_dv 'Пытаешься его охомутать, что ж ещё. Я ведь тебя прошу по-хорошему: отстань от него, если глаза дороги.'

    'Тишина, но редкие всхлипы слышны с той стороны. Не знаю, что там происходит, но чувствую, что должен вмешаться.'

    thirty_five_grad_mi '...Клади уже свою гитару и уходи отсюда. Пожалуйста... Мне не нужны проблемы...'

    thirty_five_grad_dv 'И что?'

    thirty_five_grad_mi 'Как что?..'

    thirty_five_grad_dv 'Мику-Мику-Мику. Не стоит тебе заводить здесь врагов. Ты же и так одна, даже несмотря на то, что записались в клуб именно к тебе.'
    thirty_five_grad_dv 'Так что, вряд ли к тебе кто-то на помощь придёт.'

    thirty_five_grad_mi 'Хватит мне угрожать... И знай, ко мне придут! {w} Он обещал! {w} Я верю ему! В отличие от тебя и всех вокруг, он действительно добр ко мне!'

    thirty_five_grad_dv 'Говоришь так, как будто ты...'

    # (фон музклуба внутри. Спрайты злой Алисы и испуганной Мику)
    scene bg int_musclub_day with dissolve
    play sound sfx_open_door_strong
    show 35grad_alice 2 ready_to_smash_faces reb with Dissolve(0.1):
        xalign 0.8
    show 35grad_miku 2 fear pio ponytails with Dissolve(0.1):
        xalign 0.2
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_blur 
    'Всё, хватит. Иначе такое может и до драки дойти. Я открываю дверь не резко, но и не медленно, а так, чтобы они все обратили на меня внимание. Это сработало.'
    'Две девочки, чистые противоположности друг дружке, смотрели на меня. Одна с некой долей злости, а вторая с мольбой о том, чтобы это всё поскорее закончилось.'

    thirty_five_grad_alex 'Что у вас тут происходит? Алиса, ну какого лешего, а? У тебя шило в жопе застряло?'
    thirty_five_grad_alex 'Тебе сказали уходить, так выметайся отсюда! Чего непонятного?'

    'Стоило мне только войти в здание, как тут же накатила волна тревоги с головой. Бедная Мику! Долго же она тут была одна...'

    'Затем, когда задира отошла от своей жертвы, которая тем временем хоть и пыталась стоять крепко, но дрожала, как молодая берёзка, зачинщица на выходе обернулась и злобно пояснила:'
    show 35grad_alice 2 angry reb with dspr
    thirty_five_grad_dv 'Я-то уйду, но чтобы и ты тут долго не задерживался. Понял?'

    # (музыка стоп)
    # (пропадает спрайт Алисы)
    hide 35grad_alice 2 angry reb with dissolve
    show 35grad_miku 2 fear pio ponytails with move:
        xalign 0.5
    play ambience ambience_music_club_day fadein 2
    'Наступила тишина, которая прерывалась лишь тиканьем часов.'

    'Тик-так.'

    # (музыка) КАМАКА - Nerik Cinema
    play music thirty_five_grad_Nerik_Cinema fadein 3
    $ renpy.display_notify('Сейчас играет:\nКАМАКА - Nerik Cinema')
    'Девчачья нежная, красивая фигурка слегка дрожала, словно дул холодный северный ветер.'

    'Тик-так.'

    # (спрайт плачущей Мику)
    show 35grad_miku 2 cry pio ponytails with dspr
    'А затем полились её слёзы. Одна за другой. Она закрыла циановые глазки ладонями и отвернулась от меня.'

    'Тик-так.'

    'Я подошёл ближе и не придумал ничего лучшего, как слегка приобнять девушку за плечи.'
    'Поначалу она пыталась даже вырваться, но через пару лёгких мгновений она чуть ли не лежала у меня на руках...'

    thirty_five_grad_alex 'Тише. Всё хорошо, Мику. {w} Я рядом. {w} Не беспокойся.'

    'Я не знаю, что говорить в подобных ситуациях, поэтому делал то, что велит мне сердце. Я нежно поглаживал её по голове и шептал нежные слова.'
    'Удивительно, но это даже сработало, так как она стала потихоньку, но всё же успокаиваться. Слёзы прекращались, но личико опухло.'

    thirty_five_grad_mi 'Л-лёша... Т-ты спас меня... П-прости, что ты увидел всё это...'

    'От её пулемётной речи не осталось и следа, словно передо мной стоит совершенно другой человек. Да и всё равно я рад, что смог ей хоть как-то помочь.'

    thirty_five_grad_alex 'Это ты прости меня, Мику. Это из-за меня всё это произошло.'

    thirty_five_grad_mi 'Н-не говори так! Это всё эта рыжая! Ведь даже если бы не ты, то она нашла всё равно причину. Но ты не испугался, ты защитил меня... {w} Спасибо.'

    'Последнее слово она прошептала так нежно и приятно, что пошли приятные мурашки по спине. Давно такого не испытывал.'

    thirty_five_grad_alex 'Я же обещал. Я слово стараюсь держать.'

    # (спрайт Мику улыбающийся)
    show 35grad_miku 3 smile pio ponytails with dspr
    thirty_five_grad_mi 'Раз уж ты пришёл, давай я сыграю тебе на чём-нибудь? Или лучше давай будем учиться?'
    thirty_five_grad_mi 'Ой, прости, мне сначала умыться же нужно! Совсем голова кругом! Подожди минутку, хорошо? А заодно я и для чайника воду наберу!'

    '...Теперь снова узнаю прежнюю Мику! Задорную, весёлую, живую. Настоящий ангел во плоти. Если бы такие были...'

    # (спрайт Мику пропал)
    hide 35grad_miku 3 smile pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_deblur
    thirty_five_grad_alex 'Да, чай... Было бы неплохо. Ты ещё вчера обещала.'

    'Но она меня, скорее всего, уже не услышала, так как её тут уже не было.'

    # (стоп музыка)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    scene black at thirty_five_grad_vhs with dissolve
    'Сидеть на деревянном стуле не то чтобы удобно. Мику тем временем разливала кипяток в две фарфоровые кружки. На вид очень дорогие.'
    'По-своему навевает воспоминания о детстве, когда я проводил время у бабушки.'

    # (спрайт Мику обычный)
    scene bg int_musclub_day with fade
    show 35grad_miku 2 normal pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_blur
    # (музыка) Сергей Ейбог - муз. тема Мику (сорри, я забыл как называется)
    play music music_list['so_good_to_be_careless'] fadein 3
    thirty_five_grad_alex 'Ого! А откуда у тебя такие стаканы?'
    show 35grad_miku 2 laughter pio ponytails with dspr
    thirty_five_grad_mi 'Мне их дала ока-сан. Ведь она думает, что у меня тут есть друзья. Точнее, теперь-то есть.'
    thirty_five_grad_mi 'Так что и чай я теперь буду пить не в одиночку! Правда, прости, мне дать к нему нечего...'

    thirty_five_grad_alex 'Я могу вечером или после обеда кое-что принести. Надеюсь, тебе понравится.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'А? А что-что это?!'

    'По-детски воскликнул живой оркестр.'

    thirty_five_grad_alex 'Будет сюрпризом.'

    # (Мику улыбается)
    show 35grad_miku 3 dreamy pio ponytails with dissolve
    thirty_five_grad_mi 'Лёшка, ну ты и... Я... {w} Я так рада, что...'

    'Когда уходишь в свои мысли, обычно не слышишь, что говорит тебе собеседник.'

    thirty_five_grad_alex 'А? Что ты сказала?'
    show 35grad_miku 1 resentment pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Нет, ничего! Так, просто мысли вслух. Что-то в последнее время стала так делать.'

    thirty_five_grad_alex 'Нервничаешь, поди. Кстати, наверно, твоя мама очень тебе доверяет, раз даёт такие дорогие вещи.'

    'А затем до меня дошло, что я сказал. Самому стало крайне стыдно...'

    thirty_five_grad_alex 'Ой, прости!'
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Да ничего! Лёша ведь... Я с тобой согласна. Незачем детям... Ой! То есть таким, как мы, давать такие хрупкие вещи.'
    thirty_five_grad_mi 'Но я всё равно берегу их, как зеницу ока!'

    thirty_five_grad_alex 'Знаешь, Мику, ты такая хорошая и добрая.'
    show 35grad_miku 3 normal pio ponytails with dissolve_fast
    'На этот раз она не покраснела, а словно набралась уверенности. Я рад видеть её счастливой.'
    
    show 35grad_miku 1 serious pio ponytails with dissolve_fast

    thirty_five_grad_mi 'Лёшка, а можно вопрос?'
    # show 35grad_miku 1 normal pio ponytails with dissolve_fast
    'Тон её голоса сменился с милого на серьёзный. Я принял такой же вид, официально усевшись на стуле.'

    thirty_five_grad_alex 'Естественно, всегда можно.'
    show 35grad_miku 1 normal pio ponytails with dspr
    thirty_five_grad_mi 'Как мило! В общем, как раз поэтому и спрашиваю. Почему ты мне говоришь столько добрых и хороших слов?'

    thirty_five_grad_alex 'А почему я не могу?'
    show 35grad_miku 1 thoughtful pio ponytails with dspr
    thirty_five_grad_mi 'Просто... ты же видел Алису. Прости, что говорю так прямо, но... Я верю тебе, но не воспользуешься ли ты этим?'

    'Затем моё тело размякло. Всё напряжение как рукой сняло.'

    thirty_five_grad_alex 'Мику, какая же ты глупышка. Ты хоть и молодец, что такие вопросы задаёшь, но всё же тебе стоит знать, что...'
    thirty_five_grad_alex 'Ох, что-то я устал. Наверное, пойду. У меня... дела...'

    'Слова, которые вырвались изо рта сами по себе. Надеюсь, что она не воспримет их буквально.'
    'Но уходить я не собирался, а просто посмотреть, какую реакцию выдаст аквамариновая девочка.'
    show 35grad_miku 1 sad pio ponytails with dspr
    thirty_five_grad_mi 'Лёшенька, но почему? Ты же даже чая ещё не допил...'

    # (грустная Мику)
    # show 35grad_miku 1 sad pio ponytails with dspr
    'Её вид поменялся на грустный, но не такой, каким он был раньше. Словно ей сообщили известие, что отбирают что-то родное и дорогое.'
    'Мне теперь стыдно стало...'

    thirty_five_grad_alex 'Прости. Не знаю, что на меня нашло.'
    show 35grad_miku 1 smile pio ponytails with dspr 
    thirty_five_grad_mi 'Всё хорошо, с каждым бывает! Вот. Вспомни меня вчерашнюю! До сих пор стыдно. Но всё же я рада, что ты остался.'

    'Я потянулся к чаю, который к тому времени уже успел немного остыть, хотя по уровню горячести ему ещё далеко от этой красавицы, которая сидит рядом со мной.'
    'Она - единственная, к кому моё сердце теплит приятные и самые нежные чувства.'

    'Чай был ароматным и очень пряным на вкус, с травами, которые я раньше и не пробовал.'
    'Приятный запах впечатался в мой мозг, отчего тот пытался додумать, какие же это виды растений. А может, он просто так пытался отчего-то отвлечься.'

    # (Мику обычная)
    show 35grad_miku 2 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёш, как тебе чай? Нравится?'

    thirty_five_grad_alex 'Да, очень. А что это за травы? Впервые пью такой.'
    thirty_five_grad_mi 'Конечно впервые! Ведь они с моей родины! У меня ока-сан сама лично их собирала! А я помогала!'
    thirty_five_grad_mi 'Ты только представь! Этому запасу больше пяти лет! И они такие всё равно такие вкусные!'

    thirty_five_grad_alex 'Удивительно.'

    'А затем с великой гордостью продолжила перечислять все достоинства данного напитка, словно она пиар агент.'
    'Что сказать, у неё это вполне успешно получается. Я бы купил пару мешков, если б была такая возможность.'
    # звук звяканья посуды
    'Допив остатки, я аккуратно поставил поднос на блюдечко, которое при этом звонко, но тихо звякнуло.'
    show 35grad_miku 2 laughter pio ponytails with dspr
    thirty_five_grad_mi 'Эх, как же хорошо! Каждый день такое бы делала!'

    thirty_five_grad_alex 'А что мешает?'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Запасы, Лёшка! Они же у меня не вечные! Хотя хотелось бы... Вообще, обычного чая у меня много, так что не переживай, я не жадина!'
    thirty_five_grad_mi 'По крайней мере, по отношению к тебе!'

    'И хитро ткнула меня пальчиком в бок. Её циановый маникюр был превосходно уложен. Удивительная девушка, это уж точно.'

    thirty_five_grad_alex 'Теперь ответный вопрос: а чем я такое отношение к себе заслужил?'
    show 35grad_miku 3 normal pio ponytails with dspr
    thirty_five_grad_mi 'Всё просто! Ты член моего клуба!'

    'Хоть она и сама сказала это, но в её глазах читалось что-то совершенно иное. Будь я следователем или детективом, ну или было бы большого опыта с девушками, то понял бы. Эх.'

    'Дальнейшее времяпровождение прошло довольно весело. Мику сначала сыграла для меня пару лёгких, в плане разучивания, песенок.'
    'Да-да, те самые, которые в стиле «В траве сидел кузнечик».'

    thirty_five_grad_mi 'Лёш, запомнил? Это не так уж сложно! Тут есть три главных принципа, как и во всём: внимание, точность пальцев и усидчивость!'
    thirty_five_grad_mi 'Давай я для тебя ещё раз повторю, хорошо?'

    'Я кивнул. На самом деле и так всё относительно понял, хотя практики побаиваюсь. А просто попросил для того, чтобы она снова сделала это.'
    'Приятно наблюдать, как её руки высекают музыку, словно скульптор свою фигуру.'

    'А какая же красивая музыка получалась! Даже если я буду тренироваться дни и ночи, ни черта у меня не выйдет.'

    thirty_five_grad_alex 'Мику, скажу честно, как же я завидую тебе. Точнее твоему таланту. У тебя так это прелестно получается!'

    '...Я думал, что она оценит комплимент, но заместо этого, наоборот, даже погрустнела немного.'

    # (Мику грустная)
    show 35grad_miku 2 sad pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Зато много чего другого не умею. Спасибо, конечно, за тёплые слова, но это не талант, а упорный труд. Я училась с пяти лет, Лёша. С понедельника по пятницу.'
    thirty_five_grad_mi 'И мой первый инструмент была флейта. Но прости, она у меня дома. А тут они, мягко сказать, не особо хороши. Не то дерево и сделаны не по той технологии.'

    thirty_five_grad_alex 'Мику, извини, что заставил тебя грустить.'

    # (Мику обычная)
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Вот бака! Мне, наоборот, с тобой хорошо в плане, что не одна тут! Просто меня немного расстраивают такие слова.'
    thirty_five_grad_mi 'Ведь скажи же: то, что ты умеешь управляться с инструментами - это талант или навык?'

    thirty_five_grad_alex 'Ну, навык. Но согласись, что без толики таланта человек к чему-то стремиться будет дольше, чем тот, у кого он есть.'

    thirty_five_grad_mi 'Вот именно! Лёша, а ты смотри, догадался! И это. Хватит болтать! На, держи гитару!'

    thirty_five_grad_alex 'Хорошо, ты права. Давай начинать.'
    # Возможно тут стоит добваить цг
    hide 35grad_miku 2 normal pio ponytails with dissolve_fast
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_deblur
    'Затем произошло то, до чего можно было бы и догадаться, но мой мозг был отключён.'
    'Девушка ласково передала мне свою гитару, которая была ещё тёплой от её рук, а сама встала сзади меня, отчего её хвостики «разлились» прямо на моих плечах.'
    'От них приятно пахло цветочным натуральным запахом.'

    'Если бы не гитара, я бы так и зарылся в них. Кстати о ней. Обычная акустика, которая была у кого-то из моих друзей.'
    'Но только эта гитара была деревянной и новой на вид и приятно сидела в руках. Только вот была массивной! Как её спокойно удерживает Мику?'

    thirty_five_grad_mi 'Так, Алексей. Не отвлекаемся и внимательно слушаем мой голос...'

    'Но я ласково перебил её. Больше из-за того, чтобы легонько подразнить её. Почему бы и нет?'

    thirty_five_grad_alex 'Я бы твой голос слушал вечно.'

    'На что она так же ласково прошипела:'

    thirty_five_grad_mi 'Сейчас кое-кого покусаю! Та-ак. Представь, что мои руки – твои руки и раз...'

    'Данная песенка, которая была лёгкая на вид, оказалась с подвохом. Хотя она и игралась относительно просто, вот только всё равно фальшивила.'
    'Отчего мне было стыдно перед Мику.'

    thirty_five_grad_alex 'Блин.'

    thirty_five_grad_mi 'Успокойся. Расслабься. Тебе спешить некуда. Давай ещё разок.'

    'Второй раз получился уже немного лучше. Руки всё ещё слушались плоховато, но тепло её ладоней придавало мне веры во что-то лучшее.'

    thirty_five_grad_mi 'Лёшка, а в этот раз неплохо! Неужели у тебя тоже талант?'

    thirty_five_grad_alex 'Решила мои же слова использовать?'

    thirty_five_grad_mi 'Агу! Но, правда, ты справляешься довольно хорошо.'

    'Её щёчки пылали, как и мои. Неужели я и правда, что-то могу? От этого стало тепло на душе.'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    scene bg int_musclub_day with fade
    show 35grad_miku 2 normal pio ponytails with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg int_musclub_day at thirty_five_grad_blur
    thirty_five_grad_alex 'Мику. Ты любишь читать?'

    'Внезапно спросил я. Хоть мы сейчас просто сидели и отдыхали, но всё же хотелось с ней поговорить по душам.'
    show 35grad_miku 3 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Да, даже очень! Только ты не будешь смеяться, если скажу что?'

    'Мой взгляд упал на полку возле доски, которую раньше почему-то не примечал. На ней стояли с десяток книг разной толщины.'
    'И все они были, если судить по названиям, про романтику.'

    thirty_five_grad_alex 'Конечно, нет! Я ж не Алиса.'
    show 35grad_miku 3 smile pio ponytails with dspr
    thirty_five_grad_mi 'Именно. Ты лучше её! Так вот, мне очень нравятся романтика, драма и научная фантастика. И особенно, когда это всё вместе переплетается!'
    thirty_five_grad_mi 'Романтика дарит надежду, теплоту и веру. Драма даёт понимание, что плохое всегда заканчивается, а фантастика... Ну просто фантастика!'
    show 35grad_miku 2 laughter pio ponytails with dspr
    'И тихо рассмеялась. Я хоть уже и говорил, но мне нравится, как она разговаривает. Её голос, её глаза, фигурка.'
    'Её искренняя доброта и верность... Мне хочется защищать её, и я ни о чём не жалею.'

    thirty_five_grad_alex 'Рад это слышать. Постарайся сохранить эти качества в себе.'

    thirty_five_grad_mi 'Обязательно! А это... Тебе что нравится?'
    show 35grad_miku 2 normal pio ponytails with  dspr
    thirty_five_grad_alex 'Могу сказать то же самое. Но добавь к этому хоррор и что-нибудь автобиографическое.'

    'Ох, чёрт... Лёха снова проговорился...'

    thirty_five_grad_mi 'А что такое холор? Прости, когда в словах столько букв «р» мне тяжело выговаривать.'

    thirty_five_grad_alex 'Ужастики.'

    thirty_five_grad_mi 'О. Это которые обычно рассказывают возле костра?'

    'Вспоминая такие книги, как «Призрак дома на холме», «Впусти меня» и какие-нибудь «Хребты безумия» мне, в принципе, хочется с ней согласиться.'

    thirty_five_grad_alex 'Отчасти. Но они немного... для более взрослой аудитории.'
    show 35grad_miku 3 smile pio ponytails with dspr
    thirty_five_grad_mi 'О-о-о! Лёша, вот ты...'

    # (музыка) Sergey Eybog - I Don't Blame You
    play music music_list['i_dont_blame_you'] fadein 3
    show 35grad_miku 3 shy pio ponytails with dspr
    'Наши ладони случайно, а может и нет, соприкоснулись. Это продолжилось пару секунд, но честно скажу, мне этого было мало.'
    'Я никогда ранее не держал девушку за руку, но сейчас мне было очень приятно. Да настолько, что...'

    thirty_five_grad_alex '...Тут довольно прохладно, не так ли?'

    'Сказал я практически про себя. Мне хоть и было хорошо, но не уверен, что также классно было и ей. Я не хочу её отталкивать.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ещё раз спасибо, Лёша. Извини, что вечно это говорю, но не знаю, как по-другому можно выразить то, что ты всегда рядом, когда мне нужна помощь, твоя поддержка.'
    thirty_five_grad_mi 'И, пожалуйста, не обижайся на меня за это, но... Могу тебя попросить об одной маленькой просьбе?'

    'Я в любом случае не мог бы ей отказать. Не такой я человек, который откажет в помощи.'

    thirty_five_grad_alex 'Конечно. Что ты хочешь?'

    'Проговорил я мягко. Отчего она сразу засияла, как маленькая звёздочка.'
    show 35grad_miku 3 normal pio ponytails with dspr
    thirty_five_grad_mi 'Мне нужно будет помочь кое с чем завтра, желательно с утра. Прости, сейчас пока не могу сказать конкретно.'
    thirty_five_grad_mi 'Всё на месте. Если откажешься, я всё пойму.'

    'Она смотрела на меня глазами, полными надежды. Теперь я полностью обезоружен и не мог ей отказать.'
    'На самом деле мне хочется верить в то, что я и правда ей не безразличен, в то, что она мной попросту не пользуется.'

    thirty_five_grad_alex 'Хорошо. Когда мне конкретно подходить?'
    show 35grad_miku 2 laughter pio ponytails with dspr
    'Мику мягко улыбнулась, при этом прикрыв глаза, и спокойно вздохнула:'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ох, Лёшенька, благодарю! Но прийти нужно будет примерно... в шесть утра.'

    thirty_five_grad_alex 'Ого! Так рано!'
    show 35grad_miku 2 sad pio ponytails with dspr
    thirty_five_grad_mi 'Да, прости уж. Просто хочется начать пораньше. До жары и завтрака.'

    thirty_five_grad_alex 'И не говори. В последний раз, когда я смотрел на градусник, целых тридцать пять градусов было!'

    thirty_five_grad_mi 'Кошмар какой! Хотя в Токио сейчас примерно такая же жара летом. Там зимой очень холодно, а летом очень жарко!'

    thirty_five_grad_alex 'А что тебе из этого больше нравится?'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Честно? Ничего! Я больше весну люблю...'

    thirty_five_grad_alex '...Когда возрождается природа, цветёт сакура, на улице приятная погода и можно хорошо проводить время на улице.'

    thirty_five_grad_mi 'Тысячу раз да! Ты хорошо ловишь мои мысли!'

    thirty_five_grad_alex 'Хех, стараюсь.'
    play sound sfx_dinner_jingle_normal fadein 1
    'В это время заиграл горн, оповещающий нас об обеде. Да и в принципе я сам уже проголодался, но желания идти всё так и не было.'

    thirty_five_grad_alex 'Пошли вместе, Мику?'

    'Предложил я. Надеясь на то, что она хотя бы и в этот раз не откажет.'
    show 35grad_miku 3 smile pio ponytails with dspr
    thirty_five_grad_mi 'С радостью! А то кушать всё же хочется.'

    thirty_five_grad_alex 'А вообще, ты сколько раз в день питаешься-то?'
    show 35grad_miku 2 sad pio ponytails with dspr
    thirty_five_grad_mi 'Два. Из-за такой духоты не особо хочется.'

    thirty_five_grad_alex 'Это плохо.'

    thirty_five_grad_mi 'Согласна. А что поделать? Меня ока-сан тоже заставить не может. Ну что, пойдём уже, а то сейчас все хорошие места займут.'

    thirty_five_grad_alex 'Солидарен.'

    # (фон музклуба снаружи)
    scene bg ext_musclub_day with fade
    play sound sfx_close_door_1
    'Когда мы вышли на улицу, нас окружил адский прогрев. Воздух был сильно разогрет, дышать было трудновато. И всё это в августе.'
    'Что происходило здесь в июле, даже представлять не хочется... Мику закрыла клуб и, улыбнувшись мне, вместе направилась в столовую.'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон столовой внутри)
    scene bg int_dining_hall_people_day with fade
    play ambience ambience_dining_hall_full fadein 2
    '...В помещении было полно народу, но для нас двоих всё же место нашлось.'
    'Недалеко от того самого окна, где Мику сидела в первый день. Мы вместе с ней сели туда же.'
    show 35grad_miku 1 normal pio ponytails with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg int_dining_hall_people_day at thirty_five_grad_blur
    thirty_five_grad_alex 'А я тебя видел вчера. Ты тут сидела, смотрела на меня. Приятного аппетита, кстати.'

    'Идиот! Диалог с девушкой не так начинают! Но назад дороги нет. Я не умею откатывать время на пару минут назад...'
    show 35grad_miku 1 serious pio ponytails with dspr
    thirty_five_grad_mi 'Ой, ну уж извини, что я спалилась так. И тебе тоже.'

    'Слегка обиженно протянула Мику.'
    show 35grad_miku 1 normal pio ponytails with dspr
    'Диалог не клеился от слова совсем. По ощущению, словно даже еда была не такой уж вкусной, а пюре и вовсе напоминало клей.'
    'Но есть хотелось так или иначе, поэтому впихивал себя и так, попивая холодным смородиновым компотом. Вкусняшка! Хоть что-то приятное.'

    # (спрайт Слави обычный)
    show 35grad_miku 1 normal pio ponytails with dspr:
        ease 1.0 xalign 0.2
    show 35grad_slavya 2 normal pio with dissolve:
        xalign 0.8
    thirty_five_grad_sl 'Я подсяду?'

    'Внезапный голос заставил обратить на себя внимание. Повернул голову и понял, кто стоял передо мной:'

    thirty_five_grad_alex 'Да, садись, Славь. Не занято.'

    'Мику как-то странно на нас посмотрела, но ничего не сказала.'
    'А вот Славяна, наоборот, всё говорила и говорила о том, как хорошо поработала, что ещё можно сделать на сегодня и всё в таком роде.'
    show 35grad_miku 2 serious pio ponytails with dspr
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Кстати, Лёш, можно тебя попросить кое о чём?'

    thirty_five_grad_alex 'Валяй.'
    thirty_five_grad_sl 'покажи писю'
    thirty_five_grad_sl 'Завтра мне твоя помощь нужна будет. Особенная.'

    '...Похоже, завтра у меня будет тяжёлый день. Но, а куда мне деваться? Не могу же я её послать куда подальше? Не, вообще-то могу.'
    'Только как мне потом ей в глаза смотреть? Ведь помимо Мику я думаю и о Славе...'
    'Какой бы она не была трудолюбивой, но природную красоту и интересную личность никто не отменял.'

    thirty_five_grad_alex 'Ладно, что делать-то надо? И когда?'
    thirty_five_grad_sl 'Завтра перед обедом. Я сама тебя найду, хорошо?'

    'Я кивнул.'
    show 35grad_slavya 2 laugh pio with dspr
    thirty_five_grad_sl 'Вот и отлично! Кхм.'

    'Она наигранно кашлянула в кулак. И мне это НЕ понравилось. Не люблю, когда так делают. Особенно так фальшиво.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_mi 'Ты что-то хотела?'

    'Внезапно даже для меня спросила Мику.'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Просто я вижу, как вы вместе общаетесь.'

    thirty_five_grad_mi 'И всё?'

    thirty_five_grad_sl 'И всё. Мику, ты раньше никогда ни с кем не сидела. Вот такую деталь приметила.'
    show 35grad_miku 2 normal pio ponytails with dspr
    thirty_five_grad_mi 'Ну... ладно. Молодец.'
    show 35grad_slavya 2 normal pio with dspr
    thirty_five_grad_sl 'Ах, да. Тебя ещё Ольга Дмитриевна искала, кстати. После обеда подойти к ней.'
    show 35grad_miku 2 serious pio ponytails with dspr
    thirty_five_grad_mi 'Зачем?'

    'Снова спросила Мику. Что это с ней?'
    show 35grad_slavya 2 smile pio with dspr
    thirty_five_grad_sl 'Да мне откуда знать?'

    'Хоть она это и сказала с улыбкой, но даже я почувствовал холод.'

    thirty_five_grad_sl 'Всем приятного аппетита.'

    # (Славя пропадает)
    hide 35grad_slavya 2 smile pio with dissolve
    show 35grad_miku 2 normal pio ponytails with dspr:
        ease 0.5 xalign 0.5
    'Мы с Мику кивнули. Эта противно-липкая атмосфера стояла в воздухе. Интересно, почему только стоило покинуть клуб, как сразу всё вокруг стало таким злым и неприветливым?'
    'Ощущаю себя на театральной сцене. Не пойду я к Ольге, но чувствую, что и к Мику лучше пока не надо идти.'
 
    thirty_five_grad_mi 'Лёш, можешь, пожалуйста, пока погулять? Мне в клубе... кое-что сделать надо. Ты уж прости...'

    'Виновато протянула по слогам последнее предложение. Она словно мои мысли прочитала!'

    thirty_five_grad_alex 'Ладно, надо так надо. У меня тоже свои дела были.'

    'Остаток обеда провели в спокойной тишине, которая, не побоюсь этого слова, лечила моё душевное состояние.'
    'Мысли приводились в норму, а сердце не билось так уж и быстро. Всё, в общем, хорошо. Люблю это слово – «хорошо»...'

    # (затемнение (раньше это было обычное моргание))
    # (музыка) Flawed Mangoes — Tunnel Vision
    play music thirty_five_grad_flawed_mangoes fadein 3
    $ renpy.display_notify('Сейчас играет:\nFlawed Mangoes — Tunnel Vision')
    # (фон домиков)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_houses_day with fade
    'На небе не было облаков. Одно густое тяжёлое синее небо да яркий, выжигающий глаз и кожу белый круг.'
    'Только сейчас заметил, как в послеобеденное время сознание заполняется мыслями о потерянном прошлом.'

    'Я медленно прогуливаюсь по каменной дорожке, бреду в никуда. Хм. Интересно, а родители уже ищут меня? А может, в моём мире вообще прошло только пять минут?'
    'Сложно было сказать наверняка. Да и если задуматься, то что будет, когда закончится смена? Надеюсь, что ничего плохого.'
    'Может, если повезёт, то и в мой мир меня вернут! Ха! Оптимистично.'

    'В общем, я всегда стараюсь быть оптимистом. А почему бы и нет? Что я от этого теряю? Ладно, что-то у меня ноги устали, нужно присесть.'
    'Ближайшая лавка была чистой и опрятной, словно я реально вернулся в старую добрую советскую эпоху.'

    'Хоть лавка и была совершенно обычной, деревянной, но сидеть всё равно было приятно. Только расслабился я зря. Неужели проклят? Вполне может быть.'
    'Или же это такая цена за такое... в принципе, приятное место. Даже если я был бы реально обычным пионером, то сюда возвращался бы с радостью.'

    thirty_five_grad_ul 'Эх, Лёша! Когда ты так нужен, тебя нет.'

    # (появляется Лена)
    show 35grad_lena 1 normal pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_day at thirty_five_grad_blur
    'С недовольством буркнула Лена, после чего бесцеремонно села рядом со мной. Не то, чтобы я был жадиной, но всё же хотелось провести время наедине с собой.'

    thirty_five_grad_alex 'Чего тебе? Я отдыхаю.'

    thirty_five_grad_ul 'А ты так сильно устал?'

    thirty_five_grad_alex 'Ну так что тебе?'
    show 35grad_lena 2 crabbed pio with dspr
    thirty_five_grad_ul 'Виола искала тебя, попросила, чтобы ты зашёл. Грубиян.'

    # (Лена пропала)
    hide 35grad_lena 2 crabbed pio with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_day at thirty_five_grad_deblur
    'После чего встала и собралась уходить. Я мог бы поймать её и извиниться, но что-то не очень хотелось.'
    'Странно то, что угрызения совести я совсем не испытывал. Лена мне не особо прельщала, конечно, но лично против неё ничего не имел.'

    'Спрашивается, зачем я Виоле понравился? То есть понадобился? Хотя вряд ли это оговорка по Фрейду, но другого объяснения у меня не было.'
    'В отличие от Ольги, Виолу игнорировать опасно. По крайней мере, так подсказывает моя пятая точка.'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон медпункта снаружи)
    scene bg ext_aidpost_day with fade
    'Стою под дверью медпункта и чувствую, как потеют мои ладони. Неприятное чувство ожидания натурально грызёт меня.'
    'Но стоит потерпеть, и всё будет хорошо. Я стучусь, а в ответ мне:'

    # (музыка) Between August And December - Eternal Longing
    play music music_list['eternal_longing'] fadein 3
    thirty_five_grad_cs 'Я же говорила, ты можешь входить и без стука.'

    'Голос наравне с Мику, который можно узнать из тысячи. Нет, миллионов! Он сладкий, но не приторный, манящий, но не вульгарный.'
    'Думаю, что если Мику наберётся смелости и уверенности в себе в будущем, то он будет даже сильнее, чем у Виолы. Я открываю дверь и вхожу.'

    # (фон медпункта внутри)
    # (появляется Виола)
    scene bg int_aidpost_day with dissolve
    play sound sfx_open_door_1
    play ambience ambience_medstation_inside_day fadein 2
    show 35grad_viola 1 normal reb with dspr
    if persistent.thirty_five_grad_blur_pref:
        show bg int_aidpost_day at thirty_five_grad_blur
    thirty_five_grad_alex 'Вызывали?'

    'Кабинет встретил меня приятной прохладой и жёстким спиртовым запахом. Тут выпивали? Хотя не, просто дезинфекция.'

    thirty_five_grad_cs 'Вызывают девушек распутного поведения, а порядочных людей зовут. Я надеюсь на то, что ты порядочный человек. Да, Алексей?'

    thirty_five_grad_alex 'Стараюсь вести себя по-человечески.'

    thirty_five_grad_cs 'Это хорошо, но Елена будет с этим не согласна.'

    thirty_five_grad_alex 'А? О чём это Вы?'
    show 35grad_viola 2 normal reb with dspr
    thirty_five_grad_cs 'Она уже успела прийти и нажаловаться о том, какой ты грубиян. Я не стала ей что-либо говорить, так как сама должна понять, что такое сильный мужчина.'

    thirty_five_grad_alex 'Где это вы сильных увидели? Просто настроения не было, вот и всё. Да и она мне сама не особо.'
    show 35grad_viola 2 hitry reb with dspr
    thirty_five_grad_cs 'Зато одна азиатка и явно славянской натуры девушки тебе приглянулись. Я права?'

    'Всё меньше желания было тут оставаться. Нужно уходить.'

    thirty_five_grad_alex 'Я пойду, пожалуй. У меня дела кой-какие.'
    show 35grad_viola 2 normal reb with dspr
    thirty_five_grad_cs 'Извини уж, что я такая прямолинейная. Говорю как есть. Вообще, хоть я и врач, но уши у меня повсюду как у вожатой.'

    thirty_five_grad_alex 'Это хорошо, я думаю. Но зачем вы меня звали? Нужна какая-то помощь?'
    show 35grad_viola 2 sly reb with dspr
    thirty_five_grad_cs 'Даже с моими пошлыми шутками ты всё ещё добр. Как мило.'

    thirty_five_grad_alex 'Ближе к делу. Так чем я могу помочь?'

    'Во мне сражался дух противоречия, ведь буквально не знал, как поступать! Вдруг и правда ей нужна помощь?'
    'Но попадать под сексуальное насилие мне что-то не очень хочется. Хотя любой другой парень был бы только «за».'
    show 35grad_viola 2 normal reb with dspr
    thirty_five_grad_cs 'Нет, никакая помощь мне не нужна. А вот пройти медосмотр нужно. Ведь ты вчера так его и не прошёл.'

    thirty_five_grad_alex 'А, собственно, зачем? Я ж не буду устраиваться к вам медбратом. Тем более у вас Лена есть. На ней и практикуйтесь.'
    thirty_five_grad_cs 'Его проходят все. Почти.'

    thirty_five_grad_alex 'То есть?'

    thirty_five_grad_cs 'Все, в ком я уверена. По состоянию здоровья.'

    thirty_five_grad_alex 'Так я здоров как медведь.'
    show 35grad_viola 2 sly reb with dspr
    thirty_five_grad_cs 'Слова это удобно, но нужно иногда применять и действия. Раздевайся.'

    'Я нервно сглотнул. Сколько в Союзе давали за харасмент? Потянулся к галстуку, чтобы развязать его, и в голову пришла одна глупая шутейка:'

    thirty_five_grad_alex 'А. Разве для этого специфическую музыку включать не нужно?'

    thirty_five_grad_cs 'Думаю, что пока нет. Рановато, да и день на улице как-никак.'

    thirty_five_grad_alex 'Вот если была бы ночь...'

    # (спрайт Виолы покрасневшая)
    show 35grad_viola 2 shy reb with dspr
    'Мы оба покраснели. Хотя я стал красным ещё чуточку ранее, когда стою возле взрослой женщины в расцвете сил, по пояс голый.'
    'Не сказать, что у меня прямо-таки спортивное тело, но явные пару кубиков были. Маленький бонус, но приятный.'

    thirty_five_grad_cs 'Хм. С чего бы начать... Медленно...'
    ' - протянула врач, как будто намекая на что-то такое... А затем...'

    'Она прикоснулась до моего тела. Её тёплые руки ощупывали каждую деталь моего торса. Отчего внизу становится жарко...'
    show 35grad_viola 2 normal reb with dspr
    thirty_five_grad_cs 'Хм-м-м... Ни синяков, ни ссадин. Удивительно, но с виду ты здоров.'

    thirty_five_grad_alex 'Мне почему-то кажется, что вы этот «медосмотр» специально придумали, чтобы провести пальпацию...'

    'Сказал я хоть и хмуро, но похоже, что она это восприняла как за какую-то игру.'
    thirty_five_grad_cs 'Как сказать, как сказать. Правда умрёт вместе со мной. А вообще, если без шуток, то это была лишь формальная проверка твоего здоровья, не более того.'
    thirty_five_grad_cs 'Такая проводится у всех. Даже у Ольги.'

    'На упоминании имени вожатой Виола прикусила губу, отчего мне стало немного неловко. Хотя, чёрт побери, это всё вообще концерт абсурда!'

    thirty_five_grad_cs 'Ладно, одевайся и можешь топать по своим делам.'

    'Я стал незамедлительно одеваться, чтобы побыстрее свалить отсюда. Хотя, чего я тут ханженствую.'
    'Ведь мне отчасти, как мужчине, нравится такое внимание со стороны такой дамы.'

    thirty_five_grad_alex 'Знаете, Виола, вам бы моделью работать или типа того.'
    show 35grad_viola 2 shy reb with dspr
    'Она легонько, но ярко и по-тёплому покраснела.'

    thirty_five_grad_cs 'Ох-о-хо! Это с чего ты так решил, пионер?'

    thirty_five_grad_alex 'Вы красивы. Даже очень. А почему так покраснели?'
    show 35grad_viola 2 laugh reb with dspr
    thirty_five_grad_cs 'Любой девушке приятно, когда говорят приятные вещи, причём, если это искренние слова.'

    thirty_five_grad_alex 'Абсолютно. Я ненавижу ложь.'
    show 35grad_viola 2 normal reb with dspr
    thirty_five_grad_cs 'Как и твой врач. Не личный, просто выражение.'

    'Всё. Теперь мне точно нужно идти.'

    # (музыка стоп)
    stop music fadeout 3
    # (спрайт Виолы обычный)
    
    thirty_five_grad_alex 'До свидания, Виола.'

    thirty_five_grad_cs 'Прощай, Алексей. {w}А! Постой.'

    thirty_five_grad_alex 'Что такое?'

    # (музыка) Between August And December - Glimmering Coals
    play music music_list['glimmering_coals'] fadein 3
    thirty_five_grad_cs 'Хочешь небольшой интересный факт?'

    thirty_five_grad_alex 'Почему бы и нет.'
    show 35grad_viola 2 sly reb with dspr
    thirty_five_grad_cs 'Все девочки из твоего отряда, дев...'

    thirty_five_grad_alex 'Ладно-ладно, я вас услышал, понял и осознал. До свидания!'

    # (музыка стоп)
    # (фон медпункта снаружи)
    stop music fadeout 3    
    play sound sfx_close_door_1
    scene bg thirty_five_grad_ext_aidpost_sunset with dissolve 
    'Господи, Бог ты мой! На негнущихся ногах я быстро закрываю дверь. Но даже так, перед тем, как закрыть её, я увидел самую ехидную рожицу на свете.'
    'Хорошо, что я не дал ей договорить. Да даже если и дал бы, то не стал слушать. Не хочу.'

    # (фон домиков)
    scene bg ext_houses_sunset with dissolve
    'Отойдя на приличное расстояние, (метров так на сто с лишним), я начал думать о том, что мне делать теперь.'
    'Можно полежать в домике, если там Ольги нет, конечно, а можно пойти и помочь Алисе-крысе.'
    'Ладно, она на самом деле тоже ничего, но с небольшим приветом, как и Виола. Не удивлюсь, если они родственники!'

    # (спрайт Алисы)
    show 35grad_alice 1 normal reb at thirty_five_grad_sunset_lighting with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_sunset at thirty_five_grad_blur
    thirty_five_grad_dv 'Эй, Лёх, а ты чего делал в медпункте? Неужели нашу жару не вынес и тебе плохо стало?'

    '...Как говорится, если ты не идёшь к рыжим, то рыжие идут к тебе. А может, не так говорилось. Плевать.'

    thirty_five_grad_alex 'В отличие от некоторых, у меня и свои дела есть. Да и вообще, чего ты это в клубе устроила? Что за позорище это было?'

    thirty_five_grad_dv 'Кончай, а. Не порть о себе впечатление. У пацанов свои разборки, а у нас свои.'

    thirty_five_grad_alex 'Верно. Если это не касается моих друзей.'

    'На что она обошла меня по часовой стрелке, как тогда перед Мику.'
    'Если откинуть все хиханьки и хаханьки, то Алиса – натуральная хищница, которая ни перед чем не остановится.'
    'По крайней мере, так я могу судить из опыта общения с ней.'

    # (спрайт Алисы хитрой)
    show 35grad_alice 2 tricky reb at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_dv 'Друзья? Может, уже больше, чем просто друзья?'

    thirty_five_grad_alex 'И что? Даже если это так, то каким боком это касается тебя?'

    thirty_five_grad_dv '«Если»? То есть?'

    thirty_five_grad_alex 'Отстань, а? У меня нет желания с тобой ругаться.'

    thirty_five_grad_dv 'А вот в клубе... Ты хотел...'

    thirty_five_grad_alex 'Да. Потому что ты там берега попутала.'

    # (спрайт злой Алисы)
    show 35grad_alice 2 ready_to_smash_faces reb at thirty_five_grad_sunset_lighting with dspr
    'Затем она развернулась ко мне и толкнула в грудь. Но всё же смог нормально устоять на ногах.'

    thirty_five_grad_dv 'Ну ты и козёл!'

    thirty_five_grad_alex 'А? Я в чём виноват, дурёха?'

    thirty_five_grad_dv 'В том, что ты вообще тут появился.'
    hide 35grad_alice 2 ready_to_smash_faces reb at thirty_five_grad_sunset_lighting with dissolve
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_houses_sunset at thirty_five_grad_deblur
    'С грустным голосом сообщила мне это и перед тем, как уйти, толкнула меня плечом. М-да, не очень-то весёлая атмосфера во второй половине дня!'
    'Хотя, даже в этом есть плюс – не нужно будет Алисе помогать. Вот в чём сила оптимизма!'
    '...И дурости... языка, неспособного нормально договориться...'

    # (затемнение (раньше это было обычное моргание))
    # (фон вечернего музклуба снаружи)
    # (музыка) Сергей Ейбог - Goodbye Home Shores
    scene bg thirty_five_grad_music_sunset with fade
    play music music_list['goodbye_home_shores'] fadein 3
    'Мне конкретно нечего делать. А когда нечем заняться, то либо сама судьба, либо мозг придумывает для тебя конкретные задачи. Вот, как и сейчас я иду в клуб.'
    'Пускай уже и смеркается, да и про встречу со Славей я не забыл, но хочется узнать, как там была Мику. Я стучусь в дверь, и мне ласково говорят "входи".'

    # (фон музклуба вечер внутри + грустный спрайт Мику)
    scene bg thirty_five_grad_int_music_club_sunset with dissolve
    play ambience ambience_music_club_night fadein 2
    show 35grad_miku 1 sad pio ponytails at thirty_five_grad_sunset_lighting with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_int_music_club_sunset at thirty_five_grad_blur
    thirty_five_grad_mi 'А? Лёш, это ты?'

    'Словно она ждала кого-то другого. Поэтому так грустно протянула слова.'

    thirty_five_grad_alex 'Что-то не так? Ты ждала ещё кого?'
    thirty_five_grad_mi 'Да нет. Просто, как и сказала. Хочу побыть наедине.'

    thirty_five_grad_alex 'Ладно, хорошо. Как скажешь. Но, то есть до меня ты... постоянно с кем-то была?'

    # (спрайт Мику быстро меняется с злого на грустное)
    show 35grad_miku 1 serious pio ponytails at thirty_five_grad_sunset_lighting with dspr
    $ renpy.pause(0.1)
    show 35grad_miku 1 thoughtful pio ponytails at thirty_five_grad_sunset_lighting with dspr
    'Чёрт меня дёрнул задать этот дурацкий вопрос. Её личико приняло то злое выражение, то грустное, которое попеременно менялось.'

    thirty_five_grad_alex 'Прости, Мику, я не хотел...'
    thirty_five_grad_mi 'Всё... Всё в порядке... Просто не знаю, что со мной такое. Мне то грустно, то весело! То дышать тяжело, то наоборот, словно дышу чистым горным воздухом!'
    show 35grad_miku 1 sad pio ponytails with dspr
    thirty_five_grad_mi 'А ведь это после того, как ты тут появился! Лёшка... прости! Просто погуляй пока, хорошо?'
    
    $ renpy.display_notify('Перевод с японского - Увидимся позже.')
    thirty_five_grad_alex 'Ладно, я понял. {font=NotoSansJP-Medium.ttf}また後で{/font}?'
    show 35grad_miku 1 smile pio ponytails with dspr
    thirty_five_grad_mi '{font=NotoSansJP-Medium.ttf}また後で{/font}. Говоришь очень хорошо, но с сильным акцентом, Лёшка. Но ты всё равно молодец! Горжусь тобой...'

    # (фон вечернего музклуба снаружи)
    scene bg thirty_five_grad_music_sunset with dissolve
    play ambience ambience_camp_center_night fadein 2
    'Последнее она проговорила шёпотом, отчего мне стало очень приятно. Ещё раз попрощавшись, я вышел из клуба...в плохом настроении.'
    'Словно меня вышвырнули отсюда. Хотя и девочку можно понять. У неё тоже есть свои чувства. Хм. Как и у Лены. Нужно будет извиниться.'

    'Небо принимает оранжевые тона, знаменуя собой прибытие долгожданного вечера. Жара тоже постепенно сходит на нет, уступая место обычному теплу.'
    'Вроде всё и хорошо, но словно пустота на душе. И как бы мне не было приятно тут, но всё же хочется домой...'

    # (затемнение (раньше это было обычное моргание))
    # (музыка стоп)
    # (фон спортплощадки вечером)
    scene bg thirty_five_grad_ext_playground_sunset with dissolve
    stop music fadeout 3
    'Я случайно забрёл на интересную территорию – спортплощадку. Так называемую.'
    'Потому что здесь были только футбольные ворота, два кольца для баскетбола, и несколько десятков пустующих лавок.'
    'Здесь вообще не было никого, кроме меня. Я присел на одну из таких лавок.'

    'Никогда особо спортом не интересовался. Не было ни времени, ни желания. Особенно после подработки на стройке. Хотя, может тут всё и изменится.'
    'Ведь, почему нет? Вдруг меня послали сюда ради того, чтобы я как-то поменял свою жизнь?'

    'Не сказать, что я жил совсем уж плохо. Просто никакой цели особо-то не было.'
    'Я существовал день ото дня, поддерживая родителей в материальном плане, попеременно учась в университете.'

    # (музыка) Flawed Mangoes - Tunnel Vision
    # (появляется спрайт Слави)
    play music thirty_five_grad_flawed_mangoes fadein 3
    show 35grad_slavya 2 normal pio at thirty_five_grad_sunset_lighting with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg thirty_five_grad_ext_playground_sunset at thirty_five_grad_blur
    thirty_five_grad_sl 'Лёш, всё хорошо? Что-то ты какой-то грустный. Не стесняйся, постараюсь помочь.'

    'Нежный тон голоса Слави привёл меня в чувство. Хотя, может, неприятный скрип так тоже повлиял. Неважно.'

    thirty_five_grad_alex 'Да, что-то лёгкая меланхолия накатила. А так всё в норме.'

    'Сказал я только половину правды. Всё же не стоит показывать того, как ною девушке. Это неправильно и неприятно.'
    'Мои проблемы не должны касаться друзей. Но, похоже, Славяна была другого мнения:'
    show 35grad_slavya 2 smile pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Эх, Алексей. Не стоит скрывать проблемы, пока они только в зародыше. Если тебя что-то беспокоит – обращайся в любое время!'
    thirty_five_grad_sl 'Я с радостью тебе помогу. Всё же, ты мне жизнь спас.'

    thirty_five_grad_alex 'Хех. А если бы не спас, то ты и не помогла бы?'
    show 35grad_slavya 2 laugh pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Уверяю, я бы тогда уже ничего не могла. Колись, Алиса беспокоит?'

    thirty_five_grad_alex 'Не меня лично, конечно, но там я сам разберусь. Хм...'

    'Без понятия, как правильно подступиться в подобной ситуации. С чего начать. Да и стоит ли вообще?'

    thirty_five_grad_alex 'У тебя было когда-нибудь такое чувство, что тебя словно выдернули из прежней обстановки и засунули невесть куда?'
    show 35grad_slavya 2 normal pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Конечно. Когда мне стукнуло пятнадцать, жизнь в кругу семьи для меня полностью изменилась.'

    thirty_five_grad_alex 'Это ещё почему?'

    # (спрайт грустной Слави)
    show 35grad_slavya 2 worry pio at thirty_five_grad_sunset_lighting with dspr
    'Славя сильно погрустнела. Но до слёз не дошла, сдержалась. Вместо этого выдохнув, продолжила:'

    thirty_five_grad_sl 'Мои родители развелись. Папа забрал братьев, а я осталась с матерью. Как можно понять, я не особо люблю её. Ленивица та ещё.'
    thirty_five_grad_sl 'Наш дом держался исключительно на папе, но после его ухода всё большое хозяйство упало на мои плечи.'

    thirty_five_grad_alex 'Почему он ушёл-то?'
    show 35grad_slavya 2 sad pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'По сути, из-за новой работы и желания начать новую жизнь. Он хотел забрать и меня, но суд не разрешил.'
    thirty_five_grad_sl 'Поэтому я могу понять то, о чём ты говоришь. Но в чём твоя проблема?'

    thirty_five_grad_alex 'Прости, Славя. Мне жаль слышать такое. Для меня семья эта одна из самых важных вещей в жизни. Ты очень хорошая, и не заслуживаешь этого.'

    thirty_five_grad_sl 'Никто не заслуживает. Прости, что было на обеде. На самом деле я рада, что ты так сдружился с Мику. Вам обоим это пойдёт на пользу. Просто...'

    thirty_five_grad_alex '...Ты думаешь, что я тоже там пропаду с головой?'

    thirty_five_grad_sl 'Да.'

    thirty_five_grad_alex 'Верно думаешь. Мне нравится там.'

    thirty_five_grad_sl 'Ладно.'

    # (спрайт Слави обычный)
    show 35grad_slavya 2 normal pio at thirty_five_grad_sunset_lighting with dspr
    'Удачно у меня получилось сменить тему. Да и вышло всё хорошим концом. Закатное солнышко пекло, отчего хотелось спрятаться.'

    thirty_five_grad_alex 'Славь. Сегодня вечером пляжа же не будет?'
    show 35grad_slavya 2 smile pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Ага. Мне обеда хватило.'

    thirty_five_grad_alex 'Ольга не сильно ругала?'
    show 35grad_slavya 2 normal pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Попрошу больше уважения. Ольга Дмитриевна. Наоборот, рада была, что ты так поступил. Видел бы, как она переживала. Это ужас.'
    thirty_five_grad_sl 'Поэтому она и хотела тебя видеть. Ты ходил до неё?'

    thirty_five_grad_alex 'Пока ещё нет.'
    show 35grad_slavya 2 laugh pio at thirty_five_grad_sunset_lighting with dspr
    thirty_five_grad_sl 'Ну и зря. Она же тоже человек. Ладно, хорошо, что ещё в одном домике живёте!'

    'Мы рассмеялись, я всё продолжал смотреть на красивое закатное небо. Раньше я не придавал таким мелочам значения, но только сейчас понял, что как это красиво.'
    show 35grad_slavya 2 normal pio at thirty_five_grad_sunset_lighting with dspr
    'И осознал также, что моей душе не хватает ещё кое-кого рядом...'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон вечерней столовой снаружи)
    scene bg ext_dining_hall_near_sunset with fade
    'Наступило время ужина. Люди стекаются к одному большому зданию, но оно не может вместить себя всех их. Потому младшие отряды зашли первыми и ужинают.'

    'Я тем временем сидел на одной из свободных лавок, построил ладони пирамидкой, и склонил голову вниз.'
    'Со стороны может показаться, как будто я молюсь, но, быть может, так оно и есть.'
    'Всё же хочется того, чтобы в конце смены всё было хорошо и не придётся продавать душу за свободу.'

    'Удивительно, что ко мне за всё это время никто не подсаживался, никто со мной не говорил. Даже страшно стало!'
    'Шучу, конечно, но вдали я заметил знакомые аквамариновые хвостики.'

    # (музыка) MIKULOVE
    play music thirty_five_grad_mikumylove fadein 3
    $ renpy.display_notify('Сейчас играет:\nMIKULOVE')
    'Их владелица озарялась по сторонам так, как будто что-то потеряла, но выглядела при этом немного даже смелее.'
    'Мне было очень интересно, о чём она сейчас думает. Но стоит ли к ней подойти прямо сейчас?'
    'Определённо.'

    # (спрайт Мику обычный)
    show 35grad_miku 1 normal pio ponytails at thirty_five_grad_sunset_lighting_revers with dissolve:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_sunset at thirty_five_grad_blur
    thirty_five_grad_alex 'Вечер, Мику. Кого-то ищешь?'
    show 35grad_miku 1 resentment pio ponytails with dspr
    'Её носик картошкой немножко дёрнулся, придавая её личику миловидности и детской наивности.'
    show 35grad_miku 3 normal pio ponytails with dspr
    thirty_five_grad_mi 'Да. А точнее, уже нашла!'

    'Мои щёки залились румянцем.'

    thirty_five_grad_mi 'Смотри же! Только тихо и аккуратно.'

    'Своим пальчиком она прикоснулась до моей щеки, и я, подобно кукле, повернулся в след, куда указывала хозяйка.'

    thirty_five_grad_alex 'Ух ты...'

    'Мику не соврала. На ветке дерева сидела большая чёрная птица. Её цвет перьев был настолько чёрным, что как будто сам кусочек ночи прилетел к нам.'

    # (спрайт Мику улыбается)
    show 35grad_miku 2 laughter pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Лёша, она сначала сидела на перилах в клубе, а потом улетела в сторону столовой! Прямо туда, где ты сейчас. Ой...'

    thirty_five_grad_alex 'Какое милое совпадение.'

    'Птица издала не особо приятный звук, после чего улетела, шумно маша крыльями.'

    thirty_five_grad_alex 'Ну что, следуй за ней.'

    'Сказал я без особого энтузиазма, ведь вспомнились как приятные, так и терзающие моменты нашего с ней времяпровождения.'
    'Ведь не понимаю, почему она отталкивает меня. Чего плохого я сделал? Но боюсь задать этот вопрос напрямую, ибо может произойти вообще что-то ещё хуже.'
    show 35grad_miku 2 sad pio ponytails with dspr
    thirty_five_grad_mi 'Не хочу. Лёша, я...'

    'Остановил её рукой и отвернулся. Знаю, что веду себя как придурок, поэтому снова развернулся и...'

    # (цг где Лёша обнимает Мику у столовой)
    scene cg thirty_five_grad_day2_miku with dissolve
    '...Легонько обнял её. На виду у всех. Вообще плевать. Либо сейчас, либо никогда. Но на удивление, никто даже внимания не обратил на нас. Как будто это норма.'

    'Мику стояла в ступоре, как и я. Но она не отстранилась от меня, нет, а наоборот, также нежно, ласково и мягко обняла меня за плечи.'
    'Я никогда раньше такого не делал, но мне это понравилось. Только всё равно пришлось отпустить её, иначе из-за этого могли бы быть проблемы.'

    # (цг пропадает + смущающийся спрайт Мику)
    scene bg ext_dining_hall_near_sunset with dissolve
    show 35grad_miku 3 shy pio ponytails at thirty_five_grad_sunset_lighting_revers with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_sunset at thirty_five_grad_blur
    thirty_five_grad_alex 'Прости.'

    thirty_five_grad_mi 'Лёшка, бака! Наоборот, мне понравилось... Ты такой мягенький и нежный... Скажи честно, ты всех друзей так обнимаешь?'

    'Ехидно прощебетала Мику.'

    thirty_five_grad_alex 'Нет. Только избранных.'

    'После этого у меня пропала речь. Мне было стыдно, что я такое сделал, но... К чёрту! Это стоило того!'

    thirty_five_grad_alex 'Пошли? Там уже детвора уходит. Ещё успеем самые лучшие места взять.'
    show 35grad_miku 2 laughter pio ponytails with dspr
    'Девочка тихо рассмеялась.'
    thirty_five_grad_mi 'Лучшие места – это дома. Но да, ты прав. Быстрее поедим, быстрее в клуб пойдём.'

    thirty_five_grad_alex 'О. Неужели мне можно вернуться?'

    thirty_five_grad_mi 'Даже нужно!'

    'Я пропустил её первой в здание, после чего зашёл уже сам...'

    # (музыка стоп)
    stop music fadeout 2
    # (затемнение (раньше это было обычное моргание))
    # (музыка) Between August And December - Heather
    # (фон вечерней столовой внутри + спрайт Алисы)
    scene bg int_dining_hall_sunset with fade
    play music music_list['heather']
    play ambience ambience_dining_hall_full fadein 4
    'Но вместе сесть не получилось, так как её забрали Славя и Лена. По итогу оставшись... Не, не в одиночестве. Нихрена подобного! Прямо рядом со мной села Алиса...'
    show 35grad_alice 1 normal reb at thirty_five_grad_sunset_lighting_revers with dissolve:
        xalign 0.8
    if persistent.thirty_five_grad_blur_pref:
        show bg int_dining_hall_sunset at thirty_five_grad_blur
    thirty_five_grad_dv 'Давно не виделись, кролик...'
    show 35grad_miku 2 sad pio ponytails at thirty_five_grad_sunset_lighting_revers with dspr:
        xalign 0.2
    'Я поймал на себе взгляд Мику – грустный, обеспокоенный, тяжёлый.'

    thirty_five_grad_alex 'С чего это я кролик?'

    thirty_five_grad_dv 'Пытаешься казаться смелым, а на самом деле трусливый чёрт.'

    thirty_five_grad_alex 'Ты меня это на понт не бери, поняла? Не я начал эту грызню. Что с тобой не так?'

    'Я откровенно не понимал её. То она весёлая, то злая, сейчас вообще чёрт пойми что. Как мне с ней общаться?'
    'Она словно одна большая пороховая бочка, а я – горящий уголёк.'
    show 35grad_alice 1 normal joy reb with dspr
    thirty_five_grad_dv 'На понт брать тебя пока ещё рановато. Ладно, признаюсь, погорячилась. Ты не слабак. По крайней мере, меня терпеть можешь, в отличие от некоторых.'

    'И презрительно так посмотрела на мою подругу. Была бы возможность, сейчас зарядил бы в Алису пюрешкой в рожу.'
    'Знаю, что по-ребячески, но не с кулака же её бить.'

    # (музыка стоп)
    stop music fadeout 3
    'Дальнейший приём пищи прошёл в тишине. Благо, она больше ничего не вываливала из своего рта, отчего я спокойно доел ужин.'
    # (пропадает спрайт Алисы)
    hide 35grad_alice 1 normal joy reb with dissolve
    'Когда Алиса встала из стола, то ушла так, как будто ничего не было вообще.'

    'Пора уходить и мне. Но сперва нужно найти Мику.'
    'Глазами стал искать знакомый небольшой силуэт. Всё же рост красочной азиатки был реально невысоким, она уступала мне на целую голову, а то и на полтора.'
    'Но так, к сожалению, и не нашёл.'

    'Скорее всего, девушка уже вышла, и её можно понять. В столовой воняло едой, а также было очень душно. Хотелось поскорее уже выйти, что я и сделал.'

    # (фон вечерней столовой снаружи + спрайт Мику)
    play ambience ambience_camp_center_evening fadein 4
    scene bg ext_dining_hall_near_sunset with dissolve
    show 35grad_miku 2 normal pio ponytails at thirty_five_grad_sunset_lighting_revers with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_near_sunset at thirty_five_grad_blur
    thirty_five_grad_mi 'Ой, а я уже сама хотела тебя искать. Кстати, Лёш, Алиса тебе ничего плохого не делала? А то я волновалась...'

    thirty_five_grad_alex 'Микусь, всё хорошо. Если я тебя в обиду не дам, то себя тоже.'

    # (музыка) MIKULOVE
    play music thirty_five_grad_mikumylove fadein 3
    $ renpy.display_notify('Сейчас играет:\nMIKULOVE')
    'Девочка мило прикрыла глазки и также ослепительно улыбнулась.'
    'Вроде совершенно обычная улыбка, но в то же время, очень искренняя, чистая и невинная.'

    # (спрайт Мику смущённой)
    show 35grad_miku 3 normal pio ponytails with dissolve_fast
    thirty_five_grad_mi 'Меня ещё никто так не называл...'

    thirty_five_grad_alex 'Тебе неприятно?'
    show 35grad_miku 3 normal pio ponytails with dspr
    thirty_five_grad_mi 'Совершенно нет. Это как было с объятиями. Резко, конечно, но очень приятно.'

    thirty_five_grad_alex 'Хорошо. Буду знать, как теперь тебя можно называть.'

    # (фон ночной столовой снаружи)
    scene bg ext_dining_hall_away_night with dissolve
    play ambience ambience_camp_center_evening fadein 4
    'На улице уже потемнело.'

    thirty_five_grad_mi 'Ты ещё хочешь идти в клуб?'

    'Спросила она меня. Но я даже не знаю вроде, почему бы и нет? Но в то же время я за день серьёзно так устал.'
    'Хотя стоит только внимательно приглядеться, то можно заметить, как и сама Мику уже носиком клюёт.'

    thirty_five_grad_alex 'Я спать хочу. А ты?'
    show 35grad_miku 2 normal pio ponytails at thirty_five_grad_night_lighting with dspr:
        xalign 0.5
    if persistent.thirty_five_grad_blur_pref:
        show bg ext_dining_hall_away_night at thirty_five_grad_blur 
    thirty_five_grad_mi 'Ух ты! Ждала, пока ты это скажешь. На самом деле, даже если бы ты захотел, то мы бы пошли.'

    thirty_five_grad_alex 'Не стоит так себя перетруждать.'

    thirty_five_grad_mi 'Хочешь сказать, что организм сам знает, когда ему будет лучше?'

    thirty_five_grad_alex 'Верно.'
    show 35grad_miku 2 sad pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Как мило. Ладушки. Лёш, можешь меня проводить до моего домика, пожалуйста? А то одной идти... Не особо хочется.'
    thirty_five_grad_mi 'С той стороны аллеи фонари плохо горят. Ну...'

    'Она очень милая, когда волнуется.'

    thirty_five_grad_alex 'Ни слова больше. Пройдёмте, Мику-сан. Нас ждёт недолгий, но всё же продолжительный путь.'
    show 35grad_miku 2 laughter pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Ой, Лёшенька, ну ты прямо сегодня в ударе! Меня так даже на родине не называли! Хотя я тогда ещё маленькая была...'

    'И мы вместе пошли, как самые настоящие друзья. На сердце был покой, и что-то подсказывало мне, что всё-таки будет хорошо. Если я не напортачу, конечно.'

    # (фон ночных домиков)
    scene bg thirty_five_grad_ext_houses_night with dissolve
    # (спрайт Мику обычный)
    show 35grad_miku 1 normal pio ponytails at thirty_five_grad_night_lighting with dspr:
        xalign 0.5
    thirty_five_grad_alex 'Кстати, а ты не хотела бы вернуться в Японию?'

    'Мику явно призадумалась, и пока она решала, что сказать, я наблюдал за ночным небом.'

    thirty_five_grad_mi 'Сложно сказать. По правде, мы с родителями собираемся как раз-таки уезжать туда, когда я здесь университет закончу.'
    thirty_five_grad_mi 'Но лично для меня никакой разницы. Что там я одна, что тут... {w}Блин, блин-блин, прости! Просто привыкла, что я вечно одиношенька, вот и ляпнула ерунду.'

    thirty_five_grad_alex 'Какая же ты милая, а. Удивляюсь, что у тебя никого нет. Но теперь догадываюсь, почему.'
    show 35grad_miku 2 laughter pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'А-а?'

    thirty_five_grad_alex 'Хоть в нашей жизни всё неоднозначно, но плохие люди не любят хороших.'

    'И я не вру. Хоть я и знаю Мику пару дней, но я уверен, что она ангел во плоти. Такой маленький, крохотный, и невинный.'
    'Который не то что ближнему своему, а паучку не навредит.'
    show 35grad_miku 2 normal pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Лёш, только ты так про меня говоришь. Только ты видишь меня такой. Веришь в меня... О! А вот и мой домик!'

    # (фон домика Мику и Лены ночной)
    scene bg thirty_five_grad_ext_house_of_un_night with dissolve
    # (музыка стоп)
    stop music fadeout 3
    'Он не особо выделялся среди прочих, кроме того, что в нём одном не горел свет. Значит, там никого нет? Или просто кто-то спит...'
    show 35grad_miku 2 fear pio ponytails at thirty_five_grad_night_lighting with dissolve:
        xalign 0.5
    thirty_five_grad_mi 'А? С т-тобой всё хорошо?'

    '...Только стоило обрадоваться, как за домиком увидел всю глубокую чёрную чащу леса... Обычно говорят, что долго смотря в глубину, то она начнёт потом глядеть в тебя.'
    'Так вот, эти люди не упоминают про лес. Вот тут тоже самое. Словно сейчас сами деревья выпустят в мою сторону свои корни и заберут к себе.'
    'А если присмотреться, то можно заметить, что словно кто-то смотрит прямо на меня...'
    '...А, нет, это просто чёртова сова...'

    thirty_five_grad_alex 'Д-да. Всё хорошо, просто показалось.'
    show 35grad_miku 2 normal pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Лёшенька, ты меня испугал... Но не волнуйся, ты меня защищаешь, и я тебя буду! Кстати, если что, я живу с Леной!'
    thirty_five_grad_mi 'Можешь приходить в гости, если что, но ты и так знаешь, где я обычно обитаю!'

    thirty_five_grad_alex 'Да, это уж точно!'

    'Нам вместе было хорошо. Надеюсь, что она чувствует то же самое. Я думал, что это у меня жизнь фигня и я особо никому не нужен, а оказывается...'

    thirty_five_grad_alex 'Спокойной ночи, Мику.'

    thirty_five_grad_mi 'Спокойной, Лёша...'

    'Нависла тишина, и даже она как будто давала сигнал, что пора что-то делать. Только думать долго не пришлось, так как руки сами, так и тянулись.'
    'Что это такое вообще? Так и должно быть? Не знаю и знать не хочу.'

    thirty_five_grad_alex 'Мику, ты не против, если мы... повторим?'

    # (музыка) Sergey Eybog - Meet Me There
    play music music_list ['meet_me_there'] fadein 3
    'Она даже не стала спрашивать, что именно. Забавно, но немного неразумно. Мы обнялись. Прямо как тогда, возле столовой.'
    'Так как она стояла на ступеньках, а я на земле, то мы немного выровнялись в росте, и теперь девушка спокойно могла спокойно положить свою голову мне на плечо.'

    'Её тело немного, но прижалось ко мне. Я ощущал это приятное тепло, которое нельзя передать словами...'

    '...Я просто наслаждался моментом. Одним из самых дорогих в человеческих отношениях.'
    'Где-то читал, что хватает и двадцати секунд для того, чтобы улучшить отношения между людьми. Надеюсь, это сработает и с нами.'
    show 35grad_miku 3 normal pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Лёш, а почему... Почему ты вообще решил так сделать тогда, перед столовой?'

    'Прошептала она мне на ушко. Забавно. Наверное, со стороны мы были похожи на любовников.'
    'Чёрт побери, у меня ощущение, словно я в романтическое аниме попал...'

    thirty_five_grad_alex 'Не знаю. Просто решил так сделать, чтобы потом не жалеть. А вообще, ответ так уж и нужен?'

    'Прошептал уже я. В ответ на что Мику, немного хихикнув, вышла из объятий. В её глазах, смотрящих на небо, читалось полная удовлетворённость жизнью.'

    thirty_five_grad_mi 'Это правда. Не всегда ответы приносят пользу. Но и без них нельзя чего-либо предпринимать.'

    thirty_five_grad_alex 'Ого, Мику! Да ты как стратег говоришь.'

    thirty_five_grad_mi 'Ну, мне иногда нравится думать наперёд! Ладушки, спасибо тебе за чудесный день, и ещё раз, спокойной ночи!'

    thirty_five_grad_alex 'Взаимно, Мику. Взаимно.'

    thirty_five_grad_mi 'Прошу тебя, иди осторожно, хорошо? В этой части лагеря освещение не очень, можешь споткнуться.'

    thirty_five_grad_alex 'Переживаешь как мама.'
    show 35grad_miku 2 laughter pio ponytails at thirty_five_grad_night_lighting with dspr
    thirty_five_grad_mi 'Конечно. Я ж не хочу тебе ничего плохого. Тем более, кто будет мне в клубе помогать? Ладно-ладно, шучу. До завтра!'

    # (пропадает спрайт Мику)
    hide 35grad_miku 2 laughter pio ponytails at thirty_five_grad_night_lighting with dspr
    'Перед тем, как закрыть дверь, она помахала мне на прощанье, как и я ей. А затем обернулся. Мику была права.'
    'Меня встретила хоть и не абсолютная, но всё равно густая темень. Такая не особо дружелюбная. Эх, был бы у меня фонарик...'

    # (музыка стоп)
    stop music fadeout 3
    # (затемнение (раньше это было обычное моргание))
    # (фон домика вожатой ночью)
    scene bg ext_house_of_mt_night with fade
    'Дорога до домика заняла у меня даже меньше времени, чем я рассчитывал.'
    'В нём всё ещё горел свет, а это значит только одно – меня либо ждут расспросы, либо ничего, так как Ольга могла просто выйти и оставить свет гореть специально для моего прихода.'
    'Но я на всякий случай постучался и получил положительный ответ.'

    # (фон внутри домика вожатой + спрайт Ольги в халате)
    scene bg int_house_of_mt_night with dissolve
    show 35grad_olga 2 normal paj at thirty_five_grad_night_lighting with dspr:
        xalign 0.5
    thirty_five_grad_mt 'О, Алексей. Вечер добрый.'

    thirty_five_grad_alex 'И вам.'

    'Вроде совсем обычное приветствие, но была некая доля напряжённости. И чтобы просто так не стоять у порога, я прошёл к своей постели, чтобы сесть и понять.'
    '...Как же я устал за день...'
    'Но затем вожатая вместо удивления сменила гримасу на раздражение:'

    # (спрайт злой Ольги в халате)
    show 35grad_olga 2 angry paj with dspr
    thirty_five_grad_mt 'Ничего не хочешь мне сказать?'

    thirty_five_grad_alex 'А должен?'

    thirty_five_grad_mt 'Как бы да, обязан. Почему ты так и не явился ко мне, когда тебя, Славя, попросила?'
    'Пускай Ольга и говорила без особой злости в голосе, но так или иначе читалось недовольство.'
    'Хотя, если подумать, то её можно понять, ведь на её месте я бы тоже злился.'

    thirty_five_grad_alex 'Простите меня, Ольга Дмитриевна. Вы меня работой нагрузили, да я и забыл про то, что к вам идти нужно. Так что вы не держите на меня зла?'

    'Я старался говорить максимально нежным тоном. Ведь вдруг мне повезёт? И это сработало! Почти.'

    # (спрайт Ольги обычной в халате)
    show 35grad_olga 2 normal paj with dspr
    thirty_five_grad_mt 'Ладно, горе ты моё луковое. Ложись спать, ведь завтра у тебя тяжёлый день будет.'

    'Вспоминая то, о чём меня попросили Мику и Славя, я не мог с этим спорить. Но, так или иначе, в голове стоял один важный вопрос:'

    thirty_five_grad_alex 'Ольга Дмитриевна, скажите, пожалуйста, что с моими родителями? Почему вы так резко потеряли настрой при их упоминании?'

    'И снова та же реакция. Что с утра.'

    thirty_five_grad_mt 'Давай оставим этот вопрос на утро, хорошо? Я устала.'

    'Я пожал плечами, потому что тут спорить абсолютно бесполезно. Так как она в это время уже стояла в халате, но не просила меня отвернуться. Уже хорошо.'

    # (пропадает спрайт Ольги)
    hide 35grad_olga 2 normal paj with dspr
    'После того, как я разделся, свет в домике погас, молниеносно утонув в темноте. Хорошо ещё, что в это время стоял недалеко от постели!'
    'Так что я лёг на неё, погрузившись в мир прекрасных грез.'

    # (затемнение (раньше это было обычное моргание))
    # (фон внутри домика вожатой в темноте)
    scene int_house_of_mt_night2 with dissolve
    'Вроде и устал, а сон так и не шёл. Поэтому вместо того, чтобы тупо смотреть в потолок, я вытащил свой рюкзак из-под кровати, расстегнул его.'
    'И тут я натурально пришёл в ужас...'

    # (музыка) Between August And December - Torture
    play music music_list['torture']
    '...Моё лицо обдал свежий, похожий на мартовский ветерок. Перед тем, как попасть сюда из того мира, был точно такой же. Клянусь!'
    'В итоге потянулся к телефону. Он был холодным, словно пролежал некоторое время на улице...'

    'Время было ещё раннее - десять часов вечера. И проценты зарядки никак не изменились... Мамочки...'

    '...И что я имею? В другом мире и во временной линии при этом, а так же то, что характеристика вещей сохранилась.'
    'На кой чёрт я вообще забиваю себе этим голову? Мне вообще завтра вставать как минимум в полпятого утра!'

    'Поэтому, застегнув рюкзак, я аккуратно кинул его обратно под кровать, укрылся ещё пока что свежим одеялом и уснул...'
    # (музыка стоп)
    # (закрытие глаз)
    stop music fadeout 2.0
    scene bg black at thirty_five_grad_vhs with fade
    $ persistent.day2 = True
    $ renpy.pause(1.0, hard=True)
    jump thirty_five_grad_day_three
