
init 999999999 python:

    renpy.display.screen.screens[("thirty_five_grad_nvl_old", None)]                = renpy.display.screen.screens[("nvl", None)]  
    renpy.display.screen.screens[("thirty_five_grad_main_menu_old", None)]          = renpy.display.screen.screens[("main_menu", None)]
    renpy.display.screen.screens[("thirty_five_grad_say_old", None)]                = renpy.display.screen.screens[("say", None)] 
    renpy.display.screen.screens[("thirty_five_grad_game_menu_selector_old", None)] = renpy.display.screen.screens[("game_menu_selector", None)]
    renpy.display.screen.screens[("thirty_five_grad_save_old", None)]               = renpy.display.screen.screens[("save", None)]              
    renpy.display.screen.screens[("thirty_five_grad_load_old", None)]               = renpy.display.screen.screens[("load", None)]      
    renpy.display.screen.screens[("thirty_five_grad_preferences_old", None)]        = renpy.display.screen.screens[("preferences", None)]  
    renpy.display.screen.screens[("thirty_five_grad_notify_old", None)]             = renpy.display.screen.screens[("notify", None)]
    renpy.display.screen.screens[("thirty_five_grad_skip_indicator_old", None)]     = renpy.display.screen.screens[("skip_indicator", None)]  
    renpy.display.screen.screens[("thirty_five_grad_quit_old", None)]               = renpy.display.screen.screens[("quit", None)]
    renpy.display.screen.screens[("thirty_five_grad_text_history_old", None)]       = renpy.display.screen.screens[("text_history_screen", None)]
        

        
init -1 python:

    def thirty_five_grad_screens_diactivate():
        config.window_title                                                                 = u"Бесконечное Лето"
        persistent._file_page                                                               = 1
        renpy.display.screen.screens[("main_menu", None)]                               = renpy.display.screen.screens[("thirty_five_grad_main_menu_old", None)]
        renpy.display.screen.screens[("nvl", None)]                                     = renpy.display.screen.screens[("thirty_five_grad_nvl_old", None)]
        renpy.display.screen.screens[("say", None)]                                     = renpy.display.screen.screens[("thirty_five_grad_say_old", None)]
        renpy.display.screen.screens[("game_menu_selector", None)]                      = renpy.display.screen.screens[("thirty_five_grad_game_menu_selector_old", None)]
        renpy.display.screen.screens[("save", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_save_old", None)]               
        renpy.display.screen.screens[("load", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_load_old", None)]               
        renpy.display.screen.screens[("preferences", None)]                             = renpy.display.screen.screens[("thirty_five_grad_preferences_old", None)]        
        renpy.display.screen.screens[("notify", None)]                                  = renpy.display.screen.screens[("thirty_five_grad_notify_old", None)]
        renpy.display.screen.screens[("skip_indicator", None)]                          = renpy.display.screen.screens[("thirty_five_grad_skip_indicator_old", None)]
        renpy.display.screen.screens[("quit", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_quit_old", None)]
        renpy.display.screen.screens[("text_history_screen", None)]                     = renpy.display.screen.screens[("thirty_five_grad_text_history_old", None)]
        config.mouse_displayable                                                        = persistent.thirty_five_grad_mouse_displayable_old 
        config.window_show_transition                                                   = persistent.thirty_five_grad_window_show_transition_old 
        config.window_hide_transition                                                   = persistent.thirty_five_grad_window_hide_transition_old
        config.exit_transition                                                          = persistent.thirty_five_grad_exit_transition_old
        preferences.text_cps                                                            = persistent.thirty_five_grad_text_speed_old



    def thirty_five_grad_screens_active():
        persistent._file_page                                                           = "thirty_five_grad_FilePage_game"
        config.window_title                                                             = u"re:35°"
        config.name                                                                     = "re:35°"
        renpy.display.screen.screens[("main_menu", None)]                               = renpy.display.screen.screens[("thirty_five_grad_main_menu", None)]
        renpy.display.screen.screens[("say", None)]                                     = renpy.display.screen.screens[("thirty_five_grad_adv", None)]
        renpy.display.screen.screens[("nvl", None)]                                     = renpy.display.screen.screens[("thirty_five_grad_nvl", None)]
        renpy.display.screen.screens[("notify", None)]                                  = renpy.display.screen.screens[("thirty_five_grad_notify", None)]
        renpy.display.screen.screens[("game_menu_selector", None)]                      = renpy.display.screen.screens[("thirty_five_grad_quick_menu", None)]
        renpy.display.screen.screens[("load", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_load", None)]
        renpy.display.screen.screens[("save", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_save", None)]
        renpy.display.screen.screens[("text_history", None)]                            = renpy.display.screen.screens[("thirty_five_grad_text_history", None)]
        renpy.display.screen.screens[("preferences", None)]                             = renpy.display.screen.screens[("thirty_five_grad_preferences", None)]
        renpy.display.screen.screens[("quit", None)]                                    = renpy.display.screen.screens[("thirty_five_grad_exit", None)]
        renpy.display.screen.screens[("skip_indicator", None)]                          = renpy.display.screen.screens[("thirty_five_grad_skip_indicator", None)]
        config.mouse_displayable                                                        = MouseDisplayable('images/gui/cursors/1.png',0,0)
        config.window_show_transition                                                   = Dissolve(0.5)
        config.window_hide_transition                                                   = Dissolve(0.5)
        config.exit_transition                                                          = Dissolve(0.5)
        preferences.text_cps                                                            = 48.967




    def thirty_five_grad_on_load_callback(slot):
        try:
            if persistent.thirty_five_grad_on_save_timeofday[slot]:
                _preferences.volumes['music']                                                   = persistent.thirty_five_grad_on_save_timeofday[slot][0]
                _preferences.volumes['sfx']                                                     = persistent.thirty_five_grad_on_save_timeofday[slot][1]
                _preferences.volumes['voice']                                                   = persistent.thirty_five_grad_on_save_timeofday[slot][2]
                _preferences.text_cps                                                           = persistent.thirty_five_grad_on_save_timeofday[slot][3]
                _preferences.fullscreen                                                         = persistent.thirty_five_grad_on_save_timeofday[slot][4]
                _preferences.skip_unseen                                                        = persistent.thirty_five_grad_on_save_timeofday[slot][5]
                _preferences.afm_enable                                                         = persistent.thirty_five_grad_on_save_timeofday[slot][6]
                _preferences.afm_time                                                           = persistent.thirty_five_grad_on_save_timeofday[slot][7]
                _preferences.transitions                                                        = int(persistent.thirty_five_grad_on_save_timeofday[slot][8])
        except:
            pass


    class thirty_five_grad_FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)


    def thirty_five_grad_on_save_callback(slot):
        if not persistent.thirty_five_grad_on_save_timeofday:
            persistent.thirty_five_grad_on_save_timeofday={}
        persistent.thirty_five_grad_on_save_timeofday[slot] = (
                                                        _preferences.volumes['music'], 
                                                        _preferences.volumes['sfx'], 
                                                        _preferences.volumes['voice'],
                                                        _preferences.text_cps,   
                                                        _preferences.fullscreen, 
                                                        _preferences.skip_unseen,
                                                        _preferences.afm_enable,
                                                        _preferences.afm_time,
                                                        _preferences.transitions
                                                        )



    import time


    def thirty_five_grad_time_def(st, at):
        named_tuple = time.localtime()
        img = Text(time.strftime("%H:%M:%S", named_tuple), style="thirty_five_grad_digital_counter_7_italic", size=64, text_align=1.0, xalign=1.0, color='#001919', alpha=241)
        return img, .1


    def thirty_five_grad_date_def(st, at):
        named_tuple = time.localtime()
        img = Text(time.strftime("%m.%d.%Y", named_tuple), style="thirty_five_grad_digital_counter_7_italic", size=64, text_align=1.0, xalign=1.0, color='#001919', alpha=241)
        return img, .1

    def thirty_five_grad_day_def(st, at):
        named_tuple = time.localtime()
        if time.strftime("%a", named_tuple)   == 'Mon':
            cur_day = 'ПОНЕДЕЛЬНИК'
        elif time.strftime("%a", named_tuple) == 'Tue':
            cur_day = 'ВТОРНИК'
        elif time.strftime("%a", named_tuple) == 'Wed':
            cur_day = 'СРЕДА'
        elif time.strftime("%a", named_tuple) == 'Thu':
            cur_day = 'ЧЕТВЕРГ'
        elif time.strftime("%a", named_tuple) == 'Fri':
            cur_day = 'ПЯТНИЦА'
        elif time.strftime("%a", named_tuple) == 'Sat':
            cur_day = 'СУББОТА'
        elif time.strftime("%a", named_tuple) == 'Sun':
            cur_day = 'ВОСКРЕСЕНЬЕ'

        img = Text(cur_day, style="thirty_five_grad_digital_counter_7_italic", text_align=1.0, xalign=1.0, color='#001919', alpha=241)
        return img, .1
        


    def thirty_five_grad_get_image(file):
        return "images/%s" % (file)



    def thirty_five_grad_hide_hint_appeared():
        persistent.thirty_five_grad_hide_hint = True

    def thirty_five_grad_save_hint_appeared():
        persistent.thirty_five_grad_save_hint = True


    def thirty_five_grad_blur_disable_def():
        persistent.thirty_five_grad_blur_pref = False

    def thirty_five_grad_blur_enable_def(): 
        persistent.thirty_five_grad_blur_pref = True

    def thirty_five_grad_stop_skip():
        config.skipping = False







        

    
