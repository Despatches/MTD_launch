
//convert 'yes' 'no' to '1' '0'
function db_bool_convert(val){
	var new_val = val
	switch(val){
		case "yes":
			return "1"
			break;
		case "no":
			return "0"
			break;		
	}
};



function multi_choice_evals(item){
	if (item.radio_function === undefined){
		item.radio_function="none"
	};
	if (item.styling != undefined){
		switch(item.styling){
			case 'dropdown':
				var dropdown = $(`select[id=${item.identifier}]`)
				var selected_dropdown_checkbox =$(`input[name=${item.identifier}]:checked`);
				$(selected_dropdown_checkbox).val($(dropdown).val());
				$(dropdown).change(function(){
					alert($(dropdown).val());
					$(selected_dropdown_checkbox).val($(dropdown).attr('value'));
				});
				if (results != 'none'){
					if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
						$(`input[name = ${item.identifier}][value=${results[item.identifier]['value']}]`).click()
					};
				};
				break;
			case 'block':
				// styling for reformatting radio in to a block of options 
				var rad_block = $(`div[radio_block=${item.identifier}]`);
				$(rad_block).mouseenter(function(){
					$(this).css({"background-color":"#f9f7f7"});
				});
				$(rad_block).mouseleave(function(){
					if ($(this).prop("selected") == true){
						$(this).css({"background-color":"#ede6e6"});
					} else{
						$(this).css({"background-color":"lightblue"})
					};
				});
				$(rad_block).click(function(){
					$(rad_block).each(function(){
						$(this).prop("selected", false)
						$(this).css({"background-color":"lightblue"})
					});
					$(this).css({"background-color":"#ede6e6"});
					$(this).prop("selected", true);
					//$(`input[name=${item.identifier}][value='${$(this).attr('val')}']`).click();
				});
				if (results != 'none'){
					if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
						$(`div[radio_block=${item.identifier}][hidden_value=${results[item.identifier]['value']}]`).click()
					}
				};				
		}
	} else{
		if (results != 'none'){
			if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
				$(`input[name = ${item.identifier}][value=${results[item.identifier]['value']}]`).click()
			}
		};
	};
	empty_radio_set(item.identifier, item.radio_function);

};

//converts dates as they arrive from python
function json_date_conversion(date){
	var currentDate = new Date(date);
	var date = ("0" + currentDate.getDate()).slice(-2);
	var month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
	var year = currentDate.getFullYear();
	var dateString = year + "-" + month + "-" + date;
	return dateString	
};

/*stores functions for empty and convert funtion for each input type needs to be updated as
 more input types are referencd in templates
      */
var empty_and_convert_funcs = {
	'checkbox': function(item){
		if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
		var resulty = results[item.identifier]['value']
			if (resulty == 'yes'){
				$(`input[name=${item.identifier}]`).click()
			};
		};
		$(`#${item.identifier}_empty`).click(function(){
			$(`input[name=${item.identifier}]`).prop('checked',false)
		});
	},
	'bool':function(item){
			if (results != 'none'){
				if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
				results[item.identifier]['value'] = db_bool_convert(results[item.identifier]['value'])
				//alert(results[item.identifier]['value'])
			}
		};
		multi_choice_evals(item)
	},
	'text':function(item){
			if (item.styling != undefined && item.styling['stock_options'] != undefined/*item.stock_options.options.length > 0*/){
				var stock_other = $(`#${item.identifier}_stock_other`);
				$(stock_other).slideUp();
				$(`select[id=${item.identifier}_stock]`).change(function(){
					if ($(this).val() == 'other'){
						$(stock_other).slideDown();
					}else{
						$(stock_other).slideUp()
					};
				});
				$(`#${item.identifier}_empty`).click(function(){
					$(`#${item.identifier}_stock`).val("");
					$(`${stock_other}`).val("");
					$(`${stock_other}`).slideUp();
				});
				if (results != 'none'){
					if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
						var other = true
						$(`option[group=${item.identifier}_stock]`).each(function(){
								var stock_opt = $(this).val();
								if (stock_opt == results[item.identifier]['value']){
									$(`select[id=${item.identifier}_stock]`).val(stock_opt);
									other = false;
								};
							});
							if (other == true){
								$(`select[id=${item.identifier}_stock]`).val('other');
								$(`input[id=${item.identifier}_stock_other]`).val(results[item.identifier]['value']);
								$(`div[id=${item.identifier}_stock_other]`).slideDown();
							};
					};
					//$(`input[name = ${item.identifier}][value=${results[item.identifier]['value']}]`).click();
				};
				empty_input(item['identifier']);
				if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
					var pre_value = results[item.identifier]['value'];
					if (pre_value != false || undefined){
						$(`#${item.identifier}`).val(pre_value);
					};
				};
			} else{
				empty_input(item['identifier']);
			}

		},
		'date':function(item){
			if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
				var date = json_date_conversion(results[item.identifier]['value'])				
				$(`input[id=${item.identifier}]`).val(date)
			};
		},
		'detail_text':function(item){
			$(`#${item.identifier}_empty`).click(function(){
				empty_input(item['identifier']);
			});
			if (results != 'none' && (results[item.identifier] != undefined && results[item.identifier]['value'] != (undefined || '0'))){
				var pre_value = results[item.identifier]['value'];
				$(`#${item.identifier}`).val(pre_value);
			} else{
				$(`#${item.identifier}`).val('');
			};			
		},
		'docu':function(item){
			return 0 
		},
		'email':function(item){
			if (results != 'none' && (results[item.identifier] != undefined && results[item.identifier]['value'] != (undefined || '0'))){
			var pre_value = results[item.identifier]['value'];
			$(`#${item.identifier}`).val(pre_value);			
			var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
			$(`#${item.identifier}`).keyup(function(){
				if ($(`#${item.identifier}`).val().match(validRegex)){
					$(`#${item.identifier}`).removeClass('neg_border')
				}else{
					$(`#${item.identifier}`).addClass('neg_border')
				}
			});
			empty_input(item.identifier)
		}
	}	
};

function find_form_object(q_item){
	if (q_item['input_type'] == 'none' && q_item['form_object'] != 'none'){
		form_objects[q_item['form_object']['identifier']] = q_item['form_object'];
		form_objects[q_item['form_object']['identifier']]['elements'] = {};
		return true;
	}
	return false;
}
function input_interactions(item){
	var form_object
	var element
	var in_type = item.input_type;
	if (find_form_object(item)){
		form_objects[item['form_object']['identifier']] = item['form_object'];
		form_objects[item['form_object']['identifier']]['elements'] = {};
	} else if(item['input_type'] != undefined){
		if (empty_and_convert_funcs[in_type] != undefined){
			empty_and_convert_funcs[in_type](item)
		}else if(in_type != "multi_row"){
			if (in_type == 'radio'|| in_type == 'bool_extra'){
				multi_choice_evals(item)
			}else{
				var result_val = results[item.identifier]['value'];
				if (results[item.identifier] != undefined && (!result_val || result_val!=undefined)){
					var pre_value = results[item.identifier]['value'];
						$(`#${item.identifier}`).val(pre_value);
				};
				
				empty_input(item['identifier']);
			};
		} else if (in_type == 'multi_row'){
			// do all the multi row input_interactions and data prefills
			multi_row_data_table(item.identifier, $(`#add_${item.identifier}`), item.data_rows);
			empty_and_convert(item.data_rows);
		};
		if (item['form_object'] != 'none'){
			form_object = item['form_object']['identifier'];
			element = item['form_object']['element'];
			// de-genericise object from object list
			form_objects[form_object]['elements'][element] = item['identifier'];
		}
	};

}


//emptyies radio button inputs
function empty_radio_set(radio_set, scroll_trigger){
	$(`#${radio_set}_empty`).click(function(){
		if (scroll_trigger != "none"){
			scroll_trigger()
		};		
			$(`input[name=${radio_set}]`).each(function(){
				$(this).prop("checked", false)
			});
		});
	};

//empty standard input
function empty_input(input){
	$(`#${input}_empty`).click(function(){
		$(`#${input}`).val("");
	});
};	

//creates click events for emptying inputs
//also inputs pre existing data in input areas
function empty_and_convert(data_fields){
	data_fields.forEach(item => input_interactions(item));
};


