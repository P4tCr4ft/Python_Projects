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

    hour_hand_az += (0.1/12)
    map_azimuth[hour_hand_az] = 'hour_hand_az'

    azimuth_list = [sec_hand_az, min_hand_az, hour_hand_az]
    azimuth_list.sort()
    # print('sorted azimuth list is {}'.format(azimuth_list))
    if (azimuth_list[0] + 120.0 == azimuth_list[1]) and (azimuth_list[1] + 120.0 == azimuth_list[2]):
        #solutions[x] = azimuth_list will go here, just checking what it stores in dict
        #need to reset solutions dict to empty, else with get massive

    # print(map_azimuth)

        solutions[x] = [(map_azimuth[azimuth_list[0]], azimuth_list[0]),
                        (map_azimuth[azimuth_list[1]], azimuth_list[1]),
                        (map_azimuth[azimuth_list[2]], azimuth_list[2])
                        ]

    # if (azimuth_list[0] + 120.0 == azimuth_list[1]) and (azimuth_list[1] + 120.0 == azimuth_list[2]):





    # print(solutions)
    map_azimuth = {}
    pass

print(solutions)



