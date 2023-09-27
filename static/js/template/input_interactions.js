	function multi_row_data_table(table_ref, trigger,inputs){
		console.log(table_ref)
		var new_row
		var table = $(`#${table_ref}`)
		var table_row = 0
		var cell_display = ''
		var cell_false = 0
		/*function delete_table_row(table_ref, button){
			$(button).click(function(){
				alert("4")
				$(`tr[table_name=${table_ref}][row_num=${$(this).attr('row')}]`).remove();
			});
		};*/
		var allow_details = true

		$(`#${table_ref}_asset_inputs`).slideUp();

		$(`#${table_ref}_new_asset`).click(function(){
			$(`#${table_ref}_asset_inputs`).slideDown();
		});

		function add_new_table_row(table,table_ref, new_row, row_num){
			$(table).append(new_row);
			$(`#${table_ref}_asset_inputs`).slideUp();
			$(`button[table_name='${table_ref}'][row='${row_num}']`).click(function(){
			$(`tr[table_name=${table_ref}][row_num=${$(this).attr('row')}]`).remove();
				});
			//console.log(new_row)
		}
	$(trigger).click(function(){
		/*precursor_functions.forEach(function(item){
			item();
		});*/
		if (allow_details == true){
			table_row = parseInt($(table).attr('row_num'), 10)
			table_row += 1
			new_row = `<tr table_name=${table_ref} row_num='${table_row}', uploaded = 'no', ref = 'none'>`
			$(table).attr('row_num', table_row)
			inputs.forEach(function(item){
				if (item.input_type != 'none'){
					var final_input = final_input_value(item);
					var cell_value = final_input.value;
					cell_display = '';
					cell_false = 0
					if (item.input_type == 'radio' || item.input_type == 'bool'|| item.input_type == 'checkbox'|| item.input_type == 'bool_extra'){
						if (cell_value != (false || 'empty')){cell_display = $(`input[name=${item.identifier}]:checked`).attr('display');
						};
						$(`input[name="${item.identifier}"]`).each(function(){
							$(this).prop("checked", false);
						});
					}else{
						$(`#${item.identifier}`).val("");
						if (cell_value != false){cell_display = final_input.value};
					};
					if (cell_value == false){
						cell_false = 1
					};
					
					//alert(cell_false)
					new_row += `<td row='${table_row}' type="data" table_name="${table_ref}" name="${item.identifier}" val = ${cell_value} fa=${cell_false} uploaded = 'no' ref = 'none'>${cell_display} </td>`

					item.value=undefined;
				}
				
			});
			//alert(new_row)
			new_row += `<td><button class="button is-warning is-small" row='${table_row}' table_name="${table_ref}">Delete</button></td>`
			new_row += '</tr>'
			add_new_table_row(table,table_ref, new_row,table_row);			
		};
	});

		multi_row_display_evaluations = {
			'radio': function(item, cur_row){cell_display = $(`input[name=${item.identifier}][value=${cur_row[item.identifier]}]`).attr('display')
			return cell_display
			},
			'detail_text':function(item, cur_row){
				cell_display = empty_text_values(cur_row[item.identifier])
				return cell_display
			}
		}

		if (sub_table_data != 'none'){
			if (sub_table_data[table_ref] != ('empty' || undefined)){
				//alert(sub_table_data[table_ref])
				Object.keys(sub_table_data[table_ref]['data']).forEach(function(data_row_ref){
					table_row = parseInt($(table).attr('row_num'), 10);
					table_row += 1;
					$(table).attr('row_num', table_row)
					var cur_row = sub_table_data[table_ref]['data'][data_row_ref];
					new_row = `<tr table_name=${table_ref} row_num='${table_row}' uploaded = 'yes' ref = '${data_row_ref}'>`
					inputs.forEach(function(item){
						//cur_row[item.identifier]
						var stored_data_piece = cur_row[item.identifier]

						if (stored_data_piece == undefined){
							cell_display = ''
							cell_false = 1
						} else {
							cell_false = 0
							if (multi_row_display_evaluations[item.input_type] != undefined){
								cell_display = multi_row_display_evaluations[item.input_type](item, cur_row)
							}else{
								cell_display =cur_row[item.identifier]
							};
						};
						new_row += `<td row='${table_row}' type="data" table_name="${table_ref}" name="${item.identifier}" val = ${cur_row[item.identifier]} fa=${cell_false} uploaded = 'yes' ref = '${data_row_ref}'>${cell_display}</td>`
					});
					new_row += `<td><button class="button is-warning is-small" row='${table_row}' table_name="${table_ref}">Delete</button></td>`
					new_row += '</tr>'
					add_new_table_row(table, table_ref,new_row, table_row);
				});
			};
		};
	};
function db_bool_convert(val){
	var new_val = val
	if (val == 'yes'){
		new_val = '1'
	} else if (val == 'no'){
		new_val = '0'
	};
	return new_val
};


function multi_choice_evals(item){
			if (item.radio_function === undefined){
				item.radio_function="none"
			};
			if (item.styling != undefined){
				if (item.styling == 'dropdown'){
					var dropdown = $(`select[id=${item.identifier}]`)

					$(`input[name=${item.identifier}]:checked`).val($(dropdown).val());
					$(dropdown).change(function(){
						alert($(dropdown).val());
						$(`input[name=${item.identifier}]:checked`).val($(dropdown).attr('value'));
					});
					if (results != 'none'){
						if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
							$(`input[name = ${item.identifier}][value=${results[item.identifier]['value']}]`).click()
						};
					};
				} else if (item.styling == 'block'){
					var rad_block = $(`div[radio_block=${item.identifier}]`)
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
				};
			} else{
				if (results != 'none'){
					if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined){
							$(`input[name = ${item.identifier}][value=${results[item.identifier]['value']}]`).click()
						}
					};
			};
			empty_radio_set(item.identifier, item.radio_function);
		
		};

function json_date_conversion(date){
	var currentDate = new Date(date);
	var date = ("0" + currentDate.getDate()).slice(-2);
	var month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
	var year = currentDate.getFullYear();
	var dateString = year + "-" + month + "-" + date;
	return dateString	
};

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
function input_interactions(item){
	var form_object
	var element
	if (item['input_type'] == 'none' && item['form_object'] != 'none'){
		form_objects[item['form_object']['identifier']] = item['form_object'];
		form_objects[item['form_object']['identifier']]['elements'] = {};
	} else if(item['input_type'] != undefined){
		if (empty_and_convert_funcs[item.input_type] != undefined){
			empty_and_convert_funcs[item.input_type](item)
		}else if(item.input_type != "multi_row"){
			if (item.input_type == 'radio'|| item.input_type == 'bool_extra'){
				multi_choice_evals(item)
			}else{
				
				if (results[item.identifier] != undefined && results[item.identifier]['value'] != undefined || false){
					var pre_value = results[item.identifier]['value'];
						$(`#${item.identifier}`).val(pre_value);
				};
				
				empty_input(item['identifier']);
			};
		} else if (item.input_type == 'multi_row'){
			console.log(item)
			multi_row_data_table(item.identifier, $(`#add_${item.identifier}`), item.data_rows);
			empty_and_convert(item.data_rows);
		};
		if (item['form_object'] != 'none'){
			form_object = item['form_object']['identifier']
			element = item['form_object']['element']
			form_objects[form_object]['elements'][element] = item['identifier']
		}
	};

}

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

function empty_input(input){
	$(`#${input}_empty`).click(function(){
		$(`#${input}`).val("");
	});
};	


function empty_and_convert(data_fields){
	data_fields.forEach(item => input_interactions(item));
};