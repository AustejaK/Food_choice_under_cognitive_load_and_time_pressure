# Food_choice_under_cognitive_load_and_time_pressure
 This is an oTree software for an experiment on food choice under cognitive load and time pressure.
 
 This study is a joint work with Youan Qian, Rudy Nayga Jr., and Simone Cerroni. This study was conducted as a part of EU Horizon 2020 project "COMFOCUS".
 
 In settings.py, please define:
 
     dict(
        name='comfocus_youan',
        display_name="Comfocus Experiment",
        num_demo_participants=10,
        app_sequence=['comfocus_youan'],
        TREATMENT="C2",
    )
    
and 

    PARTICIPANT_FIELDS = ['treatment', 'pair', 'product', 'picture', 'calories', 'fat', 'saturated', 'carbohydrates', 'sugars', 'fibre', 'protein', 'salt', 'page_order', 'String', 'person', 'name', 'picture_n', 'picture_wg', 'picture_wl', 'weight']


This study has 6 treatments that can be defined in settings.py:

        # Treatments:
        # C1 = control (with nutritional information)
        # T1 = treatment "high cognitive load" (with nutritional information)
        # T2 = treatment "high time pressure" (with nutritional information
        # C2 = control (with episodic future thinking)
        # T3 = treatment "high cognitive load" (with episodic future thinking)
        # T4 = treatment "high time pressure" (with episodic future thinking)
        
For episodic future thinking treatments, participants are defined in eft_list.csv and modified pictures are uploaded to _static/comfocus.
        