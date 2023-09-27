	

	/*function search_function(){
		document.querySelector('#search_text').addEventListener('keyup', function(e) {
				var match_count = 0
				matching_selection = {}
				search_term = $("input[id=search_text]").val()
				find_counter = 0
				if (search_term !== ""){
					search_length  = search_term.length
					for (let m of cur_set){
						$(`span[data-identifier='${m.unique_selection_ID}']`).empty();
						found_content_end= 0
						finds = [];
						text_length=m.answer_meaning.length
						remaining_search_length=text_length
						valid = m.answer_meaning.search(new RegExp(search_term, "i"));
						if (valid != -1){
							match_count += 1
							matching_selection.match_count = m
							found_content_end=valid+(search_length)
							finds.push([valid,found_content_end])
							remaining_search_length=remaining_search_length-found_content_end
							while(valid != -1 && remaining_search_length >= search_length){
								search_next = m.answer_meaning.substring(found_content_end)
								valid = search_next.search(new RegExp(search_term, "i"));
								if (valid != -1){
									finds.push([found_content_end+valid,found_content_end+valid+(search_length)])
									found_content_end=found_content_end+valid+(search_length)
									remaining_search_length=found_content_end
								};
							};
							$(`span[data-identifier=${m.unique_selection_ID}]`).text('');
							$(`span[data-identifier=${m.unique_selection_ID}]`).attr('search','found');
							text_position = 0
							for (let f of finds){
								find_counter += 1
								if (f[0] == text_position){
									new_span = m.answer_meaning.substring(f[0],f[1]);
									$(`span[data-identifier=${m.unique_selection_ID}]`).append(`<span style='color:blue'>${new_span}</span>`);
									text_position = f[1]
								}
								else{
									new_span = m.answer_meaning.substring(text_position,f[0]);
									$(`span[data-identifier=${m.unique_selection_ID}]`).append(`<span>${new_span}</span>`);
									new_span =  m.answer_meaning.substring(f[0],f[1]);
									$(`span[data-identifier=${m.unique_selection_ID}]`).append(`<span style='color:blue'>${new_span}</span>`);
									text_position = f[1]
								}
							};
							if (text_length != text_position){					
								new_span =  m.answer_meaning.substring(text_position);
								$(`span[data-identifier=${m.unique_selection_ID}]`).append(`<span>${new_span}</span>`);
							}
							$(`span[data-identifier=${m.unique_selection_ID}]`).append(`<span>,</span>`);

						}
						else{
								$(`span[data-identifier=${m.unique_selection_ID}]`).text(`${m.answer_meaning},`)
						}
					};
					$("p[id=matches]").removeClass("hide")
					$("#statement_matches").removeClass("hide")

					if (find_counter !== 0){
						$("span[data-identifier=find_counter]").text(`${find_counter}`)
						$("#statement_match_counter").text(`${match_count}`)
					}else{
						$("span[data-identifier=find_counter]").text(`No`)
						$("#statement_match_counter").text(`No`)
					}
					
				}
				else{
					for (let m of cur_set){
						$(`span[data-identifier='${m.unique_selection_ID}']`).empty();				
						$(`span[data-identifier='${m.unique_selection_ID}']`).text(`${m.answer_meaning},`)
					}
					$("p[id=matches]").addClass("hide")
					$("#statement_matches").addClass("hide");
				}
			});
	}*/

	/*var sample_dict = {
		//if value  = 1 use a text box to derive search term
		variable_search = 1
		// cur_set = set of data _containing strings to be searched
		cur_set = set
		// ident term of data pieces in set
	 = ident
		//piece of text to be evluated
		text_piece = meaning
	}*/
	var dicty = {'tenure':{'freehold':{},'sale':{'lease':{}}}};
	function dict_search_string(dict, search_string){
		search_string = search_string.toLowerCase();
		var terms = [];
		var cur_term_set = [];
		function keys_loop(dict){
			Object.keys(dict).forEach(function(term){
				//console.log(term, search_string)
				var new_dict = dict[term]
				if (term == search_string){
					terms.push(term)
					cur_term_set.forEach(function(term){
						terms.push(term)
					});
				} else if (Object.keys(new_dict).length >0){
					cur_term_set.push(term)
					keys_loop(new_dict)
					//console.log(cur_term_set)
				};
			});
		}
		if (Object.keys(dict).length > 0){
			keys_loop(dict)
		}
		console.log(terms)
		return terms
	};


	function search_function(search_string, dict, pass_count){
		var match_count = 0
		var cur_set = dict['cur_set']
		var set_id_ident = dict['set_id_ident']
		var variable_search = 1
		var colour = 'blue'
		function search_sequence(search_term, colour, set, pass_count){
			function descendant_spans(span){
				var descedants = $(span).find($( "span[type=subspan]" ))
				if (descedants.length > 1){
					descedants.each(function(){
						editor(this)
					});
				} else{
					editor(span)
				};
			};

			function editor(search_topic){
				text_piece = $(search_topic).data('text')
				found_content_end = 0
				finds = [];
				text_length=text_piece.length
				remaining_search_length=text_length
				valid = text_piece.search(new RegExp(search_term, "i"));
				if (valid != -1){
					match_count += 1
					//matching_selection.match_count = m
					found_content_end=valid+(search_length)
					finds.push([valid,found_content_end])
					remaining_search_length=remaining_search_length-found_content_end
					while(valid != -1 && remaining_search_length >= search_length){
						search_next = text_piece.substring(found_content_end)
						valid = search_next.search(new RegExp(search_term, "i"));
						if (valid != -1){
							finds.push([found_content_end+valid,found_content_end+valid+(search_length)])
							found_content_end=found_content_end+valid+(search_length)
							remaining_search_length=found_content_end
						};
					};
					$(search_topic).text('');
					$(search_topic).attr('search','found');
					text_position = 0
					for (let f of finds){
						find_counter += 1
						if (f[0] == text_position){
							new_span = text_piece.substring(f[0],f[1]);
							$(search_topic).append(`<span style='color:${colour}' type='subspan' data-text=${new_span}>${new_span}</span>`);
							text_position = f[1]
						}
						else{
							new_span = text_piece.substring(text_position,f[0]);
							$(search_topic).append(`<span data-text=${new_span} type='subspan'>${new_span}</span>`);
							new_span =  text_piece.substring(f[0],f[1]);
							$(search_topic).append(`<span style='color:${colour}' type='subspan' data-text=${new_span}>${new_span}</span>`);
							text_position = f[1]
						}
					};
					if (text_length != text_position){					
						new_span =  text_piece.substring(text_position);
						$(search_topic).append(`<span type='subspan' data-text=${new_span}>${new_span}</span>`);
					}
					$(search_topic).append(`<span>,</span>`);

				}else{
					$(search_topic).text($(search_topic).data('text')+',')
				};
			};
			search_length  = search_term.length
			set.forEach(function(m){
				var search_topic = $(`span[data-identifier='${m}']`)
				if (!(search_topic.length)){
					return undefined
				};
				if (pass_count == 1){
					$(search_topic).empty();
					$(search_topic).text($(search_topic).data('text'))
					editor(search_topic)
				}else{
					descendant_spans(search_topic);
				};
					
			});
			$("p[id=matches]").removeClass("hide")
			$("#statement_matches").removeClass("hide")

			if (find_counter !== 0){
				$("span[id=find_counter]").text(`${find_counter}`)
				$("#statement_match_counter").text(`${match_count}`)
			}else{
				$("span[id=find_counter]").text(`No`)
				$("#statement_match_counter").text(`No`)
			};
		};

		function main_func(search_string){
			var term_set
			match_count = 0;
			matching_selection = {};
			search_term = search_string;
			find_counter = 0;
			if (search_term !== ""){
				var red_set = []
				var pass_count = 0
				Object.keys(cur_set).forEach(function(m){
					if (cur_set[m]['relevant'] == 1){
						if(cur_set[m]['meanings'] != undefined){
							red_set.push(m)
						};
					};
				});
				if (dict['key_unit'] != undefined){
					var key_unit = dict['key_unit']
					term_set = dict_search_string(key_unit, search_string)
					colour = 'green'
					term_set.forEach(function(term){
						pass_count += 1
						search_sequence(term, colour, red_set, pass_count)
					});
					pass_count += 1
					colour = 'blue'
					search_sequence(search_string, colour, red_set ,pass_count)
				} else {
					pass_count += 1
					search_sequence(search_string, colour, red_set ,pass_count)
				};
	
			}else{
				Object.keys(cur_set).forEach(function(m){
					if(cur_set[m]['meanings'] != undefined){
						if(cur_set[m]['meanings']['meaning'] != ''){
							text_piece = cur_set[m]['meanings']['meaning']
							$(`span[data-identifier='${m}']`).empty();				
							$(`span[data-identifier='${m}']`).text(`${text_piece},`)
						};
					};
				});
				$("p[id=matches]").addClass("hide")
				$("#statement_matches").addClass("hide");
			};
		};
			
		if (dict.variable_search == undefined ||  dict.variable_search != 1){
			main_func(search_string)
		} else if (dict.variable_search == 1){
			document.querySelector(search_string).addEventListener('keyup', function(e) {
				var searchy = $(search_string).val();
				main_func(searchy);				
			});
		};
	};




