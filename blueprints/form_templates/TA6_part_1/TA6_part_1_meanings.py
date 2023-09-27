
from launch.blueprints.form_templates import value_controllers as vc
meanings = {
'data_providers_count' : {
     'value' : {
            'equation':{
                vc.larger_then : {'vari':1, 'meaning':"This data has been provided by {} people"},
                vc.less_then : {'vari':1, 'meaning':'the number of persons providing this data has not been specified'}
                },
            'default':{'meaning' : "This data has been provided by one individual"},
        }

#Injection value position notated by {}
 } ,
'postcode' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'address_line_1' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'address_line_2' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'address_town_or_city' : {

     'none' : {

         'meaning' : "The postal town/city for the property has not been specified",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'UPRN' : {

     'none' : {

         'meaning' : "A UPRN has not been specified",

     },

     'value' : {

         'meaning' : "The UPRN for this property is:{}",

     },

 } ,
'lease_or_free' : {

     'empty' : {

         'meaning' : "The tenure applicable to this Title has not been specified",
#3 Inject the Title Number into a new combined sentance if known. 
#3 SPecimen sendance " The tenure applicable to Title {} has not been specified"
     },

     'Leasehold' : {

         'meaning' : "The ownership status in this title is Leasehold",

     },

     'Freehold' : {

         'meaning' : "The ownership status in this title is Freehold",

     },

 } ,
'years_left' : {

     'none' : {
         'meaning' : "The number of years remaining (unexpired) on this Leasehold have not been specified",

     },

     'value' : {

         'meaning' : "The Leashold has {} Years remaining on the agreement",

     },

 } ,
'rent_value' : {

     'none' : {

         'meaning' : "No Ground Rent value has not been stated",

     },

     'value' : {

         'meaning' : "The Ground Rent value chageable each year is {}",

     },

 } ,
'ground_rent_increase_bool' : {

     'empty' : {

         'meaning' : "It is not stated whether the frequency of each Ground Rent increase is specified in the lease agreement",

     },

     'yes' : {

         'meaning' : "The frequency of each Ground Rent increase is specified in the lease agreement",

     },

     'no' : {

         'meaning' : "The frequency of each Ground Rent increase is not specified in the lease agreement",

     },

 } ,
'ground_rent_increase_date' : {

     'none' : {

         'meaning' : "The date of any Ground Rent increae has not been stated",

     },

     'value' : {

         'meaning' : "The next Ground Rent increase occurs on the: {}",

     },

 } ,
'ground_rent_increase_frequency' : {

     'none' : {

         'meaning' : "The frequency of Ground Rent increase occurs in an unspecified manner",

     },

     'value' : {

         'meaning' : "Ground Rent increases take place: {}",

     },

 } ,
'rent_increase_type' : {

     'empty' : {

         'meaning' : "The Type of Rent Increase has not been specified",

     },

     'Fixed' : {

         'meaning' : "The Ground rent increase is fixed",

     },

     'Variable' : {

         'meaning' : "Ground Rent increases are variable and not fixed",

     },

     'Other' : {

         'meaning' : "The type of rent increase has been defined as:{}",

     },

 } ,
'rent_increase_type_details' : {

     'true' : {

         'meaning' : "extra information has been provided regarding the rent increase type",

     },

     'false' : {

         'meaning' : "no extra information has been provided regarding the rent increase type",

     },

 } ,
'service_charge_bool' : {

     'empty' : {

         'meaning' : "It has not been specified if Service Charges have been paid or become due",

     },

     'yes' : {

         'meaning' : "Service Charges have been paid or become due",

     },

     'no' : {

         'meaning' : "No Service Charges have been paid or become due",

     },

 } ,
'last_service_charge' : {

     'none' : {

         'meaning' : "The value of the last service charge has not been specified",

     },

     'value' : {

         'meaning' : "The value of the last service charge was:£{}",

     },

 } ,
'service_charge_budget_bool' : {

     'empty' : {

         'meaning' : "No budget has been provided for the next due service charge",

     },

     'yes' : {

         'meaning' : "A budget for the next due service charge has been provided",

     },

     'no' : {

         'meaning' : "A budget for the next due service charge is not available",

     },

 } ,
'service_charge_bill_docu' : {

     'true' : {

         'meaning' : "Documentation regarding the service charge has been provided",

     },

     'false' : {

         'meaning' : "No documentation has been provided in regards to the service cahrge",

     },

 } ,
'service_charge_payments_due' : {

     'none' : {

         'meaning' : "No service charge payments are due.",

     },

     'value' : {

         'meaning' : "The next payment is due on {}",

     },

 } ,
'service_charge_pay_reciever' : {

     'empty' : {

         'meaning' : "It has not been specified who receives the service charge",

     },

     'agent' : {

         'meaning' : "Service charges are payable to the Agent",

     },

     'landlord' : {

         'meaning' : "Service charges are payable to the Landlord",

     },

     'freehold_company' : {

         'meaning' : "Service charges are payable to a Freehold Company",

     },

     'resi_assoc' : {

         'meaning' : "Service charges are payable to the Residential Association",

     },

 } ,
'service_charge_organisation' : {

     'none' : {

         'meaning' : "The organisation responsible for collecting the Service Charge has not been specified",

     },

     'value' : {

         'meaning' : "the organization responsible for collecting the service charge is the {} and the postable adress is as follows",

     },

 } ,
'service_charge_Building_name' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'service_charge_street_no' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'service_charge_street_name' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'service_charge_town_or_city' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'service_charge_postcode' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "{}",

     },

 } ,
'first_to_occupy' : {

     'empty' : {

         'meaning' : "It has not been specified if the Vendor was the first occupant of the property since it was built or converted",

     },

     'yes' : {

         'meaning' : "The Vendor has been the first occupant of the property since it was built or converted",

     },

     'no' : {

         'meaning' : "The Vendor is not the first occupant of the property since it was built or converted",

     },

 } ,
'warranties_docu' : {

     'true' : {

         'meaning' : "Documentation regardinf the warranties has been provided",

     },

     'false' : {

         'meaning' : "There are no details of the warranties and guarantees, and \
                            any planning consents or other planning documents that might have been available at the time of construction or conversion",

     },

 } ,
'property_dependant' : {

     'empty' : {

         'meaning' : "The vendor has not declared whether the sale of the property is dependant on the purchase of a seperate property",

     },

     'yes' : {

         'meaning' : "The sale is dependant upon the vendor's successful purchase of another property",

     },

     'no' : {

         'meaning' : "The vendor states that the sale of the property is not dependant on the purchase of another property",

     },

 } ,
'property_dependant_details' : {

     'true' : {

         'meaning' : "",

     },

     'false' : {

         'meaning' : "",

     },

 } ,
'school_term' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The sale is dependant upon school calendar commitments and/ or schedules",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'school_term_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "The vendor intends to schedule the sale with reference to the School calendar date: {}",

     },

 } ,
'upcoming_holiday' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule the sale with reference to a forthcoming Holiday",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'upcoming_holiday_date' : {

     'none' : {

         'meaning' : "The date of the forthcoming holiday affecting the sale time has not been described",

     },

     'value' : {

         'meaning' : "The date of the forthcoming holiday affecting the sale time is {}",

     },

 } ,
'job_move' : {

     'empty' : {

         'meaning' : "The date of the forthcoming job move the sale time has not been described",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to the Job Move date: {}",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'job_move_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'redundancy' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a redundancy arrangement",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'redundancy_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'medical' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to Medical commitment",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'medical_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'notice_to_tenant' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to the notice to a tenant",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'notice_to_tenant_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'retirement' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a retirement date",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'retirement_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'build_complete' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to a building completion date",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'build_complete_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'other_move_factor' : {

     'empty' : {

         'meaning' : "",

     },

     'yes' : {

         'meaning' : "The vendor intends to schedule a sale with reference to another/ independent event",

     },

     'no' : {

         'meaning' : "",

     },

 } ,
'other_move_factor_date' : {

     'none' : {

         'meaning' : "",

     },

     'value' : {

         'meaning' : "",

     },

 } ,
'other_move_factor_details' : {

     'true' : {

         'meaning' : "The Vendors sale will be impacted by:{}",

     },

     'false' : {

         'meaning' : "",

     },

 } ,
'works_and_alterations_count' : {
    'value' : {
            'equation':{
                vc.larger_then : {'vari':1, 'meaning':"there have been {} alterations to the property"}
                },
            'default':{'meaning' : "there have been alterations to the property"},
        }
 } ,
'planning_breach' : {

     'empty' : {

         'meaning' : "It has not been specified if any breaches of planning conditions have occurred",

     },

     'yes' : {

         'meaning' : "one or more breaches of planning conditions have occured",

     },

     'no' : {

         'meaning' : "no breaches of planning conditions have occurred",

     },

 } ,
'planning_breach_details' : {

     'true' : {

         'meaning' : "A written description of planning breach details has been provided",

     },

     'false' : {

         'meaning' : "No description of the breaches of planning conditionsw that have occured at this property have been provided",

     },

 } ,
'bulding_reg_breach' : {

     'empty' : {

         'meaning' : "It has not been stated whether there have been no breaches of Building Regulation conditions",

     },

     'yes' : {

         'meaning' : "There have been breaches of Building Regulation conditions",

     },

     'no' : {

         'meaning' : "There have been no breaches of Building Regulation conditions",

     },

 } ,
'bulding_reg_breach_details' : {

     'true' : {

         'meaning' : "Details of the building regulation breaches have been provided",

     },

     'false' : {

         'meaning' : "There has been no provision of details regarding the building regulation breaches that have occured at this property",

     },

 } ,
'unfinished_work' : {

     'empty' : {

         'meaning' : "It has not been stated whether any works have been undertaken that presently remain unfinished",

     },

     'yes' : {

         'meaning' : "Works have been undertaken that remain unfinished",

     },

     'no' : {

         'meaning' : "There have been no works undertaken that remain unfinished",

     },

 } ,
'unfinished_work_details' : {

     'true' : {

         'meaning' : "Details of the unfinished building works at this property have been provided",

     },

     'false' : {

         'meaning' : "There has been no provision of details regarding the unfinished building work at this property",

     },

 } ,
'consent_lack' : {

     'empty' : {

         'meaning' : "It has not been stated whether any works have been undertaken that lack  all necessary consent",

     },

     'yes' : {

         'meaning' : "Works have been undertaken that lack all necessary consent",

     },

     'no' : {

         'meaning' : "Now works have been undertaken that lack all necessary consent",

     },

 } ,
'consent_lack_details' : {

     'true' : {

         'meaning' : "Details have been provided regarding the works undertaken without all neccassary consent",

     },

     'false' : {

         'meaning' : "Details have not been provided regarding the works that have been undertaken without neccassary consent",

     },

 } ,
'solar_panels_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether any solar panels have been installed",

     },

     'yes' : {

         'meaning' : "Solar panels have been installed at the property",

     },

     'no' : {

         'meaning' : "Solar panels have not been installed at the property",

     },

 } ,
'solar_installation_year' : {

     'none' : {

         'meaning' : "It has not been stated in which year the Solar panels were installed at the property",

     },

     'value' : {

         'meaning' : "Solar panels were installed at the property:{}",

     },

 } ,
'solar_panels_ownership_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the solar panels are owned outright",

     },

     'yes' : {

         'meaning' : "The solar panels are owned outright",

     },

     'no' : {

         'meaning' : "The solar panels are not owned outright",

     },

 } ,
'solar_panels_long_lease_ownership_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether a long lease of the roof / air space has been granted to a solar panel provider",

     },

     'yes' : {

         'meaning' : "A long lease of the roof / air space has been granted to a solar panel provider",

     },

     'no' : {

         'meaning' : "No long lease of the roof / air space has been granted to a solar panel provider",

     },

 } ,
'solar_electrical_tarrif_docu' : {

     'true' : {

         'meaning' : "Documentation regarding the solar electrical tarriff or other information regarding the solar panel array at the property has been provided",

     },

     'false' : {

         'meaning' : "Documentation regarding the solar electrical tarriff or other information regarding the solar panel array at the property has not provided",

     },

 } ,
'protected_buildings_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the property (or any part of it) listed in the National Heritage List for England",

     },

     'yes' : {

         'meaning' : "The property (or a part of it) is listed in the National Heritage List for England",

     },

     'no' : {

         'meaning' : "The property (or any part of it) is not listed in the National Heritage List for England",

     },

     'not_known' : {

         'meaning' : "It is not known if the property (or a part of it) is listed in the National Heritage List for England",

     },

 } ,
'protected_buildings_docu' : {

     'true' : {

         'meaning' : "Documents relating to the property's protected Building Statu have been provided",

     },

     'false' : {

         'meaning' : "Documents relating to the property's Protected Building status have not been provided",

     },

 } ,
'conservation_area_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether the property (or any part of it) in a conservation area",

     },

     'yes' : {

         'meaning' : "The property (or a part of it) is in a conservation area",

     },

     'no' : {

         'meaning' : "Neither the property or any part of it is in a conservation area",

     },

     'not_known' : {

         'meaning' : "It is not known if the property (or any part of it) in a conservation area",

     },

 } ,
'conservation_area_docu' : {

     'true' : {

         'meaning' : "Details of the Conservation area have been provided",

     },

     'false' : {

         'meaning' : "Details of the Conservation area have been provided",

     },

 } ,
'TPO_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether any trees on the property are subject to a Tree Preservation Order",

     },

     'yes' : {

         'meaning' : "Trees on the property are subject to Tree Preservation Order controls",

     },

     'no' : {

         'meaning' : "No trees on the property are subject to a Tree Preservation Order",

     },

     'not_known' : {

         'meaning' : "It is not known whether any trees on the property are subject to a Tree Preservation Order",

     },

 } ,
'order_terms_complied_with' : {

     'empty' : {

         'meaning' : "It has not been stated whether the terms of the Tree Preservation Order have been complied with",

     },

     'yes' : {

         'meaning' : "The terms of the Tree Preservation Order have been complied with",

     },

     'no' : {

         'meaning' : "The terms of the Tree Preservation Order have not been complied with",

     },

     'not_known' : {

         'meaning' : "It is not known if the terms of the Tree Preservation Order have been complied with",

     },

 } ,
'TPO_docu' : {

     'true' : {

         'meaning' : "Details of the TPOs have been provided",

     },

     'false' : {

         'meaning' : "Details of the TPOs have not been provided",

     },

 } ,
'all_required_consents' : {

     'empty' : {

         'meaning' : "It has not been stated whether consent has been obtained for any matters that need permission",

     },

     'yes' : {

         'meaning' : "Consent has been obtained for any matters that need permission",

     },

     'no' : {

         'meaning' : "Consent has not been obtained for any matters that need permission",

     },

     'not_known' : {

         'meaning' : "It is not known if consent has been obtained for any matters that need permission",

     },

 } ,
'all_required_consents_details' : {

     'true' : {

         'meaning' : "Details of the consents have been provided",

     },

     'false' : {

         'meaning' : "Details concerning required consents have not been provided",

     },

 } ,
'charges_bool' : {

     'empty' : {

         'meaning' : " It has not been stated whether the property owner is required to pay any charges relating to the property (apart from council tax, utility charges etc",

     },

     'yes' : {

         'meaning' : "The property owner is liable to pay charges relating to the property (apart from council tax, utility charges etc) ",

     },

     'no' : {

         'meaning' : "The property owner is liable to pay charges relating to the property (apart from council tax, utility charges etc)",

     },

 } ,
'charges_details' : {

     'true' : {

         'meaning' : "Details of the charges have been provided",

     },

     'false' : {

         'meaning' : "Details have not been provided in relation to the charges imposed on the owner",

     },

 } ,
'maintain_road_bool' : {

     'empty' : {

         'meaning' : "It has not been stated whether there is an obligation to pay anything towards the costs of maintaining roads, footpaths or other facilities",

     },

     'yes' : {

         'meaning' : "There is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",

     },

     'no' : {

         'meaning' : "There is no obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",

     },

     'not_known' : {

         'meaning' : "It is not known whether there is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities",

     },

 } ,
'maintain_road_payement_details' : {

     'true' : {

         'meaning' : "Details of the Road maintenance payment have been provided",

     },

     'false' : {

         'meaning' : "Details of the Road maintenance payment have been provided",

     },

 } ,
'private_road' : {

     'empty' : {

         'meaning' : "It has not been specified if the property on a private road or is the road that gives access to or adjoins the property a private road",

     },

     'yes' : {

         'meaning' : "The property is on a private road or is the road that gives access to or adjoins the property a private road",

     },

     'no' : {

         'meaning' : "The property is not on a private road or is the road that gives access to or adjoins the property a private road",

     },

     'not_known' : {

         'meaning' : "It is not known if the property is on a private road or is the road that gives access to or adjoins the property a private road",

     },

 } ,
'public_expense_road' : {

     'empty' : {

         'meaning' : "It has not been specified whether the roads leading to the property are maintained at public expense",

     },

     'yes' : {

         'meaning' : "The roads leading to the property are maintained at public expense",

     },

     'no' : {

         'meaning' : "The roads leading to your property are maintained at public expense",

     },

     'not_known' : {

         'meaning' : "It is not known if the roads leading to the property are maintained at public expense",

     },

 } ,

'mains_drainage' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a mains drainage network connection",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a mains drainage network",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not have a mains drainage network connection",

 	 },

 } ,
'electricity' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to an electrical supply",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a electrical supply",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit froma connection to an eectrical supply",

 	 },

 } ,
'water_supply' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a water supply",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a water supply",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to a water supply",

 	 },

 } ,
'gas' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a mains gas supply",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection to a mains gas supply",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to a mains gas supply",

 	 },

 } ,
'broadband' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a broadband connection",

 	 },

 	 'yes' : {

 		 'meaning' : "The property has the benefit of a broadband connection",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not currently benefit from a broadband connection",

 	 },

 } ,
'sewage_plant' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to a private sewage plant",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a private sewage plant",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefits from a private sewage plant",

 	 },

 } ,
'telephone_landlines' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Telephone Landlines",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from a connection Telephone Landlines",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not have connection to Telephone Landlines",

 	 },

 } ,
'solar_panels' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Solar Panels",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from connected Solar Panels",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from a connection to solar panels",

 	 },

 } ,
'heat_pumps' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property benefits from a connection to Ground or air heat pumps",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from connected Ground or air heat pumps",

 	 },

 	 'no' : {

 		 'meaning' : "The property does benefit from the connection of Ground or air heat pumps",

 	 },

 } ,
'other_provisioned_services' : {

 	 'empty' : {

 		 'meaning' : "No other additional provisioned services have been disclosed",

 	 },

 	 'yes' : {

 		 'meaning' : "The property benefits from aditional provisioned services not already mentioned",

 	 },

 	 'no' : {

 		 'meaning' : "The property does not benefit from any other provsisioned services beyond those already disclosed",

 	 },

 } ,
'other_provisioned_services_details' : {

 	 'true' : {

 		 'meaning' : "Details regarding the additional provisioned services have been provided",

 	 },

 	 'false' : {

 		 'meaning' : "No details regarding the additional provisioned services have been provided",

 	 },

 } ,
'shared_facilities_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether there are any areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)",

 	 },

 	 'yes' : {

 		 'meaning' : "There are areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)",

 	 },

 	 'no' : {

 		 'meaning' : "There are not any areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)",

 	 },

 } ,
'shared_facilities_text_details' : {

 	 'true' : {

 		 'meaning' : "Details of the shared facilities have been provided",

 	 },

 	 'false' : {

 		 'meaning' : "No details of the facilities this property shares with other properties have been provided",

 	 },

 } ,
'parking_arrangement_details' : {

 	 'true' : {

 		 'meaning' : "Details regarding the parking arrangements of the property have been provided",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'controlled_parking' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether the property is in a controlled parking zone or within a local authority parking scheme",

 	 },

 	 'yes' : {

 		 'meaning' : "Ther property is in a controlled parking zone or within a local authority parking scheme",

 	 },

 	 'no' : {

 		 'meaning' : "The property is not in a controlled parking zone or within a local authority parking scheme",

 	 },

 	 'not_known' : {

 		 'meaning' : "The diclosure provider does not know if the property is in a controlled parking zone or within a local authority parking scheme",

 	 },

 } ,
'live_at_prop_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether the disclosure provider lives at the property",

 	 },

 	 'yes' : {

 		 'meaning' : "The disclosure provider lives at the property",

 	 },

 	 'no' : {

 		 'meaning' : "The disclosure provider does not live at the property",

 	 },

 } ,
'over_17_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether anyone other then the diclosure provider aged 17 or over live at the property",

 	 },

 	 'yes' : {

 		 'meaning' : "Individuals other then the disclosure provider aged 17 or over live at the property",

 	 },

 	 'no' : {

 		 'meaning' : "No other individuals other then the disclosure provider aged 17 or over live at the property",

 	 },

 } ,
'over_17_count' : {
	 'value' : {

	 	 'meaning' : "There are currently {} individuals aged 17 or over living at the property"

	 },

 } ,
'lodgers_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether any of the occupiers aged 17 or over other then the disclosees are tennants or lodgers",

 	 },

 	 'yes' : {

 		 'meaning' : "Some or all of the occupiers aged 17 or over are tennants or lodgers",

 	 },

 	 'no' : {

 		 'meaning' : "None of the occupiers aged 17 or over are tennants or lodgers",

 	 },

 } ,
'agree_to_leave_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed whether all the occupiers aged 17 and over have agreed to leave before completion",

 	 },

 	 'yes' : {

 		 'meaning' : "All of the occupiers aged 17 and over have agreed to leave the property before completion of the sale",

 	 },

 	 'no' : {

 		 'meaning' : "Not all or none of occupiers aged 17 and over have agreed to leave the property before completion of the sale",

 	 },

 } ,
'occupiers_contract_sign_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed whether all the occupiers aged 17 and over have agreed to sign the sale contract",

 	 },

 	 'yes' : {

 		 'meaning' : "All the occupiers aged 17 and over have agreed to sign the sale contract",

 	 },

 	 'no' : {

 		 'meaning' : "Not all or none of the occupiers aged 17 and over have agreed to sign the sale contract",

 	 },

 } ,
'vacant_possession_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether this property is being sold with vacant possession",

 	 },

 	 'yes' : {

 		 'meaning' : "This property is being sold with vacant possession",

 	 },

 	 'no' : {

 		 'meaning' : "This property is not being sold with vacant possession",

 	 },

 } ,
'vacant_possession_proof_docu' : {

 	 'true' : {

 		 'meaning' : "Documentation has been provided as proof that this property will be sold with vacant possession",

 	 },

 	 'false' : {

 		 'meaning' : "Documentation has not been provided as proof that this property will be sold with vacant possession",

 	 },

 } ,
'flooding_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether this property has ever flooded",

 	 },

 	 'yes' : {

 		 'meaning' : "This property has previoulsy suffered flooding",

 	 },

 	 'no' : {

 		 'meaning' : "This property has as far as is known not suffered from flooding",

 	 },

 } ,
'flood_events_count' : {
	 'value' : {

	 	 'meaning' : "There have been {} known flood events recorded at this property"

	 },

 } ,
'flood_risk_report_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed as to whether a flood risk report has been created for the property",

 	 },

 	 'yes' : {

 		 'meaning' : "A floood risk report has been ctreated for the property",

 	 },

 	 'no' : {

 		 'meaning' : "A flood risk report has not been created for the property",

 	 },

 } ,
'flood_risk_report_docu' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'nearby_development_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been disclosed if any of the disclosure providers have been told about plans for any building or developments that might affect someone's abuility to peacefully use and enjoy the property",

 	 },

 	 'yes' : {

 		 'meaning' : "There are plans for development or buildings that may affect someone's abuility to peacefully use and enjoy the property",

 	 },

 	 'no' : {

 		 'meaning' : "There are no known plans for development or buildings that may affect someone's abuility to peacefully use and enjoy the property",

 	 },

 } ,
'nearby_development' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'complaints_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether there have been any complaints about the property or a property nearby",

 	 },

 	 'yes' : {

 		 'meaning' : "There have been complaints about the property or a property nearby",

 	 },

 	 'no' : {

 		 'meaning' : "There have not been any known complaints about the property or a property nearby",

 	 },

 } ,
'complaints_details' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'disputes_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated if any of the disclosure propviders are aware of anything thjat might lead to a dipute about your property or a property nearby",

 	 },

 	 'yes' : {

 		 'meaning' : "There are things that may lead to a dispute about the property or a property nearby",

 	 },

 	 'no' : {

 		 'meaning' : "there is nothing known that might lead to a dispute about the property or a property nearby",

 	 },

 } ,
'disputes_details' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'knotweed_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not ben stated whether the property is affected by Japanese Knotweed",

 	 },

 	 'yes' : {

 		 'meaning' : "The property is affected by Japanese Knotweed",

 	 },

 	 'no' : {

 		 'meaning' : "The property is not affected by Japanese Knotweed",

 	 },

 } ,
'knotweed' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'mining_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether the property is in a mining area",

 	 },

 	 'yes' : {

 		 'meaning' : "The property is in a mining area",

 	 },

 	 'no' : {

 		 'meaning' : "The property is not in a mining area",

 	 },

 } ,
'mining' : {

 	 'true' : {

 		 'meaning' : "information regarding this properties status as within a mining area has been provided",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'influence_decision_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether anything has happened in the property that a buyer might want to know or that might influence their decision to purchase the property",

 	 },

 	 'yes' : {

 		 'meaning' : "Something has happened in the property that a buyer might want to know or that might influence their decision to purchase the property",

 	 },

 	 'no' : {

 		 'meaning' : "Nothing has happed in the property that is known that a buyer might want to know or that might influence their decision to purchase the property",

 	 },

 } ,
'influence_decision' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'neighbours_access_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been stated whether any neighbours or members of the public do or do not have the right to enter the property or any part of it",

 	 },

 	 'yes' : {

 		 'meaning' : "Some neighbours or members of the public have a right to enter the some or all of the property",

 	 },

 	 'no' : {

 		 'meaning' : "No neighbours or members of the public have a right to enter onto any part of the property",

 	 },

 } ,
'neighbours_access' : {

 	 'true' : {

 		 'meaning' : "",
 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 } ,
'anything_else_bool' : {

 	 'empty' : {

 		 'meaning' : "It has not been declared if there is anything else that the nuyer might want to know that may influence thier decision to buy or sell the property",

 	 },

 	 'yes' : {

 		 'meaning' : "It has been been declared that there is other information that the buyer might want to know or might influence their decision to buy the property",

 	 },

 	 'no' : {

 		 'meaning' : "It has been declared that there is not other information not already disclosed that a buyer might want to know about the property or that might influence their decision to buy the property",

 	 },

 } ,
'anything_else' : {

 	 'true' : {

 		 'meaning' : "",

 	 },

 	 'false' : {

 		 'meaning' : "",

 	 },

 }
 }