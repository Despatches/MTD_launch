reader = ['FCA', 'principle'],
purpose = ['regulator_compliance', 'principal_compliance','paper-trail', 'legal_contract', 'legal_case_compliance', 
'underwriter_cover', 'marketing_terms', 'inhouse_pii', '3rd_party_pii', 'product_training', ]

gbr = 'general binding rules for small sewage discharge to ground'
mortgage_product = 'finance product'
ssp = 'small sewage treatment plant'
bdh = 'boundary demarcation or segregation hardware'
condue = 'within the purview of full disclosure and due diligence and conveyance of title'

boundary_dispute_data=''#

mortgage_components = {
	'small_sewage_treatment_plant_intallation':{
		'target_markets':{
			'stamps':{'general-binding-rules-small-sewage-discharge-to-the-ground':False},

			'description':f'purchase and installation of {ssp}',

			f'match_steps':f"""properties that are sold after 1 January 2015 must either comply {gbr} at the point of completion, or the new
							owner must ensure that the correct works are undertaken to comply with the rules else apply for an environmental permit
							to continue to discharge sewage to ground in the current format""",

			'target_market':"""Properties that are being sold which have either not been sold since 31st December 2014 and do not comply with the general 
								binding rules or properties that have sold but still do not comply with the general binding rules for small sewage discharge to ground.
								Properties who have an environmental permit for the current sewage discharge would not require the
								permit if made to comply with the rules would also be target properties""",
			
			'match_target_needs':{
									'basic' :f"""installation of small sewage treatment plants in properties that do not comply with the {gbr}
									can often be expensive. The small sewage treatment plants are seldom valued at below £2500 discluding
									installation costs and vat. The {mortgage_producut} reduces the upfront cost of buying a property that requires 
									a new sewage treatment plant either to comply with the {gbr} or because they wish to be more environmentally
									conscious and thus install a small sewage treatment plant as opposed to utilising a environment agency exemption
									permit. Inclusion of an extra indemnity layer for the installation of the sewage treatment plant in case of 
									unexpected delays in the new owners use of the property is also important.""",

									'how':f"""collaborations with {ssp} manufacturers allows a guaranteed acquisition price for the correctly sized {ssp}. correct size of 
											{ssp} can be determined by"""
								},

			'collaborations':['company_title':'','role':'','written_agreement':'', 'role_in_approval':""]
		}
	},

	'boundary_fence':{
		'target_markets':{
			'stamps':{
				'boundary_disclosure':True,
				'outside_area':True
			},

			'description':'purchase and installation of new boundary demarcation or segregation hardware (fencing of property)',

			'match_steps':f"""Properties sold with outdoor areas must have de-marked boundaries in order to provide security of title.
							Where boundaries are in poor condition, e.g the fencing or demarcation is:insecure, in poor condition, is
							no longer in place, inconsistent or unclear. The product provides for the repair of the given boundaries."""

			'match_target_needs':{
				'basic':f"""Correct installation of boundary demarcation or segregation hardware helps to protect a title's condition.
						UK property boundaries are determined upon the principle of occupation and beneficial use administered and assigned under a Torrens procedural framework, 
						as a result the ownership of the property that is not clearly and competently enclosed,  utilized and protected may become liable to challenge and be
						considered to have changed to the beneficial user or encloser of the property should they enforce it. 
						This may be effected through an application and is known as adverse possession. 
						Importantly:  {boundary_dispute_data} An significant number of boundary defects and additionally many potentially costly disputes between neighbors are
						caused by disagreements over poor application of physical boundary position demarcation and administrative discipline. 
						Many boundary disputes originate and are caused by no less than differing recollections of position, alignment or features over a period
						of time.  
						It is extremely beneficial for boundaries to be robustly verified within discrete disclosure and secured by detailed physical procedure promptly: {condue}"""
			}
		},

		'mitigated_risk':{
			'boundary_position_dispute':{
				'risk':'dispute arising over correct position of title boundary',
				'effect':''
			},
			'adverse_position':{
				'risk':'decrease in land total area',
				'effect'{'decreased_security_value':{}}
			},
		}
	}

	'oil_tank':{
		'target_markets':{ 
			'stamps':{
				'boundary_disclosure':True,
				'outside_area':True
			},

			'description':'funding for purchase and installation of replacement oil storage tank and support infrastructure compliant with regulatory obligations (including OFTEC standards)',

			# 'match_steps' : Factual Need ; For the additional Lending 
			'match_steps':f"""Properties sold with oil storage tanks must ensure infrastructure meets the legal regulatory standards to comply with security of title obligations.
							Oil tanks in poor condition or failing to comply with contemporaneous legal standards,  binding obligations and best practice, e.g fire breaks, environmental protection measures bunded, leak alert, spill mitigation emergency response and safe replenishment plans.
							are in place.  The product provides for the replacement of infrastructure and provision of domestic fuel management tools to ensure the property can be maintained safely for occupants and the environment in compliance with regulations."""



			# 'match_target_needs' : Basic : how this matches the 
									# 	How 
			'match_target_needs':{
				'basic':f"""Correct installation of oil storage and supply pipework infrastructure is an essential component of a property's operational integrity and must be sustained in compliance to protect a title's condition.
						Environmental regulations determine the proximity of risk arsing from oil storage to be determined by the physical relationships of known hazards to discrete ecological assets , natural habitats.  
						Landowners and occupiers are bound in law to protect the environment and the public domain from harm as directed by: under the occupiers liability [Occupiers Liablity Act 1957] 
						Oil tanks are required to be bunded to contain the leakage of fuel from a principal tank. 
						
						Fuel risks arise where tanks are:[ 
							not bunded by a secondary containment vessel, 
							located within 10m of a water channel or drain or sewer or ditch or culvert,
							located on raised ground or gradients exhibiting runoff characteristics,
							replenished in proximity in proximity to a high risk landscape or adjacent feature,
							oy replenished without reference to a safe delivery plan, 
							not inspected and evaluated on a regular basis by a competent person,
							located within 1.8m of non fire rated building], ****


						Failure to comply with oil storage regulations may lead to enforcement action from regulators; Building Standards, Environment Agency.
						Properties not complying with oil storage regulations may breach planning regulations.
						Regulatory interventions can take the form of; advice and encouragement to comply, regulatory enforcement, prosecution.
						Contamination of land owned or occupied by a third party will invariably result in a claim for costs form insurers and effected parties.
						Contamination resulting in displacement from a dwelling, business interruption can result in substantial claims for damages.
						In the event of a contamination arsing from a defective oil storage installation a claim in negligence with punitive damages may arise.

						Contamination of land may effect the continued use of the land and adversely effect the Title's security value.
						Importantly: Oil delivery professionals that become aware of a storage facility failing to meet the conformity standard cannot replenish fuel supplies.  
						Many oil leaks arise form legacy tank installations when the owner is unaware of oil storage regulations and a failure to comply with the required standard.
						It is extremely beneficial for OIl storage installations to be inspected by an Oftec recognised professional to determine compliance status. : {condue}"""
			},
		},

		'mitigated_risk':{
			'oil_tank_complince_standard':{
				'risk':'dispute arising over correct position of title boundary',
				'effect':''
			},
			'environmental_assessment':{
				'risk':'evaluate_proximate_risk-build_protocol',
				'effect'{'decrease_risk_exposure':{}}
			},
			'regulation_publication':[
				'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1108428/ADJ_2022.pdf',
				]
			},
			'regulation_reference':[
			'The Building Regulations 2010','Combustion appliances and fuel storage systems','J6':'Protection of liquid fuel storage systems'
				]
					'''															1.8m away from non-fire rated eaves of a building
																				1.8m away from a non-fire rated building or structure (e.g. garden sheds)
																				1.8m away from openings (such as doors or windows) in a fire rated building or structure (e.g. brick-built house/garage)
																				1.8m away from liquid fuel appliance flue terminals
																				760mm away from a non-fire rated boundary, such as a wooden boundary fence
																				600mm away from screening (e.g. trellis and foliage) that does not form part of the boundary.
																				If separation distance is not possible then fire protection barrier with a minimum 30 min fire rating required.'''
					]
			},	

		}
}