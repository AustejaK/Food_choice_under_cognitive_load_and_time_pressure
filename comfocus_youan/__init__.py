import random

from otree.api import *


doc = """
This is a software for a study on food choice under cognitive load and time pressure.
Author: Austėja Kažemekaitytė (University of Trento), a.kazemekaityte@unitn.it
Joint work with Youan Qian, Rudy Nayga Jr., and Simone Cerroni
"""


class C(BaseConstants):
    NAME_IN_URL = 'comfocus_youan'
    PLAYERS_PER_GROUP = None
    tasks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    NUM_ROUNDS = len(tasks)
    participation = cu(7)
    bonus = cu(3)
    time = 30
    memorization = 10
    memorization_2 = 20
    time_pressure = 10
    kilos = 15


class Subsession(BaseSubsession):
    pass

class Products(ExtraModel):
    pair = models.IntegerField()
    product = models.StringField()
    picture = models.StringField()
    calories = models.StringField()
    fat = models.StringField()
    saturated = models.StringField()
    carbohydrates = models.StringField()
    sugars = models.StringField()
    fibre = models.StringField()
    protein = models.StringField()
    salt = models.StringField()


class Pictures(ExtraModel):
    person = models.IntegerField()
    name = models.StringField()
    picture_n = models.StringField()
    picture_wl = models.StringField()
    picture_wg = models.StringField()


def creating_session(subsession: Subsession):
    # random_draw = 1
    # or
     random_draw = random.randint(1, len(C.tasks))

    rows = read_csv(__name__ + '/products.csv', Products)
    number_products = len(rows)

    pair = []
    product = []
    picture = []
    calories = []
    fat = []
    saturated = []
    carbohydrates = []
    sugars = []
    fibre = []
    protein = []
    salt = []

    for i in range(0, number_products):
        pair.append(rows[i]['pair'])
        product.append(rows[i]['product'])
        picture.append(rows[i]['picture'])
        calories.append(rows[i]['calories'])
        fat.append(rows[i]['fat'])
        saturated.append(rows[i]['saturated'])
        carbohydrates.append(rows[i]['carbohydrates'])
        sugars.append(rows[i]['sugars'])
        fibre.append(rows[i]['fibre'])
        protein.append(rows[i]['protein'])
        salt.append(rows[i]['salt'])

    rows2 = read_csv(__name__ + '/eft_list.csv', Pictures)
    number_pictures = len(rows2)

    person = []
    name = []
    picture_n = []
    picture_wl = []
    picture_wg = []

    for i in range(0, number_pictures):
        person.append(rows2[i]['person'])
        name.append(rows2[i]['name'])
        picture_n.append(rows2[i]['picture_n'])
        picture_wl.append(rows2[i]['picture_wl'])
        picture_wg.append(rows2[i]['picture_wg'])

    for p in subsession.get_players():
        p.participant.pair = pair
        p.participant.product = product
        p.participant.picture = picture
        p.participant.calories = calories
        p.participant.fat = fat
        p.participant.saturated = saturated
        p.participant.carbohydrates = carbohydrates
        p.participant.sugars = sugars
        p.participant.fibre = fibre
        p.participant.protein = protein
        p.participant.salt = salt
        p.participant.person = person
        p.participant.name = name
        p.participant.picture_n = picture_n
        p.participant.picture_wl = picture_wl
        p.participant.picture_wg = picture_wg

        rounds_1 = list(range(1, len(C.tasks) + 1))
        rounds_total = rounds_1
        random.shuffle(rounds_1)
        rounds_order = C.tasks
        p.participant.page_order = dict(zip(rounds_order, rounds_total))
        p.participant.num_rounds = C.NUM_ROUNDS

        p.participant.weight = random.randint(0, 1)

        p.participant.random_draw = random_draw
        p.treatment = subsession.session.config['TREATMENT']
        # Treatments:
        # C1 = control (with nutritional information)
        # T1 = treatment "high cognitive load" (with nutritional information)
        # T2 = treatment "high time pressure" (with nutritional information
        # C2 = control (with episodic future thinking)
        # T3 = treatment "high cognitive load" (with episodic future thinking)
        # T4 = treatment "high time pressure" (with episodic future thinking)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()
    consent = models.BooleanField(choices=[[1, "Acconsento a partecipare a questo studio"]], widget=widgets.RadioSelect,
                                  label="")
    accept = models.BooleanField(choices=[1], widget=widgets.RadioSelect,
                                  label="")
    page_consent = models.IntegerField()

    choice_trial = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    sequence_trial = models.IntegerField()
    memo_trial = models.StringField(label="", min_length=7, max_length=7)

    choice_1 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_2 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_3 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_4 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_5 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_6 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_7 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_8 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_9 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_10 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_11 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])
    choice_12 = models.BooleanField(widget=widgets.RadioSelect, choices=[0,1])

    choice_1_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_2_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_3_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_4_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_5_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_6_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_7_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_8_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_9_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_10_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_11_memo = models.StringField(label="", min_length=7, max_length=7)
    choice_12_memo = models.StringField(label="", min_length=7, max_length=7)

    choice_1_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_2_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_3_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_4_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_5_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_6_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_7_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_8_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_9_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_10_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_11_memo_ans = models.StringField(label="", min_length=7, max_length=7)
    choice_12_memo_ans = models.StringField(label="", min_length=7, max_length=7)

    choice_1_timeout = models.BooleanField(default=False)
    choice_2_timeout = models.BooleanField(default=False)
    choice_3_timeout = models.BooleanField(default=False)
    choice_4_timeout = models.BooleanField(default=False)
    choice_5_timeout = models.BooleanField(default=False)
    choice_6_timeout = models.BooleanField(default=False)
    choice_7_timeout = models.BooleanField(default=False)
    choice_8_timeout = models.BooleanField(default=False)
    choice_9_timeout = models.BooleanField(default=False)
    choice_10_timeout = models.BooleanField(default=False)
    choice_11_timeout = models.BooleanField(default=False)
    choice_12_timeout = models.BooleanField(default=False)

    age = models.IntegerField(min=1920, max=2024, label="1.	Il tuo anno di nascita:")
    gender = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "M"], [1, "F"]], label="2. Sesso")
    education = models.IntegerField(widget=widgets.RadioSelect,
                                    choices=[
                                        [0, "Scuola elementare"],
                                        [1, "Diploma di Scuola media"],
                                        [2, "Diploma di scuola superiore o equivalente"],
                                        [3, "Laurea triennale"],
                                        [4, "Laurea magistrale(o a ciclo unico)"],
                                        [5, "Dottorato"],
                                        [6, "Diploma di specializzazione"]],
                                        label="3. Qual è il livello più alto di istruzione che hai conseguito?")
    income = models.IntegerField(label="4.	Qual è stato il reddito annuo del tuo nucleo familiare nel 2023?")
    sport = models.IntegerField(choices=[
                                        [0, "Mai "],
                                        [1, "Una volta al mese"],
                                        [2, "Una volta alla settimana"],
                                        [3, "2-3 volte a settimana"],
                                        [4, "4-6 volte a settimana "],
                                        [5, "Una volta al giorno "],
                                        [6, "Più di una volta al giorno "]
    ], label="5. Quanto spesso fai attività fisica? (Includi solo i periodi di attività fisica superiori a 20 minuti).")
    smoker = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "Sì"], [1, "No"]], label="6. Sono un fumatore:")
    smoker_2 = models.IntegerField(blank=True, label="6.1 Se sì, indichi il numero di sigarette che consumi quotidianamente.")
    smoker_3 = models.BooleanField(blank=True, label="6.2 Hai fumato di recente, nelle ultime due ore?")
    alcohol = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "Sì"], [1, "No"]], label="7. Consumo di bevande alcoliche:")
    alcohol_2 = models.IntegerField(widget=widgets.RadioSelect, label="7.1 Hai bevuto bevande alcoliche nelle ultime 24 ore?", choices=[[0, "Sì"], [1, "No"]])
    caffeine = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "Sì"], [1, "No"]], label="8. Hai bevuto bevande contenenti caffeina o teina nelle ultime 4 ore?")
    sleep = models.IntegerField(label="9. Quante ore hai dormito la notte scorsa?")
    breakfast = models.IntegerField(label="10. Quanti giorni alla settimana fai colazione?",
                                    choices=[
                                        [0, "0 giorni"],
                                        [1, "1 giorno"],
                                        [2, "2 giorni"],
                                        [3, "3 giorni"],
                                        [4, "4 giorni"],
                                        [5, "5 giorni"],
                                        [6, "6 giorni"],
                                        [7, "7  giorni"]
    ])
    last_meal = models.StringField(label="11. A che ora hai mangiato l'ultimo pasto oggi?")
    hunger = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[
        [1, "1 - per niente affamato/a"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5"],
        [6, "6"],
        [7, "7"],
        [8, "8"],
        [9, "9 - Estremamente affamato/a"]
    ],
                                 label="12. Indichi, su una scala da 1 a 9, lo stato di fame all'inizio della sessione (1 = per niente affamato/a; 9 = Estremamente affamato/a).")
    health = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "Sì"], [1, "No"]], label="13. Hai gravi problemi di salute?")
    medicines = models.BooleanField(widget=widgets.RadioSelect, choices=[[0, "Sì"], [1, "No"]], label="14. Stai usando dei farmaci?")
    medicines_2 = models.LongStringField(label="14.1 Se sì, si prega di indicare i nomi dei farmaci.", blank=True)
    labels = models.BooleanField(widget=widgets.RadioSelectHorizontal, choices=[[0, "Sì"], [1, "No"]],
                                 label="Di solito leggi le etichette nutrizionali?", blank=True)
    attention = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[
        [1, "1 - per niente"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5 - massima attenzione"]
    ], label="Quanta attenzione hai prestato alle etichette nutrizionali in questo studio? ", blank=True)
    attention_2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[
        [1, "1 - per niente"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5 - massima attenzione"]
    ], label="Quanta attenzione hai prestato alle tue foto in questo studio? ", blank=True)
    time_pressure = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[
        [1, "1 - senza pressione"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5 - sotto massima pressione"]
    ], label="Quanto sei sentita/o sotto pressione temporale quando hai fatto delle scelte alimentari?", blank=True)
    cognitive_load = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[
        [1, "1 - nessuno sforzo"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5 - massimo sforzo"]
    ], label="Quanto impegno hai messo nel memorizzare i numeri ogni volta?", blank=True)
    comments = models.LongStringField(label="Commenti e suggerimenti:")

    prod1 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod2 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod3 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod4 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod5 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod6 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod7 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod8 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod9 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod10 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod11 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod12 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod13 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod14 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod15 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod16 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod17 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod18 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod19 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod20 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod21 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod22 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod23 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])
    prod24 = models.IntegerField(blank=True, label="", choices=[[1, 'Sì']])


    #Page times
    page_1 = models.StringField()
    page_2 = models.StringField()
    page_3 = models.StringField()
    page_4 = models.StringField()
    page_5 = models.StringField()
    page_6 = models.StringField()
    page_6_2 = models.StringField()
    page_7 = models.StringField()
    page_8 = models.StringField()
    page_9 = models.StringField()
    page_10 = models.StringField()
    page_11 = models.StringField()
    page_12 = models.StringField()
    page_13_0 = models.StringField()
    page_13 = models.StringField()
    page_14 = models.StringField()
    page_14_memo = models.StringField()
    page_14_memo_answer = models.StringField()
    page_15 = models.StringField()
    page_16 = models.StringField()
    page_17 = models.StringField()
    page_18 = models.StringField()
    page_18_memo = models.StringField()
    page_18_memo_ans = models.StringField()
    page_19 = models.StringField()
    page_19_memo = models.StringField()
    page_19_memo_ans = models.StringField()
    page_20 = models.StringField()
    page_20_memo = models.StringField()
    page_20_memo_ans = models.StringField()
    page_21 = models.StringField()
    page_21_memo = models.StringField()
    page_21_memo_ans = models.StringField()
    page_22 = models.StringField()
    page_22_memo = models.StringField()
    page_22_memo_ans = models.StringField()
    page_23 = models.StringField()
    page_23_memo = models.StringField()
    page_23_memo_ans = models.StringField()
    page_24 = models.StringField()
    page_24_memo = models.StringField()
    page_24_memo_ans = models.StringField()
    page_25 = models.StringField()
    page_25_memo = models.StringField()
    page_25_memo_ans = models.StringField()
    page_26 = models.StringField()
    page_26_memo = models.StringField()
    page_26_memo_ans = models.StringField()
    page_27 = models.StringField()
    page_27_memo = models.StringField()
    page_27_memo_ans = models.StringField()
    page_28 = models.StringField()
    page_28_memo = models.StringField()
    page_28_memo_ans = models.StringField()
    page_29 = models.StringField()
    page_29_memo = models.StringField()
    page_29_memo_ans = models.StringField()
    page_30 = models.StringField()
    page_30_memo = models.StringField()
    page_30_memo_ans = models.StringField()
    page_31 = models.StringField()
    page_31_memo = models.StringField()
    page_31_memo_ans = models.StringField()
    page_32 = models.StringField()
    page_32_memo = models.StringField()
    page_32_memo_ans = models.StringField()
    page_33 = models.StringField()
    page_33_memo = models.StringField()
    page_33_memo_ans = models.StringField()
    page_34 = models.StringField()
    page_34_memo = models.StringField()
    page_34_memo_ans = models.StringField()
    page_35 = models.StringField()
    page_35_memo = models.StringField()
    page_35_memo_ans = models.StringField()
    page_36 = models.StringField()
    page_36_memo = models.StringField()
    page_36_memo_ans = models.StringField()
    page_37 = models.StringField()
    page_37_memo = models.StringField()
    page_37_memo_ans = models.StringField()
    page_38 = models.StringField()
    page_38_memo = models.StringField()
    page_38_memo_ans = models.StringField()
    page_39 = models.StringField()
    page_39_memo = models.StringField()
    page_39_memo_ans = models.StringField()
    page_40 = models.StringField()
    page_40_memo = models.StringField()
    page_40_memo_ans = models.StringField()
    page_41 = models.StringField()
    page_41_memo = models.StringField()
    page_41_memo_ans = models.StringField()
    page_42 = models.StringField()
    page_43 = models.StringField()
    page_44 = models.StringField()
    page_45 = models.StringField()
    page_46 = models.StringField()
    page_47 = models.StringField()
    page_48 = models.StringField()
    page_49 = models.StringField()
    page_50 = models.StringField()


# PAGES
class Consent(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['consent']

class Privacy(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['accept']

class Blank_no_time(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_1 = str(time.time_ns())


class EDA_calibration(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_2 = str(time.time_ns())

class EDA_calibration_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_3 = str(time.time_ns())


class EDA_calibration_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    timeout_seconds = 60*4

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_4 = str(time.time_ns())


# Instructions
class Instructions_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_5 = str(time.time_ns())

class Instructions_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_6 = str(time.time_ns())

class Instructions_2_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_6_2 = str(time.time_ns())

class Instructions_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_7 = str(time.time_ns())

class Instructions_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_8 = str(time.time_ns())

class Instructions_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_9 = str(time.time_ns())

class Instructions_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_10 = str(time.time_ns())

class Instructions_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_11 = str(time.time_ns())

# Trial
class Trial_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_12 = str(time.time_ns())

class Trial_2_memo(Page):
    timeout_seconds = C.memorization
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == "T1" or\
               player.round_number == 1 and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.sequence_trial = sequence_trial
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_14_memo = str(time.time_ns())

class Trial_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_14 = str(time.time_ns())

    form_model = 'player'
    form_fields = ['choice_trial']

class Trial_2_memo_answer(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == "T1" or\
               player.round_number == 1 and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['memo_trial']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_14_memo_answer = str(time.time_ns())
        if player.memo_trial == str(player.sequence_trial):
            print("won bonus")
        else:
            print("no bonus")

# Task
class Task_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_16 = str(time.time_ns())

class Task_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_17 = str(time.time_ns())



# Blank pages
class Blank_0(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == "T1" or \
               player.round_number == 1 and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_13_0 = str(time.time_ns())

class Blank_1(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_13 = str(time.time_ns())

class Blank_2(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_15 = str(time.time_ns())

class Blank_3(Page):
    timeout_seconds = 5
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_18 = str(time.time_ns())

class Blank_3_memo(Page):
    timeout_seconds = 5
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1'] and player.treatment == "T1" \
               or player.round_number == player.participant.page_order['1'] and player.treatment == "T3"


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_18_memo = str(time.time_ns())

class Blank_3_memo_ans(Page):
    timeout_seconds = 5
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1'] and player.treatment == "T1" \
               or player.round_number == player.participant.page_order['1'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_18_memo_ans = str(time.time_ns())

class Blank_4(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_20 = str(time.time_ns())

class Blank_4_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2']  and player.treatment == "T1" \
               or player.round_number == player.participant.page_order['2'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_20_memo = str(time.time_ns())

class Blank_4_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2'] and player.treatment == "T1" \
               or player.round_number == player.participant.page_order['2'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_20_memo_ans = str(time.time_ns())

class Blank_5(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_22 = str(time.time_ns())

class Blank_5_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3'] and player.treatment == "T1" \
               or player.round_number == player.participant.page_order['3'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_22_memo = str(time.time_ns())

class Blank_5_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['3'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_22_memo_ans = str(time.time_ns())

class Blank_6(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_24 = str(time.time_ns())

class Blank_6_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['4'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_24_memo = str(time.time_ns())

class Blank_6_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['4'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_24_memo_ans = str(time.time_ns())

class Blank_7(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_26 = str(time.time_ns())

class Blank_7_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['5'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_26_memo = str(time.time_ns())

class Blank_7_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['5'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_26_memo_ans = str(time.time_ns())

class Blank_8(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_28 = str(time.time_ns())

class Blank_8_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['6'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_28_memo = str(time.time_ns())

class Blank_8_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['6'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_28_memo_ans = str(time.time_ns())

class Blank_9(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_30 = str(time.time_ns())

class Blank_9_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['7'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_30_memo = str(time.time_ns())

class Blank_9_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['7'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_30_memo_ans = str(time.time_ns())

class Blank_10(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_32 = str(time.time_ns())

class Blank_10_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['8'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_32_memo = str(time.time_ns())

class Blank_10_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['8'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_32_memo_ans = str(time.time_ns())

class Blank_11(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_34 = str(time.time_ns())

class Blank_11_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['9'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_34_memo = str(time.time_ns())

class Blank_11_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['9'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_34_memo_ans = str(time.time_ns())

class Blank_12(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_36 = str(time.time_ns())

class Blank_12_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['10'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_36_memo = str(time.time_ns())

class Blank_12_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['10'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_36_memo_ans = str(time.time_ns())

class Blank_13(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_38 = str(time.time_ns())

class Blank_13_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['11'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_38_memo = str(time.time_ns())

class Blank_13_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['11'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_38_memo_ans = str(time.time_ns())

class Blank_14(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_40 = str(time.time_ns())

class Blank_14_memo(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['12'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_40_memo = str(time.time_ns())

class Blank_14_memo_ans(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['12'] and player.treatment == "T3"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_40_memo_ans = str(time.time_ns())

class Blank_15(Page):
    timeout_seconds = 5

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_42 = str(time.time_ns())


# Choices
class Choice_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_1']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[0]
        picture_2 = player.participant.picture[1]
        product_1 = player.participant.product[0]
        product_2 = player.participant.product[1]
        calories_1 = player.participant.calories[0]
        calories_2 = player.participant.calories[1]
        fat_1 = player.participant.fat[0]
        fat_2 = player.participant.fat[1]
        saturated_1 = player.participant.saturated[0]
        saturated_2 = player.participant.saturated[1]
        carbohydrates_1 = player.participant.carbohydrates[0]
        carbohydrates_2 = player.participant.carbohydrates[1]
        sugars_1 = player.participant.sugars[0]
        sugars_2 = player.participant.sugars[1]
        fibre_1 = player.participant.fibre[0]
        fibre_2 = player.participant.fibre[1]
        protein_1 = player.participant.protein[0]
        protein_2 = player.participant.protein[1]
        salt_1 = player.participant.salt[0]
        salt_2 = player.participant.salt[1]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_19 = str(time.time_ns())
        if timeout_happened:
            player.choice_1 = 0
            player.choice_1_timeout = True


class Choice_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_2']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[2]
        picture_2 = player.participant.picture[3]
        product_1 = player.participant.product[2]
        product_2 = player.participant.product[3]
        calories_1 = player.participant.calories[2]
        calories_2 = player.participant.calories[3]
        fat_1 = player.participant.fat[2]
        fat_2 = player.participant.fat[3]
        saturated_1 = player.participant.saturated[2]
        saturated_2 = player.participant.saturated[3]
        carbohydrates_1 = player.participant.carbohydrates[2]
        carbohydrates_2 = player.participant.carbohydrates[3]
        sugars_1 = player.participant.sugars[2]
        sugars_2 = player.participant.sugars[3]
        fibre_1 = player.participant.fibre[2]
        fibre_2 = player.participant.fibre[3]
        protein_1 = player.participant.protein[2]
        protein_2 = player.participant.protein[3]
        salt_1 = player.participant.salt[2]
        salt_2 = player.participant.salt[3]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_21 = str(time.time_ns())
        if timeout_happened:
            player.choice_2 = 0
            player.choice_2_timeout = True


class Choice_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2"  or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_3']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[4]
        picture_2 = player.participant.picture[5]
        product_1 = player.participant.product[4]
        product_2 = player.participant.product[5]
        calories_1 = player.participant.calories[4]
        calories_2 = player.participant.calories[5]
        fat_1 = player.participant.fat[4]
        fat_2 = player.participant.fat[5]
        saturated_1 = player.participant.saturated[4]
        saturated_2 = player.participant.saturated[5]
        carbohydrates_1 = player.participant.carbohydrates[4]
        carbohydrates_2 = player.participant.carbohydrates[5]
        sugars_1 = player.participant.sugars[4]
        sugars_2 = player.participant.sugars[5]
        fibre_1 = player.participant.fibre[4]
        fibre_2 = player.participant.fibre[5]
        protein_1 = player.participant.protein[4]
        protein_2 = player.participant.protein[5]
        salt_1 = player.participant.salt[4]
        salt_2 = player.participant.salt[5]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_23 = str(time.time_ns())
        if timeout_happened:
            player.choice_3 = 0
            player.choice_3_timeout = True


class Choice_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_4']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[6]
        picture_2 = player.participant.picture[7]
        product_1 = player.participant.product[6]
        product_2 = player.participant.product[7]
        calories_1 = player.participant.calories[6]
        calories_2 = player.participant.calories[7]
        fat_1 = player.participant.fat[6]
        fat_2 = player.participant.fat[7]
        saturated_1 = player.participant.saturated[6]
        saturated_2 = player.participant.saturated[7]
        carbohydrates_1 = player.participant.carbohydrates[6]
        carbohydrates_2 = player.participant.carbohydrates[7]
        sugars_1 = player.participant.sugars[6]
        sugars_2 = player.participant.sugars[7]
        fibre_1 = player.participant.fibre[6]
        fibre_2 = player.participant.fibre[7]
        protein_1 = player.participant.protein[6]
        protein_2 = player.participant.protein[7]
        salt_1 = player.participant.salt[6]
        salt_2 = player.participant.salt[7]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_25 = str(time.time_ns())
        if timeout_happened:
            player.choice_4 = 0
            player.choice_4_timeout = True


class Choice_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_5']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[8]
        picture_2 = player.participant.picture[9]
        product_1 = player.participant.product[8]
        product_2 = player.participant.product[9]
        calories_1 = player.participant.calories[8]
        calories_2 = player.participant.calories[9]
        fat_1 = player.participant.fat[8]
        fat_2 = player.participant.fat[9]
        saturated_1 = player.participant.saturated[8]
        saturated_2 = player.participant.saturated[9]
        carbohydrates_1 = player.participant.carbohydrates[8]
        carbohydrates_2 = player.participant.carbohydrates[9]
        sugars_1 = player.participant.sugars[8]
        sugars_2 = player.participant.sugars[9]
        fibre_1 = player.participant.fibre[8]
        fibre_2 = player.participant.fibre[9]
        protein_1 = player.participant.protein[8]
        protein_2 = player.participant.protein[9]
        salt_1 = player.participant.salt[8]
        salt_2 = player.participant.salt[9]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_27 = str(time.time_ns())
        if timeout_happened:
            player.choice_5 = 0
            player.choice_5_timeout = True


class Choice_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_6']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[10]
        picture_2 = player.participant.picture[11]
        product_1 = player.participant.product[10]
        product_2 = player.participant.product[11]
        calories_1 = player.participant.calories[10]
        calories_2 = player.participant.calories[11]
        fat_1 = player.participant.fat[10]
        fat_2 = player.participant.fat[11]
        saturated_1 = player.participant.saturated[10]
        saturated_2 = player.participant.saturated[11]
        carbohydrates_1 = player.participant.carbohydrates[10]
        carbohydrates_2 = player.participant.carbohydrates[11]
        sugars_1 = player.participant.sugars[10]
        sugars_2 = player.participant.sugars[11]
        fibre_1 = player.participant.fibre[10]
        fibre_2 = player.participant.fibre[11]
        protein_1 = player.participant.protein[10]
        protein_2 = player.participant.protein[11]
        salt_1 = player.participant.salt[10]
        salt_2 = player.participant.salt[11]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_29 = str(time.time_ns())
        if timeout_happened:
            player.choice_6 = 0
            player.choice_6_timeout = True


class Choice_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_7']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[12]
        picture_2 = player.participant.picture[13]
        product_1 = player.participant.product[12]
        product_2 = player.participant.product[13]
        calories_1 = player.participant.calories[12]
        calories_2 = player.participant.calories[13]
        fat_1 = player.participant.fat[12]
        fat_2 = player.participant.fat[13]
        saturated_1 = player.participant.saturated[12]
        saturated_2 = player.participant.saturated[13]
        carbohydrates_1 = player.participant.carbohydrates[12]
        carbohydrates_2 = player.participant.carbohydrates[13]
        sugars_1 = player.participant.sugars[12]
        sugars_2 = player.participant.sugars[13]
        fibre_1 = player.participant.fibre[12]
        fibre_2 = player.participant.fibre[13]
        protein_1 = player.participant.protein[12]
        protein_2 = player.participant.protein[13]
        salt_1 = player.participant.salt[12]
        salt_2 = player.participant.salt[13]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_31 = str(time.time_ns())
        if timeout_happened:
            player.choice_7 = 0
            player.choice_7_timeout = True


class Choice_8(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_8']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[14]
        picture_2 = player.participant.picture[15]
        product_1 = player.participant.product[14]
        product_2 = player.participant.product[15]
        calories_1 = player.participant.calories[14]
        calories_2 = player.participant.calories[15]
        fat_1 = player.participant.fat[14]
        fat_2 = player.participant.fat[15]
        saturated_1 = player.participant.saturated[14]
        saturated_2 = player.participant.saturated[15]
        carbohydrates_1 = player.participant.carbohydrates[14]
        carbohydrates_2 = player.participant.carbohydrates[15]
        sugars_1 = player.participant.sugars[14]
        sugars_2 = player.participant.sugars[15]
        fibre_1 = player.participant.fibre[14]
        fibre_2 = player.participant.fibre[15]
        protein_1 = player.participant.protein[14]
        protein_2 = player.participant.protein[15]
        salt_1 = player.participant.salt[14]
        salt_2 = player.participant.salt[15]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_33 = str(time.time_ns())
        if timeout_happened:
            player.choice_8 = 0
            player.choice_8_timeout = True


class Choice_9(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2"  or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_9']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[16]
        picture_2 = player.participant.picture[17]
        product_1 = player.participant.product[16]
        product_2 = player.participant.product[17]
        calories_1 = player.participant.calories[16]
        calories_2 = player.participant.calories[17]
        fat_1 = player.participant.fat[16]
        fat_2 = player.participant.fat[17]
        saturated_1 = player.participant.saturated[16]
        saturated_2 = player.participant.saturated[17]
        carbohydrates_1 = player.participant.carbohydrates[16]
        carbohydrates_2 = player.participant.carbohydrates[17]
        sugars_1 = player.participant.sugars[16]
        sugars_2 = player.participant.sugars[17]
        fibre_1 = player.participant.fibre[16]
        fibre_2 = player.participant.fibre[17]
        protein_1 = player.participant.protein[16]
        protein_2 = player.participant.protein[17]
        salt_1 = player.participant.salt[16]
        salt_2 = player.participant.salt[17]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_35 = str(time.time_ns())
        if timeout_happened:
            player.choice_9 = 0
            player.choice_9_timeout = True


class Choice_10(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2"  or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_10']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[18]
        picture_2 = player.participant.picture[19]
        product_1 = player.participant.product[18]
        product_2 = player.participant.product[19]
        calories_1 = player.participant.calories[18]
        calories_2 = player.participant.calories[19]
        fat_1 = player.participant.fat[18]
        fat_2 = player.participant.fat[19]
        saturated_1 = player.participant.saturated[18]
        saturated_2 = player.participant.saturated[19]
        carbohydrates_1 = player.participant.carbohydrates[18]
        carbohydrates_2 = player.participant.carbohydrates[19]
        sugars_1 = player.participant.sugars[18]
        sugars_2 = player.participant.sugars[19]
        fibre_1 = player.participant.fibre[18]
        fibre_2 = player.participant.fibre[19]
        protein_1 = player.participant.protein[18]
        protein_2 = player.participant.protein[19]
        salt_1 = player.participant.salt[18]
        salt_2 = player.participant.salt[19]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_37 = str(time.time_ns())
        if timeout_happened:
            player.choice_10 = 0
            player.choice_10_timeout = True


class Choice_11(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2" or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_11']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[20]
        picture_2 = player.participant.picture[21]
        product_1 = player.participant.product[20]
        product_2 = player.participant.product[21]
        calories_1 = player.participant.calories[20]
        calories_2 = player.participant.calories[21]
        fat_1 = player.participant.fat[20]
        fat_2 = player.participant.fat[21]
        saturated_1 = player.participant.saturated[20]
        saturated_2 = player.participant.saturated[21]
        carbohydrates_1 = player.participant.carbohydrates[20]
        carbohydrates_2 = player.participant.carbohydrates[21]
        sugars_1 = player.participant.sugars[20]
        sugars_2 = player.participant.sugars[21]
        fibre_1 = player.participant.fibre[20]
        fibre_2 = player.participant.fibre[21]
        protein_1 = player.participant.protein[20]
        protein_2 = player.participant.protein[21]
        salt_1 = player.participant.salt[20]
        salt_2 = player.participant.salt[21]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_39 = str(time.time_ns())
        if timeout_happened:
            player.choice_11 = 0
            player.choice_11_timeout = True


class Choice_12(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12']

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.treatment == "T2"  or player.treatment == "T4":
            return C.time_pressure

    form_model = 'player'
    form_fields = ['choice_12']

    @staticmethod
    def vars_for_template(player: Player):
        picture_1 = player.participant.picture[22]
        picture_2 = player.participant.picture[23]
        product_1 = player.participant.product[22]
        product_2 = player.participant.product[23]
        calories_1 = player.participant.calories[22]
        calories_2 = player.participant.calories[23]
        fat_1 = player.participant.fat[22]
        fat_2 = player.participant.fat[23]
        saturated_1 = player.participant.saturated[22]
        saturated_2 = player.participant.saturated[23]
        carbohydrates_1 = player.participant.carbohydrates[22]
        carbohydrates_2 = player.participant.carbohydrates[23]
        sugars_1 = player.participant.sugars[22]
        sugars_2 = player.participant.sugars[23]
        fibre_1 = player.participant.fibre[22]
        fibre_2 = player.participant.fibre[23]
        protein_1 = player.participant.protein[22]
        protein_2 = player.participant.protein[23]
        salt_1 = player.participant.salt[22]
        salt_2 = player.participant.salt[23]
        eft_normal = player.participant.picture_n[player.id_in_group-1]
        if player.participant.weight == 0:
            pic_1 = player.participant.picture_wl[player.id_in_group-1]
            pic_2 = player.participant.picture_wg[player.id_in_group - 1]
        else:
            pic_1 = player.participant.picture_wg[player.id_in_group - 1]
            pic_2 = player.participant.picture_wl[player.id_in_group-1]

        return dict(product_1=product_1, product_2=product_2,
                    calories_1=calories_1, calories_2=calories_2, fat_1=fat_1, fat_2=fat_2, saturated_1=saturated_1,
                    saturated_2=saturated_2,carbohydrates_1=carbohydrates_1, carbohydrates_2=carbohydrates_2,
                    sugars_1=sugars_1, sugars_2=sugars_2, fibre_1=fibre_1, fibre_2=fibre_2, protein_1=protein_1,
                    protein_2=protein_2, salt_1=salt_1, salt_2=salt_2,
                    image_path_product_1='comfocus/{}'.format(picture_1),
                    image_path_product_2='comfocus/{}'.format(picture_2),
                    pic_1='comfocus/{}'.format(pic_1),
                    pic_2='comfocus/{}'.format(pic_2),
                    pic_n='comfocus/{}'.format(eft_normal),
                    order_shuffle=player.participant.weight
                    )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_41 = str(time.time_ns())
        if timeout_happened:
            player.choice_12 = 0
            player.choice_12_timeout = True


# Memorization task treatment
class Choice_1_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['1'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_1_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_19_memo = str(time.time_ns())


class Choice_2_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['2'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_2_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_21_memo = str(time.time_ns())


class Choice_3_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['3'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_3_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_23_memo = str(time.time_ns())


class Choice_4_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['4'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_4_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_25_memo = str(time.time_ns())


class Choice_5_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['5'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_5_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_27_memo = str(time.time_ns())


class Choice_6_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['6'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_6_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_29_memo = str(time.time_ns())


class Choice_7_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['7'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_7_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_31_memo = str(time.time_ns())


class Choice_8_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['8'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_8_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_33_memo = str(time.time_ns())


class Choice_9_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['9'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_9_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_35_memo = str(time.time_ns())


class Choice_10_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10'] and player.treatment == "T1" or \
               player.round_number == player.participant.page_order['10'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_10_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_37_memo = str(time.time_ns())


class Choice_11_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['11'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_11_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_39_memo = str(time.time_ns())


class Choice_12_memo(Page):
    timeout_seconds = C.memorization

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['12'] and player.treatment == "T3"

    @staticmethod
    def vars_for_template(player: Player):
        import random
        sequence = [random.randint(0, 9) for _ in range(7)]
        sequence_trial = int(''.join(map(str, sequence)))
        player.choice_12_memo = str(sequence_trial)
        return dict(number=sequence_trial)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_41_memo = str(time.time_ns())


# Memorization task answers
class Choice_1_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['1'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['1'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_1_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_19_memo_ans = str(time.time_ns())


class Choice_2_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['2'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['2'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_2_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_21_memo_ans = str(time.time_ns())


class Choice_3_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['3'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['3'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_3_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_23_memo_ans = str(time.time_ns())


class Choice_4_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['4'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['4'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_4_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_25_memo_ans = str(time.time_ns())


class Choice_5_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['5'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['5'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_5_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_27_memo_ans = str(time.time_ns())


class Choice_6_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['6'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['6'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_6_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_29_memo_ans = str(time.time_ns())


class Choice_7_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['7'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['7'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_7_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_31_memo_ans = str(time.time_ns())


class Choice_8_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['8'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['8'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_8_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_33_memo_ans = str(time.time_ns())


class Choice_9_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['9'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['9'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_9_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_35_memo_ans = str(time.time_ns())


class Choice_10_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['10'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['10'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_10_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_37_memo_ans = str(time.time_ns())


class Choice_11_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['11'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['11'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_11_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_39_memo_ans = str(time.time_ns())


class Choice_12_memo_ans(Page):
    timeout_seconds = C.memorization_2

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.page_order['12'] and player.treatment == "T1" or\
               player.round_number == player.participant.page_order['12'] and player.treatment == "T3"

    form_model = 'player'
    form_fields = ['choice_12_memo_ans']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_41_memo_ans = str(time.time_ns())


# Questionnaire
class Questionnaire_0(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_43 = str(time.time_ns())

class Questionnaire_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'income']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_44 = str(time.time_ns())

class Questionnaire_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['sport', 'smoker', 'smoker_2', 'smoker_3', 'alcohol', 'alcohol_2']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_45 = str(time.time_ns())

class Questionnaire_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['caffeine', 'sleep', 'breakfast', 'last_meal', 'hunger']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_46 = str(time.time_ns())

class Questionnaire_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['health', 'medicines', 'medicines_2',
                   'prod1', 'prod2', 'prod3', 'prod4', 'prod5', 'prod6',
                   'prod7', 'prod8', 'prod9', 'prod10', 'prod11', 'prod12',
                   'prod13', 'prod14', 'prod15', 'prod16', 'prod17', 'prod18',
                   'prod19', 'prod20', 'prod21', 'prod22', 'prod23', 'prod24']

    @staticmethod
    def vars_for_template(player: Player):
        pr1 = player.participant.product[0]
        pr2 = player.participant.product[1]
        pr3 = player.participant.product[2]
        pr4 = player.participant.product[3]
        pr5 = player.participant.product[4]
        pr6 = player.participant.product[5]
        pr7 = player.participant.product[6]
        pr8 = player.participant.product[7]
        pr9 = player.participant.product[8]
        pr10 = player.participant.product[9]
        pr11 = player.participant.product[10]
        pr12 = player.participant.product[11]
        pr13 = player.participant.product[12]
        pr14 = player.participant.product[13]
        pr15 = player.participant.product[14]
        pr16 = player.participant.product[15]
        pr17 = player.participant.product[16]
        pr18 = player.participant.product[17]
        pr19 = player.participant.product[18]
        pr20 = player.participant.product[19]
        pr21 = player.participant.product[20]
        pr22 = player.participant.product[21]
        pr23 = player.participant.product[22]
        pr24 = player.participant.product[23]

        return dict(pr1=pr1, pr2=pr2, pr3=pr3, pr4=pr4, pr5=pr5, pr6=pr6, pr7=pr7, pr8=pr8, pr9=pr9, pr10=pr10, pr11=pr11,
                    pr12=pr12, pr13=pr13, pr14=pr14, pr15=pr15, pr16=pr16, pr17=pr17, pr18=pr18, pr19=pr19, pr20=pr20,
                    pr21=pr21, pr22=pr22, pr23=pr23, pr24=pr24)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_47 = str(time.time_ns())

class Questionnaire_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    form_model = 'player'
    form_fields = ['labels', 'attention', 'attention_2', 'time_pressure', 'cognitive_load', 'comments'
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time
        player.page_47 = str(time.time_ns())


# Final
class Results_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

class Results_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        # random_round = player.participant.random_draw
        random_round = player.participant.page_order[f'{player.participant.random_draw}']
        inverted_dict = {str(value): key for key, value in player.participant.page_order.items()}
        choice_situation = inverted_dict[f'{random_round}']
        choice_field_name = f'choice_{choice_situation}'
        choice = getattr(player.in_round(random_round), choice_field_name)
        sequence = {
            1: (0, 1),
            2: (2, 3),
            3: (4, 5),
            4: (6, 7),
            5: (8, 9),
            6: (10, 11),
            7: (12, 13),
            8: (14, 15),
            9: (16, 17),
            10: (18, 19),
            11: (20, 21),
            12: (22, 23)
        }
        if choice is False:
            picture_number = sequence[int(choice_situation)][0]
        else:
            picture_number = sequence[int(choice_situation)][1]
        picture = player.participant.picture[picture_number]
        if player.treatment == "C1" or player.treatment == "C2":
            player.payoff = C.participation
        elif player.treatment == "T1" or player.treatment == "T3":
            number = getattr(player.in_round(random_round), f'choice_{choice_situation}_memo')
            guess = getattr(player.in_round(random_round), f'choice_{choice_situation}_memo_ans')
            if str(number) == str(guess):
                player.payoff = C.participation + C.bonus
            else:
                player.payoff = C.participation
        elif player.treatment == "T2" or player.treatment == "T4":
            timeout = getattr(player.in_round(random_round), f'choice_{choice_situation}_timeout')
            if timeout is False:
                player.payoff = C.participation + C.bonus
            else:
                player.payoff = C.participation

        return dict(payoff=player.payoff, picture='comfocus/{}'.format(picture), draw=random_round)


page_sequence = [
    Consent,
    Privacy,
    Blank_no_time,
    EDA_calibration,
    EDA_calibration_2,
    EDA_calibration_3,
    Instructions_1,
    Instructions_2,
    Instructions_2_2,
    Instructions_3,
    Instructions_4,
    Instructions_5,
    Instructions_6,
    Instructions_7,
    Trial_1,
    Blank_0,
    Trial_2_memo,
    Blank_1,
    Trial_2,
    Blank_2,
    Trial_2_memo_answer,
    Task_1,
    Task_2,
    Blank_3_memo,
    Choice_1_memo,
    Blank_3,
    Choice_1,
    Blank_3_memo_ans,
    Choice_1_memo_ans,
    Blank_4_memo,
    Choice_2_memo,
    Blank_4,
    Choice_2,
    Blank_4_memo_ans,
    Choice_2_memo_ans,
    Blank_5_memo,
    Choice_3_memo,
    Blank_5,
    Choice_3,
    Blank_5_memo_ans,
    Choice_3_memo_ans,
    Blank_6_memo,
    Choice_4_memo,
    Blank_6,
    Choice_4,
    Blank_6_memo_ans,
    Choice_4_memo_ans,
    Blank_7_memo,
    Choice_5_memo,
    Blank_7,
    Choice_5,
    Blank_7_memo_ans,
    Choice_5_memo_ans,
    Blank_8_memo,
    Choice_6_memo,
    Blank_8,
    Choice_6,
    Blank_8_memo_ans,
    Choice_6_memo_ans,
    Blank_9_memo,
    Choice_7_memo,
    Blank_9,
    Choice_7,
    Blank_9_memo_ans,
    Choice_7_memo_ans,
    Blank_10_memo,
    Choice_8_memo,
    Blank_10,
    Choice_8,
    Blank_10_memo_ans,
    Choice_8_memo_ans,
    Blank_11_memo,
    Choice_9_memo,
    Blank_11,
    Choice_9,
    Blank_11_memo_ans,
    Choice_9_memo_ans,
    Blank_12_memo,
    Choice_10_memo,
    Blank_12,
    Choice_10,
    Blank_12_memo_ans,
    Choice_10_memo_ans,
    Blank_13_memo,
    Choice_11_memo,
    Blank_13,
    Choice_11,
    Blank_13_memo_ans,
    Choice_11_memo_ans,
    Blank_14_memo,
    Choice_12_memo,
    Blank_14,
    Choice_12,
    Blank_14_memo_ans,
    Choice_12_memo_ans,
    # Blank_15,
    Questionnaire_0,
    Questionnaire_1,
    Questionnaire_2,
    Questionnaire_3,
    Questionnaire_4,
    Questionnaire_5,
    Results_1,
    Results_2
    ]
