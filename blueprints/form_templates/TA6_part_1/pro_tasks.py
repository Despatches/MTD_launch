
pro_meanings = {
'data_providers_count' : {
     'value' : {
            'equation':{
                'larger_than' : {
                	'vari':1, 
                	'meaning':"The disclosure representing the vendor interest in this property has been provided by {} people",
			  		"dd_task": ["Ensure the disclosing parties are legally entitled to represent the vendor interest and obligations."],
			        "pro_meaning": "The disclosure representing the vendor interest in this property has been provided by {} people"
                },
                'less_than' : {
                	'vari':1, 
                	'meaning':'The number of persons providing this data has not been specified',
			  		"dd_task": ["Ensure all required parties have made a disclosure or endorsed this document"],
			        "pro_meaning": "The number of persons providing this data has not been specified"               	
                }
                },
            'default':{
            	'meaning' : "This data has been provided by one individual",
            	"dd_task": ["Determine if any other individual is a proprietory party to the sale.", "Secure disclosure from any other proprietory parties to the sale"],
			    "pro_meaning": "This data has been provided by one individual"
			   },
        }

#Injection value position notated by {}
 } ,
'postcode' : {

     'none' : {

         'meaning' : "",
 		"dd_task": ["Ensure address declarations are complete and valid."],
        "pro_meaning": "The address details are incomplete"
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 },
'address_line_1' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'address_line_2' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'address_town_or_city' : {

     'none' : {

         'meaning' : "The postal town/city for the property has not been specified",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'UPRN' : {

     'none' : {

         'meaning' : "A UPRN has not been specified",
 		"dd_task": ["Locate and update the UPRN to enable the disclosure search features to operate effectively"],
        "pro_meaning": "Missing UPRN may undermine searches designed to locate important data about this property"
     },

     'value' : {

         'meaning' : "The UPRN for this property is:{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'lease_or_free' : {

     'empty' : {

         'meaning' : "The tenure applicable to this Title has not been specified",
#		3 Inject "dd_task": [""],
        "pro_meaning":  "the Title Number into a new combined sentence if known."
#3 SPecimen sentence " The tenure applicable to Title {} has not been specified"
     },

     'Leasehold' : {

         'meaning' : "The ownership status in this title is Leasehold",
 		"dd_task": ["Propagate disclosures to the Freeholder and or managing agent"],
        "pro_meaning": "The property is Leasehold: verification shall be required from the Freehold interest."
     },

     'Freehold' : {

         'meaning' : "The ownership status in this title is Freehold",
 		"dd_task": [""],
        "pro_meaning": "The ownership status in this title is Freehold"
     },

 } ,
'years_left' : {

     'none' : {
         'meaning' : "The number of years remaining (unexpired) on this Leasehold have not been specified",
 		"dd_task": ["The discloser must confirm the number of years remaining upon the lease. "],
        "pro_meaning": ["Without a declaration stating the number of years that remain on the lease the lending security disclosure obligation will not be fulfilled", 
                        ],
     },

     'value' : {

         'meaning' : "The Leasehold has {} Years remaining on the agreement",
 		"dd_task": ["Evaluate the requirement to extend the leasehold term and verify the opportunity and cost to do so if required"],
        "pro_meaning": "The Leasehold has {} Years remaining on the agreement"
     },

 } ,
'rent_value' : {

     'none' : {

         'meaning' : "No Ground Rent value has been stated",
 		"dd_task": ["The discloser must confirm the value of the ground rent if the lease document is not (yet) available for inspection. "],
        "pro_meaning": "No Ground Rent value has been stated"
     },

     'value' : {

         'meaning' : "The Ground Rent value chargeable each year is {}",
 		"dd_task": [""],
        "pro_meaning": "The Ground Rent value chargeable each year is {}"
     },

 } ,
'ground_rent_increase_bool' : {

     'empty' : {
         'meaning' : ["It is not stated whether the lease specifies when the Ground Rent will be increased",],
 		"dd_task": ["Inspect the lease agreement to verify if the date of the next ground rent increase is stated",
                    "Enter in MTD Ledger"],
        "pro_meaning": "It is not stated whether the lease specifies the date Ground rent will be increased"
     },

     'yes' : {

         'meaning' : ["The date of each Ground Rent increase is specified in the lease agreement", 
                    "Enter in MTD Ledger"],
 		"dd_task": ["Inspect the lease agreement and identify the date of the next Ground Rent increase", 
                    "Enter in MTD Ledger"],
        "pro_meaning": "The frequency of each Ground Rent increase is specified in the lease agreement"
     },

     'no' : {

         'meaning' : "The date of each Ground Rent increase is not specified in the lease agreement",
 		"dd_task": ["Inspect the Leasehold agreements to identify where the frequency of Ground Rent increases is specified", "Enter in MTD Ledger"],
        "pro_meaning": ["The date of each Ground Rent increase is not specified in the lease agreement",
                        "Other documentation must be located to verify the date any Ground Rent will increase"]
     },

 } ,
'ground_rent_increase_date' : {

     'none' : {

         'meaning' : "The date of any Ground Rent increase has not been stated",
 		"dd_task": ["Inspect the Lease document to verify the date of the next ground rent increase", 
                    "Enter in MTD Ledger"],
        "pro_meaning": "The date of the next Ground Rent increase has not been stated"
     },

     'value' : {

         'meaning' : "The next Ground Rent increase occurs on the: {}",
 		"dd_task": [""],
        "pro_meaning": "The next Ground Rent increase occurs on the: {}"
     },

 } ,
'ground_rent_increase_frequency' : {

     'none' : {

         'meaning' : "The frequency of Ground Rent increase is not specified",
 		"dd_task": ["A declaration from the Freeholder is required to verify the frequency of any Ground Rent increase "],
        "pro_meaning": "The frequency of Ground Rent increase is not unspecified"
     },

     'value' : {

         'meaning' : "Ground Rent increases take place: {}",
 		"dd_task": [""],
        "pro_meaning": "Ground Rent increases take place: {}"
     },

 } ,
'rent_increase_type' : {

     'empty' : {

         'meaning' : "The Type of Rent Increase has not been specified",
 		"dd_task": ["In the absence of confirmation within the lease document a declaration from the Freeholder is required to verify the Type of Rent Increase applicable"],
        "pro_meaning": "The Type of Rent Increase has not been specified"
     },

     'Fixed' : {

         'meaning' : "The Ground rent increase is fixed",
 		"dd_task": [""],
        "pro_meaning": "The Ground rent increase is fixed"
     },

     'Variable' : {

         'meaning' : "Ground Rent increases are variable and not fixed",
 		"dd_task": [""],
        "pro_meaning": "Ground Rent increases are variable and not fixed"
     },

     'Other' : {

         'meaning' : "The type of rent increase has been defined as:{}",
 		"dd_task": [""],
        "pro_meaning": "The type of rent increase has been defined as:{}"
     },

 } ,
'rent_increase_type_details' : {

     'true' : {

         'meaning' : "Extra information has been provided regarding the rent increase type",
 		"dd_task": ["Ensure the increment by which rent increase is applied complies with existing regulations", 
                    "Enter in MTD Ledger"],
        "pro_meaning": "Extra information has been provided regarding the rent increase type"
     },

     'false' : {

         'meaning' : "No extra information has been provided regarding the rent increase type",
 		"dd_task": ["Unless the Rent Increase Type is specified within the lease the rent increase type must be confirmed by the Freeholder"],
        "pro_meaning": "No extra information has been provided regarding the rent increase type"
     },

 } ,
'service_charge_bool' : {

     'empty' : {

         'meaning' : [ "It has not been confirmed that Service charge payments have been paid and are currently up to date",
                        ""],
 		"dd_task": ["Confirmation from the Freeholder or managing agent is required to determine if service charge payments have been paid and are currently up to date"],
        "pro_meaning": "It has not been confirmed that Service charge payments have been paid and are currently up to date"
     },

     'yes' : {

         'meaning' : "Service charge payments have been paid and are currently up to date",
 		"dd_task": ["Locate a statement of the service charges balance confirming the account status as satisfied",
                    "Confirm in MTD Ledger"],
        "pro_meaning": "Service charge payments have been paid and are currently up to date"
     },

     'no' : {

         'meaning' : "The Service Charges now due have not been paid",
 		"dd_task": ["Confirmation of Service Charge account status can be obtained from the freeholder or associated managing agent",
                    "Obtain a contemporaneous Service Charge statement detailing all outstanding fees, costs and charges"],
        "pro_meaning": "The Service Charges now due have not been paid"
     },

 } ,
'last_service_charge' : {

     'none' : {

         'meaning' : "The value of the last service charge has not been specified",
 		"dd_task": ["Obtain a Service Charge statement detailing all outstanding fees, costs and charges",
                    "The service charge statement can be obtained from the freeholder or associated managing agent"],
        "pro_meaning": "In the absence of a budget for future service charges the purchaser may be exposed to substantial unforseen costs and potential stress",
     },

     'value' : {

         'meaning' : "The value of the last service charge was:£{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_budget_bool' : {

     'empty' : {

         'meaning' : "No budget has been provided for the next due service charge",
 		"dd_task": ["A forecast or budget for the next Service Charges can be obtained from the freeholder or associated managing agent"],
        "pro_meaning": "In the absence of a budget for future service charges the purchaser may be exposed to substantial unforseen costs and potential stress",
     },

     'yes' : {

         'meaning' : "A budget for the next due service charge has been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "A budget for the next due service charge is not available",
 		"dd_task": ["Verify the reason for the absence of a formal budget and obtain a prospective estimated budget"],
        "pro_meaning": "In the absence of a budget for future service charges the purchaser may be exposed to substantial unforseen costs and potential stress",
     },

 } ,
'service_charge_bill_docu' : {

     'true' : {

         'meaning' : "Documentation regarding the service charge has been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "No documentation has been provided in regards to the service charge",
 		"dd_task": ["In the absence of a declaration from the vendor a verification from the Freeholder or managing agent will be required"],
        "pro_meaning": ""
     },

 } ,
'service_charge_payments_due' : {

     'none' : {

         'meaning' : "No service charge payments are due.",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "The next payment is due on {}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_pay_reciever' : {

     'empty' : {

         'meaning' : "It has not been specified who receives the service charge",
 		"dd_task": ["Identify the designated recipient of Service Charges to ensure the purchaser can comply with lease obligations"],
        "pro_meaning": ""
     },

     'agent' : {

         'meaning' : "Service charges are payable to the Agent",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'landlord' : {

         'meaning' : "Service charges are payable to the Landlord",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'freehold_company' : {

         'meaning' : "Service charges are payable to a Freehold Company",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'resi_assoc' : {

         'meaning' : "Service charges are payable to the Residential Association",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_organisation' : {

     'none' : {

         'meaning' : "The organisation responsible for collecting the Service Charge has not been specified",
 		"dd_task": ["Identify the designated recipient of Service Charges to ensure the purchaser can comply with lease obligations"],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "the organization responsible for collecting the service charge is the {} and the postable adress is as follows",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_Building_name' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_street_no' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_street_name' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_town_or_city' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'service_charge_postcode' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'first_to_occupy' : {

     'empty' : {

         'meaning' : "It has not been specified if the Vendor was the first occupant of the property since it was built or converted",
 		"dd_task": ["FCA regulations require lenders to determine the first occupant status: this first occumant status must be determine to ensure funding requirements can be exercised without delay or compliance risk"],
        "pro_meaning": "The absence of first occupant status is an FCA compliance obligation and will be required by the purchaser to comply with lending security requirements (if relying upon a mortgage)",
     },

     'yes' : {

         'meaning' : "The Vendor has been the first occupant of the property since it was built or converted",
 		"dd_task": ["Ensure all compliance requirements associated with conversion or construction have been achieved"],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The Vendor is not the first occupant of the property since it was built or converted",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'warranties_docu' : {

     'true' : {

         'meaning' : "Documentation regarding the warranties has been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "There are no details of the warranties and guarantees",
 		         "dd_task": ["Ensure all compliance requirements associated with any conversion or construction have been achieved"],
        "pro_meaning": ""               
        #    any planning consents or other planning documents that might have been available at the time of construction or conversion",

     },

 } ,
'property_dependant' : {

     'empty' : {

         'meaning' : "The vendor has not declared whether the sale of the property is dependent on the purchase of a seperate property",
 		"dd_task": ["Obtain confirmation from the vendor regarding the dependency of this sale to any other transaction purchase or sale of another property"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The sale is dependent upon the vendor's successful purchase of another property",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The vendor states that the sale of the property is not dependent on the purchase of another property",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'property_dependant_details' : {

     'true' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent transaction need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

 } ,
'school_term' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The sale is dependent upon school calendar commitments and/ or schedules",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'school_term_date' : {

     'none' : {

         'meaning' : "Details of the vendors dependent school term dates need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer",
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "The vendor intends to schedule the sale with reference to the School calendar date: {}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'upcoming_holiday' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule the sale with reference to a forthcoming Holiday",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'upcoming_holiday_date' : {

     'none' : {

         'meaning' : "The date of the forthcoming holiday affecting the sale time has not been described",
 		"dd_task": ["Details of the vendor's dependent upcoming holiday schedule need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "The date of the forthcoming holiday affecting the sale time is {}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'job_move' : {

     'empty' : {

         'meaning' : "The date of the forthcoming job move the sale time has not been described",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to the Job Move date: {}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'job_move_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent job move date and confirmed status need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

 } ,
'redundancy' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a redundancy arrangement",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'redundancy_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'medical' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to Medical commitment",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'medical_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'notice_to_tenant' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to the notice to a tenant",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'notice_to_tenant_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent notice to tenant and confirmed future vacant possession status need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'retirement' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a retirement date",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'retirement_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'build_complete' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a building completion date",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'build_complete_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent build completion date and the confirmed present build progression status need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'other_move_factor' : {

     'empty' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to another/ independent event",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'other_move_factor_date' : {

     'none' : {

         'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent other move factor date and confirmed status need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

 } ,
'other_move_factor_details' : {

     'true' : {

         'meaning' : "The Vendors sale will be impacted by:{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "",
 		"dd_task": ["Details of the vendor's dependent other move factor details need to be verified to evaluate potential; completion risks, impact upon negotiations, ongoing cost, potential delays and associated costs for the buyer"],
        "pro_meaning": ""
     },

 } ,
'works_and_alterations_count' : {
    'value' : {
        'equation':{
            'larger_than' : {
                'vari':1, 
                'meaning':"there have been {} alterations to the property",
                 "dd_task": [""],
                 "pro_meaning": "",
            }
		     }, 
        'default':{
            'meaning' : "there have been alterations to the property",
            "dd_task": ["A schedule of alterations needs to be obtained from the vendor confirming the date of each work undertaken, the alteration's completion and conformity status"],
            "pro_meaning": ""
		  }
    }
 } ,
'planning_breach' : {

     'empty' : {

         'meaning' : "It has not been specified if any breaches of planning conditions have occurred",
 		"dd_task": ["The vendor must disclose whether any planning conditions have been breached"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "one or more breaches of planning conditions have occurred",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "no breaches of planning conditions have occurred",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'planning_breach_details' : {

     'true' : {

         'meaning' : "A written description of planning breach details has been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "No description of the breaches of planning conditions that have occurred at this property have been disclosed",
 		"dd_task": ["The nature of each breach needs to be disclosed by the vendor, including: the date of each breach, whether the has been observed or recorded by a planning officer, whether enforcement has been applied"],
        "pro_meaning": ""
     },

 } ,
'bulding_reg_breach' : {

     'empty' : {

         'meaning' : "It has not been stated whether there have been no breaches of Building Regulation conditions",
 		"dd_task": ["A statement from the vendor is required to determine the status of Building Regulations conformity"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "There have been breaches of Building Regulation conditions",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "There have been no breaches of Building Regulation conditions",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'bulding_reg_breach_details' : {

     'true' : {

         'meaning' : "Details of the building regulation breaches have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "There has been no provision of details regarding the building regulation breaches that have occured at this property",
 		"dd_task": ["A statement from the vendor is required to determine details of the Building Regulations breach: including: the date of each breach, whether the has been observed or recorded by a planning officer, whether enforcement has been applied"],
        "pro_meaning": ""
     },

 } ,
'unfinished_work' : {

     'empty' : {

         'meaning' : "It has not been stated whether any works have been undertaken that presently remain unfinished",
 		"dd_task": ["A statement from the vendor is required to confirm whether any works have been undertaken that presently remain unfinished"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "Works have been undertaken that remain unfinished",
 		"dd_task": [""],
        "pro_meaning": "Unfinished building works at this property may not meet building standards",
     },

     'no' : {

         'meaning' : "There have been no works undertaken that remain unfinished",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'unfinished_work_details' : {

     'true' : {

         'meaning' : "Details of the unfinished building works at this property have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "There has been no provision of details regarding the unfinished building work at this property",
 		"dd_task": ["A statement from the vendor is required to confirm each of the works that have been undertaken that presently remain unfinished"],
        "pro_meaning": "There ae incomplete building works for which it is possible building regulations conformity has not been achieved",
     },

 } ,
'consent_lack' : {

     'empty' : {

         'meaning' : "It has not been stated whether any works have been undertaken that lack all necessary consent",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "Works have been undertaken that lack all necessary consent",
 		"dd_task": ["Determine the nature of the missing consents"],
        "pro_meaning": "The actuality of works without the necessary consents may expose the purchaser to; enforcement action , potential regularisation costs,lending security delays, indemnity costs (where avaialable), potenital transaction failure ",
     },

     'no' : {

         'meaning' : "No works have been undertaken that lack all necessary consent",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'consent_lack_details' : {

     'true' : {

         'meaning' : "Details have been provided regarding the works undertaken without all necessary consent",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Details have not been provided regarding the works that have been undertaken without necessary consent",
 		"dd_task": ["Determine the nature of the missing consents"],
        "pro_meaning": "The actuality of works undertaken without the necessary consents may expose the purchaser to; enforcement action , potential regularisation costs,lending security delays, indemnity costs (where avaialable), potenital transaction failure if these details are not declared",
     },

 } ,
'solar_panels_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether any solar panels have been installed",
 		"dd_task": ["Determine whether solar panels have been installed"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "Solar panels have been installed at the property",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "Solar panels have not been installed at the property",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'solar_installation_year' : {

     'none' : {

         'meaning' : "It has not been stated in which year the Solar panels were installed at the property",
 		"dd_task": ["Determine the year Solar panels were installed"],
        "pro_meaning": ""
     },

     'value' : {

         'meaning' : "Solar panels were installed at the property:{}",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'solar_panels_ownership_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the solar panels are owned outright",
 		"dd_task": ["The vendor must disclose whether the solar panels are owned outright "],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The solar panels are owned outright",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The solar panels are not owned outright",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'solar_panels_long_lease_ownership_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether a long lease of the roof / air space has been granted to a solar panel provider",
 		"dd_task": ["Determine how long the long lease of the roof / air space has been granted to the provider"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "A long lease of the roof / air space has been granted to a solar panel provider",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "No long lease of the roof / air space has been granted to a solar panel provider",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'solar_electrical_tarrif_docu' : {

     'true' : {

         'meaning' : "Documentation regarding the solar electrical tariff or other information regarding the solar panel array at the property has been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Documentation regarding the solar electrical tariff or other information regarding the solar panel array at the property has not provided",
 		"dd_task": ["The vendor must disclose the applicable solar electric tariff assigned to this sola panel array"],
        "pro_meaning": ""
     },

 } ,
'protected_buildings_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the property (or any part of it) listed in the National Heritage List for England",
 		"dd_task": ["The vendor should be asked to disclose and assigned listed property status in the National Heritage List for England"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The property (or a part of it) is listed in the National Heritage List for England",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The property (or any part of it) is not listed in the National Heritage List for England",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known if the property (or a part of it) is listed in the National Heritage List for England",
 		"dd_task": ["The vendor should be asked to disclose and assigned listed property status in the National Heritage List for England"],
        "pro_meaning": ""
     },

 } ,
'protected_buildings_docu' : {

     'true' : {

         'meaning' : "Documents relating to the property's protected Building Status have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Documents relating to the property's Protected Building status have not been provided",
 		"dd_task": ["The vendor should disclose any documents concerning the property documents relating to the National Heritage List for England"],
        "pro_meaning": ""
     },

 } ,
'conservation_area_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the property (or any part of it) is in a conservation area",
 		"dd_task": ["The vendor should disclose if any part of the property is located within a conservation area"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The property (or a part of it) is in a conservation area",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "Neither the property or any part of it is in a conservation area",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known if the property (or any part of it) in a conservation area",
 		"dd_task": ["The vendor should disclose any documents concerning the property documents relating to the conservation area"],
        "pro_meaning": ""
     },

 } ,
'conservation_area_docu' : {

     'true' : {

         'meaning' : "Details of the Conservation area have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Details of the Conservation area have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'TPO_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether any trees on the property are subject to a Tree Preservation Order",
 		"dd_task": ["The vendor should disclose if any trees on the property have been identified and protected by a Tree Preservation Order"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "Trees on the property are subject to Tree Preservation Order controls",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "No trees on the property are subject to a Tree Preservation Order",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "The vendor should disclose if any trees on the property have been identified and protected by a Tree Preservation Order",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'order_terms_complied_with' : {

     'empty' : {

         'meaning' : "It has not been stated whether the terms of the Tree Preservation Order have been complied with",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The terms of the Tree Preservation Order have been complied with",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The terms of the Tree Preservation Order have not been complied with",
 		"dd_task": ["The Tree Preservation Order (TPO) terms that have not been obeyed need to be disclosed by the vendor"],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known if the terms of the Tree Preservation Order have been complied with",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
 'TPO_docu':{

     'true' : {

         'meaning' : "Details of the TPOs have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Details of the TPOs have not been provided",
 		"dd_task": ["The applicable TPO conditions and related compliance issues need to be disclosed"],
        "pro_meaning": ""
     },

 } ,
'all_required_consents' : {

     'empty' : {

         'meaning' : "It has not been stated whether consent has been obtained for any matters that need permission",
 		"dd_task": [""],
        "pro_meaning": "The vendor must declare the consent has not been obtained for any matters that need permission",
     },

     'yes' : {

         'meaning' : "Consent has been obtained for any matters that need permission",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "Consent has not been obtained for any matters that need permission",
 		"dd_task": ["Consent should be obtained for any matters that need permission"],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known if consent has been obtained for any matters that need permission",
 		"dd_task": ["Consent should be obtained for any matters that need permission"],
        "pro_meaning": ""
     },

 } ,
'all_required_consents_details' : {

     'true' : {

         'meaning' : "Details of the consents have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Details concerning required consents have not been provided",
 		"dd_task": ["Details of the matters that require consents need to be provided by the vendor"],
        "pro_meaning": ""
     },

 } ,
'charges_bool' : {

     'empty' : {

         'meaning' : " It has not been stated whether the property owner is required to pay any charges relating to the property (apart from council tax, utility charges etc",
 		"dd_task": [" The vendor must confirm whether the property owner is required to pay any charges relating to the property"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The property owner is liable to pay charges relating to the property (apart from council tax, utility charges etc) ",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The property owner is not liable to pay charges relating to the property (apart from council tax, utility charges etc)",
 		"dd_task": [""],
        "pro_meaning": ""
     },

 } ,
'charges_details' : {

     'true' : {

         'meaning' : "Details of the charges have been provided",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'false' : {

         'meaning' : "Details have not been provided in relation to the charges imposed on the owner",
 		"dd_task": [" The vendor must confirm whether the property owner is required to pay any charges relating to the property"],
        "pro_meaning": ""
     },

 } ,
'maintain_road_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether there is an obligation to pay anything towards the costs of maintaining roads, footpaths or other facilities",
 		"dd_task": ["The vendor must confirm whether the property owner has an obligation to pay anything towards the costs of maintaining roads, footpaths or other facilities"],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "There is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "There is no obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known whether there is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",
 		"dd_task": ["The lease must be inspected or the freeholder needs to determine whether the property owner has an obligation to pay anything towards the costs of maintaining roads, footpaths or other facilities"],
        "pro_meaning": ""
     },

 } ,
'maintain_road_payement_details' : {

     'true' : {

         'meaning' : "Details of the Road maintenance payment have been provided",
 		"dd_task": ["Inspect the disclosure to ensure the provisioned data provides an clear indication of frequency and cost calculations"],
        "pro_meaning": "Under disclosure of costs contributions often result in protracted renegotiation and or abandonment of the transaction"
     },

     'false' : {

         'meaning' : "Details of the Road maintenance payment have not been provided",
 		"dd_task": ["Details of any Road maintenance payment needs to be provided "],
        "pro_meaning": "It is essential to disclose to a prospective buyer any potential costs that may arise in relation to the access to the property"
    
     },

 } ,
'private_road' : {

     'empty' : {

         'meaning' : "It has not been specified if the property is on a private road or is located on a road that gives access to or adjoins the property from a private road",
 		"dd_task": ["The private or public status of the road providing access to the property needs to be determined."],
        "pro_meaning": ""
     },

     'yes' : {

         'meaning' : "The property is on a private road or is the road that gives access to or adjoins the property a private road",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The property is not on a private road or is the road that gives access to or adjoins the property a private road",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'not_known' : {

         'meaning' : "It is not known if the property is on a private road or is on a road that gives access to or adjoins the property from a private road",
 		"dd_task": ["The private or public status of the road providing access to the property needs to be determined."],
        "pro_meaning": ""
     },

 } ,
'public_expense_road' : {

     'empty' : {

         'meaning' : "It has not been specified whether the roads leading to the property are maintained at public expense",
 		"dd_task": ["it needs to be determined whether the road providing access to the property is maintained at public expense"],
        "pro_meaning": "It is essential to disclose to a prospective buyer any potential costs that may arise in relation to the access to the property"
    
     },

     'yes' : {

         'meaning' : "The roads leading to the property are maintained at public expense",
 		"dd_task": [""],
        "pro_meaning": ""
     },

     'no' : {

         'meaning' : "The roads leading to your property are maintained at public expense",
 		"dd_task": ["Determine how the maintenance of the road leading to the property is funded"],
        "pro_meaning": "It is essential to disclose to a prospective buyer any potential costs that may arise in relation to the access to the property"
     },

     'not_known' : {

         'meaning' : "It is not known if the roads leading to the property are maintained at public expense",
 		"dd_task": ["The leasehold contract, the freeholder or public authority need to be consulted to determine whether the road providing access to the property is maintained at public expense"],
        "pro_meaning": ""
     },

 } ,

'mains_drainage' : {

 	 'empty' : {  

 		 'meaning' : "It has not been stated whether the property benefits from a mains drainage network connection",
 		"dd_task": ["The vendor needs to confirm whether the property is connected to mains drainage",
                    "If connected, identify the sellers satisfaction and any relevant performance history with the mains drainage supply",
                    "If not connected, determine whether any prior proposition to connect to the mains drainage network has been abandoned or declined"],
        "pro_meaning": ["A failure to disclose any deficiencies concerning the reliability, provision and or quality of the mains drainage may result in a Seller liability and professional indemnity exposure",
                        "A failure to disclose any practical or financial barriers preventing the connection to the mains drainage network may result in a Seller liability and professional indemnity exposure]"]
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a mains drainage network",
 		"dd_task": ["Identify the sellers satisfaction and any relevant performance history with the mains drainage supply"],
        "pro_meaning": ["A failure to disclose any deficiencies concerning the reliability, provision and or quality of the electricity supply may result in a Seller liability and professional indemnity exposure",
                        ""]
 	 },

 	 'no' : {

 		 'meaning' : "The property does not have a mains drainage network connection",
 		"dd_task": ["Determine whether any prior proposition to connect to the mains drainage network has been abandoned or declined"],
        "pro_meaning": ["A failure to disclose any practical or financial barriers preventing a connection to the mains drainage network may result in a Seller liability and professional indemnity exposure"],
 	 },

 } ,
'electricity' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to an electrical supply",
 		"dd_task": ["The vendor needs to confirm whether the property is connected to mains electricity",
                    "Determine whether any prior proposition to connect to the mains electricity network has been abandoned or declined"],
        "pro_meaning": ["A failure to disclose any deficiencies concerning the reliability, provision and or quality of the electricity supply may result in a Seller liability and professional indemnity exposure",
                        ""]
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a mains electricity supply",
 		"dd_task": ["Identify the sellers satisfaction and any relevant performance history with the electricity supply"],
        "pro_meaning": "A failure to disclose any deficiencies concerning the reliability, provision and or quality of the electricity supply may result in a Seller liability and professional indemnity exposure",
                        
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to a mains electricity supply",
 		"dd_task": ["It should be determined whether the infrastructure required to support a live connection to the mains electricity supply is installed at the property"],
        "pro_meaning": ["A failure to disclose any deficiencies concerning the reliability, provision and or quality of the electricity supply may result in a Seller liability and professional indemnity exposure",
                        "A failure to disclose any practical or financial barriers preventing the provision of the electricity supply may result in a Seller liability and professional indemnity exposure"]
 	 },

 } ,
'water_supply' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a water supply",
 		"dd_task": ["The vendor needs to confirm whether the property benefits from a connection to a water supply",
                    "Identify the sellers satisfaction and any relevant performance history with the water supply supply"],
        "pro_meaning": ["A failure to disclose any deficiencies concerning the provision and or quality of an existing water supply may result in a Seller liability and professional indemnity exposure"
                    "A failure to disclose any practical or financial barriers preventing the provision of a mains water supply may result in a Seller liability and professional indemnity exposure",]
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a water supply",
 		"dd_task": ["Confirm the quality, reliability and pressure of the water supply",
                    "Identify the sellers satisfaction and any relevant performance history with the water supply"],
        "pro_meaning": "A failure to disclose any deficiencies concerning the provision and or quality of the water supply may result in a Seller liability and professional indemnity exposure",
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to a water supply",
 		"dd_task": ["It should be determined whether the infrastructure required to support a mains water supply is installed at the property"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of a mains water supply may result in a Seller liability and professional indemnity exposure",
 	 },

 } ,
'gas' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a mains gas supply",
 		"dd_task": ["The vendor needs to confirm whether the property benefits from a connection to a mains gas supply"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of mains gas may result in a Seller liability and professional indemnity exposure",
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a mains gas supply",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to a mains gas supply",
 		"dd_task": [""],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of mains gas may result in a Seller liability and professional indemnity exposure",
 	 },

 } ,
'broadband' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a broadband connection",
 		"dd_task": ["The vendor should confirm whether the property benefits from a broadband connection"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of Broadband may result in a Seller liability and professional indemnity exposure"
 	 },

 	 'yes' : {

 		 'meaning' : "The property has the benefit of a broadband connection",
 		"dd_task": ["Determine the mode of connectivity by which the broadband connection is provided"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not currently benefit from a broadband connection",
 		"dd_task": ["The vendor needs to confirm whether the property has previously benefited from a broadband connection and the speed of the connection"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of a broadband may result in a Seller liability and professional indemnity exposure"
 	 },

 } ,
'sewage_plant' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a private sewage plant",
 		"dd_task": ["The vendor needs to confirm whether the property benefits from a connection to a private sewage plant"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of a private sewage plant may result in a Seller liability and professional indemnity exposure"
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a private sewage plant",
 		"dd_task": ["The specification of the private sewage plant together with arrangements for maintenance and service charges need to be disclosed "],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefits from a private sewage plant",
 		"dd_task": ["In the absence of a viable mains sewage connection confirm the property is capable of sustaining a private sewage plant"],
        "pro_meaning": ""
 	 },

 } ,
'telephone_landlines' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Telephone Landlines",
 		"dd_task": ["Determine from the seller whether a telephone line is now or has previously been installed"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of a telephone may result in a Seller liability and professional indemnity exposure",
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection Telephone Landlines",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not have connection to Telephone Landlines",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'solar_panels' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Solar Panels",
 		"dd_task": ["Determine the existing and the potential solar capacity for this property",
                    ],
        "pro_meaning": ["A failure to disclose any practical or financial barriers preventing the provision of Solar Panels may result in a Seller liability and professional indemnity exposure",
                        "Buyers seeking to implement or enhance sustainability credentials can expect disclosure of the potential solar capacity"]
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from connected Solar Panels",
 		"dd_task": ["Identify whether there is sufficient space to increase the number of solar panels on the existing mounting location"],
        "pro_meaning": "Buyers seeking to improve the sustainability credentials can expect disclosure of the potential solar capacity "
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to solar panels",
 		"dd_task": ["Determine whether information is available to confirm whether the property contains the necessary attributes to support a viable installation of solar panels"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of Solar Panels may result in a Seller liability and professional indemnity exposure"
 	 },

 } ,
'heat_pumps' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Ground or Air Heat Pumps",
 		"dd_task": ["Confirmation of any installed Ground or Air Heat Pumps is required including their operational status"],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of Ground or Air Heat Pumps may result in a Seller liability and professional indemnity exposure"
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from connected Ground or Air Heat Pumps",
 		"dd_task": ["Confirmation of the operational status o any installed Ground or Air Heat Pumps is required",
                    "Confirmation of condition, operating performance / capacity, servicing cost and warranty is desirable "],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from the connection of Ground or Air Heat Pumps",
 		"dd_task": [""],
        "pro_meaning": "A failure to disclose any practical or financial barriers preventing the provision of Ground or Air Heat Pumps may result in a Seller liability and professional indemnity exposure"
 	 },

 } ,
'other_provisioned_services' : {

 	 'empty' : {

 		 'meaning' : "No other additional provisioned services have been disclosed",
 		"dd_task": ["Confirmation of any additional provisioned service is required (type, active status, periodic operational cost)"],
        "pro_meaning": ["If the property does not benefit from any other provisioned services there is a riding obligation to confirm",
                    "Buyers can reasonably expect to be notified of any service; sought but not installed,  the reason the service was not installed",
                    "A failure to disclose any practical or financial barriers preventing a service provision may result in a Seller liability and professional indemnity exposure "]
 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from additional provisioned services not already mentioned",
 		"dd_task": ["Confirmation of any additional provisioned service is required (type, active status, periodic operational cost)"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from any other provisioned services beyond those already disclosed",
 		"dd_task": ["Where commonly provisioned services are absent but desired by the purchaser a confirmation of availability may be considered appropriate", 
                    "Where a commonly available or trending emergent service is not in place identify whether the application was declined or refused"],
        "pro_meaning": ["The property does not benefit from any other provisioned services",
                    "Buyers can reasonably expect to be notified of any service; sought but not installed,  the reason the service was not installed",
                    "A failure to disclose any practical or financial barriers preventing a service provision may result in a Seller liability and professional indemnity exposure"]
 	 },

 } ,
'other_provisioned_services_details' : {

 	 'true' : {

 		 'meaning' : "Details regarding the additional provisioned services have been provided",
 		"dd_task": ["The details provided should be checked to confirm all additional services were included in the data provided",
                    "Check each service disclosure contains appropriate data (such as)  ; performance, operating or periodic cost, and other data "],
        "pro_meaning": "Confirmation of the additional provisioned services has been provided",
 	 },

 	 'false' : {

 		 'meaning' : "No details regarding the additional provisioned services have been provided",
 		"dd_task": ["Details of additional provisioned services must be provided to a prospective buyer"],
        "pro_meaning": ["Confirmation of the additional provisioned services has not yet been provided",
                        "the existence of other services will be deemed material information to the Material Title Disclosure",
                        "undisclosed installed services may impact upon a buyer and the viability and or cost of execute plans",
                        "failure to disclose services may create a seller liability and exposure to Professional Liability claim "],
 	 },

 } ,
'shared_facilities_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether there are any areas or facilities shared with neighbour (excluding common parts of a leasehold block or estate)",
 		"dd_task": ["Any areas or facilities shared with neighbour should be confirmed by the vendor, in the absence of disclosure, confirmation may be obtained from the freeholder or managing agent"],
        "pro_meaning": ["A prospective buyer will reasonably expect declaration of any shared facilities",
                        "Absence of a declaration of shared services may be sufficient to found a claim in the event the property is later considered devalued or a transaction does not proceed after identifying a shared facility status"]
 	 },

 	 'yes' : {

 		 'meaning' : "There are areas or facilities shared with neighbour (excluding common parts of a leasehold block or estate)",
 		"dd_task": ["The areas or facilities shared with neighbour should be confirmed" ,
                    "in the absence of disclosure, confirmation may be obtained from the freeholder or managing agent"],
        "pro_meaning": "The property does share areas or facilities with neighbour "
 	 },

 	 'no' : {

 		 'meaning' : "There are not any areas or facilities shared with neighbour (excluding common parts of a leasehold block or estate)",
 		"dd_task": [""],
        "pro_meaning": "  "
 	 },

 } ,
'shared_facilities_text_details' : {

 	 'true' : {

 		 'meaning' : "Details of the shared facilities have been provided",
 		"dd_task": ["Determine which facilities are shared and the terms applicable to their use."],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "No details of the facilities this property shares with other properties have been provided",
 		"dd_task": ["A plan showing the location of facilities this property shares with other properties should be disclosed"],
        "pro_meaning": "The mode, convenience and impact of shared facilities may impact a buyers evaluation of the property, full details should be established"
 	 },

 } ,
'parking_arrangement_details' : {

 	 'true' : {

 		 'meaning' : "Details regarding the parking arrangements of the property have been provided",
 		"dd_task": ["Determine from the parking arrangement details provided: annual costs, restrictions and limitations, assignment and usage conditions "],
        "pro_meaning": "Information has been provided regarding parking arrangements: the detail and completeness of data needs to be assessed",
 	 },

 	 'false' : {

 		 'meaning' : "Details regarding the parking arrangements assigned to the property has not been provided",
 		"dd_task": ["Details regarding the parking arrangements for the property should be provided"],
        "pro_meaning": "The benefit and burdens of parking arrangements at the property cannot be fully determined without further information.",
 	 },

 } ,
'controlled_parking' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed whether the property is in a controlled parking zone or within a local authority parking scheme",
 		"dd_task": ["Details of any controlled parking arrangements for the property should be provided"],
        "pro_meaning": ["The impact of controlled parking upon the convenience or enjoyment and value of the property cannot be determined without further information",
                        ""]
 	 },

 	 'yes' : {

 		 'meaning' : "The property is in a controlled parking zone or within a local authority parking scheme",
 		"dd_task": ["Details of the controlled parking arrangements should be provided"],
        "pro_meaning": "The impact of controlled parking upon the convenience or enjoyment and value of the property cannot be determined without further information",
 	 },

 	 'no' : {

 		 'meaning' : "The property is not in a controlled parking zone or within a local authority parking scheme",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'not_known' : {

 		 'meaning' : "The disclosure provider does not know if the property is in a controlled parking zone or within a local authority parking scheme",
 		"dd_task": ["The local authority and any private road management agent may determine the location of any controlled parking zone "],
        "pro_meaning": "The impact of controlled parking upon the convenience or enjoyment and value of the property cannot be determined without further information",
 	 },

 } ,
'live_at_prop_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether the disclosure provider lives at the property",
 		"dd_task": ["The discloser should declare if they reside at the property",
                        "A person making a disclosure and not resident should clarify their familiarity and level of knowledge of the property"
                        "Determine whether the discloser has a detailed knowledge of the; property history, the locality, events that have effected the property and residents thereto "],
        "pro_meaning": ["Without further information the discloser has not at face value established they are able to make a comprehensive statement regarding all details about the property",
                        "Professionals are on warning to carefully consider the likely transparency and clarity the disclosures can provide if the provider has and or does not live at the property "]
 	 },

 	 'yes' : {

 		 'meaning' : "The disclosure provider lives at the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The disclosure provider does not live at the property",
 		"dd_task": ["The person making this disclosure should clarify their familiarity and level of knowledge of the property"],
        "pro_meaning": "Without further information the discloser has not at face value established they are able to make a comprehensive statement regarding all details about the property",
 	 },

 } ,
'over_17_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether anyone other then the disclosure provider aged 17 or over live at the property",
 		"dd_task": ["Confirm whether any other person aged 17 or over lives at this property"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "Individuals other then the disclosure provider aged 17 (or over) do live at the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "No other individuals other then the disclosure provider aged 17 or over live at the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'over_17_count' : {
	 'value' : {

	 	 'meaning' : "There are currently {} individuals aged 17 or over living at the property",
 		"dd_task": [""],
        "pro_meaning": ""
	 },

 } ,
'lodgers_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether any of the occupiers aged 17 or over (other then the disclosees) are tenants or lodgers",
 		"dd_task": ["Confirmation is required to determine if any occupiers aged 17 or over (other then the disclosees) are tenants or lodgers at this property"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "Some or all of the occupiers aged 17 or over are tenants or lodgers",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "None of the occupiers aged 17 or over are tenants or lodgers",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'agree_to_leave_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed whether all the occupiers aged 17 and over have agreed to leave before completion",
 		"dd_task": ["The vendor must disclose whether all the occupiers aged 17 and over have agreed to leave before completion"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "All of the occupiers aged 17 and over have agreed to leave the property before completion of the sale",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "Not all or none of occupiers aged 17 and over have agreed to leave the property before completion of the sale",
 		"dd_task": ["More information is required to determine why the occupier/s aged 17 and over have not agreed to leave before completion",
                     "An undertaking by the occupiers to leave the property before the property sale completion takes place will be required"],
        "pro_meaning": " "
 	 },

 } ,
'occupiers_contract_sign_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed whether all the occupiers aged 17 and over have agreed to sign the sale contract",
 		"dd_task": ["Confirmation is required that all the occupiers aged 17 and over have agreed to sign the sale contract"],
        "pro_meaning": "A liability may arise if this matter remains unresolved and subsequently results in delays costs or abandonment of the transaction"
 	 },

 	 'yes' : {

 		 'meaning' : "All the occupiers aged 17 and over have agreed to sign the sale contract",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "Not all or none of the occupiers aged 17 and over have agreed to sign the sale contract",
 		"dd_task": ["Confirmation is required that all the occupiers aged 17 and over have agreed to sign the sale contract"],
        "pro_meaning": ""
 	 },

 } ,
'vacant_possession_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether this property is being sold with vacant possession",
 		"dd_task": ["Confirmation is required that this property is being sold with vacant possession"],
        "pro_meaning": "Professionals acting in this transaction may be exposed to liability should transaction delays or costs or abandonment transpire because vacant possession cannot be achieved and insufficient inquiries have been pursued with regard thereto"
 	 },

 	 'yes' : {

 		 'meaning' : "This property is being sold with vacant possession",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "This property is not being sold with vacant possession",
 		"dd_task": ["Confirmation is required detailing why this property is not being sold with vacant possession",
                    "Details are required of the tenure and status of any occupier of the property that intends to remain at the property after the sale"],
        "pro_meaning": ""
 	 },

 } ,
'vacant_possession_proof_docu' : {

 	 'true' : {

 		 'meaning' : "Documentation has been provided as proof that this property will be sold with vacant possession",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "Documentation has not been provided as proof that this property will be sold with vacant possession",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'flooding_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether this property has ever flooded",
 		"dd_task": ["Undertake independent checks to assess whether local flood risks exist,"
                    "Determine whether there is a history of flooding in the area"],
        "pro_meaning": "All professionals acting in this transaction must exhibit extra care to identify any previous flood event and continues flood risk"
 	 },

 	 'yes' : {

 		 'meaning' : "This property has previously suffered flooding",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "This property has as far as is known not suffered from flooding",
 		"dd_task": ["Verify whether the discloser has a local knowledge (and for how long) to determine the extent of their awareness of local flood events"],
        "pro_meaning": "Professionals with local knowledge and access to verification tools to identify local flood events not known to the discloser"
 	 },

 } ,
'flood_events_count' : {
	 'value' : {

	 	 'meaning' : "There have been {} known flood events recorded at this property",
 		"dd_task": [""],
        "pro_meaning": ""
	 },

 } ,
'flood_risk_report_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether a flood risk report has been created for the property",
 		"dd_task": ["If a flood report cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "A flood risk report has been created for the property",
 		"dd_task": [""],
        "pro_meaning": "Ensure the flood risk report is clearly referenced in the Market Particulars"
 	 },

 	 'no' : {

 		 'meaning' : "A flood risk report has not been created for the property",
 		"dd_task": ["Determine from the discloser whether any mitigations measures have been undertaken to negative the flood risk "],
        "pro_meaning": "Buyers can expect Professionals to provide clarity regarding the existence of any recurrent flood risks "
 	 },

 } ,
'flood_risk_report_docu' : {

 	 'true' : {

 		 'meaning' : "",
 		"dd_task": ["Check documentation to identify any obvious omissions",
                    "If a flood report cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity",
                    "Determine whether any insurance claims documentation is available from the flood incident",
                    "Determine whether any repair works documentation or warranty certificates are available from repairs "],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": ["A copy of a food report is required",
                    "If a flood report cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity",
                    "Determine whether any insurance claims documentation is available from the flood incident",
                    "Determine whether any repair works documentation or warranty certificates are available from repairs "],
        "pro_meaning": "Most floods result in documentation, an under-disclosure of flood events may lead to profound liability implications"
 	 },

 } ,
'nearby_development_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed if any of the disclosure providers have been told about plans for any building or developments that might affect someone's ability to peacefully use and enjoy the property",
 		"dd_task": ["A statement is required to confirm if any plans are known of any building or developments that might affect someone's ability to peacefully use and enjoy the property",
                        "If a statement cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom report and or a specialised indemnity"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "There are plans for development or buildings that may affect someone's ability to peacefully use and enjoy the property",
 		"dd_task": ["Check the details for any inadvertent under-disclosure where local development plans are public knowledge but not known by the discloser"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "There are no known plans for development or buildings that may affect someone's ability to peacefully use and enjoy the property",
 		"dd_task": [" "],
        "pro_meaning": ["It may be that local development plans exist that are common knowledge but unknown to the discloser, a duty to assist to remedy any under-disclosure must be assumed"]
 	 },

 } ,
'nearby_development' : {

 	 'true' : {

 		 'meaning' : "",
 		"dd_task": ["Details of the plans for development or buildings that may affect someone's ability to peacefully use and enjoy the property are required",
                    "Check the discloser provides sufficient and accurate details of local plans that may affect the property"],
        "pro_meaning":[ "Agents are deemed to possess an elevated awareness of development within their locale sufficient to impose a duty to disclose nearby development",
                        ""]
 	 },

 	 'false' : {

 		 'meaning' : "No additional documentation has been provided in relation to nearby development",
 		"dd_task": ["Ensure the disclosure of any relevant plans for future local development are notified to prospective buyers"],
        "pro_meaning": "Agents are deemed to possess an elevated awareness of development within their locale sufficient to impose a duty to disclose nearby development"
 	 },

 } ,
'complaints_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether there have been any complaints about the property or a property nearby",
 		"dd_task": ["A statement confirming the existence of any complaints either past and present is required"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "There have been complaints about the property or a property nearby",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "There have not been any known complaints about the property or a property nearby",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'complaints_details' : {

 	 'true' : {

 		 'meaning' : "",
 		"dd_task": ["Details of any complaints past and present are required"],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'disputes_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated if any of the disclosure providers are aware of anything that might lead to a dispute about your property or a property nearby",
 		"dd_task": ["A statement is required to confirm the risk of any factor or matter presently being or developing into a dispute"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "There are things that may lead to a dispute about the property or a property nearby",
 		"dd_task": ["Detailed disclosure of these matters that may cause dispute is required"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "There is nothing known that might lead to a dispute about the property or a property nearby",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'disputes_details' : {

 	 'true' : {

 		 'meaning' : "Details have been provided in relation to the disputes that have arisen",
 		"dd_task": [""],
        "pro_meaning": "Any under disclosure of disputes may have sustained negative implications"
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'knotweed_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property is affected by Japanese Knotweed",
 		"dd_task": ["Confirmation of any past and present knotweed infestations are required",
                    "If a statement confirming the knotweed existence status cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": "It has not been stated whether the property is affected by Japanese Knotweed, the absence of full disclosure represents a significant risk to the buyer"
 	 },

 	 'yes' : {

 		 'meaning' : "The property is affected by Japanese Knotweed",
 		"dd_task": ["Confirmation of the knotweed infestation and past works to remove the infestation are required,",
                    "It is normally appropriate for a professional to assess the degree of infestation and determine the costs associated with removal"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property is not affected by Japanese Knotweed",
 		"dd_task":   [""],
        "pro_meaning": ""
 	 },

 } ,
'knotweed' : {

 	 'true' : {

 		 'meaning' : "",
 		"dd_task": ["Ensure a clear plan identifying the location of the Knotweed is provided"],
        "pro_meaning": "Apply extra care to identify for signs of knotweed around all parts of the property especially near buildings"
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": ["If a statement confirming the knotweed existence status cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey"
                    "There is a likelihood that a specialised indemnity may be required"],
        "pro_meaning": ["There are substantial risks associated with not providing full disclosure in respect to Knotweed",
                        "A failure to take all reasonable steps to declare and report knotweed can have Professional Indemnity implications"]
 	 },

 } ,
'mining_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property is in a mining area",
 		"dd_task": ["A search of; ground / geological stability / Con29 / mining activity may be appropriate",
                    "If a statement confirming the status of mining cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": "The absence of the mining status in the area may delay administration"
 	 },

 	 'yes' : {

 		 'meaning' : "The property is in a mining area",
 		"dd_task": ["A search of; ground / geological stability / Con29 / mining activity may be appropriate and or required by lenders for the transaction to progress",
                    "If a statement confirming the status of mining cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "The property is not in a mining area",
 		"dd_task": ["If the statement confirming the status of mining is insufficient for this purchase the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": "A formal determination confirming the status of ground stability may still be required propagating a need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity",
 	 },

 } ,
'mining' : {

 	 'true' : {

 		 'meaning' : "information regarding this properties status as within a mining area has been provided",
 		"dd_task": ["A moe detailed determination confirming the status of ground stability may likely be required propagating a need to rely upon a contemporary assessment from a formal search resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "No documents have been provided in relation to mining in the area ",
 		"dd_task": ["If a statement confirming the status of mining cannot be provided by the vendor the Buyer may need to rely upon a contemporary assessment from another resource or otherwise a custom survey and or specialised indemnity"],
        "pro_meaning": ""
 	 },

 } ,
'influence_decision_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether anything has happened in the property that a buyer might want to know or that might influence their decision to purchase the property",
 		"dd_task": ["Ensure the discloser understands the impact of not completing this section"],
        "pro_meaning": "Unless disclosed any subsequent information that comes to light is likely to negatively impact the prospect of a sale progressing and or the value at which a transaction completes "
 	 },

 	 'yes' : {

 		 'meaning' : "Something has happened in the property that a buyer might want to know or that might influence their decision to purchase the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "Nothing has happened in the property that is known that a buyer might want to know or that might influence their decision to purchase the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'influence_decision' : {

 	 'true' : {

 		 'meaning' : "",
 		"dd_task": ["Inspect the documents to ensure the information is clear and sufficiently complete to convey any potential risk or negative impact"],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": ["Verify with the discloser what information can be provided to better explain the other implied matters could influence a buyer",
                    "Encourage the discloser to carefully detail any additional matters of importance that may have a negative impact upon a purchaser evaluation of the property"],
        "pro_meaning": "A failure to disclose underlying matters that could negatively influence a potential buyer decision may result in liability and potential failure of the transaction"
 	 },

 } ,
'neighbour_access_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether any neighbour or members of the public do or do not have the right to enter the property or any part of it",
 		"dd_task": ["A statement is required to specify if any neighbour or class of public person are entitled to enter onto the property",
                    "Inspect the Title document to determine if any 3rd party access rights have been registered against the property"],
        "pro_meaning": "Without a declaration regarding the status of 3rd party access to the property the value may be impaired and conveyance elements may become protracted"
 	 },

 	 'yes' : {

 		 'meaning' : "Some neighbour or members of the public have a right to enter the some or all of the property",
 		"dd_task": ["Determine the extent the rights of access have been exercised"],
        "pro_meaning": "Third party access rights over the property may negatively impact the quiet, peaceful enjoyment and privacy of the property"
 	 },

 	 'no' : {

 		 'meaning' : "No neighbour or members of the public have a right to enter onto any part of the property",
 		"dd_task": [""],
        "pro_meaning": "The absence of third party access rights over the property improves the privacy value of the property"
 	 },

 } ,
'neighbour_access' : {

 	 'true' : {

 		 'meaning' : "",

        "dd_task": ["A statement is required to specify the identity of the neighbour and class of public persons entitled to enter onto the property",
                    "A confirmation plan and statement is required to specify the location of the property and the means of entry onto the property that may be exercised by any neighbour or member of the public ",
                    "Disclosure required of: any terms rights or restrictions that apply to any neighbour or member of the public seeking to rely upon a right to enter onto the property must be disclosed",
                    "Documenting and the extent of any 3rd party access",
                    "Evaluate the negative impact resulting from the 3rd party access rights if exercised to their full extent"],
        "pro_meaning":
                 [  "Ensure prospective buyers understand the possible impact 3rd party access rights may have upon the quiet and peaceful enjoyment and privacy of the property"]		
 	 },

 	 'false' : {

 		 'meaning' : "",
 		"dd_task": ["A statement is required to specify the identity of the neighbour and class of public persons entitled to enter onto the property",
                    "A confirmation plan and statement is required to specify the location of the property and the means of entry onto the property that may be exercised by any neighbour or member of the public ",
                    "Disclosure required of: any terms rights or restrictions that apply to any neighbour or member of the public seeking to rely upon a right to enter onto the property must be disclosed"],
        "pro_meaning": "Undisclosed rights of access that emerge during the sale process or subsequent to a transaction may result in; 1. professional indemnity exposure, and  2. client liability"
 	 },

 } ,
'anything_else_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been declared if there is anything else that the buyer might want to know that may influence their decision to buy or sell the property",
 		"dd_task": ["The buyer should be consulted to determine if the absence of an answer an oversight",
                    "Explain to the buyer the consequences not disclosing information could have in regard to a sale progressing to completion"],
        "pro_meaning": ""
 	 },

 	 'yes' : {

 		 'meaning' : "It has been been declared that there is other information that the buyer might want to know or might influence their decision to buy the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 	 'no' : {

 		 'meaning' : "It has been declared that there is no other information that has not already been disclosed that a buyer might want to know about the property or that might influence their decision to buy the property",
 		"dd_task": [""],
        "pro_meaning": ""
 	 },

 } ,
'anything_else' : {

 	 'true' : {

 		 'meaning' : "Additional information has been provided that is relevant to the buyer and may influence their evaluation of the property",
 		"dd_task": ["Full disclosure is required of any information the vendor believes that the buyer might want to know or might influence their decision to buy the property"],
        "pro_meaning": ""
 	 },

 	 'false' : {

 		 'meaning' : "The documentation regarding the existence of other factors has not been provided",
 		"dd_task": [""],
        "pro_meaning": "Missing documentation regarding the additional information may delay or undermine the prospective buyer's assessment of the property"
 	 },

 }
 }