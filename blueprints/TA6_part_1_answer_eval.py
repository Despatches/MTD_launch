if ('5p2p1p1' == 'empty')

def yes_no_mark(liysy):
	marker = []
	yes_mark = False
	empty_mark = False
	unknown_mark = False
	for option in listy:
		if option == 'yes':
			if yes_mark == False:
				yes_mark = True
				marker.append('factors')
		if option == 'empty':
			if empty_mark == False:
				empty_mark = True
				marker.append('emptys')
		if option == 'not_known' or option == 'not_sure':
			if unknown_mark == False:
				unknown_mark = True
				marker.append('unknown')				
			

	return marker
	
move_timing = (5p2p1p1, 5p2p2p1, 5p2p3p1, 5p2p4p1, 5p2p5p1, 5p2p6p1
				5p2p7p1, 5p2p8p1, 5p2p9p1)

move_time_mark = yes_no_mark(move_timing)


property_alterations = (6p1p1, 6p1p2, 6p1p3, 6p1p4, 
						6p1p5, 6p1p6, 6p1p7, 6p1p8)

prop_alter_mark = yes_no_mark(property_alterations)
#for alter in property_alterations:
#	if alter == 'yes':
#		prop_alter_mark = 1
#		break

liabilities = (7p1p1, 7p1p2, 7p1p3, 7p1p4)

liabitlities_mark = yes_no_mark(liabilities)
#for li in liabitlities_mark:
#	if alter == 'yes':
#		prop_alter_mark = 1
#		break

listing_or_conserve = (9p1, 10p1, 9p2)

listing_or_conserve_mark = yes_no_mark(listing_or_conserve)


extra_consents =(13p1, )

extra_consents_mark = yes_no_mark(extra_consents)


access_complications = (13p1, 13p2, 13p3)

access_complications_mark =  access_complications

shared_facilties= ()










