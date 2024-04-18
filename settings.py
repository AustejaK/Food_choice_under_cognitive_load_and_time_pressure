
from os import environ


SESSION_CONFIGS = [
    dict(
        name='LUT_course',
        display_name="LUT Behavioural Economics course (Limits of rationality + Risk & Uncertainty)",
        app_sequence=['behavioural_econ'],
        num_demo_participants=3,
        TREATMENT='RU7'
    ),
    # dict(
    #     name='visionary_feed_add',
    #     display_name="VISIONARY: essential oils for methane reduction",
    #     app_sequence=['visionary_feed_add'],
    #     num_demo_participants=5,
    #     TREATMENT='RBS',
    #     policy_mix='50'
    # ),
    # dict(
    #     name='LUT_course_2',
    #     display_name="LUT Behavioural Economics course (strategic interaction)",
    #     app_sequence=['behavioural_econ_2'],
    #     num_demo_participants=6,
    #     TREATMENT='SI1'
    # ),
    # dict(
    #     name='LUT_course_3',
    #     display_name="LUT Behavioural Economics course (strategic interaction - Weak Link game)",
    #     app_sequence=['behavioural_econ_weak_link'],
    #     num_demo_participants=3,
    #     TREATMENT='SI3'
    # ),
    # dict(
    #     name='LUT_course_4',
    #     display_name="LUT Behavioural Economics course (strategic interaction - PGG)",
    #     app_sequence=['public_goods_simple'],
    #     num_demo_participants=3,
    #     TREATMENT='SI6'
    # ),
    # dict(
    #     name='LUT_course_5',
    #     display_name="LUT Behavioural Economics course (strategic interaction - Trust game)",
    #     app_sequence=['trust'],
    #     num_demo_participants=4,
    #     TREATMENT='SI7'
    # ),
    # dict(
    #     name='smaller_group',
    #     display_name="Grouping for online experiments (grouping by arrival time + fallback to smaller group +"
    #                  "custom waiting screen)",
    #     app_sequence=['smaller_group_1', 'smaller_group_2', 'smaller_group_4', 'smaller_group_5'],
    #     num_demo_participants=10,
    # ),
    # dict(
    #     name='news_prosumers',
    #     display_name="news_prosumers_trial",
    #     app_sequence=['news_prosumers_1', 'news_prosumers_2', 'news_prosumers_3', 'news_prosumers_4',
    #                   'news_prosumers_5', 'news_prosumers_6'],
    #     num_demo_participants=5,
    #     TREATMENT='prosumer',
    #     prolific_link="link_1"
    # ),
    # dict(
    #     name='news_prosumers_test',
    #     display_name="news_prosumers_trial_specific",
    #     app_sequence=['news_prosumers_6'],
    #     num_demo_participants=5,
    #     prolific_link="link_1"
    # ),
    # dict(
    #     name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=4
    # )
    # dict(
    #     name='CM_full',
    #     display_name="CM full",
    #     num_demo_participants=12,
    #     app_sequence=['CM_consent', 'CM_instr', 'CM_trial_no_group',
    #                   'CM_DCE_1', 'CM_DCE_2', 'CM_CM_1', 'CM_survey',
    #                   'CM_final_no_group'],
    #     TREATMENT=9,
    #     completion_code ='CF3Q5H5K',
    #     exchange_pounds=0.88
    # ),
    # dict(
    #     name='methane_emissions',
    #     display_name="Methane emissions",
    #     num_demo_participants=1,
    #     app_sequence=['methane_emissions'],
    #     TREATMENT="new",
    # ),
    dict(
        name='comfocus_youan',
        display_name="Comfocus Youan Experiment",
        num_demo_participants=11,
        app_sequence=['comfocus_youan'],
        TREATMENT="C2",
    ),
    # dict(
    #     name='CM_trial',
    #     display_name="CM short",
    #     num_demo_participants=10,
    #     app_sequence=['CM_consent', 'CM_DCE_1', 'CM_DCE_2', 'CM_CM_1', 'CM_CM_2'],
    # ),
    # dict(
    #     name='CM_instructions_QSR',
    #     display_name="CM instructions (QSR-FR-AQ)",
    #     num_demo_participants=4,
    #     app_sequence=['CM_instructions_QSR'],
    #     TREATMENT=4,
    #     completion_code ='CODEXXXXXX',
    # ),
    # dict(
    #     name='CM_instructions_FR',
    #     display_name="CM instructions (FR-QSR-AQ)",
    #     num_demo_participants=4,
    #     app_sequence=['CM_instructions_FR'],
    #     TREATMENT=7,
    #     completion_code='CODEXXXXXX',
    # ),
    # dict(
    #     name='CM_instructions_AQ',
    #     display_name="CM instructions (AQ-QSR-FR)",
    #     num_demo_participants=4,
    #     app_sequence=['CM_instructions_AQ'],
    #     TREATMENT=9,
    #     completion_code='CODEXXXXXX',
    # ),
    # dict(
    #     name='CM_instructions_AQ_FR',
    #     display_name="CM instructions (AQ-FR-QSR)",
    #     num_demo_participants=4,
    #     app_sequence=['CM_instructions_AQ_FR'],
    #     TREATMENT=9,
    #     completion_code='CODEXXXXXX',
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
#
# PARTICIPANT_FIELDS = ['treatment_p', 'group_size', 'CE_choice_practice',
#                       'group_list_pred_A_practice', 'group_list_pred_B_practice', 'group_list_pred_C_practice',
#                       'id_resto', 'wait_page_arrival', 'waiting_time', 'past_group_id',
#                       'contador', 'replace_predictions_practice',
#                       'player_temp_AB', 'num_players',
#                       'group_pre_A', 'group_pre_B', 'group_pre_C', 'group_elec', 'random_choice',
#                       'Test_choices_A', 'Test_choices_B', 'Test_choices_C',
#                       'Test_choices_A_pred', 'Test_choices_B_pred', 'Test_choices_C_pred',
#                       'num_prob_replace', 'num_prob_not_replace', 'num_Test_choices_A_prob', 'num_Test_choices_B_prob',
#                       'num_Test_choices_C_prob', 'num_payoff_A_guess', 'num_payoff_B_guess', 'num_payoff_C_guess',
#                       'num_Test_choices_A_pred', 'num_Test_choices_B_pred', 'num_Test_choices_C_pred',
#                       'num_Test_payoff_a_pred', 'num_Test_payoff_b_pred', 'num_Test_payoff_c_pred',
#                       'random_choice_practice', 'task_rounds', 'screen_rounds', 'price_list', 'String',
#                       'mug_payoff', 'group_elec', 'predA', 'predB', 'predC',
#                       'CE_choice_1', 'CE_choice_2', 'CE_choice_3', 'CE_choice_4', 'CE_choice_5', 'CE_choice_6',
#                       'CE_choice_7', 'CE_choice_8', 'CE_choice_9', 'CE_choice_10',
#                       'list_choices_A', 'list_choices_B', 'list_choices_C',
#                       'group_list_pred_A', 'group_list_pred_B', 'group_list_pred_C', 'CE_choice',
#                       'replace_predictions', 'price_list_aux', 'is_dropout',
#                       'nome', 'via', 'aggiuntivo', 'cap', 'localita', 'provincia',
#                       'scenario_list', 'scenario_list_aux', 'num_rounds', 'surveys_rounds',
#                       'completion_code', 'exchange_pounds',
#                       'payoff1_a', 'payoff1_b', 'payoff1_c', 'payoff2_a', 'payoff2_b', 'payoff2_c',
#                       'payoff3_a', 'payoff3_b', 'payoff3_c', 'payoff4_a', 'payoff4_b', 'payoff4_c',
#                       'payoff5_a', 'payoff5_b', 'payoff5_c', 'payoff6_a', 'payoff6_b', 'payoff6_c',
#                       'payoff7_a', 'payoff7_b', 'payoff7_c', 'payoff8_a', 'payoff8_b', 'payoff8_c',
#                       'payoff9_a', 'payoff9_b', 'payoff9_c',
#                       'CE1_pred_A', 'CE1_pred_B', 'CE1_pred_C', 'CE2_pred_A', 'CE2_pred_B', 'CE2_pred_C',
#                       'CE3_pred_A', 'CE3_pred_B', 'CE3_pred_C', 'CE4_pred_A', 'CE4_pred_B', 'CE4_pred_C',
#                       'CE5_pred_A', 'CE5_pred_B', 'CE5_pred_C', 'CE6_pred_A', 'CE6_pred_B', 'CE6_pred_C',
#                       'CE7_pred_A', 'CE7_pred_B', 'CE7_pred_C', 'CE8_pred_A', 'CE8_pred_B', 'CE8_pred_C',
#                       'CE9_pred_A', 'CE9_pred_B', 'CE9_pred_C',
#                       'CE_choice_1_aux', 'CE_choice_2_aux', 'CE_choice_3_aux', 'CE_choice_4_aux', 'CE_choice_5_aux',
#                       'CE_choice_6_aux', 'CE_choice_7_aux', 'CE_choice_8_aux', 'CE_choice_9_aux', 'choice_aux',
#                       'cm_choice', 'dc_choice', 'substitute', 'AUX_rounds',
#                       'DC_rounds', 'page_order',
#                       'page_no_1', 'page_no_2', 'page_no_3', 'page_no_4', 'page_no_5',
#                       'page_no_6', 'page_no_7', 'page_no_8', 'page_no_9', 'page_no_10',
#                       'page_no_1aux', 'page_no_2aux', 'page_no_3aux', 'page_no_4aux', 'page_no_5aux',
#                       'page_no_6aux', 'page_no_7aux', 'page_no_8aux', 'page_no_9aux', 'page_no_10aux',
#                       'CM_predictions', 'group_size_2', 'dropout_mark',
#                       'q1_1', 'q1_2', 'q1_3', 'q2_1', 'q2_2', 'q2_3', 'q3_1', 'q3_2', 'q3_3', 'q1', 'q2', 'q3',
#                       'treatment']

# PARTICIPANT_FIELDS = ['news_list', 'tasks_1', 'tables_1', 'coins_1', 'RET_trial_value', 'RET_trial_country', 'expiry_1',
#                       'expiry_2',
#                       'tasks_2', 'tables_2', 'coins_2', 'RET_first_value', 'RET_first_country',
#                       'tasks_3', 'tables_3', 'coins_3', 'RET_second_value', 'RET_second_country',
#                       'secondgen', 'treatment', 'expiry_3',
#                       'info', 'read', 'stars', 'starspeople', 'comments', 'content', 'starsrating',
#                       'NEWS_bought_second', 'NEWS_total_cost', 'RET_first_correct', 'RET_second_correct',
#                       'RET_first_earnings', 'RET_second_earnings', 'GUESS_own_first_earnings',
#                       'GUESS_own_second_earnings', 'prolific_link', 'GUESS_own_first', 'GUESS_own_second',
#                       'GUESS_other_first', 'GUESS_other_second'
#                       ]

PARTICIPANT_FIELDS = ['treatment', 'pair', 'product', 'picture', 'calories', 'fat', 'saturated', 'carbohydrates',
                      'sugars', 'fibre', 'protein', 'salt', 'page_order', 'String', 'person', 'name', 'picture_n',
                      'picture_wg', 'picture_wl', 'weight']


SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'IT'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(
        name='experiment_room_1',
        display_name='Experiment room 1',
        participant_label_file='_rooms/experiment_room_1.txt',
    ),
    dict(
        name='experiment_room_2',
        display_name='Experiment room 2',
        participant_label_file='_rooms/experiment_room_2.txt',
    ),
    dict(
        name='experiment_room_3',
        display_name='Experiment room 3',
        participant_label_file='_rooms/experiment_room_3.txt',
    ),
    dict(
        name='experiment_room_4',
        display_name='Experiment room 4',
        participant_label_file='_rooms/experiment_room_4.txt',
    ),
    dict(
        name='experiment_room_5',
        display_name='Experiment room 5',
        participant_label_file='_rooms/experiment_room_5.txt',
    )
]

 

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

ADMIN_USERNAME = "admin"

SECRET_KEY = '6663459074285'

INSTALLED_APPS = ['otree']
