
function search_text_and_highight(){
	for (let m of meaning){
					$(`span[id='${m[3]}']`).empty();
					found_content_end= 0
					finds = [];
					text_length=m[0].length
					remaining_search_length=text_length
					valid = m[0].search(new RegExp(search_term, "i"));
					if (valid != -1){
						found_content_end=valid+(search_length)
						finds.push([valid,found_content_end])
						remaining_search_length=remaining_search_length-found_content_end
						while(valid != -1 && remaining_search_length >= search_length){
							search_next = m[0].substring(found_content_end)
							valid = search_next.search(new RegExp(search_term, "i"));
							if (valid != -1){
								finds.push([found_content_end+valid,found_content_end+valid+(search_length)])
								found_content_end=found_content_end+valid+(search_length)
								remaining_search_length=found_content_end
							};
						};
						$(`span[id=${m[3]}]`).text('');
						$(`span[id=${m[3]}]`).attr('search','found');
						text_position = 0
						for (let f of finds){
							find_counter +=1
							if (f[0] == text_position){
								new_span = m[0].substring(f[0],f[1]);
								$(`span[id=${m[3]}]`).append(`<span style='color:blue'>${new_span}</span>`);
								text_position = f[1]
							}
							else{
								new_span = m[0].substring(text_position,f[0]);
								$(`span[id=${m[3]}]`).append(`<span>${new_span}</span>`);
								new_span = m[0].substring(f[0],f[1]);
								$(`span[id=${m[3]}]`).append(`<span style='color:blue'>${new_span}</span>`);
								text_position = f[1]
							}
						};
						if (text_length != text_position){					
							new_span = m[0].substring(text_position);
							$(`span[id=${m[3]}]`).append(`<span>${new_span}</span>`);
						}
						$(`span[id=${m[3]}]`).append(`<span>,</span>`);

					}
					else{
							$(`span[id=${m[3]}]`).text(`${m[0]},`)
					}
				};
}

