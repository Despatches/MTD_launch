meanings = {
    "postcode": 
        {"none": {"meaning": ""}, "value": {"meaning": "{}"}},
    "address_line_1": 
        {"none": {"meaning": ""}, "value": {"meaning": "{}"}},
    "address_line_2": 
        {"none": {"meaning": ""}, "value": {"meaning": "{}"}},
    "address_town_or_city": {
        "none": {
                "meaning": "The postal town/city for the property has not been specified"
        },
        "value": 
                {"meaning": "{}"},
    },
    "UPRN": {
        "none": 
                {"meaning": "A UPRN has not been specified"},
        "value": 
                {"meaning": "The UPRN for this property is:{}"},
    },
    "lease_or_free": {
        "empty": {
            "meaning": "The tenure applicable to this Title has not been specified"
        },
        "Leasehold": 
                {"meaning": "The status of this property title is Leasehold"},
        "Freehold": 
                {"meaning": "The status of this property title is Freehold"},
    },
    "years_left": {
        "none": {
            "meaning": "The number of years remaining (unexpired) on this Leasehold has not been specified"
        },
        "value": 
                {"meaning": "The Leasehold has {} Years remaining on the agreement"},
    },
    "rent_value": {
        "none": 
                {"meaning": "No Ground Rent value has been stated"},
        "value": 
                {"meaning": "The Ground Rent value chargeable each year is {}"},
    },
    "ground_rent_increase_bool": {
        "empty": {
            "meaning": "It has not been stated whether the frequency of each Ground Rent increase is specified in the lease agreement"
        },
        "yes": {
            "meaning": "The frequency of each Ground Rent increase is specified in the lease agreement"
        },
        "no": {
            "meaning": "The frequency of each Ground Rent increase is not specified in the lease agreement"
        },
    },
    "ground_rent_increase_date": {
        "none": 
                {"meaning": "The date of any Ground Rent increase has not been stated"},
        "value": 
                {"meaning": "The next Ground Rent increase occurs on the: {}"},
    },
    "ground_rent_increase_frequency": {
        "none": {
                    "meaning": "The frequency of Ground Rent increase occurs in an unspecified manner"
        },
        "value":    
                    {"meaning": "Ground Rent increases take place: {}"},
    },
    "rent_increase_type": {
        "empty": 
                {"meaning": "The Type of Rent Increase has not been specified"},
        "Fixed":
                {"meaning": "The Ground rent increase is fixed"},
        "variable": 
                {"meaning": "Ground Rent increases are variable and not fixed"},
        "Other": 
                {"meaning": "The type of rent increase has been defined as:{}"},
    },
    "rent_increase_type_details": {
        "true": {
            "meaning": "Extra information has been provided regarding the rent increase type"
        },
        "false": {
            "meaning": "No extra information has been provided regarding the rent increase type"
        },
    },
    "service_charge_bool": {
        "empty": {
            "meaning": "It has not been specified if Service Charges have been paid or become due"
        },
        "yes":
             {"meaning": "Service Charges have been paid or become due"},
        "no": 
            {"meaning": "No Service Charges have been paid or become due"},
    },
    "last_service_charge": {
        "none": {
            "meaning": "The value of the last service charge has not been specified"
        },
        "value": 
            {"meaning": "The value of the last service charge was:£{}"},
    },
    "service_charge_budget_bool": {
        "empty": {
            "meaning": "No budget has been provided for the next due service charge"
        },
        "yes": {
            "meaning": "A budget for the next due service charge has been provided"
        },
        "no": 
            {"meaning": "A budget for the next due service charge is not available"},
    },
    "service_charge_bill_docu": {
        "true": {
            "meaning": "Documentation regarding the service charge has been provided"
        },
        "false": {
            "meaning": "No documentation has been provided with regard to the service charge"
        },
    },
    "service_charge_payments_due": {
        "none": 
                {"meaning": "No service charge payments are due."},
        "value": 
                {"meaning": "The next payment is due on {}"},
    },
    "service_charge_pay_reciever": {
        "empty": {
                "meaning": "It has not been specified who receives the service charge"
        },
        "agent": 
                {"meaning": "Service charges are payable to the Agent"},
        "landlord": 
                {"meaning": "Service charges are payable to the Landlord"},
        "freehold_company": {
            "meaning": "Service charges are payable to a Freehold Company"
        },
        "resi_assoc": {
            "meaning": "Service charges are payable to the Residential Association"
        },
    },
    "service_charge_organisation": {
        "none": {
            "meaning": "The organisation responsible for collecting the Service Charge has not been specified"
        },
        "value": {
            "meaning": "The organization responsible for collecting the service charge is the {} and the postable address is as follows"
        },
    },
    "service_charge_Building_name": {
        "none": 
                {"meaning": "The building name or number reference is missing from the contact address for the service charge recipient"},
        "value": 
                {"meaning": "{}"},
    },
    "service_charge_street_no": 
        {"none": 
                {"meaning": "The street name is missing from the contact address for the service charge recipient"}, 
        "value": 
                {"meaning": "{}"}
    },
    "service_charge_street_name": 
        {"none": 
                {"meaning": ""}, 
         "value": 
                {"meaning": "{}"}
     },
    "service_charge_town_or_city": {
        "none": 
                {"meaning": "The town or city is missing from the contact address for the service charge recipient"},
        "value": 
                 {"meaning": "{}"},
    },
    "service_charge_postcode": 
        {"none": 
            {"meaning": "The contact address postcode detail for the organisation that receive the service charges is incomplete"}, 
        "value": 
            {"meaning": "{}"}
     },
    "first_to_occupy": {
        "empty": {
            "meaning": "It has not been specified if the Vendor was the first occupant of the property since it was built or converted"
        },
        "yes": {
            "meaning": "The Vendor has been the first occupant of the property since it was built or converted"
        },
        "no": {
            "meaning": "The Vendor is not the first occupant of the property since it was built or converted"
        },
    },
    "warranties_docu": {
        "true": 
            {"meaning": "Documentation regarding the building warranties has been provided"},
        "false": {
            "meaning": "There are no details of the warranties and guarantees, and any planning consents or other planning documents that might have been available at the time of construction or conversion of this property"
        },
    },
    "property_dependant": {
        "empty": {
            "meaning": "The vendor has not declared whether the sale of the property is dependant on the purchase of a seperate property"
        },
        "yes": {
            "meaning": "The sale is dependant upon the vendor's successful purchase of another property"
        },
        "no": {
            "meaning": "The vendor has provided no indication that the sale of the property is dependant upon the purchase of another property"
        },
    },
    "property_dependant_details": {
        "true": 
            {"meaning": "Details have been provided regarding the vendor's dependancy upon the successful purchase of another property"}, 
        "false": 
            {"meaning": "Details have not been provided regarding the vendor's dependancy upon the successful purchase of another property"}
    },
    "school_term": {
        "empty": 
            {"meaning": ""},
        "yes": {
            "meaning": "The sale is dependant upon school calendar commitments and/ or schedules"
        },
        "no": 
            {"meaning": "The sale is not dependant upon school calendar commitments and/ or schedules"},
    },
    "school_term_date": {
        "none": 
            {"meaning": "The vendor has not disclosed the school calendar date to which the move may be scheduled"},
        "value": {
            "meaning": "The vendor intends to schedule the sale with reference to the School calendar date: {}"
        },
    },
    "upcoming_holiday": {
        "empty": 
            {"meaning": ""},
        "yes": {
            "meaning": "The vendor intends to schedule the sale with reference to a forthcoming Holiday"
        },
        "no": 
            {"meaning": "The vendor has not indicated any intent to schedule the sale with reference to a forthcoming Holiday"},
    },
    "upcoming_holiday_date": {
        "none": {
            "meaning": "The date of the forthcoming holiday affecting the proposed sale schedule/s has not been disclosed"
        },
        "value": {
            "meaning": "The date of the forthcoming holiday affecting the property sale schedule is {}"
        },
    },
    "job_move": {
        "empty": {
            "meaning": ""
        },
        "yes": {
            "meaning": "The vendor intends to schedule a sale with reference to a Job Move date: {}"
        },
        "no": 
            {"meaning": "The vendor has not indicated any intent to schedule a sale with reference to a Job Move date"},
    },
    "job_move_date": 
        {"none": 
            {"meaning": "No date has been provided in relation to any job move that may effec the sale progression"}, 
        "value": 
            {"meaning": "{The vendor's sale is dependant upon a job move date of: {} }"}
            },
    "redundancy": {
        "empty": 
                {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to a redundancy arrangement"
        },
        "no": 
            {"meaning": "The vendor has not indicated any intent to schedule a sale with reference to a redundancy arrangement"},
    },
    "redundancy_date": {
        "none": 
            {"meaning": "A date has not been provided to confirm when the Vendor's redundancy takes place"}, 
        "value": 
            {"meaning": "The vendor intends to schedule a sale with reference to their redundancy arrangements effective on: {}"}
    },
    "medical": {
        "empty": 
                {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to a Medical commitment"
        },
        "no": {"meaning": "The vendor has not indicated any intent to schedule a sale with reference to a Medical commitment"},
    },
    "medical_date": {
        "none": 
            {"meaning": "No date has been provided relating to the vendor's schedule of Medical commitments effecting the timing of this sale"}, 
        "value": 
            {"meaning": "The vendor's Medical commitment date effecting the timing of this sale is: {}"}
    },
    "notice_to_tenant": {
        "empty": 
                {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to a Notice issued to a tenant"
        },
        "no": 
                {"meaning": "The vendor has not indicated an intent to schedule a sale with reference to a Notice issued to a tenant"},
    },
    "notice_to_tenant_date": {
        "none": 
                {"meaning": "The vendor has not provided the date of the 'notice to tenant to which they intend to schedule the sale"}, 
        "value": 
                {"meaning": "The date of the vendor's 'notice to tenant' is: {} "}
    },
    "retirement": {
        "empty":    
             {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to a retirement date"
        },
        "no": 
            {"meaning": "The vendor has not indicated an intent to schedule a sale with reference to a retirement date"},
    },
    "retirement_date":  {
        "none": 
            {"meaning": "The vendor has not provided the date of the retirement to which they intend to schedule the sale"}, 
        "value": 
            {"meaning": "The vendor's 'retirement date' is: {} "}
            },
    "build_complete": {
        "empty": 
                {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to a building completion date"
        },
        "no":   
                {"meaning": "The vendor has not indicated an intent to schedule a sale with reference to a building completion date"},
    },
    "build_complete_date": {
        "none": 
            {"meaning": "The vendor has not provided the date of the building completion to which they intend to schedule the sale"}, 
        "value": 
            {"meaning": "The vendor's building completion date is: {} "}
            },
    "other_move_factor": {
        "empty": 
                {"meaning": ""},
        "yes": {
                "meaning": "The vendor intends to schedule a sale with reference to another independent event"
        },
        "no":   
                {"meaning": "The vendor has not indicated an intent to schedule this sale in relation to any other reference to another independent event"},
    },
    "other_move_factor_date": {
        "none": 
                {"meaning": "No date has been provided in relation to this 'other' move factor"},
        "value": 
                {"meaning": "The date of the 'other' move factor is: {}"}
                },
    "other_move_factor_details": {
        "true": 
                {"meaning": "The Vendors sale will be impacted by:{}"},
        "false": 
                {"meaning": "No details have been provided in relation to the 'other' move factor that may impact hte transaction schedule"},
    },
    "planning_breach": {
        "empty": {
            "meaning": "It has not been specified if any breaches of planning conditions have occurred"
        },
        "yes": 
            {"meaning": "At least one or more breaches of planning conditions have occured"},
        "no": 
            {"meaning": "No breaches of planning conditions have occurred"},
    },
    "planning_breach_details": {
        "true": {
            "meaning": "A written description of planning breach details effecting this property has been provided"
        },
        "false": {
            "meaning": "No details have been provided regarding the breaches of planning conditions that have occured at this property"
        },
    },
    "bulding_reg_breach": {
        "empty": {
            "meaning": "It has not been stated whether there have or have not been any breaches of Building Regulation conditions"
        },
        "yes": {
            "meaning": "There have been breaches of Building Regulation conditions that effect this property"
        },
        "no": {
            "meaning": "There have been no breaches of Building Regulation conditions that effect this property"
        },
    },
    "bulding_reg_breach_details": {
        "true": {
            "meaning": "Dcumentation has been provided regarding the building regulation breaches that effect this property"
        },
        "false": {
            "meaning": "No documentation has been provided regarding the building regulation breaches that have occured at this property"
        },
    },
    "unfinished_work": {
        "empty": {
            "meaning": "It has not been stated whether any works have been undertaken that presently remain unfinished"
        },
        "yes": 
            {"meaning": "Works have been undertaken to this property that remain unfinished"},
        "no": 
            {"meaning": "There have been no works undertaken to this property that remain unfinished"},
    },
    "unfinished_work_details": {
        "true": {
            "meaning": "Details of the unfinished building works at this property have been provided"
        },
        "false": {
            "meaning": "No work details have been provided regarding the unfinished building work at this property"
        },
    },
    "consent_lack": {
        "empty": {
            "meaning": "It has not been stated whether any works have been undertaken that lack all of the necessary consents"
        },
        "yes": {""
            "meaning": "Works have been undertaken to this property that lack all of the necessary consents"
        },
        "no": {
            "meaning": "No works have been undertaken to this property that lack all of the necessary consents"
        },
    },
    "consent_lack_details": {
        "true": {
            "meaning": "Details have been provided regarding the works that have been undertaken to this property without all of the neccassary consents"
        },
        "false": {
            "meaning": "Details have not been provided regarding the works that have been undertaken to this property without all of the neccassary consents"
        },
    },
    "solar_panels_bool": {
        "empty": {
            "meaning": "It has not been stated whether any solar panels have been installed at this property"
        },
        "yes": 
            {"meaning": "Solar panels have been installed at the property"},
        "no": 
            {"meaning": "Solar panels have not been installed at the property"},
    },
    "solar_installation_year": {
        "none": {
            "meaning": "It has not been stated in which year the Solar panels were installed at the property"
        },
        "value": 
            {"meaning": "Solar panels have been installed at the property:{}"},
    },
    "solar_panels_ownership_bool": {
        "empty": {
            "meaning": "It has not been stated whether the solar panels are owned outright"
        },
        "yes": 
            {"meaning": "The solar panels installed upon this property are owned outright"},
        "no": 
            {"meaning": "The solar panels installed upon this property are not owned outright"},
    },
    "solar_panels_long_lease_ownership_bool": {
        "empty": {
            "meaning": "It has not been stated whether a long lease of the roof / air space has been granted to a solar panel provider"
        },
        "yes": {
            "meaning": "A long lease of the roof / air space has been granted to a solar panel provider"
        },
        "no": {
            "meaning": "No long lease of the roof / air space has been granted to a solar panel provider"
        },
    },
    "solar_electrical_tarrif_docu": {
        "true": {
            "meaning": "No documentation has been provided regarding the solar electrical tarriff or other information regarding the solar panel array at this property"
        },
        "false": {
            "meaning": "No documentation has been provided regarding the solar electrical tarriff or other information regarding the solar panel array at this property"
        },
    },
    "protected_buildings_bool": {
        "empty": {
            "meaning": "It has not been stated whether the property (or any part of it) is listed in the National Heritage List for England"
        },
        "yes": {
            "meaning": "The property (or any part of it) is listed in the National Heritage List for England"
        },
        "no": {
            "meaning": "The property is not listed in the National Heritage List for England"
        },
        "not_known": {
            "meaning": "It is not known if the property (or any part of it) is listed in the National Heritage List for England"
        },
    },
    "protected_buildings_docu": {
        "true": {
            "meaning": "Documents relating to the property's protected Building Statu have been provided"
        },
        "false": {
            "meaning": "No documents relating to the property's Protected Building status have been provided"
        },
    },
    "conservation_area_bool": {
        "empty": {
            "meaning": "It has not been stated whether the property (or any part of it) is in a conservation area"
        },
        "yes": 
            {"meaning": "The property (or a part of it) is in a conservation area"},
        "no": {
            "meaning": "Neither the property or any part of it is in a conservation area"
        },
        "not_known": {
            "meaning": "It is not known if the property (or any part of it) in a conservation area"
        },
    },
    "conservation_area_docu": {
        "true": 
            {"meaning": "Details of the Conservation area have been provided"},
        "false": 
            {"meaning": "Details of the Conservation area have not been provided"},
    },
    "TPO_bool": {
        "empty": {
            "meaning": "It has not been stated whether any trees on the property are subject to a Tree Preservation Order"
        },
        "yes": {
            "meaning": "Trees on the property are subject to Tree Preservation Order controls"
        },
        "no": {
            "meaning": "No trees on the property are subject to a Tree Preservation Order"
        },
        "not_known": {
            "meaning": "It is not known whether any trees on the property are subject to a Tree Preservation Order"
        },
    },
    "order_terms_complied_with": {
        "empty": {
            "meaning": "It has not been stated whether compliance with the terms of the Tree Preservation Order has been sustained"
        },
        "yes": {
            "meaning": "Compliance with the terms of the Tree Preservation Order have been sustained"
        },
        "no": {
            "meaning": "Compliance with the terms of the Tree Preservation Order have not been achieved"
        },
        "not_known": {
            "meaning": "It is not known if there has been full compliance with the terms the terms of the Tree Preservation Order"
        },
    },
    "TPO_docu": {
        "true": 
            {"meaning": "Documentation regarding the TPOs has has provided"},
        "false": 
            {"meaning": "Documentation regarding the TPOs has not been provided"},
    },
    "all_required_consents": {
        "empty": {
            "meaning": "It has not been stated whether consent has been obtained for all matters that need or require them"
        },
        "yes": {
            "meaning": "Consents has been obtained for any matters that require them"
        },
        "no": {
            "meaning": "Consents have not been obtained for all matters that require them"
        },
        "not_known": {
            "meaning": "It is not known if consents have been obtained for all matters that require them"
        },
    },
    "all_required_consents_details": {
        "true": 
            {"meaning": "Details of the consents have been provided"},
        "false": {
            "meaning": "Details concerning required consents have not been provided"
        },
    },
    "charges_bool": {
        "empty": {
            "meaning": " It has not been stated whether the property owner is required to pay any charges relating to the property (independent to council tax and utility charges)"
        },
        "yes": {
            "meaning": "The property owner is liable to pay charges relating to the property (independent to council tax and utility charges) "
        },
        "no": {
            "meaning": "The property owner is liable to pay charges relating to the property (independent to council tax and utility charges)"
        },
    },
    "charges_details": {
        "true": 
            {"meaning": "Details of the charges have been provided"},
        "false": {
            "meaning": "Details have not been provided in relation to the charges imposed on the owner"
        },
    },
    "maintain_road_bool": {
        "empty": {
            "meaning": "It has not been stated whether there is an obligation to pay anything towards the costs of maintaining roads, footpaths or other facilities"
        },
        "yes": {
            "meaning": "There is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities"
        },
        "no": {
            "meaning": "There is no obligation to pay towards the costs of maintaining roads, footpaths and or other facilities"
        },
        "not_known": {
            "meaning": "It is not known whether there is an obligation to pay towards the costs of maintaining roads, footpaths and or other facilities"
        },
    },
    "maintain_road_payement_details": {
        "true": {
            "meaning": "Details of the Road maintenance payment have been provided"
        },
        "false": {
            "meaning": "Details of the Road maintenance payment have not been provided"
        },
    },
    "private_road": {
        "empty": {
            "meaning": "It has not been specified if the property is on a private road or,  is the road that gives access to or adjoins the property a private road"
        },
        "yes": {
            "meaning": "The property is on a private road or,  is located on the road that gives access to or adjoins the property over a private road"
        },
        "no": {
            "meaning": "The property is not on a private road or, is the road that gives access to or adjoins the property over a private road"
        },
        "not_known": {
            "meaning": "It is not known if the property is on a private road or, is the road that gives access to or adjoins the property over a private road"
        },
    },
    "public_expense_road": {
        "empty": {
            "meaning": "It has not been specified whether the roads leading to the property are maintained at public expense"
        },
        "yes": {
            "meaning": "The roads leading to the property are maintained at public expense"
        },
        "no": {
            "meaning": "The roads leading to the property are not maintained at public expense"
        },
        "not_known": {
            "meaning": "It is not known if the roads leading to the property are maintained at public expense"
        },
    },
    "mains_drainage": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a mains drainage network connection"
        },
        "yes": {
            "meaning": "The property benefits from a connection to a mains drainage network"
        },
        "no": {
            "meaning": "The property does not benefit from a connection to the mains drainage network"
        },
    },
    "electricity": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to an electrical supply"
        },
        "yes": {
            "meaning": "The property benefits from a connection to an electrical supply"
        },
        "no": {
            "meaning": "The property does not benefit from a connection to an electrical supply"
        },
    },
    "water_supply": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to a water supply"
        },
        "yes": 
            {"meaning": "The property benefits from a connection to a water supply"},
        "no": {
            "meaning": "The property does not benefit from a connection to a water supply"
        },
    },
    "gas": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to a mains gas supply"
        },
        "yes": {
            "meaning": "The property benefits from a connection to a mains gas supply"
        },
        "no": {
            "meaning": "The property does not benefit from a connection to a mains gas supply"
        },
    },
    "broadband": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to broadband"
        },
        "yes": 
            {"meaning": "The property has the benefit of a broadband connection"},
        "no": {
            "meaning": "The property does not currently benefit from a broadband connection"
        },
    },
    "sewage_plant": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to a private sewage plant"
        },
        "yes": 
            {"meaning": "The property benefits from a private sewage plant"},
        "no": 
            {"meaning": "The property does not benefit from a private sewage plant"},
    },
    "telephone_landlines": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to Landline Telephone services"
        },
        "yes": {
            "meaning": "The property benefits from a Landline Telephone connection"
        },
        "no": {
            "meaning": "The property does not benefit from a Landline Telephone connection"
        },
    },
    "solar_panels": {
        "empty": {
            "meaning": "It has not been stated whether Solar Panels have been installed on the property"
        },
        "yes": 
            {"meaning": "Solar Panels have been installed on the property"},
        "no": {
            "meaning": "Solar Panels have not been installed on the property"
        },
    },
    "heat_pumps": {
        "empty": {
            "meaning": "It has not been stated whether the property benefits from a connection to Ground or air heat pumps"
        },
        "yes": {
            "meaning": "The property benefits from connected Ground or air heat pumps"
        },
        "no": {
            "meaning": "The property does not benefit from the connection of Ground or air heat pumps"
        },
    },
    "other_provisioned_services": {
        "empty": {
                "meaning": "No other additional provisioned services have been disclosed"
        },
        "yes": {
                "meaning": "The property benefits from additional provisioned services not previously disclosed"
        },
        "no": {
                "meaning": "The property does not benefit from any other provisioned services beyond those already disclosed"
        },
    },
    "other_provisioned_services_details": {
        "true": {
                "meaning": "Details regarding the additional provisioned services have been provided"
        },
        "false": {
                "meaning": "No details regarding the additional provisioned services have been provided"
        },
    },
    "shared_facilities_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether the property includes any areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)"
        },
        "yes": {
                "meaning": "There are areas or facilities shared with neighbours (excluding common parts of a leasehold block or estate)"
        },
        "no": {
                "meaning": "No areas or facilities are shared with neighbours (excluding common parts of a leasehold block or estate)"
        },
    },
    "shared_facilities_text_details": {
        "true": 
                {"meaning": "Details of the shared facilities have been provided"},
        "false": 
                {"meaning": "No details of the facilities this property shares with other properties have been provided"
        },
    },
    "parking_arrangement_details": {
        "true": {
            "meaning":      "Details regarding the parking arrangements of the property have been provided"
        },
        "false": 
                {"meaning": "Detials regarding the parking arrangements for the property have not been provided"},
    },
    "controlled_parking": {
        "empty": {
                "meaning": "It has not been disclosed as to whether the property is in a controlled parking zone or within a local authority parking scheme"
        },
        "yes": {
                "meaning": "Ther property is in a controlled parking zone or within a local authority parking scheme"
        },
        "no": {
                "meaning": "The property is not in a controlled parking zone or within a local authority parking scheme"
        },
        "not_known": {
                "meaning": "The disclosure provider does not know if the property is in a controlled parking zone or within a local authority parking scheme"
        },
    },
    "live_at_prop_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether the disclosure provider lives at the property"
        },
        "yes": 
                {"meaning": "The disclosure provider lives at the property"},
        "no": 
                {"meaning": "The disclosure provider does not live at the property"},
    },
    "over_17_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether anyone other then the diclosure provider aged 17 or over lives at the property"
        },
        "yes": {
                "meaning": "Individuals other then the disclosure provider aged 17 or over live at the property"
        },
        "no": {
                "meaning": "No other individuals other then the disclosure provider aged 17 or over live at the property"
        },
    },
    "lodgers_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether any of the occupiers aged 17 or over other then the disclosees are tennants or lodgers"
        },
        "yes": {
                "meaning": "Some or all of the occupiers aged 17 or over are tennants or lodgers"
        },
        "no": {
                "meaning": "None of the occupiers aged 17 or over are tennants or lodgers"
        },
    },
    "agree_to_leave_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether all the occupiers aged 17 and over have agreed to leave before completion"
        },
        "yes": {
                "meaning": "All of the occupiers aged 17 and over have agreed to leave the property before completion of the sale"
        },
        "no": {
                "meaning": "Not all or none of occupiers aged 17 and over have agreed to leave the property before completion of the sale"
        },
    },
    "occupiers_contract_sign_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether all the occupiers aged 17 and over have agreed to sign the sale contract"
        },
        "yes": {
                "meaning": "All the occupiers aged 17 and over have agreed to sign the sale contract"
        },
        "no": {
                "meaning": "Not all or none of the occupiers aged 17 and over have agreed to sign the sale contract"
        },
    },
    "vacant_possession_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether this property is being sold with vacant possession"
        },
        "yes": 
                {"meaning": "This property is being sold with vacant possession"},
        "no": 
                {"meaning": "This property is not being sold with vacant possession"},
    },
    "vacant_possession_proof_docu": {
        "true": {
                "meaning": "Documentation has been provided as proof that this property will be sold with vacant possession"
        },
        "false": {
                "meaning": "Documentation has not been provided as proof that this property will be sold with vacant possession"
        },
    },
    "flooding_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether this property has ever flooded"
        },
        "yes": 
                {"meaning": "This property has previoulsy suffered from one or more incidents of flooding"},
        "no": 
                {"meaning": "This property has not (as far as the discloser knows) ever suffered from flooding"
        },
    },
    "flood_risk_report_bool": {
        "empty": {
                "meaning": "It has not been disclosed whether a flood risk report has been created for this property"
        },
        "yes": 
                {"meaning": "A floood risk report has been created for this property"},
        "no": 
                {"meaning": "A flood risk report has not been created for this property"},
    },
    "flood_risk_report_docu":
         {
         "true": 
                {"meaning": "The Flood Risk report documentation has been provided"}, 
        "false": 
                {"meaning": "No Flood Risk reports have been provided"}
        },
    "nearby_development_bool": {
        "empty":    
            { "meaning": "It has not been disclosed if any of the disclosure providers have been told about plans for any building or developments that might affect someone's ability to peacefully use and enjoy the property"
        },
        "yes":
             { "meaning": "There are plans for development or buildings that may affect someone's ability to peacefully use and enjoy the property"
        },
        "no": 
            { "meaning": "There are no known plans for development or buildings that may affect someone's ability to peacefully use and enjoy the property"
        },
    },
    "nearby_development": 
        {"true":
                 {"meaning": "Further details regarding the nearby development have been provided"}, 
         "false": 
                 {"meaning": "No details regarding the nearby development have been provided"}
    },
    "complaints_bool": {
        "empty": {
                 "meaning": "It has not been stated whether there have been any complaints about the property or a property nearby"
        },
        "yes": {
                 "meaning": "There has been one or more complaints about the property or a property nearby"
        },
        "no": {
                "meaning": "There have not been any known complaints about the property or a property nearby"
        },
    },
    "complaints_details": 
      {"true": 
                {"meaning": "Further details of the complains have been supplied"}, 
      "false": 
                {"meaning": "No further details regarding the complains have been supplied"}},
    "disputes_bool": {
        "empty": {
                  "meaning": "It has not been stated if any of the disclosure providers are aware of anything that might lead to a dispute about this property or a property nearby"
        },
        "yes": {
                  "meaning": "There are things that may lead to a dispute about the property or a property nearby"
        },
        "no": {
                 "meaning": "The discloser is unaware of anything that might lead to a dispute about the property or a property nearby"
        },
    },
    "disputes_details":
         {"true": 
                {"meaning": "Details of the disputes effecting this property have been supplied"}, 
        "false":
                 {"meaning": "No details regarding the disputes effecting this property have been supplied"}},
    "knotweed_bool": {
        "empty": {
                "meaning": "It has not been stated whether the property is affected by Japanese Knotweed"
        },
        "yes":
                 {"meaning": "The property is affected by Japanese Knotweed"},
        "no": 
                {"meaning": "The property is not affected by Japanese Knotweed"},
    },
    "knotweed": 
        {"true": 
                {"meaning": "Details have been provided regarding the effect and extent of Japanese knotweed on this property"}, 
        "false": 
                {"meaning": "No details have been provided regarding the effect and extent of notweed on this property"}},
    "mining_bool": {
        "empty": {
            "meaning": "It has not been stated whether the property is in a mining area"
        },
        "yes": 
                {"meaning": "The property is in a mining area"},
        "no": 
                {"meaning": "The property is not in a mining area"},
    },
    "mining": {
        "true": {
            "meaning": "Information regarding this properties status within a mining area has been provided"
        },
        "false": {
            "meaning": "No other information regarding this property's status within a mining area has been provided"
        },
    },
    "influence_decision_bool": {
        "empty": {
            "meaning": "It has not been stated whether anything has happened in the property that a buyer might want to know or that might influence their decision to purchase the property"
        },
        "yes": {
            "meaning": "Something has happened in the property that a buyer might want to know or that might influence their decision to purchase the property"
        },
        "no": {
            "meaning": "Nothing has happed in the property that is known that a buyer might want to know or that might influence their decision to purchase the property"
        },
    },
    "influence_decision": {
        "true": {
            "meaning": "Other information that might influence the buyers decision to purchase the property has been provided"
        },
        "false": {
            "meaning": "the Other information that might influence the buyers decision to purchase the property has not been expanded upon"
        },
    },
    "neighbours_access_bool": {
        "empty": {
            "meaning": "It has not been stated whether any neighbours or members of the public have any right to enter the property or any part of it"
        },
        "yes": {
            "meaning": "Some neighbours or members of the public have a right to enter part or all of the property"
        },
        "no": {
            "meaning": "No neighbours or members of the public have a right to enter onto any part of the property"
        },
    },
    "neighbours_access": {
        "true": {
            "meaning": "Information has been provided regarding neighbnour access to the property"
        },
        "false": {
            "meaning": "No information has been provided regarding neighbour access to the property "
        },
    },
    "anything_else_bool": {
        "empty": {
            "meaning": "It has not been declared if there is anything else that the buyer might want to know that may influence thier decision to buy or sell the property"
        },
        "yes": {
            "meaning": "It has been been declared that there is other information that the buyer might want to know or might influence their decision to buy the property"
        },
        "no": {
            "meaning": "There is no other information not already provided that the discloser/s consider a buyer might want to know about the property or that might influence their decision to buy the property"
        },
    },
    "anything_else": 
        {"true": 
            {"meaning": "Additional details have been provided regarding information not previously provided that a buyer might want to know and might influence their decisiont to buy the property"}, 
        "false": 
            {"meaning": "No details have been provided regarding the additional information not previously provided that a buyer might want to know and might influence their decisiont to buy the property"}
            },
    "data_providers": {
        "value": {
            "equation": {
                "larger_than": {
                    "vari": 1,
                    "meaning": "This data has been provided by {} people",
                },
                "less_than": {
                    "vari": 1,
                    "meaning": "The number of persons providing this data has not been specified",
                },
            },
            "default": 
                    {"meaning": "This data has been provided by one individual"},
        },
        "row_wrap": {"wrap": "{row}", "preface": "increment"},
        "rows": {
            "data_provider_first_name": {
                "none": 
                        {"meaning": ""},
                "value": 
                        {"meaning": "{}"},
            },
            "data_provider_middle_name": {
                "none": 
                        {"meaning": ""},
                "value": 
                        {"meaning": "{}"},
            },
            "data_provider_surname": {
                "none": 
                        {"meaning": ""},
                "value": 
                        {"meaning": "{}"},
            },
            "data_provider_type": {
                "empty": 
                        {"meaning": ""},
                "seller": 
                        {"meaning": "The vendor"},
                "seller_rep": 
                        {"meaning": ""},
                "Other": 
                        {"meaning": ""},
            },
            "data_provider_type_details": {
                "true": 
                        {"meaning": ""},
                "false": 
                        {"meaning": ""},
            },
            "data_provider_middle_names": {
                "none": 
                        {"meaning": ""},
                "value": 
                        {"meaning": "{}"},
            },
        },
        "none": {"meaning": ""},
    },
    "works_and_alterations": {
        "none": {"meaning": ""},
        "value": {
            "equation": {
                "larger_than": {
                    "vari": 0,
                    "meaning": "There have been {} alterations made to the property",
                }
            },
            "default": {
                    "meaning": "There have been no notable alterations to the property, no details of alterations can be recalled or are recorded"
            },
        },
        "rows": {
            "building_works_and_alterations": {
                "empty": 
                        {"meaning": ""},
                "resi": 
                        {"meaning": "Part of the property is not used for residential occupation eg commercial use"},
                "replace_element": 
                        {"meaning": "Since 1 April 2002 the installation of replacement elements has taken place, such as ; replacement windows, roof windows, roof lights, glazed doors"},
                "garage_conversion": 
                        {"meaning": "During the vendor's ownership a garage conversion has been undertaken"},
                "extension": 
                        {"meaning": "During the vendor's ownership an extention of the property has been undertaken"},
                "conservatory": 
                        {"meaning": "During the vendor's ownership a conservatory has been installed"},
                "loft_conversion":
                         {"meaning": "During the vendor's ownership a loft conversion has been undertaken"},
                "wall_remove": 
                        {"meaning": "During the vendor's ownership one or more walls have been removed"},
                "other_change": 
                        {"meaning": "During the vendor's ownership unspecified works and alterations have been undertaken"},
            },
            "property_alterations_work_details": {
                "true": 
                        {"meaning": "Details of the alteration works undertaken at the property have been disclosed"},
                "false": 
                        {"meaning": "No details of the alteration works undertaken at the property have been disclosed"},
            },
            "alterations_work_start": {
                "none": 
                        {"meaning": "The date the alterations works to the property commenced has not been disclosed"},
                "value": 
                        {"meaning": "The alterations started on {}"},
            },
            "alterations_work_end": {
                "none": 
                        {"meaning": "The date the alteratons works to the property ended has not been disclosed"},
                "value": 
                        {"meaning": "The alterations ended on {}"},
            },
            "property_works_completed_bool": {
                "empty": 
                        {"meaning": "It has not been confirmed whether the alteration works undertaken at the property have been completed"},
                "yes": 
                        {"meaning": "The alteration works undertaken at the property have been completed"},
                "no": 
                        {"meaning": "The alteration works undertaken at the property have not been completed"},
            },
            "completion_of_work_details": {
                "true": 
                        {"meaning": "Details of the completion of works has been provided"},
                "false": 
                        {"meaning": "Details of the completion of works has not been provided"},
            },
        },
    },
    "over_17": {
        "none": 
            {"meaning": "There are no other persons aged seventeen (17) or over living at the property"},
        "value": {
            "meaning": "There are currently {} individuals aged 17 or over living at the property"
        },
        "rows": {
            "first_name_17": 
                  {"none": 
                            {"meaning": ""},
                    "value": 
                            {"meaning": ""}},
            "middle_name_17": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": ""}},
            "surname_17": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": ""}},
        },
    },
    "flood_events": {
        "none":     
                    {"meaning": "There have not been any flooding events at this property"},
        "value": {
            "equation": {
                "larger_than": {
                    "vari": 0,
                    "meaning": "There have been {} recorded flood events at the property",
                }
            },
            "default": {
                    "meaning": "There have been no notable flood events where the details can be recalled or are recorded"
            },
        },
        "rows": {
            "flood_type": {
                "empty": 
                    {"meaning": "The nature of the flooding has not been specified"},
                "Ground water": 
                    {"meaning": "The property has been flooded by Groundwater"},
                "Sewer flooding": 
                    {"meaning": "The property has been flooded from Sewers "},
                "Surface water": 
                    {"meaning": "The property has been flooded by surface water "},
                "Coastal flooding": 
                    {"meaning": "The property has been flooded by Coastal flooding "},
                "River flooding": 
                    {"meaning": "The property has been flooded by river discharge "},
                "Other": 
                    {"meaning": "The property has been flooded by either several factors or otherwise attributable to another source other than the most common causes  "},
            },
            "other_flood_type_description": {
                "true": 
                    {"meaning": "An additional detailed description of the flood event/s has been provided: {}"},
                "false": 
                    {"meaning": "No additional detailed description of the flood event/s has been provided"},
            },
            "flood_event_date":
                {"none": 
                    {"meaning": "The dates of the flood event/s have not been provided"}, 
                 "value": 
                    {"meaning": "A flood event occurred on: {}"}
                    },
            "flood_area_details": 
                {"true": 
                    {"meaning": "Details of the areas that were effected by flooded have been disclosed"}, 
                "false": 
                    {"meaning": "No details have been provided of the areas that were effected by flooding"}
                    },
        },
                },
              "disclose_address_line_1": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": "{}"}},
                "disclose_address_line_2": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": "{}"}},
                "disclose_address_line_3": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": "{}"}},
                "disclose_postcode_address_town_or_city": {
                    "none": 
                            {"meaning": ""},
                    "value": 
                            {"meaning": "{}"},
                },
                "disclose_postcode": 
                    {"none": 
                            {"meaning": ""}, 
                    "value": 
                            {"meaning": "{}"}},
                "disclose_UPRN": 
                    {"none": 
                            {"meaning": "The UPRN for this property has not been disclosed"}, 
                    "value": 
                            {"meaning": "The UPRN of the property is {}"}
                },
}
