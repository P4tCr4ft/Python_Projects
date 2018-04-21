'''
Assumptions:

This script solves this problem using 360 decimal degrees in a circle.
Every second, each hand moves a discrete distance.
Every second, the second hand moves 6.0 degrees.
Every second, the minute hand moves 0.1 decimal degrees.
Every second, the hour hand moves (0.1/12) decimal degrees.
In one complete cycle of the analog clock the second hand moves 43,200 times.

This script works by monitoring the azimuth of each hand, and checking whether they
are 120 degrees apart, meaning all hands would be equidistant from each other.
Azimuth being 0 degrees for hand pointing straight up, 90 degrees for hand pointing
to the 3, etc.
'''

sec_hand_az = 0.0
min_hand_az = 0.0
hour_hand_az = 0.0
solutions = {}
rough_solutions = {}
map_azimuth = {}

for x in range(43200):
    sec_hand_az += 6.0
    map_azimuth[sec_hand_az] = 'sec_hand_az'
    if sec_hand_az == 360.0:
        sec_hand_az = 0.0

    min_hand_az += 0.1
    map_azimuth[min_hand_az] = 'min_hand_az'
    if min_hand_az == 360.0:
        min_hand_az = 0.0

    hour_hand_az += (0.1/12.0)
    map_azimuth[hour_hand_az] = 'hour_hand_az'

    azimuth_list = [sec_hand_az, min_hand_az, hour_hand_az]
    azimuth_list.sort()

    if (azimuth_list[0] + 120.0 == azimuth_list[1]) and (azimuth_list[1] + 120.0 == azimuth_list[2]):

        solutions[str(x)] = [(map_azimuth.get(azimuth_list[0]), azimuth_list[0]),
                        (map_azimuth.get(azimuth_list[1]), azimuth_list[1]),
                        (map_azimuth.get(azimuth_list[2]), azimuth_list[2])
                        ]

    # Below obtains a solution, if hands are equidistant within plus/minus 2 degrees
    # See rough_solution

    if ((azimuth_list[1] - 2.0) <= (azimuth_list[0] + 120.0) <= (azimuth_list[1] + 2.0)) and \
        ((azimuth_list[2] - 2.0) <= (azimuth_list[1] + 120.0) <= (azimuth_list[2] + 2.0)):

        rough_solutions[str(x)] = [(map_azimuth.get(azimuth_list[0]), azimuth_list[0]),
                        (map_azimuth.get(azimuth_list[1]), azimuth_list[1]),
                        (map_azimuth.get(azimuth_list[2]), azimuth_list[2])
                        ]

    map_azimuth = {}


print('Exact solutions are {}'.format(solutions))

for k, v in rough_solutions.items():
    print('\nRough solutions are {}, {}'.format(k, v))

print('\nThere are no solutions where all hands are exactly equidistant\n'\
      'There is one solution where hands are equidistant within plus/minus 2 degrees of equidistance\n'\
      'This occurs at iteration {}, which equates to a time of about {}:{}:{}'.format(list(rough_solutions.keys())[0],
                                                            (round((list(rough_solutions.values())[0][0][1])/12)*12),
                                                            round((list(rough_solutions.values())[0][1][1])/6),
                                                            round((list(rough_solutions.values())[0][2][1])/6)))

