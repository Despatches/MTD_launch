function list_match(value, list){
	var list_len = list.length
	var count = 0
	var match = false
	while (count < list_len){
		if (value == list[count]){
			match = true
		};
		count++
	};
	return match
};
function reliance_input_colector(item){
	var data_input_collector
	var collect_val
	if (item.type == 'radio' || item.type == 'bool' ||  item.type == 'bool_extra' || item.type == 'checkbox'){
		data_input_collector = $(`input[name='${item.identifier}']`)
		collect_val =  $(`input[name=${item.identifier}]`)
	} else {
		data_input_collector = $(`#${item.identifier}`)
	}
	return [collect_val, data_input_collector]
}
function bulk_send_reliances(form_flow_controls, type='form'){
	form_flow_controls.forEach(function(reliance_set){
		$(`#${reliance_set.control_subject}_container`).slideUp();
		$(`#${reliance_set.control_subject}_warning`).slideUp();

		var rel_len = reliance_set.reliances.length
		var view_change = false
		var control_subject = reliance_set.control_subject
		//function rel_eval(rel_len, reliances, change){

		//}
		reliance_set.reliances.forEach(function(item){
			var data_input_collector;
			var collect_val;
			var new_reliance_value;
			returns = reliance_input_colector(item)
			data_input_collector  = returns[1]
			collect_val = returns[0]
			$(data_input_collector).change(function(){
				if (item.type == 'radio' || item.type == 'bool' ||  item.type == 'bool_extra' || item.type == 'checkbox'){
					new_reliance_value = $(`input[name='${item.identifier}']:checked`).val()
				}else {
					new_reliance_value = (`#${item.identifier}`).val()
				}
				var matchy =list_match(new_reliance_value,item.value)
				if (type == 'form'){
					if (matchy == true){
						if ($(`#${control_subject}_warning`).attr('confirmed') != 'true'){
							$(`#${control_subject}_warning`).slideDown()
						};
					} else if (matchy == false|| new_reliance_value.length  == 0){
						$(`#${control_subject}_warning`).slideUp();
					};			
					if ($(`#${control_subject}_container`).attr('status') != 'locked'){
						if (matchy == true){
							$(`#${control_subject}_container`).slideDown()
								.attr('flow_control', 'on')
						} else if (matchy == false || new_reliance_value.length == 0){
							$(`#${control_subject}_container`).slideUp()
								.attr('flow_control', 'off')
						};
					};
					$(`#${item.identifier}_empty`).click(function(){
						$(`#${control_subject}_container`).slideUp();
						$(`#${control_subject}_warning`).slideUp();
					});
				} else if (type == 'sections'){
					if (matchy == true){

					}else if (matchy == false){
						
					}
				};
			});
		});
	});
};