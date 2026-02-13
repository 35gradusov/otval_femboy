#https://makevisualnovels.itch.io/make-visual-novels-rspv1
#я удалил все комментарии автора, начинающиеся с '//', тк эта версия ренпая (7.4.11.2266) залупа полная

init python:


# Variables Section


    colorOperations ="""
    uniform vec4 u_color;
    """
    intensityOperations ="""
    uniform float u_intensity;
    """
    toggleMode = """
    uniform float u_mode;
    """
   
    commonVars ="""
    uniform float u_lod_bias;
    uniform sampler2D tex0;
    uniform float u_time;
    varying vec2 v_tex_coord;
    """
   
    aberrationVars="""
    uniform float u_aberrationAmount;
    """


    simulatedLightingVars ="""
        uniform vec3 u_back_light_color;
        uniform vec3 u_fill_light_color;
        uniform vec3 u_key_light_color; 
        uniform vec2 u_back_light_direction; 
        uniform vec2 u_back_light_position;
        uniform vec2 u_fill_light_direction; 
        uniform vec2 u_key_light_position; 
        uniform float u_back_light_intensity;
        uniform float u_fill_light_intensity;
        uniform float u_key_light_intensity; 
        uniform float u_key_light_radius; 
    """

    newSimLightVars = """
    uniform vec3 u_fill_light_color;
    uniform vec3 u_key_light_color;
    uniform vec2 u_key_light_position;
    uniform float u_fill_light_intensity; 
    uniform float u_key_light_intensity; 
    uniform float u_key_light_radius; 
    uniform vec2 u_rim_light_position;    
    uniform float u_rim_light_radius;     
    uniform float u_rim_light_intensity;  
    uniform vec3 u_rim_light_color;       

    """

    perlinShaderVars = """
    uniform float u_warpIntensity;
    uniform float u_flipIntensity;
    uniform float u_speed;
    uniform float u_scale;
    uniform float u_flipScale;
    uniform float u_flipSpeed;
    uniform float u_fps;
    uniform float u_minSmooth;
    uniform float u_maxSmooth;
    """

# Functions Section

    hsvFunctions = """
    vec3 rgb2hsv(vec3 c) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));


    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
    }


    vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }
    """

    perlinFunctions = """
    float rand(vec2 c)
    {
        return fract(sin(dot(c.xy, vec2(12.9898, 78.233))) *
                        43758.5453123);
    }

    float Perlin(vec2 x)
    {  
        vec2 index = floor(x);
        vec2 fractal = fract(x);
        float a = rand(index);
        float b = rand(index + vec2(1.0, 0.0));
        float c = rand(index + vec2(0.0, 1.0));
        float d = rand(index + vec2(1.0, 1.0));
        vec2 blur = fractal * fractal * (3.0 - 2.0 * fractal);
        return mix(a, b, blur.x) +
            (c - a) * blur.y * (1.0 - blur.x) +
            (d - b) * blur.x * blur.y;
    }


    vec2 Noise2D(vec2 uv, float frame)
    {
.


        vec2 q = vec2(0.0);
        q.x = Perlin(uv);
        q.y = Perlin(uv + 1.0);


        vec2 r = vec2(0.0);
        r.x = Perlin( uv + 1.0*q + vec2(1.7,9.2)+ 0.15 * frame );
        r.y = Perlin( uv + 1.0*q + vec2(8.3,2.8)+ 0.126 * frame);
        return clamp(r, 0.0, 1.0);
    }


    """


# Shader Meat


    aAberrationShader = """
        vec2 uv = v_tex_coord;        
        float offset =  cos(u_time * 1.3 * 3.14159) * (u_aberrationAmount * 0.001);
        vec2 redUV = uv + vec2(offset, 0.0);
        vec2 greenUV = uv;
        vec2 blueUV = uv - vec2(offset, 0.0);
        vec2 alphaUV = uv;


        vec4 red = texture2D(tex0, redUV, u_lod_bias);
        vec4 green = texture2D(tex0, greenUV, u_lod_bias);
        vec4 blue = texture2D(tex0, blueUV, u_lod_bias);
        vec4 alpha = texture2D(tex0, alphaUV, u_lod_bias);


        gl_FragColor = vec4(red.r, green.g, blue.b, alpha.a);
        """


    sAberationShader = """
        vec2 uv = v_tex_coord;        
        float offset =  u_aberrationAmount * 0.001;
        vec2 redUV = uv + vec2(offset, 0.0);
        vec2 greenUV = uv;
        vec2 blueUV = uv - vec2(offset, 0.0);
        vec2 alphaUV = uv;


        vec4 red = texture2D(tex0, redUV, u_lod_bias);
        vec4 green = texture2D(tex0, greenUV, u_lod_bias);
        vec4 blue = texture2D(tex0, blueUV, u_lod_bias);
        vec4 alpha = texture2D(tex0, alphaUV, u_lod_bias);


        gl_FragColor = vec4(red.r, green.g, blue.b, alpha.a);


    """
   
    colorDepth16Shader="""
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv, u_lod_bias);
        color.rgb = floor(color.rgb * 4.0) / 4.0;
        if (color.a == 0.0 ) discard;
        color += vec4(0.125,0.125,0.125, 0.0);
        color.rgb = floor(color.rgb * 8.0) / 8.0;
        gl_FragColor = color;
    """


    colorDepth256Shader="""
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv, u_lod_bias);
        color.rgb = floor(color.rgb * 8.0) / 8.0;
        gl_FragColor = color;
    """
   
    mangaStyleShader="""
        vec4 col = texture2D(tex0, v_tex_coord, u_lod_bias);
        if (col.a == 0.0) discard;
        vec3 hsv = rgb2hsv(col.rgb);
        if (hsv.z < u_intensity || hsv.y < 0.0025) {
        col *= vec4(0.01,0.01,0.01,1.0);
        } else {
        col= u_color;
        }
        gl_FragColor = col;
    """
   
    staticNoiseShader="""
        vec2 uv = v_tex_coord;
        vec4 colorShift = vec4(0.9, 0.7, 1.0, 1.0);
            uv.x += sin(u_time * 0.5) * 0.12;
            uv.y += cos(u_time * 0.5) * 0.11;
            vec4 color = texture2D(tex0, v_tex_coord, u_lod_bias) * u_color;
            float alpha = texture2D(tex0, v_tex_coord, u_lod_bias).a;
            float brightFactor = 1.0 - u_mode;
            float darkFactor = u_mode;
            float staticValue = alpha > 0.0 ? fract(sin(dot(v_tex_coord + u_time, vec2(12.9898, 78.233))) * 43758.5453) : 0.0;
            float noise = smoothstep(0.0, u_intensity, staticValue);


            color.rgb = ((color.rgb + noise * brightFactor) + (color.rgb * noise * darkFactor)) - color.rgb * (1.0 - brightFactor);
            gl_FragColor = vec4(color.r,color.g, color.b, color.a);
    """
   
    vhsShader="""
            vec2 uv = v_tex_coord;
            uv.x += sin(u_time * 0.5) * 0.12;
            uv.y += cos(u_time * 0.5) * 0.11;
            vec4 color = texture2D(tex0, v_tex_coord, u_lod_bias) * u_color;
            float scanline = fract(uv.y * 50.0) < 0.5 ? 0.95 : 1.0;
            color.rgb *= scanline;
            float alpha = texture2D(tex0, v_tex_coord, u_lod_bias).a;
            float noise = alpha > 0.0 ? fract(sin(dot(v_tex_coord + u_time, vec2(12.9898, 78.233))) * 43758.5453) : 0.0;
            color.rgb += noise * 0.1;
            gl_FragColor = vec4(color.r,color.g, color.b, color.a);
    """

    newSimLightingShader = """
    vec2 uv = v_tex_coord;
    vec4 color = texture2D(tex0, uv, u_lod_bias);
    if (color.a < 0.01) discard;
    float a0 = color.a;
    float a1 = texture2D(tex0, uv + vec2(0.008, 0.0)).a;
    float a2 = texture2D(tex0, uv - vec2(0.008, 0.0)).a;
    float a3 = texture2D(tex0, uv + vec2(0.0, 0.008)).a;
    float a4 = texture2D(tex0, uv - vec2(0.0, 0.008)).a;
    float alpha_gradient = max(
        abs(a0 - a1),
        max(abs(a0 - a2),
        max(abs(a0 - a3),
            abs(a0 - a4)))
    );
    float glow_width = 1.0;
    float edge_glow = smoothstep(0.0, glow_width, alpha_gradient);
    float dist_to_rim = distance(uv, u_rim_light_position);
    float rim_falloff = smoothstep(u_rim_light_radius * 0.7, u_rim_light_radius, dist_to_rim);
    float feather = smoothstep(0.0, 3.0, edge_glow);
    float falloff = pow(feather * (1.0 - rim_falloff), 0.5);
    vec3 rim_light = u_rim_light_color * falloff * u_rim_light_intensity;
    vec3 fill_light_contribution = u_fill_light_color * u_fill_light_intensity;
    float key_light_distance = distance(uv, u_key_light_position);
    float key_light_falloff = smoothstep(u_key_light_radius, 0.0, key_light_distance);
    vec3 key_light_contribution = u_key_light_color * key_light_falloff * u_key_light_intensity;
    vec3 final_color = (color.rgb + rim_light + fill_light_contribution + key_light_contribution) * color.a;
    gl_FragColor = vec4(final_color, color.a);
    """

    #This is the old simulated lighting shader with the whack backlight implementation.  I kept it around for now.
    simulatedLightingShader = """
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv, u_lod_bias);
        if(color.a < 0.01) discard; 
        float edge_factor = 1.0 - smoothstep(0.0, 0.05, min(uv.x, 1.0 - uv.x) * min(uv.y, 1.0 - uv.y));
        vec2 to_light = normalize(uv - u_back_light_position);
        float back_light = max(dot(to_light, u_back_light_direction), 0.0);
        vec3 back_light_contribution = u_back_light_color * back_light * u_back_light_intensity * edge_factor;
        vec3 fill_light_contribution = u_fill_light_color * u_fill_light_intensity;
        float key_light_distance = distance(uv, u_key_light_position);
        float key_light_intensity = smoothstep(u_key_light_radius, 0.0, key_light_distance);
        vec3 key_light_contribution = u_key_light_color * key_light_intensity * u_key_light_intensity;
        vec3 final_color = (color.rgb + fill_light_contribution + back_light_contribution + key_light_contribution) * color.a;
        gl_FragColor = vec4(final_color, color.a);
    """


    warpFragmentShader = """
    
    float frame = floor(u_time * (u_fps));
    vec2 uv = v_tex_coord.st;
    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);
    distort = distort * 2.0 - 1.0; 
    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
   

    float frameMod = step(mod(frame, 2.0), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
   

    invertDistort = invertDistort * 2. - 1.;  



    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
   

    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
provided settings.

, distort.y * 0.2 + 0.5);


sing the provided settings
with caution.

+ 0.5, invertDistort.y * 0.2 + 0.5, 1);


    gl_FragColor = color;
    """


    TakeOnMeFragmentShader = """



    float frame = floor(u_time * (u_fps));
   

    vec2 uv = v_tex_coord.st;



    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);


    distort = distort * 2.0 - 1.0;

    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
   

    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
   

    float frameMod = step(mod(frame, 2.0), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
   
  
    invertDistort = invertDistort * 2. - 1.;  

    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
   


    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
    
   
    if (color.a == 0.0) discard;
    vec3 hsv = rgb2hsv(color.rgb);


    if (hsv.z < u_intensity || hsv.y < 0.0025) {  
        color *= vec4(0.01,0.01,0.01,1.0);
    } else {
    color= u_color; 
}
    gl_FragColor = color;
    """


    #Shader Registration


    renpy.register_shader("MakeVisualNovels.PerlinWarp",
        variables=commonVars+perlinShaderVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,
        vertex_200="",
        fragment_300=warpFragmentShader)


    renpy.register_shader("MakeVisualNovels.AnimatedAberration",
        variables=commonVars+aberrationVars,
        vertex_functions="",
        fragment_functions="",
        vertex_200="",
        fragment_300=aAberrationShader)


    renpy.register_shader("MakeVisualNovels.StillAberration",
        variables=commonVars+aberrationVars,
        vertex_functions="",
        fragment_functions="",
        vertex_200="",
        fragment_300=sAberationShader)


    renpy.register_shader("MakeVisualNovels.256colors",
    variables=commonVars,
    vertex_functions="",
    fragment_functions="",
    vertex_200="",
    fragment_300=colorDepth256Shader)
   
    renpy.register_shader("MakeVisualNovels.16colors",
    variables=commonVars,
    vertex_functions="",
    fragment_functions="",
    vertex_200="",
    fragment_300=colorDepth16Shader)
   
    #lmao
    renpy.register_shader("MakeVisualNovels.TakeOnMe",
        variables=commonVars+perlinShaderVars+intensityOperations+colorOperations,
        vertex_functions="",
        fragment_functions=perlinFunctions+hsvFunctions,
        vertex_200="",
        fragment_300=TakeOnMeFragmentShader)
   
    renpy.register_shader("MakeVisualNovels.VHS",
        variables=commonVars+colorOperations,
        fragment_300=vhsShader)


    renpy.register_shader("MakeVisualNovels.Static",
        variables=commonVars+colorOperations+intensityOperations+toggleMode,
        fragment_300=staticNoiseShader)


    renpy.register_shader("MakeVisualNovels.OldSimulatedLighting",
        variables=commonVars+simulatedLightingVars,
        fragment_300=simulatedLightingShader)

    renpy.register_shader("MakeVisualNovels.Manga",
        variables=commonVars+intensityOperations+colorOperations,
        vertex_functions="",
        fragment_functions=hsvFunctions,
        vertex_200="",
        fragment_300=mangaStyleShader)

    renpy.register_shader("MakeVisualNovels.SimulatedLighting",
        variables=commonVars+newSimLightVars,
        fragment_300=newSimLightingShader)






