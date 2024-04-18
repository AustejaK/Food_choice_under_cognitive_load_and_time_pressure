# Food_choice_under_cognitive_load_and_time_pressure
 This is an oTree software for an experiment on food choice under cognitive load and time pressure.
 
 This study is a joint work with Youan Qian, Rudy Nayga Jr., and Simone Cerroni. This study was conducted as a part of EU Horizon 2020 project "COMFOCUS".
 
 In settings.py, please define:
 
     dict(
        name='comfocus_youan',
        display_name="Comfocus Youan Experiment",
        num_demo_participants=11,
        app_sequence=['comfocus_youan'],
        TREATMENT="C2",
    )
    
and 

    PARTICIPANT_FIELDS = ['treatment', 'pair', 'product', 'picture', 'calories', 'fat', 'saturated', 'carbohydrates', 'sugars', 'fibre', 'protein', 'salt', 'page_order', 'String', 'person', 'name', 'picture_n', 'picture_wg', 'picture_wl', 'weight']
