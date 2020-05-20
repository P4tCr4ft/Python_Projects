# Config file for Python MODBUS over TCP/IP reading RTU SCADA signals - Kiamal Solar Farm

import logging

# For RTU test mode from the command line, this flag will cause program to run once only.
# It will also disable any other activity, such as MySQL, Solcast, EDD, etc.
# When this flag is disabled (False), the program will be configured to run as a service,
# in full production mode with all capabilities enabled.
rtu_test_only = True
# rtu_test_only = False


# When logging level is set to DEBUG the logger (which is root logger) picks up the messaging
# from all the other pymodbus libraries, as well as any Infolite module logging at that level. This is useful
# for tracking errors, and having a very detail view of operations.
# For normal operations in production, the INFO level is appropriate.
# logging_level = logging.DEBUG
logging_level = logging.INFO

# For each data type enter name and MODBUS address in pairs.
# Coils and Discrete Input dictionaries simply have name and modbus_address.

# For Holding Registers and/or Input Registers, they will be in type dependent dictionaries,
# depending whether they are floats or integers. They also have a list of values is this order;
#   [modbus_address, allowed_min_value, allowed_max_value, scaling*]
#   * scaling only if it exists

# If HR and/or IR signal modbus_addresses are incrementing by 2 (they are using 2 registers each)
# it means they are 32Bit integers or Floats


# Listed below are dictionaries of every possible type of modbus address in existence (except 64Bit),
# that may need to be read on an RTU, including the possibles for control tags,
# ie, control tags can only be coil or HR as they require write not just read.

# # All possible control tag variations
# coil_control_tags = {}
# hr_16bit_float_control_tags = {}
# hr_32bit_float_control_tags = {}
# hr_16bit_int_control_tags = {}
# hr_32bit_int_control_tags = {}
#
# # All possible data type variations
# coils = {}
# discrete_inputs = {}
# hr_16bit_floats = {}
# hr_32bit_floats = {}
# hr_16bit_ints = {}
# hr_32bit_ints = {}
# ir_16bit_floats = {}
# ir_32bit_floats = {}
# ir_16bit_ints = {}
# ir_32bit_ints = {}

coil_control_tags = {
    # 'unit_limit_dispatch_max_flag': 7,
    # 'unit_limit_dispatch_min_flag': 8,
    'dispatch_mw_flag': 0,
    'six_sec_raise_flag': 1,
    'six_sec_lower_flag': 2,
    'sixty_sec_raise_flag': 3,
    'sixty_sec_lower_flag': 4,
    'five_min_raise_flag': 5,
    'five_min_lower_flag': 6,
}

hr_32bit_float_control_tags = {
    # 'unit_limit_dispatch_max_generator_limit': [1016, 0, 150],
    # 'unit_limit_dispatch_min_generator_limit': [1018, 0, 150],
    # 'forecast_power'
    'dispatch_mw': [10, 0, 150],
    'six_sec_raise_mw': [12, 0, 150],
    'six_sec_lower_mw': [14, 0, 9999],
    'sixty_sec_raise_mw': [16, 0, 12],
    'sixty_sec_lower_mw': [40, 30, 50],
    'five_min_raise_mw': [46, 0, 60],
    'five_min_lower_mw': [48, 0, 150],
}

coils = {
    # 'some': 7,
    # 'random': 8,
    # 'signals': 0,
    # 'if_there': 1,
    # 'is_no_discrete': 2,
    # 'blah1': 0,
    # 'blah2': 1,
    # 'blah3': 2,
    # 'blah4': 3,
    # 'blah5': 4,
    # 'blah6': 5,
    # 'blah7': 6,
    # 'blah8': 7,
    # 'blah9': 8,
    # 'blah10': 9,
    # 'blah11': 10,
    # 'blah12': 11,
    # 'blah13': 12,
    # 'blah14': 13,
    # 'blah15': 14,
    # 'blah16': 15,
    # 'blah17': 16,
    # 'blah18': 17,
    # 'blah19': 18,
    # 'blah20': 19,
    # 'blah21': 20,
    # 'blah22': 21,
    # 'blah23': 22,
    # 'blah24': 23,
    # 'blah25': 24,
    # 'blah26': 25,
    # 'blah27': 26,
    # 'blah28': 27,
    # 'blah29': 28,
    # 'blah30': 29,
    # 'blah31': 30,
    # 'blah32': 31,
    # 'blah33': 32,
    # 'blah34': 33,
    # 'blah35': 34,
    # 'blah36': 35,
    # 'blah37': 36,
    # 'blah38': 37,
    # 'blah39': 38,
    # 'blah40': 39,
    # 'blah41': 40,
    # 'blah42': 41,
    # 'blah43': 42,
    # 'blah44': 43,
    # 'blah45': 44,
    # 'blah46': 45,
    # 'blah47': 46,
    # 'blah48': 47,
    # 'blah49': 48,
    # 'blah50': 49,
    # 'blah51': 50,
    # 'blah52': 51,
    # 'blah53': 52,
    # 'blah54': 53,
    # 'blah55': 54,
    # 'blah56': 55,
    # 'blah57': 56,
    # 'blah58': 57,
    # 'blah59': 58,
    # 'blah60': 59,
    # 'blah61': 60,
    # 'blah62': 61,
    # 'blah63': 62,
    # 'blah64': 63,
    # 'blah65': 64,
    # 'blah66': 65,
    # 'blah67': 66,
    # 'blah68': 67,
    # 'blah69': 68,
    # 'blah70': 69,
    # 'blah71': 70,
    # 'blah72': 71,
    # 'blah73': 72,
    # 'blah74': 73,
    # 'blah75': 74,
    # 'blah76': 75,
    # 'blah77': 76,
    # 'blah78': 77,
    # 'blah79': 78,
    # 'blah80': 79,
    # 'blah81': 80,
    # 'blah82': 81,
    # 'blah83': 82,
    # 'blah84': 83,
    # 'blah85': 84,
    # 'blah86': 85,
    # 'blah87': 86,
    # 'blah88': 87,
    # 'blah89': 88,
    # 'blah90': 89,
    # 'blah91': 90,
    # 'blah92': 91,
    # 'blah93': 92,
    # 'blah94': 93,
    # 'blah95': 94,
    # 'blah96': 95,
    # 'blah97': 96,
    # 'blah98': 97,
    # 'blah99': 98,
    # 'blah100': 99,
    # 'blah101': 100,
    # 'blah102': 101,
    # 'blah103': 102,
    # 'blah104': 103,
    # 'blah105': 104,
    # 'blah106': 105,
    # 'blah107': 106,
    # 'blah108': 107,
    # 'blah109': 108,
    # 'blah110': 109,
    # 'blah111': 110,
    # 'blah112': 111,
    # 'blah113': 112,
    # 'blah114': 113,
    # 'blah115': 114,
    # 'blah116': 115,
    # 'blah117': 116,
    # 'blah118': 117,
    # 'blah119': 118,
    # 'blah120': 119,
    # 'blah121': 120,
    # 'blah122': 121,
    # 'blah123': 122,
    # 'blah124': 123,
    # 'blah125': 124,
    # 'blah126': 125,
    # 'blah127': 126,
    # 'blah128': 127,
    # 'blah129': 128,
    # 'blah130': 129,
    # 'blah131': 130,
    # 'blah132': 131,
    # 'blah133': 132,
    # 'blah134': 133,
    # 'blah135': 134,
    # 'blah136': 135,
    # 'blah137': 136,
    # 'blah138': 137,
    # 'blah139': 138,
    # 'blah140': 139,
    # 'blah141': 140,
    # 'blah142': 141,
    # 'blah143': 142,
    # 'blah144': 143,
    # 'blah145': 144,
    # 'blah146': 145,
    # 'blah147': 146,
    # 'blah148': 147,
    # 'blah149': 148,
    # 'blah150': 149,
    # 'blah151': 150,
    # 'blah152': 151,
    # 'blah153': 152,
    # 'blah154': 153,
    # 'blah155': 154,
    # 'blah156': 155,
    # 'blah157': 156,
    # 'blah158': 157,
    # 'blah159': 158,
    # 'blah160': 159,
    # 'blah161': 160,
    # 'blah162': 161,
    # 'blah163': 162,
    # 'blah164': 163,
    # 'blah165': 164,
    # 'blah166': 165,
    # 'blah167': 166,
    # 'blah168': 167,
    # 'blah169': 168,
    # 'blah170': 169,
    # 'blah171': 170,
    # 'blah172': 171,
    # 'blah173': 172,
    # 'blah174': 173,
    # 'blah175': 174,
    # 'blah176': 175,
    # 'blah177': 176,
    # 'blah178': 177,
    # 'blah179': 178,
    # 'blah180': 179,
    # 'blah181': 180,
    # 'blah182': 181,
    # 'blah183': 182,
    # 'blah184': 183,
    # 'blah185': 184,
    # 'blah186': 185,
    # 'blah187': 186,
    # 'blah188': 187,
    # 'blah189': 188,
    # 'blah190': 189,
    # 'blah191': 190,
    # 'blah192': 191,
    # 'blah193': 192,
    # 'blah194': 193,
    # 'blah195': 194,
    # 'blah196': 195,
    # 'blah197': 196,
    # 'blah198': 197,
    # 'blah199': 198,
    # 'blah200': 199,
}

discrete_inputs = {
    # 'unit_limit_dispatch_max_flag_fb': 46,
    # 'unit_limit_dispatch_min_flag_fb': 47,
    'dispatch_mw_flag_fb': 1,
    'six_sec_raise_flag_fb': 2,
    'six_sec_lower_flag_fb': 3,
    'sixty_sec_raise_flag_fb': 4,
    'sixty_sec_lower_flag_fb': 5,
    'five_min_raise_flag_fb': 6,
    'five_min_lower_flag_fb': 7,
    # 'CollGrp1_cb_status_open': 8,
    # 'CollGrp1_cb_status_closed': 9,
    # 'CollGrp2_cb_status_open': 10,
    # 'CollGrp2_cb_status_closed': 11,
    # 'CollGrp5_cb_status_open': 12,
    # 'CollGrp5_cb_status_closed': 13,
    # 'CollGrp6_cb_status_open': 14,
    # 'CollGrp6_cb_status_closed': 15,
    # 'CollGrp7_cb_status_open': 16,
    # 'CollGrp7_cb_status_closed': 17,
    # 'CollGrp8_cb_status_open': 18,
    # 'CollGrp8_cb_status_closed': 19,
    # 'CollGrp11_cb_status_open': 20,
    # 'CollGrp11_cb_status_closed': 21,
    # 'CollGrp12_cb_status_open': 22,
    # 'CollGrp12_cb_status_closed': 23,
    # 'cb_220kV_cp_status_open': 24,
    # 'cb_220kV_cp_status_closed': 25,
    # 'cb_33kV_Transformer1A_open': 26,
    # 'cb_33kV_Transformer1A_closed': 27,
    # 'cb_33kV_Transformer1B_open': 28,
    # 'cb_33kV_Transformer1B_closed': 29,
    # 'cb_1A_Incomer_No1_open': 30,
    # 'cb_1A_Incomer_No1_closed': 31,
    # 'cb_1A_Incomer_No2_open': 32,
    # 'cb_1A_Incomer_No2_closed': 33,
    # 'cb_1B_Incomer_No1_open': 34,
    # 'cb_1B_Incomer_No1_closed': 35,
    # 'cb_1B_Incomer_No2_open': 36,
    # 'cb_1B_Incomer_No2_closed': 37,
}

hr_32bit_floats = {
    # 'number_gen_units_connected': [2, 0, 150],
    # 'seconds_until_dispatch_interval_end': [4, 0, 70],
    # 'dispatch_interval_timestamp_year': [800, 0, 9999]
    # 'dispatch_interval_timestamp_month': [801, 0, 12]
    # 'dispatch_interval_timestamp_day': [802, 0, 31]
    # 'dispatch_interval_timestamp_hour': [803, 0, 24]
    # 'dispatch_interval_timestamp_minute': [804, 0, 60]
    # 'unit_limit_dispatch_max_generator_limit_fb': [805, 0, 150]
    # 'unit_limit_dispatch_min_generator_limit_fb': [806, 0, 150]
    'dispatch_mw_fb': [36, 0, 200],
    'six_sec_raise_mw_fb': [38, 0, 20],
    'six_sec_lower_mw_fb': [20, 10, 20],
    'sixty_sec_raise_mw_fb': [22, 0, 20],
    'sixty_sec_lower_mw_fb': [24, 0, 20],
    'five_min_raise_mw_fb': [30, 0, 20],
    'five_min_lower_mw_fb': [32, 0, 20],
    'number_avail': [42, 0, 150],
    'number_gen': [44, 0, 150],
    #     'active_power': [18],
    #     'local_limit_mw': [20],
    #     'met1_irradiance': [22],
    #     'met1_air_temperature': [24],
    #     'met1_surface_temperature': [26],
    #     'met1_wind_speed': [28],
    #     'met1_wind_direction': [30],
    #     'met2_irradiance': [32],
    #     'met2_air_temperature': [34],
    #     'met2_surface_temperature': [36],
    #     'met2_wind_speed': [38],
    #     'met2_wind_direction': [40],
    #     'CollGrp1_active_power': [42],
    #     'CollGrp1_av_track_angle': [44],
    #     'CollGrp2_active_power': [46],
    #     'CollGrp2_av_track_angle': [48],
    #     'CollGrp5_active_power': [50],
    #     'CollGrp5_av_track_angle': [52],
    #     'CollGrp6_active_power': [54],
    #     'CollGrp6_av_track_angle': [56],
    #     'CollGrp7_active_power': [58],
    #     'CollGrp7_av_track_angle': [60],
    #     'CollGrp8_active_power': [62],
    #     'CollGrp8_av_track_angle': [64],
    #     'CollGrp11_active_power': [66],
    #     'CollGrp11_av_track_angle': [68],
    #     'CollGrp12_active_power': [70],
    #     'CollGrp12_av_track_angle': [72],
    #     'possible_power': [74],
    # 'inverter1_active_power': [76],
    # 'inverter2_active_power': [78],
    # 'inverter3_active_power': [80],
    # 'inverter4_active_power': [82],
    # 'inverter5_active_power': [84],
    # 'inverter6_active_power': [86],
    # 'inverter7_active_power': [88],
    # 'inverter8_active_power': [90],
    # 'inverter9_active_power': [92],
    # 'inverter10_active_power': [94],
    # 'inverter11_active_power': [96],
    # 'inverter12_active_power': [98],
    # 'inverter13_active_power': [100],
    # 'inverter14_active_power': [102],
    # 'inverter15_active_power': [104],
    # 'inverter16_active_power': [106],
    # 'inverter17_active_power': [108],
    # 'inverter18_active_power': [110],
    # 'inverter19_active_power': [112],
    # 'inverter20_active_power': [114],
    # 'inverter21_active_power': [116],
    # 'inverter22_active_power': [118],
    # 'inverter23_active_power': [120],
    # 'inverter24_active_power': [122],
    # 'inverter25_active_power': [124],
    # 'inverter26_active_power': [126],
    # 'inverter27_active_power': [128],
    # 'inverter28_active_power': [130],
    # 'inverter29_active_power': [132],
    # 'inverter30_active_power': [134],
    # 'inverter31_active_power': [136],
    # 'inverter32_active_power': [138],
    # 'inverter33_active_power': [140],
    # 'inverter34_active_power': [142],
    # 'inverter35_active_power': [144],
    # 'inverter36_active_power': [146],
    # 'inverter37_active_power': [148],
    # 'inverter38_active_power': [150],
    # 'inverter39_active_power': [152],
    # 'inverter40_active_power': [154],
    # 'inverter41_active_power': [156],
    # 'inverter42_active_power': [158],
    # 'inverter43_active_power': [160],
    # 'inverter44_active_power': [162],
    # 'inverter45_active_power': [164],
    # 'inverter46_active_power': [166],
    # 'inverter47_active_power': [168],
    # 'inverter48_active_power': [170],
    # 'inverter49_active_power': [172],
    # 'inverter50_active_power': [174],
    # 'inverter51_active_power': [176],
    # 'inverter52_active_power': [178],
    # 'inverter53_active_power': [180],
    # 'inverter54_active_power': [182],
    # 'inverter55_active_power': [184],
    # 'inverter56_active_power': [186],
    # 'inverter57_active_power': [188],
    # 'inverter58_active_power': [190],
    # 'inverter59_active_power': [192],
    # 'inverter60_active_power': [194],
    # 'inverter61_active_power': [196],
    # 'inverter62_active_power': [198],
    # 'inverter63_active_power': [200],
    # 'inverter64_active_power': [202],
    # 'inverter65_active_power': [204],
    # 'inverter66_active_power': [206],
    # 'inverter67_active_power': [208],
    # 'inverter68_active_power': [210],
    # 'inverter69_active_power': [212],
    # 'inverter70_active_power': [214],
    # 'inverter71_active_power': [216],
    # 'inverter72_active_power': [218],
    # 'inverter73_active_power': [220],
    # 'inverter74_active_power': [222],
    # 'inverter75_active_power': [224],
    # 'inverter76_active_power': [226],
    # 'inverter77_active_power': [228],
    # 'inverter78_active_power': [230],
    # 'inverter79_active_power': [232],
    # 'inverter80_active_power': [234],
    # 'inverter81_active_power': [236],
    # 'inverter82_active_power': [238],
    # 'inverter83_active_power': [240],
    # 'inverter84_active_power': [242],
    # 'inverter85_active_power': [244],
    # 'inverter86_active_power': [246],
    # 'inverter87_active_power': [248],
    # 'inverter88_active_power': [250],
    # 'inverter89_active_power': [252],
    # 'inverter90_active_power': [254],
    # 'inverter91_active_power': [256],
    # 'inverter92_active_power': [258],
    # 'inverter93_active_power': [260],
    # inverter94_active_power
    # inverter95_active_power
    # inverter96_active_power
    # inverter97_active_power
    # inverter98_active_power
    # inverter99_active_power
    # inverter100_active_power
    # inverter101_active_power
    # inverter102_active_power
    # inverter103_active_power
    # inverter104_active_power
    # inverter105_active_power
    # inverter106_active_power
    # inverter107_active_power
    # inverter108_active_power
    # inverter109_active_power
    # inverter110_active_power
    # inverter111_active_power
    # inverter112_active_power
    # inverter113_active_power
    # inverter114_active_power
    # inverter115_active_power
    # inverter116_active_power
    # inverter117_active_power
    # inverter118_active_power
    # inverter119_active_power
    # inverter120_active_power
    # inverter121_active_power
    # inverter122_active_power
    # inverter123_active_power
    # inverter124_active_power
    # inverter125_active_power
    # inverter126_active_power
    # inverter127_active_power
    # inverter128_active_power
    # inverter129_active_power
    # inverter130_active_power
    # inverter131_active_power
    # inverter132_active_power
    # inverter133_active_power
    # inverter134_active_power
    # inverter135_active_power
    # inverter136_active_power
    # inverter137_active_power
    # inverter138_active_power
    # inverter139_active_power
    # inverter140_active_power
    # inverter141_active_power
    # inverter142_active_power
    # inverter143_active_power
    # inverter144_active_power
    # inverter145_active_power
    # inverter146_active_power
    # inverter147_active_power
    # inverter148_active_power
    # inverter149_active_power
    # inverter150_active_power
    # inverter1_accum_energy
    # inverter2_accum_energy
    # inverter3_accum_energy
    # inverter4_accum_energy
    # inverter5_accum_energy
    # inverter6_accum_energy
    # inverter7_accum_energy
    # inverter8_accum_energy
    # inverter9_accum_energy
    # inverter10_accum_energy
    # inverter11_accum_energy
    # inverter12_accum_energy
    # inverter13_accum_energy
    # inverter14_accum_energy
    # inverter15_accum_energy
    # inverter16_accum_energy
    # inverter17_accum_energy
    # inverter18_accum_energy
    # inverter19_accum_energy
    # inverter20_accum_energy
    # inverter21_accum_energy
    # inverter22_accum_energy
    # inverter23_accum_energy
    # inverter24_accum_energy
    # inverter25_accum_energy
    # inverter26_accum_energy
    # inverter27_accum_energy
    # inverter28_accum_energy
    # inverter29_accum_energy
    # inverter30_accum_energy
    # inverter31_accum_energy
    # inverter32_accum_energy
    # inverter33_accum_energy
    # inverter34_accum_energy
    # inverter35_accum_energy
    # inverter36_accum_energy
    # inverter37_accum_energy
    # inverter38_accum_energy
    # inverter39_accum_energy
    # inverter40_accum_energy
    # inverter41_accum_energy
    # inverter42_accum_energy
    # inverter43_accum_energy
    # inverter44_accum_energy
    # inverter45_accum_energy
    # inverter46_accum_energy
    # inverter47_accum_energy
    # inverter48_accum_energy
    # inverter49_accum_energy
    # inverter50_accum_energy
    # inverter51_accum_energy
    # inverter52_accum_energy
    # inverter53_accum_energy
    # inverter54_accum_energy
    # inverter55_accum_energy
    # inverter56_accum_energy
    # inverter57_accum_energy
    # inverter58_accum_energy
    # inverter59_accum_energy
    # inverter60_accum_energy
    # inverter61_accum_energy
    # inverter62_accum_energy
    # inverter63_accum_energy
    # inverter64_accum_energy
    # inverter65_accum_energy
    # inverter66_accum_energy
    # inverter67_accum_energy
    # inverter68_accum_energy
    # inverter69_accum_energy
    # inverter70_accum_energy
    # inverter71_accum_energy
    # inverter72_accum_energy
    # inverter73_accum_energy
    # inverter74_accum_energy
    # inverter75_accum_energy
    # inverter76_accum_energy
    # inverter77_accum_energy
    # inverter78_accum_energy
    # inverter79_accum_energy
    # inverter80_accum_energy
    # inverter81_accum_energy
    # inverter82_accum_energy
    # inverter83_accum_energy
    # inverter84_accum_energy
    # inverter85_accum_energy
    # inverter86_accum_energy
    # inverter87_accum_energy
    # inverter88_accum_energy
    # inverter89_accum_energy
    # inverter90_accum_energy
    # inverter91_accum_energy
    # inverter92_accum_energy
    # inverter93_accum_energy
    # inverter94_accum_energy
    # inverter95_accum_energy
    # inverter96_accum_energy
    # inverter97_accum_energy
    # inverter98_accum_energy
    # inverter99_accum_energy
    # inverter100_accum_energy
    # inverter101_accum_energy
    # inverter102_accum_energy
    # inverter103_accum_energy
    # inverter104_accum_energy
    # inverter105_accum_energy
    # inverter106_accum_energy
    # inverter107_accum_energy
    # inverter108_accum_energy
    # inverter109_accum_energy
    # inverter110_accum_energy
    # inverter111_accum_energy
    # inverter112_accum_energy
    # inverter113_accum_energy
    # inverter114_accum_energy
    # inverter115_accum_energy
    # inverter116_accum_energy
    # inverter117_accum_energy
    # inverter118_accum_energy
    # inverter119_accum_energy
    # inverter120_accum_energy
    # inverter121_accum_energy
    # inverter122_accum_energy
    # inverter123_accum_energy
    # inverter124_accum_energy
    # inverter125_accum_energy
    # inverter126_accum_energy
    # inverter127_accum_energy
    # inverter128_accum_energy
    # inverter129_accum_energy
    # inverter130_accum_energy
    # inverter131_accum_energy
    # inverter132_accum_energy
    # inverter133_accum_energy
    # inverter134_accum_energy
    # inverter135_accum_energy
    # inverter136_accum_energy
    # inverter137_accum_energy
    # inverter138_accum_energy
    # inverter139_accum_energy
    # inverter140_accum_energy
    # inverter141_accum_energy
    # inverter142_accum_energy
    # inverter143_accum_energy
    # inverter144_accum_energy
    # inverter145_accum_energy
    # inverter146_accum_energy
    # inverter147_accum_energy
    # inverter148_accum_energy
    # inverter149_accum_energy
    # inverter150_accum_energy
}

hr_16bit_ints = {
    'CollGrp1_number_available': [0, 0, 25],
    'CollGrp1_number_generating': [1, 0, 25],
    'CollGrp2_number_available': [2, -10, 25],
    'CollGrp2_number_generating': [3, 0, 25],
    'CollGrp5_number_available': [4, -10, 25, 10],
    'CollGrp5_number_generating': [5, 5, 25, 10],
    # 'CollGrp6_number_available': [6, 0, 25],
    # 'CollGrp6_number_generating': [7, 0, 25],
    # 'CollGrp7_number_available': [8, 0, 25],
    # 'CollGrp7_number_generating': [9, 0, 25],
    # 'CollGrp8_number_available': [10, 0, 25],
    # 'CollGrp8_number_generating': [11, 0, 25],
    # 'CollGrp11_number_available': [12, 0, 25],
    # 'CollGrp11_number_generating': [13, 0, 25],
    # 'CollGrp12_number_available': [14, 0, 25],
    # 'CollGrp12_number_generating': [15, 0, 25],
    # 'inverter1_status': [16, 0, 7],
    # 'inverter2_status': [17, 0, 7],
    # 'inverter3_status': [18, 0, 7],
    # 'inverter4_status': [19, 0, 7],
    # 'inverter5_status': [20, 0, 7],
    # 'inverter6_status': [21, 0, 7],
    # 'inverter7_status': [22, 0, 7],
    # 'inverter8_status': [23, 0, 7],
    # 'inverter9_status': [24, 0, 7],
    # 'inverter10_status': [25, 0, 7],
    # 'inverter11_status': [26, 0, 7],
    # 'inverter12_status': [27, 0, 7],
    # 'inverter13_status': [28, 0, 7],
    # 'inverter14_status': [29, 0, 7],
    # 'inverter15_status': [30, 0, 7],
    # 'inverter16_status': [31, 0, 7],
    # 'inverter17_status': [32, 0, 7],
    # 'inverter18_status': [33, 0, 7],
    # 'inverter19_status': [34, 0, 7],
    # 'inverter20_status': [35, 0, 7],
    # 'inverter21_status': [36, 0, 7],
    # 'inverter22_status': [37, 0, 7],
    # 'inverter23_status': [38, 0, 7],
    # 'inverter24_status': [39, 0, 7],
    # 'inverter25_status': [40, 0, 7],
    # 'inverter26_status': [41, 0, 7],
    # 'inverter27_status': [42, 0, 7],
    # 'inverter28_status': [43, 0, 7],
    # 'inverter29_status': [44, 0, 7],
    # 'inverter30_status': [45, 0, 7],
    # 'inverter31_status': [46, 0, 7],
    # 'inverter32_status': [47, 0, 7],
    # 'inverter33_status': [48, 0, 7],
    # 'inverter34_status': [49, 0, 7],
    # 'inverter35_status': [50, 0, 7],
    # 'inverter36_status': [51, 0, 7],
    # 'inverter37_status': [52, 0, 7],
    # 'inverter38_status': [53, 0, 7],
    # 'inverter39_status': [54, 0, 7],
    # 'inverter40_status': [55, 0, 7],
    # 'inverter41_status': [56, 0, 7],
    # 'inverter42_status': [57, 0, 7],
    # 'inverter43_status': [58, 0, 7],
    # 'inverter44_status': [59, 0, 7],
    # 'inverter45_status': [60, 0, 7],
    # 'inverter46_status': [61, 0, 7],
    # 'inverter47_status': [62, 0, 7],
    # 'inverter48_status': [63, 0, 7],
    # 'inverter49_status': [64, 0, 7],
    # 'inverter50_status': [65, 0, 7],
    # 'inverter51_status': [66, 0, 7],
    # 'inverter52_status': [67, 0, 7],
    # 'inverter53_status': [68, 0, 7],
    # 'inverter54_status': [69, 0, 7],
    # 'inverter55_status': [70, 0, 7],
    # 'inverter56_status': [71, 0, 7],
    # 'inverter57_status': [72, 0, 7],
    # 'inverter58_status': [73, 0, 7],
    # 'inverter59_status': [74, 0, 7],
    # 'inverter60_status': [75, 0, 7],
    # 'inverter61_status': [76, 0, 7],
    # 'inverter62_status': [77, 0, 7],
    # 'inverter63_status': [78, 0, 7],
    # 'inverter64_status': [79, 0, 7],
    # 'inverter65_status': [80, 0, 7],
    # 'inverter66_status': [81, 0, 7],
    # 'inverter67_status': [82, 0, 7],
    # 'inverter68_status': [83, 0, 7],
    # 'inverter69_status': [84, 0, 7],
    # 'inverter70_status': [85, 0, 7],
    # 'inverter71_status': [86, 0, 7],
    # 'inverter72_status': [87, 0, 7],
    # 'inverter73_status': [88, 0, 7],
    # 'inverter74_status': [89, 0, 7],
    # 'inverter75_status': [90, 0, 7],
    # 'inverter76_status': [91, 0, 7],
    # 'inverter77_status': [92, 0, 7],
    # 'inverter78_status': [93, 0, 7],
    # 'inverter79_status': [94, 0, 7],
    # 'inverter80_status': [95, 0, 7],
    # 'inverter81_status': [96, 0, 7],
    # 'inverter82_status': [97, 0, 7],
    # 'inverter83_status': [98, 0, 7],
    # 'inverter84_status': [99, 0, 7],
    # 'inverter85_status': [100, 0, 7],
    # 'inverter86_status': [101, 0, 7],
    # 'inverter87_status': [102, 0, 7],
    # 'inverter88_status': [103, 0, 7],
    # 'inverter89_status': [104, 0, 7],
    # 'inverter90_status': [105, 0, 7],
    # 'inverter91_status': [106, 0, 7],
    # 'inverter92_status': [107, 0, 7],
    # 'inverter93_status': [108, 0, 7],
    # 'inverter94_status': [109, 0, 7],
    # 'inverter95_status': [110, 0, 7],
    # 'inverter96_status': [111, 0, 7],
    # 'inverter97_status': [112, 0, 7],
    # 'inverter98_status': [113, 0, 7],
    # 'inverter99_status': [114, 0, 7],
    # 'inverter100_status': [115, 0, 7],
    # 'inverter101_status': [116, 0, 7],
    # 'inverter102_status': [117, 0, 7],
    # 'inverter103_status': [118, 0, 7],
    # 'inverter104_status': [119, 0, 7],
    # 'inverter105_status': [120, 0, 7],
    # 'inverter106_status': [121, 0, 7],
    # 'inverter107_status': [122, 0, 7],
    # 'inverter108_status': [123, 0, 7],
    # 'inverter109_status': [124, 0, 7],
    # 'inverter110_status': [125, 0, 7],
    # 'inverter111_status': [126, 0, 7],
    # 'inverter112_status': [127, 0, 7],
    # 'inverter113_status': [128, 0, 7],
    # 'inverter114_status': [129, 0, 7],
    # 'inverter115_status': [130, 0, 7],
    # 'inverter116_status': [131, 0, 7],
    # 'inverter117_status': [132, 0, 7],
    # 'inverter118_status': [133, 0, 7],
    # 'inverter119_status': [134, 0, 7],
    # 'inverter120_status': [135, 0, 7],
    # 'inverter121_status': [136, 0, 7],
    # 'inverter122_status': [137, 0, 7],
    # 'inverter123_status': [138, 0, 7],
    # 'inverter124_status': [139, 0, 7],
    # 'inverter125_status': [140, 0, 7],
    # 'inverter126_status': [141, 0, 7],
    # 'inverter127_status': [142, 0, 7],
    # 'inverter128_status': [143, 0, 7],
    # 'inverter129_status': [144, 0, 7],
    # 'inverter130_status': [145, 0, 7],
    # 'inverter131_status': [146, 0, 7],
    # 'inverter132_status': [147, 0, 7],
    # 'inverter133_status': [148, 0, 7],
    # 'inverter134_status': [149, 0, 7],
    # 'inverter135_status': [150, 0, 7],
    # 'inverter136_status': [151, 0, 7],
    # 'inverter137_status': [152, 0, 7],
    # 'inverter138_status': [153, 0, 7],
    # 'inverter139_status': [154, 0, 7],
    # 'inverter140_status': [155, 0, 7],
    # 'inverter141_status': [156, 0, 7],
    # 'inverter142_status': [157, 0, 7],
    # 'inverter143_status': [158, 0, 7],
    # 'inverter144_status': [159, 0, 7],
    # 'inverter145_status': [160, 0, 7],
    # 'inverter146_status': [161, 0, 7],
    # 'inverter147_status': [162, 0, 7],
    # 'inverter148_status': [163, 0, 7],
    # 'inverter149_status': [164, 0, 7],
    # 'inverter150_status': [165, 0, 7],
}

hr_32bit_ints = {
    'CollGrp7_number_generating': [6, -10, 25, 100],
    'CollGrp8_number_available': [8, -10, 25],
}

# Dictionary of RTUs including associated connection info and SCADA signals

rtus = {'rtu1': {
    'rtu_ip': '192.168.1.115',
    'rtu_port': 502,
    'rtu_slave_id': 1,
    'coil_control_tags': coil_control_tags,
    'hr_32bit_float_control_tags': hr_32bit_float_control_tags,
    'coils': coils,
    'discrete_inputs': discrete_inputs,
    'hr_32bit_floats': hr_32bit_floats,
}, 'rtu2': {
    'rtu_ip': '192.168.1.115',
    'rtu_port': 502,
    'rtu_slave_id': 1,
    'hr_16bit_ints': hr_16bit_ints,
    'hr_32bit_ints': hr_32bit_ints,
}
}
