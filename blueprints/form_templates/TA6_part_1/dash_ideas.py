notes={
[
	'notes_identifier':'mtd_live_disclosure_summary',
	'notes_name':'Live Disclosures Summary',

		'Sections':['Section_name':'Disclosor Profile',
		'section_identifier':'disclosor_profile',
		'main_display':[
				{	
				
					'functional_location':'dashboard',
					'display_title':'Global Oversight',
					'description':'Display the total number of Live Material Disclosures issued by ID of Professional Disclosor',
					'input_source':['Pending','Commenced','Progressing'],
					'identifier':'global_oversight',
					'display_type':{'number', 'value related graphic'},
				},
				{	
				
					'functional_location':'dashboard',
					'display_title':'Live Disclosures Total',
					'description':'Display the total number of Live Material Disclosures issued by ID of Professional Disclosor',
					'input_source':['Pending','Commenced','Progressing'],
					'identifier':'disclosor_live_total',
					'display_type':{'number', 'value related graphic'},
				},
				{	
				
					'functional_location':'dashboard',
					'display_title':'Demobilised Disclosures Total',
					'description':'Display the total number of Demobilised Material Disclosures issued by ID of Professional Disclosor',
					'input_source':['Unsuccessful','Bounced', 'Declined', 'Unsubscribed'],
					'identifier':'demob_disclosures_total',
					'display_type':{'number', 'value related graphic'},
				},
				{	
				
					'functional_location':'dashboard',
					'display_title':'Endangered Disclosures Total',
					'description':'Display the total number of Demobilised Material Disclosures issued by ID of Professional Disclosor',
					'input_source':['Slow', 'Stalled','Overdue','Abandoned'],
					'identifier':'disclosor_total_live',
					'display_type':{'number', 'value related graphic'},
				},

				{	
				
					'functional_location':'dashboard',
					'display_title':'Support Required',
					'description':'Display the total number of Demobilised Material Disclosures issued by ID of Professional Disclosor',
					'input_source':['Slow', 'Stalled','Overdue','Abandoned'],
					'identifier':'disclosor_total_live',
					'display_type':{'number','value related graphic'},
				},

				]


Dashboard Numbers

Prospects	- 	Vendors
			-	Buyers

Recipients	- 	# V (Vendors)
				# B (Buyers)

Disclosure Invitations
Opens	(opened communication	
Clicks	(click though to Disclosure)

DASHBOARD 
Disclosure ( DISPLAY Values:   % or #  )
Total			(a)	Life Number of Total

Pending		(b)		Issued but not commenced	“TIME"				Y
Commenced	(c) 	ID & address sections completed					Y -	
Progressing	(d) 	Questions answered in at least 2 sections		Y - 	No multi user logging - if/when disco non custom input to calc commencement

Stalled		(e) 	Unfinished form, and (b) no progress “TIME" 		Y - progressing time …?
Overdue		(f) 	Unfinished at Target date)  Target date start point	Y -  DB set’s start , Standard due-date counter - display concern - react options 
Endangered 	(h)  	Disclosure Form not visited after “TIME”
Abandoned 	(g)  	Disclosure Form not complete after “TIME”



Possible Dashboard Display Options

"client_prgression_status"
"prgression":

Unsuccessful
Bounced
Declined
Unsubscribed

Support Insights
Incomplete section/s
Missing Extra Data
Skipped Micro Form Data
Stalled progression

Support Tools
Reach out to customer
Arrange a call

Disclosor Total
Commenced
Completed

Qualitative
Standards full
Standard 


Stall Rescues
Abandoned