

//add new table row to multi row data tables
function add_new_table_row(table,table_ref, new_row, row_num){
	$(table).append(new_row);
	$(`#${table_ref}_asset_inputs`).slideUp();
	$(`button[table_name='${table_ref}'][row='${row_num}']`).click(function(){
	$(`tr[table_name=${table_ref}][row_num=${$(this).attr('row')}]`).remove();
		});
}


// creates input triggers for multi row tables and infils multi row data in tables
function multi_row_data_table(table_ref, trigger,inputs){
	var new_row
	var table = $(`#${table_ref}`)
	var table_row = 0
	var cell_display = ''
	var cell_false = 0
	var allow_details = true

	$(`#${table_ref}_asset_inputs`).slideUp();

	$(`#${table_ref}_new_asset`).click(function(){
		$(`#${table_ref}_asset_inputs`).slideDown();
	});

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
					if //(item.input_type == 'radio' || item.input_type == 'bool'|| item.input_type == 'checkbox'|| item.input_type == 'bool_extra'){
						(item.input_type == ('radio' || 'bool'||'checkbox'||'bool_extra')){
						if (cell_value != (false || 'empty')){
							cell_display = $(`input[name=${item.identifier}]:checked`).attr('display');
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
						cell_display = ''
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
			'radio': function(item, cur_row){cell_display = $(`input[name=${item.identifier}][value=${cur_row[item.identifier]['value']}]`).attr('display')
			return cell_display
			},
			'detail_text':function(item, cur_row){
				cell_display = empty_text_values(cur_row[item.identifier])
				return cell_display
			}
		}

		/* FILLs table with already chosen multi selections */
		function table_pre_fill(data_row_ref){
			//console.log(data_row_ref)
			table_row = parseInt($(table).attr('row_num'), 10);
			table_row++;
			$(table).attr('row_num', table_row)
			//var cur_row = sub_table_data[table_ref]['data'][data_row_ref];
			var cur_row = data_row_ref;
			new_row = `<tr table_name=${table_ref} row_num='${table_row}' uploaded = 'no' ref = '${data_row_ref}'>`
			for (var i = 0; i<inputs.length;i++){
				var item = inputs[i];
				if (item.input_type == "none"){continue};
				//cur_row[item.identifier]
//				console.log(cur_row[item.identifier]['value'])
				var stored_data_piece = data_row_ref[item.identifier]
				if (stored_data_piece == undefined){
					cell_display = ''
					cell_false = 1
				} else {
					cell_false = 0
					if (multi_row_display_evaluations[item.input_type] != undefined){
						cell_display = multi_row_display_evaluations[item.input_type](item, data_row_ref);
					}else{
						cell_display = cur_row[item.identifier]['value'];
					};
				};
				new_row += `<td row='${table_row}' type="data" table_name="${table_ref}" name="${item.identifier}" val = ${cur_row[item.identifier]['value']} fa=${cell_false} uploaded = 'yes' ref = '${data_row_ref}'>${cell_display}</td>`
			};
			new_row += `<td><button class="button is-warning is-small" row='${table_row}' table_name="${table_ref}">Delete</button></td>`
			new_row += '</tr>'
			add_new_table_row(table, table_ref,new_row, table_row);
		};
		//console.log(results)
		if (results[table_ref] != undefined && results[table_ref]['rows'] != 'none'){
			results[table_ref]['rows'].forEach(table_pre_fill);
		}
		
	};