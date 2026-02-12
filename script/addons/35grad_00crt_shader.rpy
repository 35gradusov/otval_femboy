# https://devilspider.itch.io/crt-monitor-shader

#### CRT SHADER by Devil Spiδεr####
# This shader introduces a CRT-like effect shader that distorts a displayable in a fish-eye style. It also adds a scanline effect so it can mimic a CRT monitor.
# This takes four parameters: u_renpy_factor, u_renpy_scanlines, u_renpy_border and u_renpy_bcolor
#    u_renpy_factor (float) affects the curvature of the shader, with positive values curving the displayable towards the center and negative values doing the same but towards the edges.
#    u_renpy_scanlines (float) affects the intensity of the scanline effect. The best value is somewhere between 0.05 and 0.1 as too high values can cause pure blank'n'white stripes.
#    u_renpy_border (float) sets the intensity of the border relative to the displayable's size. This parameter is best used if you have a positive u_renpy_factor value, as it provides a smooth outline.
# I recommend setting this value to 0.01 for when this shader is applied to a full-screen displayable.
#    u_renpy_bcolor (tuple of 3 floats) sets the color of the border mentioned above. If you want to use a hex code, you can set this value to Color("#hexcode").rgb
# To apply the shader, copy the following transform template, replacing (thing) with the image you want to apply it to, changing the parameters as you see fit.
# show (thing):
#     mesh true
#     shader "akumo.crt"
#     u_renpy_factor 0.0 u_renpy_scanlines 0.0 u_renpy_border 0.0 u_renpy_bcolor Color("#000").rgb
# You don't need to copy the show (thing) line if you're defining it within a transform.
#
# I have also included a new convenience layer called "under" you can put images onto since applying the CRT shader onto a layer renders out a checkerboard pattern behind it.

init python:

    renpy.add_layer("under", below="master", menu_clear=False)
    renpy.register_shader("akumo.crt",variables="""
        uniform float u_time;
        uniform float u_renpy_factor;
        uniform float u_renpy_scanlines;
        uniform float u_renpy_border;
        uniform vec3 u_renpy_bcolor;
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
        varying vec2 v_andsize;
        varying vec4 v_pos;
        varying vec2 uv;
        attribute vec4 a_position;
    """,fragment_functions="""
        float radius(vec2 p)
        {
            return sqrt(pow(p.x-0.5,2.0)+pow(p.y-0.5,2.0));
        }
        vec2 zoom(vec2 p, float f)
        {
            return vec2(p.x-(p.x-0.5)*f,p.y-(p.y-0.5)*f);
        }
        vec2 distort(vec2 p, float f)
        {
            return zoom(p, radius(p)*f);
        }

        float border(float p, float f)
        {
            return clamp(-abs((p-0.5)/f)+(0.5/f)+1.0,0.0,1.0);
        }
    """, vertex_200 = """
        v_coords = a_tex_coord;
        v_andsize = u_model_size;
        v_pos = a_position;
        uv = v_pos.xy/v_andsize;
    """, fragment_300="""
        vec2 lens = distort(uv, -u_renpy_factor);
        vec4 tex = texture2D(tex0, lens);
        vec3 col = vec3(sin(v_andsize.x*u_time-v_andsize.y*lens.y)*u_renpy_scanlines);
        if ((lens.x > 1.0 || lens.x < 0.0)||(lens.y > 1.0 || lens.y < 0.0)){
            if (u_renpy_border==0.0){
                gl_FragColor = vec4(0.0);
            }else{
                float distance = border(lens.x,u_renpy_border)*border(lens.y,u_renpy_border);
                gl_FragColor = vec4(distance*u_renpy_bcolor, distance);
            }
        } else {
        gl_FragColor = vec4(tex + vec4(col*tex.a, tex.a));
        }
    """)
