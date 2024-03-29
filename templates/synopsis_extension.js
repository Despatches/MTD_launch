function colour_calc(section_counter){
	if (!((section_counter + 2)%2)){
		colour = 'grey'
	} else{
		colour = 'black'
	}
	return colour
};
var section_data = {'collated':{'risk':{'high':[],'standard':[]},'fraud':{'high':[],'standard':[]},'competancy':{'high':[],'standard':[]}}};
var section_counter = 0;
var total_count = 1;

function colour_calc(section_counter){
	if (!((section_counter + 2)%2)){
		colour = 'grey'
	} else{
		colour = 'black'
	}
	return colour
};

function reached_section_loop(loop, form_data_set){
//function reached_section_loop(loop, sections=sections, counter=form_data.reached_section,loop_parameters = undefined){
	section_counter = 0;
	total_count = 1;
	while (section_counter < counter){
		var section = form_data_set['sections'][section_counter]
		loop(section, form_data_set)
		section_counter += 1
	};
};

function all_sections(type){
	var on_off = false
	if (type == 'none'){
		on_off = true
	};
	$('input[group=sections]').each(function(){
			if ($(this).prop('checked') == on_off){
				$(this).click()
			};
		}); 
};

function if_result_relevant(ident_process, params = undefined){
	if (results[selec_ident] != undefined) {
		if (results[selec_ident]['relevant'] == 1){
			if (params != undefined){
				ident_process(params)
			}else{
				ident_process()
			}
		};
	};
};


function meaning_span(data){
	if (data['span_subject'] == undefined){
		span_subject = cur_item
	} else{
		span_subject = data['span_subject'];
	};
	if (data['append_area'] == undefined){
		append_area = current_meaning_section
	} else{
		append_area = data['append_area'];
	};					

	[['risk',max_risk],['fraud',max_fraud],['competancy',max_competancy]].forEach(function(type){
		if (span_subject[`${type[0]}_potential`] == 1){
			type[1] += 1;
			section_data[`${section}`][type[0]]['max'] +=1;
		};
		if (span_subject[type[0]] != undefined){
			calculated_competancy += span_subject[type[0]];
			section_data[`${section}`][type[0]]['calculated'] += span_subject[type[0]];
		};							
	});				
	if(span_subject['meanings'] != undefined){
		if(span_subject['meanings']['meaning'] != ''){
			displayed_mean_count += 1;
			/*var new_span = `
				<span 
					data-meaning="${results[item]['meanings']}" 
					type="meaning"`
				for (let s of searchable_data)*/
			if (span_subject['input_type'] == 'detail_text'){
				if (span_subject['non_format_text'] != undefined){
					non_format_text = 'true'
				};
			};
			var display_meaning
			if (span_subject['meanings']['edit_meaning'] != undefined){
				display_meaning = span_subject['meanings']['edit_meaning']
			} else{
				display_meaning = span_subject['meanings']['meaning'] +','
			};
			if (span_subject['fraud'] == undefined){
				span_subject['fraud']= 0
			}
			if (span_subject['competancy'] == undefined){
				span_subject['competancy']= 0
			}
			if (span_subject['risk'] == undefined){
				span_subject['risk']= 0
			}
			var meaning_span_html =`<span
					data-styling = "{\'color\' : \'${colour}\', \'background-color\':\'transparent\' ,\'border\':\'none\'}"
					data-color='${colour}'
					data-background_color='transparent'
					data-border='none'
					class="stand_text" 
					data-meaning="${span_subject['meanings']['meaning']}"
					data-text = '${display_meaning}'
					data-fraud="${span_subject['fraud']}"
					data-competancy="${span_subject['competancy']}"
					data-risk="${span_subject['risk']}"  
					type="meaning"
					data-identifier="${selec_ident}"
					data-total_count = ${total_count}
					section=${section_counter}
					data-object='false'
					data-non_format_text = "${non_format_text}"
					data-been_edited = 'false'
					style='color:${colour};'
				>
						${display_meaning}
				</span>`
			$(append_area).append(meaning_span_html);

			total_work_tasks += span_subject.work_tasks.length;
			//console.log(total_work_tasks);
			total_count += 1;
		};
	};
};


function create_meaning_span(form_set){
	var cur_item = form_set['results'][selec_ident];
	if (cur_item['input_type'] != 'multi_row'){
		meaning_span({'span_subject':cur_item, 'append_area':current_meaning_section});
	} else if(cur_item['input_type'] === 'multi_row'){
		var multi_span = `<span type='multi' multi_group='${selec_ident}'></span>`
		$(current_meaning_section).append(multi_span);
		var cur_multi_span = $(`span[type=multi][multi_group=${selec_ident}]`)
		meaning_span({'span_subject':cur_item, 'append_area':cur_multi_span});
		if (cur_item['data_rows'] != 'none'){
			/*var data_row_count = 0
			var new_data_row = `<span type='data_row' multi_group='${cur_item.identifier}' row_count=${data_row_count}></span>`
			cur_item['data_rows'].forEach(function(row){
				$(cur_multi_span).append(new_data_row)
				var cur_data_row = $(`span[type=data_row][multi_group=${cur_item.identifier}][row_count=${data_row_count}]`)
				Object.keys(row).forEach(function(ident){
					if_result_relevant(meaning_span,{'span_subject':row[ident], 'append_area':cur_data_row})
				});
				data_row_count += 1
			});*/
		};
		};
};

	var work_task_html = `<div id='work_task_table_holder'><div id='work_task_table_wrapper'style="height:200px;overflow-y:auto;width:270px;"><table class='table' id='selec_work_task_table'><tr><th style='width:50px'>Task</th><th style='width:50px'>Completion Deadline</th></tr></table></div></div>`

	var revert_css={'color':'','background-color':'', 'border':''}
	var max_competancy = 0;
	var max_fraud = 0;
	var max_risk = 0;
	var calculated_competancy = 0;
	var calculated_fraud = 0;
	var calculated_risk = 0;
	var form_set = JSON.parse({{form_set | tojson}})
	var curform_set = form_set
	var total_work_tasks = 0
	var selec_ident;
	const meaning_body = $('#meaning_body')
	var meaning_string = $(`p[id=meaning_string][form=${form_data.form_name}]`)
	var fraud_comp_risk = {'risk':{'colour':{'color':'purple'}},'fraud':{'colour':{'background-color':'red'}},'competancy':{'colour':{'border': '5px solid orange'}}};
	var section_data = {'collated':{'risk':{'high':[],'standard':[]},'fraud':{'high':[],'standard':[]},'competancy':{'high':[],'standard':[]}}};
	var section_counter = 0;
	var total_count = 1;
		function meaning_body_extend(){

	}

	//data_captures = {form_data['form_name']:{'results':results,'questions':questions,'sections':sections,'start_obj':start_obj,'section_names':section_names,'form_data':form_data}}

	/*Object.keys(data_captures).forEach(function(form){
		cur_form = data_captures[form]
	});*/
	/*custom_statement = {'basic_data':function(){
			statement_elements = ['postcode', 'address_line_1', 'address_line_2', 'address_town_or_city']
			var some_exist = false;
			for	(let s of statement_elements){
				if (results[selec_ident]['relevant'] == 1 && results[selec_ident]['meanings'] != (undefined || '')){
					some_exist = true;
				}
			}
			if (some_exist == true){

			}
		}
	}*/

	function intiation(section){
		var questions = curform_set['questions']
		var section_names = curform_set['section_names']
		var results = curform_set['results']
		colour = colour_calc(section_counter);
		//console.log(colour);
		var section_container_html = `<input class='hide' group='sections' id='topic' type='checkbox' name=${section} checked>
			<button class='button is-small is-success' group='sections' id='topic' type='checkbox' name=${section}>${section_names[section_counter]}</button>`
		$(`#fil`).append(section_container_html);
			section_data[`${section}`] = {};
			//console.log(section)
			var section_text_html = `<div style='display:flex;flex-direction:row;'><div><button class='button is-success is-small' group='sections_shortcut' name='${section}' t_name='${section_names[section_counter]}' style='margin-bottom:50%;margin-right:5px;height:100%'>-</button></div><div type='section_text' id=${section}><span><span></div>`
			$(meaning_string).append(section_text_html);
			current_meaning_section = $(`div[type=section_text][id=${section}]`);
			var displayed_mean_count = 0;
			section_data[`${section}`]['risk'] = {'max':0,'calculated':0, 'percent':0};
			section_data[`${section}`]['competancy'] = {'max':0,'calculated':0, 'percent':0};
			section_data[`${section}`]['fraud'] = {'max':0,'calculated':0, 'percent':0};
			//console.log(section, questions[section])
			questions[section].forEach(function(item){
				selec_ident = item.identifier
				if (item['input_type'] == 'multi_row'){
					selec_ident += '_count'
				};
				var non_format_text = 'false'
				//console.log(selec_ident)
					if (item['object'] != undefined){
		//if (objects['disclosure_address'] != undefined){
					//console.log(objects['disclosure_address'])
					var address = curform_set['objects']['disclosure_address'];
					var address_meaning = 'The address of the property being disclosed has been given as';
					

					mainline_address_items = ['first_line','second_line', 'third_line'];
					var ad_count = 0;
					mainline_address_items.forEach(function(item){
						if (address[item] != undefined){
							if (address[item]['value'] != undefined || ''){
								if (ad_count == 0){
									address_meaning += ' ' + address[item]['value'] 
								} else {
									address_meaning += ', ' + address[item]['value']
								}
								ad_count += 1
							}
						}
					});
					if (address['postcode']['value'] != undefined || ''){
						address_meaning += ', ' + address['postcode']['value']
					} else{
						address_meaning += ', a postcode for the property has not been supplied'
					};
					disclosure_address_html = `<span 
						data-styling = "{\"color\" : \"${colour}\", \"background-color\":\"transparent\" ,\"border\":\"none\"}"
						data-color='${colour}'
						data-background-color ='transparent'
						data-border='none'
						class="stand_text"  type='meaning' data-identifier='disclosure_address' data-object='true' data-total_count = ${total_count} section=${section_counter}>${address_meaning}
						</span>`
					$(current_meaning_section).append(disclosure_address_html)
					total_count += 1;
		//}
				};
				if_result_relevant(create_meaning_span);
			});
			Object.keys(fraud_comp_risk).forEach(function(marker){
				var percent = section_data[`${section}`][marker]['calculated']/section_data[`${section}`][marker]['max'];
				section_data[`${section}`][marker]['percent'] = percent;
				if (percent > 0){
					section_data['collated'][marker]['standard'].push(section)
				}
				if (percent > 0.5){
					section_data['collated'][marker]['high'].push(section)
				};
			});
			
			/*if (displayed_mean_count == 0){
				$('input[type=checkbox][group=sections][name=section]').remove()
			}*/
			$(meaning_string).append('<span>\n</span>')
			$(meaning_string).append(`</div><div style='margin-bottom:10px'></div>`)
	};
	$('#work_task_number').text(`${total_work_tasks}`)


	//console.log(max_competancy,max_fraud, max_risk)
	//console.log(calculated_competancy,calculated_fraud,calculated_risk)

	$('button[group=sections]').click(function(){
		$(`input[type=checkbox][group=sections][name=${$(this).attr('name')}]`).click()
	});


		//way to display the name of the section  via section shortcut buttons
	/*$('button[group=sections_shortcut]').each(function(){
		$(this).mouseenter(function(){
			$('#section_name_tag').text($(this).attr('t_name'))
			$('#section_name_tag').removeClass('hide')
				.animate({top:event.pageY, left: event.pageX, 'z-index': 1});
		})
		$(this).mouseleave(function(){
			$('#section_name_tag').addClass('hide')
		})
	});*/

	function section_switcher(changer){
		var sec_name = $(changer).attr('name')
		if ($(changer).prop('checked') == false){
			$(`div[type=section_text][id=${sec_name}]`).slideUp();
			$(`span[type=meaning][section=${sec_name}]`).slideUp();
			$(`button[group=sections][name=${sec_name}]`).removeClass('is-success')
				.addClass('is-warning')
			$(`button[group=sections_shortcut][name=${sec_name}]`).removeClass('is-success')
				.addClass('is-warning')
				.animate({'height':'10px'})
				.text('+')
		} else if ($(changer).prop('checked') == true){
			$(`div[type=section_text][id=${sec_name}]`).slideDown();
			$(`span[type=meaning][section=${sec_name}]`).removeClass('hide')
			$(`button[group=sections][name=${sec_name}]`).removeClass('is-warning')
				.addClass('is-success')
			$(`button[group=sections_shortcut][name=${sec_name}]`).removeClass('is-warning')
				.addClass('is-success')
				.animate({'height':'100%'})
				.text('-')
		};
	}
	$('input[type=checkbox][group=sections]').change(function(){
		section_switcher(this)
	});
	$('button[group=sections_shortcut]').click(function(){
		$(`input[name=${$(this).attr('name')}][group=sections]`).click()
	});

	$('button[group=sections_shortcut]').mouseenter()

	$('#view_all_topic_toggle').click(function(){
		all_sections('n')
	});
	/*Object.keys(results).forEach(function(item){
		if (results[item]['relevant'] == 1 && results[item]['meanings'] != undefined){
			if(results[item]['meanings']['meaning'] != ''){
				/*var new_span = `
					<span 
						data-meaning="${results[item]['meanings']}" 
						type="meaning"`
					for (let s of searchable_data)*/
				/*$("div[id=meaning_body]").append(`
					<span 
						class="stand_text" 
						data-meaning="${results[item]['meanings']}" 
						data-fraud="${results[item]['fraud']}"
						data-competancy="${results[item]['competancy']}"
						data-risk="${results[item]['risk']}"  
						type="meaning"
						data-identifier="${item}"
					>
							${results[item]['meanings']['meaning']},
					</span>`
				)
			}
		}
	});*/

	let divmin = false;
	let getinfo = false;
	var selec_meaning = "empty"
	var selec_ans
	var infoid
	var selec_set_counter= 0
	//var selection_sets = JSON.parse({ selection_sets | tojson})
	var cur_set = []
	var side_view = false;
	var unformatted_text_tab = false;
	var text_alter_tool = false;
	var report_previewer = false;
	var report_collected = false;
	//number_of_selec_sets = $("meta[id=pydata").data( "numselecsets" )
	var sets = {};
	var matching_selection = [];
	var work_task_view = false;
	var document_viewer_tab = false;
	var current_data = 1;
	var old_data;

	// allows text to be altered in the text editor sweet (chooses target)
	var text_alter_pointer;

	//prevents User seeing element movements
	function close_work_task_module(){
		$("#open_note_module, #statement_alters").slideDown();				
		$("#work_task_module").slideUp();
		work_task_view = false;
		$("#open_work_task_module").text("Add Work Task");
	}

	function side_and_modules(){
		$("#work_task_module, #work_task_detail, #alter_statement_options").slideUp()

		$("#open_work_task_module").click(function(){
			if (work_task_view == false){
				$("#open_note_module, #statement_alters").slideUp();
				$("#work_task_module").slideDown();
				work_task_view = true
				$("#open_work_task_module").text("Cancel Work Task");
			}else if (work_task_view == true){
				close_work_task_module()				
			};
		});
		$("#selec_competancy").mouseenter(function(){
			//alert("5")
		});
	};

	side_and_modules();

	function fraud_or_comp(f_or_c){
		colour = fraud_comp_risk[f_or_c]['colour']
		if ($(`input[type=checkbox][value=${f_or_c}]`).prop("checked") == true){
			$("span[type=meaning]").each(function(){
				if ($(this).data(`${f_or_c}`) == 1){
					$(this).css(colour)
						.attr("marked",+1);
				};
			});
		}else if($(`input[type=checkbox][value=${f_or_c}]`).prop("checked") == false){
			$("span[type=meaning]").each(function(){
				var act_mean = $(this).data()
				if (act_mean[f_or_c] == 1){
					var new_style = {}
					default_style = ['color','border']
					default_style.forEach(function(style){
						if (colour[style] != undefined){
							new_style[style] = act_mean[style]
						}
					});
					if(colour['background-color'] != undefined){
						new_style['background-color'] = 'transparent'
					};
					$(this).css(new_style)
					$(this).attr("marked",-1);
				};
			});
		};
	};

	Object.keys(fraud_comp_risk).forEach(function(marker){
		fraud_or_comp(marker)
	});

	function selec_data_viewer(){
			if (selec_ans.competancy == 1){
			$("p[id=selec_competancy]").text("")
		}else{
			$("p[id=selec_competancy]").text("")
		}
		if (selec_ans.fraud_imp == 1){
			$("p[id=selec_fraud]").text("This selection may indicate fraudulent behavior")
		}else{
			$("p[id=selec_fraud]").text("")
		}
		if (selec_ans.fraud_imp == 1){
			$("p[id=selec_fraud]").text("This selection may indicate fraudulent behavior")
		}else{
			$("p[id=selec_fraud]").text("")
		}
	};

	function side_view_selec_meaning(){
			$("#side_viewer").removeClass("hide")
			$(selec_meaning).css( {"background-color":"grey"} );
			selec_ans = $(selec_meaning).data()
			//meaning_lft_rgt(function(a){(a).css({"color":"grey"})})
			selec_data_viewer()
	};

	function non_side_selec_meaning(){
		$("#divId").css( {position:"absolute", top:event.pageY, left: event.pageX});
		$("#divId").toggleClass("hide");
		selec_data_viewer()
	};

	function remove_selec_mean_grey(){
		$(selec_meaning).css( { 'background-color':'transparent' } );
		selec_ans = $(selec_meaning).data()
		//meaning_lft_rgt(function(a){(a).css( { 'color':'black' } )});

	};

	function add_work_task_to_table(work_task){
		$('#selec_work_task_table').append(`
			<tr row_type='work_task_data' work_id=${work_task['id']}>
				<td style='width:50px' task_element = 'header'>
					${work_task['work_task_header']}
				</td>
				<td task_element = 'date'>
					${work_task['work_task_date']}
				</td>
				<td>
					<div>
						<button type='button' function='view_specific_task' class='button is-success' 
							data-id='${work_task['id']}'
							data-header='${work_task['work_task_header']}'
							data-date='${work_task['work_task_date']}' data-info='${work_task['work_task_info']}' data-client_issue='${work_task['client_issue']}'>
							Details
						</button>
					</div>
					<div>
						<button class='button is-warning' id='delete_work_task' work_id=${work_task['id']}>
							Delete
						</button
					</div>
					<div>
						<button class='button is-success' id='complete_work_task' work_id=${work_task['id']}>
							Mark as Complete
						</button
					</div>					
				</td>
			</tr>`);
		delete_work_tasks()
	}
	function eval_deselect_style(meaning){
		var meaning_data= $(meaning).data();
		var final_css = {}
		$(`input[type=checkbox][set=fraud_comp_risk]`).each(function(){
			var mark_type = $(this).val()
			//console.log($(this).prop('checked'))
			if ($(this).prop('checked') == true && meaning_data[mark_type] == 1){
				var styles = fraud_comp_risk[mark_type]['colour']
				Object.keys(styles).forEach(function(style){
					final_css[style] = styles[style]
				});
			}
		});
		default_style = ['color','border']
		default_style.forEach(function(style){
			console.log(meaning_data[style])
			if (final_css[style] == undefined){
				final_css[style] = meaning_data[style]
			}
		});
		if (final_css['background-color'] == undefined){
			final_css['background-color'] = 'transparent'
		}
		if (unformatted_text_tab === true && $(meaning).attr('data-non_format_text') == 'true'){
			final_css['color'] = 'blue'
		}
		$(meaning).css(final_css)

	};
	function deselect_meaning(meaning){
		//$("span[type=meaning]").removeClass("text_hover")
		//console.log(revert_css)
			//$(meaning).css(revert_css);
		eval_deselect_style(meaning)
		$(meaning).css({'background-color':revert_colour})
	};
	var revert_colour
	function hover_meaning(meaning){
		if((side_view == true && this == selec_meaning) == false){
			/*console.log($(meaning).attr('styling'))
			if ($(meaning).css('color')){
				revert_css['color'] = JSON.parse($(meaning).attr('styling'))['color']
			} else{
				revert_css['color'] = $(meaning).css('color');
			}
			revert_css['background-color'] = $(meaning).css('background-color');
			revert_css['border'] = $(meaning).css('border');*/
			revert_colour = $(meaning).css('background-color')
			selec_ans =$(meaning).data()
			$(meaning).css( {"background-color":"white"} );
			//meaning_lft_rgt(function(a){(a).addClass("text_hover")})
		};
	}
	function meaning_scroller(new_focus){
		var x = 0;
		var y = 0;
		//$('#main_body').addClass('stop-scrolling');

		//$(new_focus).focus({ preventScroll: true })
		$(new_focus).parentsUntil($('#meaning_string').parent()).each(function(){
			console.log($(this).attr('id'))
			console.log(x , y)
		  x +=$(this).position().left;
		  y +=$(this).position().top;
		});
		//y+=$('#meaning_body').height()
		console.log(x , y)
		/*if (y>0){
			y = y*-1
		}*/
		document.querySelector('#meaning_body').scrollTo({
			  top: y,
			  left: x,
			  behavior: "smooth",
			})
		//$('#main_body').removeClass('stop-scrolling');
	}
	function arrow_meaning_scroll(){
		deselect_meaning($(`span[type=meaning][data-total_count=${old_data}]`))
		var new_focus = $(`span[type=meaning][data-total_count=${current_data}]`)

		meaning_scroller(new_focus)

		if (side_view === false){
			hover_meaning($(new_focus))
		} else{
			$(new_focus).click();
		};
		//$(new_focus)[0].scrollIntoView();
		if(text_alter_tool === true){
			upload_new_meaning_text()
			$('#text_edit_default_box').text($(new_focus).attr('data-meaning'))
			$('#text_edit_orig_box').text($(new_focus).text());
			$('#text_edit_new_box').val($(new_focus).text());
			new_target_text_alter(new_focus)
		};
	};

	function upload_new_meaning_text(){
		console.log($('#text_edit_new_box').val(), $('#text_edit_orig_box').text())
		if ($('#text_edit_new_box').val() != $('#text_edit_orig_box').text()){
			var alter_text_data = {}
			alter_text_data.form = form_data.form
			alter_text_data.form_name = form_data.form_name
			alter_text_data.identifier = $(text_alter_pointer).data('identifier')
			alter_text_data.new_text = $('#text_edit_new_box').val();
			alter_text_data =JSON.stringify(alter_text_data)
			$.ajax({
				data:{data:alter_text_data},
				url : '/alter_meaning_text',
				type : "POST",
				success : function(data){
					console.log(data)
				}
			});
		};
	};
	function scroll_forward(){
		close_mark_box()
		if (current_data < total_count){
			old_data = current_data
			reserve_data = current_data
			current_data += 1;
			while ($(`span[type=meaning][data-total_count=${current_data}]`).parent().hasClass('hide') == true && current_data > total_count ==false){
				current_data += 1
			};
			if (current_data < (total_count)){
				arrow_meaning_scroll()
			} else {
				current_data = reserve_data
				arrow_meaning_scroll()
			};
		};
	}

	function meaning_manip(){
		$("span[type=meaning]").click(function(e){
			if(text_alter_tool === true){
				upload_new_meaning_text()
				new_target_text_alter(this)
				$('#text_edit_default_box').text($(this).attr('data-meaning'))
				$('#text_edit_orig_box').text($(this).text());
				$('#text_edit_new_box').val($(this).text());
			};
			$('#selection_work_tasks').empty()
			if (selec_meaning != "empty"){
				remove_selec_mean_grey()
			};
			selec_meaning = this;
			selec_ans =$(this).data();
			current_data = selec_ans.total_count;
			//id = selec_ans.id;
			getinfo = true;
			//infoid = id;
			var grabber
			if (side_view === false && text_alter_tool ===false){
				non_side_selec_meaning();	
			}else if (side_view === true || text_alter_tool ===true){
				console.log(selec_ans['object'])
				if (selec_ans['object'] == 'false'){
					if (results[selec_ans.identifier]['input_type'] == 'detail_text'){
						$('#detail_text_span').text(results[selec_ans.identifier]['value'])
					} else {
						$('#detail_text_span').text('')
					};
				};
				var side_markers = {
					'fraud' : $('#side_mod_fraud_mark'),
					'competancy':$('#side_mod_comp_mark'),
					'risk':$('#side_mod_risk_mark')
				};
				Object.keys(side_markers).forEach(function(mark){
					if (selec_ans[mark] == 1){
						$(side_markers[mark]).prop('disabled',false)
					} else {
						$(side_markers[mark]).prop('disabled',true)
					}
				}) 
				if (selec_ans.object == 'true'){
					grabber = objects[selec_ans.identifier]
				} else {
					grabber = results[selec_ans.identifier]
				}
				close_work_task_module();
				side_view_selec_meaning();
				//if (selec_ans)
				console.log(grabber)
				if (grabber['work_tasks'].length > 0){
					$('#selection_work_tasks').append(work_task_html)
					grabber['work_tasks'].forEach(function(work_task){
						add_work_task_to_table(work_task)
					});
				} else {
					$('#selection_work_tasks').append('<div>No Active Tasks</div>')
				}
				$('button[function=view_specific_task]').click(function(){
					var viewed_work_task = $(this).data();
					$('#work_task_table_holder').addClass('hide');
					$('#work_task_view_detail').text(viewed_work_task.info);
					$('#work_task_detail').slideDown();
				});
			};

		});

		document.onkeydown = (e) =>{
			if ($(document.activeElement).attr('id') != 'text_edit_new_box'){
				var reserve_data = 0
				e = e || window.event;
				if (e.keyCode === 39){
					scroll_forward()
				} else if (e.keyCode === 37){
					close_mark_box()
					if (current_data > 1){
						old_data = current_data
						reserve_data = current_data
						current_data -= 1;
						while ($(`span[type=meaning][data-total_count=${current_data}]`).parent().hasClass('hide') == true && current_data < 1 == false){
								current_data -= 1
						};
						if (current_data > 0){
							arrow_meaning_scroll()
						} else{
							current_data = reserve_data
							arrow_meaning_scroll()
						};
					};
				};
			};
		};

		$("span[type=meaning]").mouseenter(function(e){
			hover_meaning(this)
		});

		$("#divId").mouseenter(function(e){
			if (divmin == false){
				divmin = true;
			};
		});

		function close_divID(){
			if (side_view == false){
				$("#divId").addClass("hide");
			  	//$("p[id=selec_competancy]").text("");
			}else if (side_view == true){
				$("#side_viewer").addClass("hide")
			};
			close_work_task_module();
		};
		$("#divId").mouseleave(function(){
			if (getinfo == false){
				if (divmin == true){
		 			divmin = false;
		 		};
		 		if ($("#divId").hasClass("hide")==false){
		 			close_divID()
		  		};
		 	};
		 	if ($("#divId").hasClass("hide")==false){
		  		close_divID()
		  	};
		});
		$("span[type=meaning]").mouseleave(function() {
			setTimeout(function(){
				if (divmin == true){}
				else if ($("#divId").hasClass("hide")==false){
		  			$("#divId").toggleClass("hide");
		  			getinfo = false
				};
			});
			deselect_meaning(this)
			if ((this == selec_meaning && side_view == true)== false){
				deselect_meaning(this)
			}
		});
		/*$("button[id=change_selec]").click(function(e){
			if (infoid == undefined){alert("bb")}
			else{
			baseUrl = "{{urlr}}"
			page="change_selection/"
			particular_id= "{{particular_id}}/"
			selec_set_ID="{{selec_set_ID}}/"
			url = ""+baseUrl+page+particular_id+selec_set_ID+infoid+"/"+selec_ans
			window.location.href = url
			}
		});

		("button[id=change_selec]").click(function(e){});
	*/
		$("input[type=checkbox][set=fraud_comp_risk]").click(function(){
			var marker = $(this).val()
			fraud_or_comp(marker)
		});

	};
	meaning_manip()

	$("button[id=prev_selec_set").click(function(e){
		selec_set_counter += 1;
		if (selec_set_counter > 0){$("button[id=earlier_selec_set").attr('disabled', false)}
		if(selec_set_counter == number_of_selec_sets){
			alert(selec_set_counter)
			$(this).attr('disabled', true)};
		//get_mp_selecs()

	});

	$("button[id=earlier_selec_set").click(function(e){
		selec_set_counter -= 1;
		if(selec_set_counter == 0){
			$(this).attr('disabled', true)};
		//get_mp_selecs()
	});

	//get_mp_selecs()

	$('input[type=radio][name=Topic]').change(function(){
		if (this.value=="topic"){
			$('#datfil').slideUp();
			$('#fil').slideDown();
		}
		else if(this.value!="data"){
			 $("#checkbox").attr("checked", false);
			 $('#fil').slideUp();
			 $('#datfil').slideDown();
		}
	});

	var mod_marks_pairs = {
		'#side_mod_fraud_mark':'This selection may indicate fraudulent behavior',
		'#side_mod_comp_mark':'This selection suggests the disclosee may have some existential gaps in their knowlage of the property',
		'#side_mod_risk_mark':'This selection may a potential risk to the security of the transaction'
	};

	function close_mark_box(){
		$(`#mod_mark_box`).addClass('hide')
	}

	function mod_marks(marker, text){
		var mod_marker_text = `#side_mod_${marker}_mark`
		$(mod_marker_text).mouseenter(function(){
			$(`#mod_statement`).text(text);
			$(`#mod_mark_box`).removeClass('hide')
			.css({position:"absolute", top:event.pageY, left: event.pageX, 'z-index': 1});
		})
		.mouseleave(function(){
			close_mark_box()
		});

	};

	function box_popup(marker, text, append = false){
		$(marker).mouseenter(function(){
			$(`#mod_mark_box`).text('');
			$(`#mod_mark_box`).empty();
			if (append === false){
				$(`#mod_mark_box`).text(text);
			} else{
				$(`#mod_mark_box`).append(text)
			}
			$(`#mod_mark_box`).removeClass('hide') 
			.css({position:"absolute", top:event.pageY, left: event.pageX, 'z-index': 1});
		})
		.mouseleave(function(){
			close_mark_box()
		});
	};

	fraud_comp_risk_sec_div = { 'high_risk':function(count){
						var popup =`<div>
							<p id='view_high_risk_sections'><span id='high_risk_sections_count'>${count}</span> sections<br> sections with a high level of potential risk<span></span></p>
						</div>`
						return popup;
					},
			'standard_risk':function(count){
				var popup =`<div>
							<p id='view_risk_sections'><span id='risk_sections_count'>${count}</span> sections <br>with some potential risk<span></span></p>
						</div>`
					return popup;
				},	
			'high_competancy':function(count){
				var popup =	`<div>
							<p id='view_high_competancy_sections'><span id='high_competancy_sections_count'>${count}</span> sections which suggest high difficulties with <br>the form filler's knowledge of the property<span></span></p>
						</div>`
					return popup;
				},
		'standard_competancy':function(count){
			var popup =	`<div>
				<p id='view_competancy_sections'><span id='competancy_sections_count'>${count}</span> sections which suggest difficulties with the <br>form filler's knowledge of the property<span></span></p>
			</div>`
			return popup;	
			},
		'high_fraud':function(count){	
			var popup =`<div>
							<p id='view_high_fraud_sections'><span id='high_fraud_sections_count'>${count}</span> sections with a high <br>level of potential fraud<span></span></p>
						</div>`
			return popup;	
			},
		'standard_fraud':function(count){
			var popup =`<div>
							<p id='view_fraud_sections'><span id='fraud_sections_count'>${count}</span> sections with potential<br> fraud elements<span></span></p>
						</div>`
			return popup;	
			},
	}	
	/*Object.keys(fraud_comp_risk).forEach(function(marker){
		err_sec_count = section_data['collated'][marker]['high'].length;
		$(`#high_${marker}_sections_count`).text(err_sec_count);
		err_sec_count = section_data['collated'][marker]['standard'].length;
		$(`#${marker}_sections_count`).text(err_sec_count);		
	});*/
	/*Object.keys(fraud_comp_risk).forEach(function(marker){
		$(`#view_high_${marker}_sections`).click(function(){
			all_sections('none')
			section_data['collated'][marker]['high'].forEach(function(section){
				$(`input[group=sections][name=${section}]`).click();
			});
			if ($(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).prop('checked') == false){
				$(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).click();
			};
		});
		$(`#view_${marker}_sections`).click(function(){
			all_sections('none')
			section_data['collated'][marker]['standard'].forEach(function(section){
				$(`input[group=sections][name=${section}]`).click();
			});
			if ($(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).prop('checked') == false){
				$(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).click();
			};
		});		
	});*/

	const side_view_col = `
			<div class="column is-one-third" id="side_holder">
				<div class="hide" id="side_viewer">
					<div class="box" style='height:450px;'>
						<button id='side_mod_fraud_mark' class = "button is-small is-danger" >F</button>
						<button id='side_mod_comp_mark' class = "button is-small is-warning" >C</button>
						<button id='side_mod_risk_mark' class = "button is-small is-link">R</button>
						<p id="selec_competancy"></p>
						<p id="selec_fraud"></p>
						<div>
							<span id='detail_text_span'></span>
						</div>
						<div id="statement_alters">
							<button class = "button is-small" id="change_selec"> Change Selection</button>
							<button class = "button is-small" id="alter_selec_text"> Alter Statement</button>
						</div>
							<div id="alter_statement_options">
								<button class = "button is-small" id="add_statement"> add statement</button>
								<button class = "button is-small" id="alter_statement_text">alter statement</button>
							</div>
							<div id=selection_work_tasks>
								<div id='work_task_detail'>
									<p id='work_task_view_detail'></p>
								</div>
							</div>
							<div>
								<button class = "button is-small is-success" id="open_work_task_module">
									Add Work Task
								</button>
								<button class = "button is-small is-success" id="open_note_module">
									Add note
								</button>			
								<div id="work_task_module">
									<div style="display:flex; flex-direction:row;">
										<div style="display:flex; flex-direction:column;">
											<div>Task Description</div>
											<input type="text" id="work_task_header">
										</div>
										<div style="display:flex; flex-direction:column;">
											<button id="add_work_task_schedule">
												Add Schedule Date
											</button>
											<input type="date" class="date" id="work_task_date">
										</div>
									</div>
									<div style="display:flex; flex-direction:column;">
										<div> Task Data</div>
										<textarea id="work_task_info"></textarea>
									</div>
									<div>
										<button class="button is-small is-success" id="create_work_task">
											Create Work Task
										</button>
									</div>			
								</div>
								<div id="stand_note_module" class="hide">
									<div style="display:flex; flex-direction:column;">
										<input type="text">
									</div>
								</div>
							</div>
					</div>
				</div>
			</div>`
	function toggle_side_view(){
		if (side_view === false){
			rh_tab_clearer('side_view')
			$("#divId").addClass("hide")
			$("#meaning_and_side").append(side_view_col);
			side_and_modules();
			$("#toggle_side_view").text("Hide side view");
			side_view = true;
			$(`span[type=meaning][data-total_count=${current_data}]`).click();
			side_view_selec_meaning();

			Object.keys(mod_marks_pairs).forEach(function(marker){
				box_popup(marker, mod_marks_pairs[marker]);
			});

			/*$('#change_selec').click(function(){

			});*/
			side_view = true;
		}else if (side_view === true){
			remove_selec_mean_grey()
			$("#side_holder").remove()
			$("#toggle_side_view").text("Open side view")
			side_view = false;
			non_side_selec_meaning()			
		}
	$("#create_work_task").click(function(){
			work_task_data_sender()
		});
	}

		// Adding work tasks does not always update the table within the module correctly
	function work_task_data_sender(){
		var work_task_data = {}
		work_task_data.work_task_header = $("#work_task_header").val()
		work_task_data.work_task_date = $("#work_task_date").val()
		work_task_data.work_task_info = $("#work_task_info").val()
		work_task_data.identifier = $(selec_meaning).data("identifier");
		work_task_data.form_name = form_data.form_name
		work_task_data.form = form_data.form
		work_task_data.client_issue = 0
		console.log(JSON.stringify(work_task_data))
		//add_note_or_work_task(work_task_data)
		$.ajax({
			url : '/create_form_work_task',
			data : {data : JSON.stringify(work_task_data)},
			type : "POST",
			success : function(data){
				console.log(data)
				if (!$('#work_task_table_holder').length){
					$('#selection_work_tasks').empty()
					.append(work_task_html)
				}
				var new_tasks = JSON.parse(data);
				results[work_task_data.identifier]['work_tasks'].push(new_tasks[(new_tasks.length)-1]);
				var cur_tasks = results[work_task_data.identifier]['work_tasks'];
				add_work_task_to_table(cur_tasks[(cur_tasks.length)-1]);

			}
		});
	};

	// process requires duplication for the purposes of standard notes without work type element
	// requirement of implication of looging of task completions
	function delete_work_tasks(){
		$('#delete_work_task').click(function(){
			var ajax_return
			var work_task_id = $(this).attr('work_id')
			var work_task_data = {'id':work_task_id}
			work_task_data.form = form_data.form
			$.ajax({
				url : '/delete_form_work_task',
				data : {data : JSON.stringify(work_task_data)},
				type : 'POST',
				success : function(data){
					console.log(data)
					if (data === 'success'){
						$(`tr[work_id=${work_task_id}]`).remove()
					};
					if (!$('tr[row_type=work_task_data]').length){
						$('#selection_work_tasks').empty()
						.append('<div>No Active Tasks</div>')
					};
				}
			});

		});
	};

	function complete_work_task(){
		$('#complete_work_task').click(function(){
			var work_task_data = {'id':work_task_id}
			work_task_data.form
			$.ajax({
				url: '/complete_work_task',
				data : {data : JSON.stringify(work_task_data)},
				type : 'POST',
				success : function(data){
					console.log(data)

				}
			})
		});
	};

	function deselect_query_tabs(){
		$('li[group=query_tabs]').removeClass('is-active')
	};

	function clear_unformatted_text(){
		deselect_query_tabs();
		unformatted_text_tab = false
		$("#unformatted_text_checker").remove();
		$(`span[type=meaning][data-non_format_text=true]`).each(function(){
			eval_deselect_style(this)
		});
	};
	function clear_text_alter_tool(){
		deselect_query_tabs();
		$('#text_alter_tool').remove();
		text_alter_tool=false;
	};

	function clear_document_viewer_tab(){
		deselect_query_tabs();
		$('#document_viewer').remove();
		document_viewer_tab=false;
	};

	function clear_report_previewer_tab(){
		deselect_query_tabs();
		$('#report_previewer').addClass('hide');
		$('#meaning_body').removeClass('hide');
		report_previewer =false;
	};

	var unformatted_text_div = `
	<div class="column is-one-third" id='unformatted_text_checker'>
		<div class='box'>
			<div>
				<table class='table'>
					<thead>
					 	<tr>
					 		<td>
					 			TEXT
					 		</td>
					 		<td>
					 			Mark
					 		</td>
					 	<tr>
					 </thead>
					 <tbody id='unformat_text_scroller'
				 style='overflow:scroll; display:block;height:70%'>
					 </tbody>
				</table>
			</div>
		</div>
	</div>`;

	var text_alter_tool_div = `
	<div class="column is-one-third" id='text_alter_tool'>
		<div>
			Default Text
			<div class='box' id='text_edit_default_box'></div>
		</div>
		<div>
			Origional Text
			<div class='box' id='text_edit_orig_box'></div>
		</div>
		<div class='box'>
			<div>New Text</div>
			<textarea class='textarea' id='text_edit_new_box' cols=20></textarea>
		</div>
	</div>`;

	function edit_meaning_text(text_alter_pointer){
		$(text_alter_pointer).text($('#text_edit_new_box').val());
		if ($('#text_edit_new_box').val() != ($('#text_edit_orig_box').text())){
			$(text_alter_pointer).css({'background-color':'green'});
		} else {
			eval_deselect_style(target);
		};
	};
	function new_target_text_alter(target){
		text_alter_pointer = target
		$('#text_edit_new_box').on('input propertychange paste', function() {
			edit_meaning_text(text_alter_pointer)
		});
	};
	function evaluate_query_tabs(tab){
		if (tab == 'unformatted_text_tab'){
			if (unformatted_text_tab == false){
				rh_tab_clearer()
				$("#meaning_and_side").append(unformatted_text_div);
				unformatted_text_tab = true
				Object.keys(results).forEach(function(result){
					if (results[result]['non_format_text'] != undefined){
					var unformat_text_display = `<tr question = '${result}' table='unformatted_text_table' style='margin-bottom:5px;'><td>
						<div root='${result}' value='${results[result]['non_format_text']['value']}'>
							${results[result]['non_format_text']['value']}
						</div>
						</td><td><button class='button'>mark</button><button func='add_unformat_text' root='${result}'class='button' add_val='${results[result]['non_format_text']['value']}'>Add Text to Report</button></td></tr>`

						$('#unformat_text_scroller').append(unformat_text_display);
					};
				});
				$('tr[table=unformatted_text_table]').mouseenter(function(){
					var no_form_parent = $(this).attr('question')
					if ($(`span[type=meaning][data-identifier=${no_form_parent}]`)){
						var new_focus = $(`span[type=meaning][data-identifier=${no_form_parent}]`);
						meaning_scroller(new_focus)
						current_data = $(new_focus).data('total_count');
						hover_meaning(new_focus)
					};
				})
				.mouseleave(function(){
					var new_focus = $(`span[type=meaning][data-identifier=${$(this).attr('question')}]`);
					deselect_meaning(new_focus)
				})
				$('button[func=add_unformat_text]').click(function(){
					var unformat_text_add = $(this).attr('root');
					var add_val = $(this).attr('add_val')
					$('#text_alter_tool_selector').click();
					var new_focus = $(`span[type=meaning][data-identifier=${unformat_text_add}]`);
					$(new_focus).click();
					$('#text_edit_new_box').val(add_val)
					edit_meaning_text(new_focus);
				});
			};
			$(`span[type=meaning]`).each(function(){
				if ($(this).attr('data-non_format_text') == 'true'){
					$(this).css({'color':'blue'});
				};
			});
		} else if(tab == 'text_alter_tool_selector'){
			if (text_alter_tool == false){
				rh_tab_clearer();
				$('#minimise_left_side_bar').click();
				$("#meaning_and_side").append(text_alter_tool_div);
				text_alter_tool = true;
				$('#text_edit_new_box').keydown(function(e){
					if (e.keyCode === 13){
						event.preventDefault();
						scroll_forward()
					} 
				})
			};
		}else if(tab == 'preview_report'){
			if (report_previewer == false){
				rh_tab_clearer();
				if (report_collected != true){
					var report;
					report_constructor()
						.then((data) =>{
								report = data
								$('#meaning_body').addClass('hide');
								$('#report_previewer').removeClass('hide');
								$('#report_previewer').append(`${report}`)
								$('div[type=report_page]').each(function(){
									var width = $(this).css('width')
									console.log(width,width*1.41)
									0.02
									$(this).css({'height':`${parseInt(width, 10)*1.41}`+'px','font-size':`${parseInt(width, 10)*0.02}`+'px'})
								})
								report_collected = true
						})
						.catch((error) => {
		    			console.log(error)
		  			})
		  	} else{
		  		$('#report_previewer').removeClass('hide');
		  		$('#meaning_body').addClass('hide');
		  	}
		  	report_previewer = true
		  };
		} else if(tab == 'document_grab'){
			console.log('reached')
			if (document_viewer_tab == false){
				rh_tab_clearer();
				var view_docs_tab = `
					<div class="column is-one-third box" id='document_viewer'>
						<table class='table'>
						<thead>
						 	<tr>
						 		<td>
						 			Section
						 		</td>
						 		<td>
						 			Documents
						 		</td>
						 	<tr>
						 </thead>
						 <tbody id='document_viewer_scroller'
					 style='overflow:scroll; height:300px'>
						 </tbody>
					</table>
					</div>`;
				$("#meaning_and_side").append(view_docs_tab);
				function add_section_docu(section){
					var contains_docs =  false;
					var section_doc_count = 0
					function tally_section_documents(){
						if (curform_set['results'][selec_ident]['documents'].length > 0){
							section_doc_count += curform_set['results'][selec_ident]['documents'].length
						}
					};
					questions[section].forEach(function(item){
						selec_ident = item.identifier;
						if_result_relevant(tally_section_documents)
					});
					if (section_doc_count > 0){
						var section_contains_doc = `
						<tr table='section_documents_table'>
							<td>
							<div>
								${curform_set['section_names'][section_counter]}
							</div>
							</td>
							<td>
								${section_doc_count}
							</td>
							<td>
								<button>View Documents</button>
							</td>
						</tr>`
						$('#document_viewer_scroller').append(section_contains_doc);
					}
				}
				reached_section_loop(add_section_docu)
				/*Object.keys(results).forEach(function(result){
					if (results[result]['documents'].length > 0){
						var doc_list = ''
						results[result]['documents'].forEach(function(doc){
							doc_list += doc['document_name']
						});
						var data_contains_doc = `
						<tr question = '${result}' table='unformatted_text_table'>
							<td>
							<div root='${result}' value='${results[result]}'>
								${result}
							</div>
							</td>
							<td>
							</td>
						</tr>`

						$('#document_viewer_scroller').append(data_contains_doc);
					};
				});*/
				document_viewer_tab = true;
			}
		} else if (tab == 'active_work_tasks'){

		}
	};

	function if_result_relevant(ident_process, params = undefined){
		if (results[selec_ident] != undefined) {
			if (results[selec_ident]['relevant'] == 1){
				if (params != undefined){
					ident_process(params)
				}else{
					ident_process()
				}
			};
		}else{console.log(results,selec_ident,'5')};
	}; 
	function report_constructor(){
		return new Promise((resolve, reject) =>	{
		var report_constructor = {};
		report_constructor.form = form_data.form
		report_constructor.form_name = form_data.form_name
		report_constructor= JSON.stringify(report_constructor);
			$.ajax({
				data:{data:report_constructor},
				url:'/report_constructor',
				type : "POST",
				success : function(data){
						resolve(data)
					},
				error :function(error){
					reject(error)
				}
			});
		});
	}

	function rh_tab_clearer(ignore='none'){
		var rh_tabs = {
			'side_view':[side_view, toggle_side_view], 
			'unformatted_text':[unformatted_text_tab, clear_unformatted_text],
			'text_alter_tool':[text_alter_tool,clear_text_alter_tool],
			'document_grab':[document_viewer_tab,clear_document_viewer_tab],
			'report_previewer':[report_previewer, clear_report_previewer_tab]
		};
		Object.keys(rh_tabs).forEach(function(tab){
			if (tab != ignore){
				console.log(rh_tabs[tab])
				if (rh_tabs[tab][0] ===true){
					rh_tabs[tab][1]();
				};
			};
		});
	};

$(document).ready(function(){

	reached_section_loop(intiation)


	$('#minimise_left_side_bar').click(function(){
		if (!$('#open_left_margin').length){
			$('#left_side_bar').slideUp();
			$('#center_col').prepend(`<div
				id='open_left_margin' style='width:7%;height:100%;'></div>`);
			$('#center_col').css({'margin-left':'5px','display':'flex','flex-direction':'row'});
		}
		$('#open_left_margin').click(function(){
			$('#open_left_margin').remove();
			$('#center_col').css({'margin-left':'0'});
			$('#left_side_bar').slideDown();
		});
	});

	$('li[group=query_tabs]').click(function(){
		deselect_query_tabs()
		$(this).addClass('is-active')
		console.log($(this).attr('id'))
		evaluate_query_tabs($(this).attr('id'))
	});

	$('button[group=further_disclosures][disc_name=solar]').mouseenter(function(){
		$('span[data-identifier=solar_panels_bool]').css({'background-color':'red'})
		meaning_scroller($('span[data-identifier=solar_panels_bool]'))
	});

	$('button[group=further_disclosures][disc_name=solar]').mouseleave(function(){
		$('span[data-identifier=solar_panels_bool]').css({'background-color':'transparent'})
	});

	search_function('#search_text', {
		'variable_search' : 1,
		'cur_set' : results,
		'set_id_ident':'identifier',
		'key_unit':dicty
	});

	$("#toggle_side_view").click(function(){
		toggle_side_view()
	});

	$("#create_work_task").click(function(){
		work_task_data_sender()
	});

	$('button[group=section_frc]').each(function(){
		var marker = $(this).attr('frc');
		var level = $(this).attr('level');
		$(this).click(function(){
			all_sections('none')
			section_data['collated'][marker][level].forEach(function(section){
				$(`input[group=sections][name=${section}]`).click();
			});
			if ($(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).prop('checked') == false){
				$(`input[type=checkbox][set=fraud_comp_risk][value=${marker}]`).click();
			};			
		});
		var div_find = ''+level+'_'+marker
		console.log(div_find)
		var sec_no = section_data['collated'][marker][level].length;
		if (sec_no == 0){
			$('#'+$(this).attr('id')).prop('disabled',true)
		} else{
			box_popup('#'+$(this).attr('id'),fraud_comp_risk_sec_div[div_find](sec_no),true)
		}
	});

$('button[group=sub_disc]').click(function(){
	var form_name = $(this).attr('sub_disc')
	var exension_data = {form_name:form_name, root_linkage:'TA6_part_1',root_linkage_id:form_set['form']}
	$.ajax({
		url:'/extend_synopsis',
		data:{data:JSON.stringify(exension_data)},
		type:'post',
		success:function(data){
			var data = JSON.parse(data)
			$('#meaning_body').append(`<p id="meaning_string" form='${data[form_name]}'>`)
			meaning_string = $(`p[id=meaning_string][form=${data[form_name]}]`)
			results=data['results']
			reached_section_loop(intiation, data)
		}
	})
});		

});



