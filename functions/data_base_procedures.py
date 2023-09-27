from launch import db
from flask import Blueprint, render_template, redirect, url_for, request, flash, session

def counter(selec_set_ID):
	counter = db.cursor()
	query = "update selection_routines.market_particulars_selection_set set selection_ID_counter = selection_ID_counter+1 where market_particulars_selections_set_ID=%s;"
	params = (selec_set_ID,)
	counter.execute(query,params)

	query = "select @ID_counter := `selection_ID_counter` from selection_routines.market_particulars_selection_set where `market_particulars_selections_set_ID`=%s;"
	counter.execute(query,params)
	count=counter.fetchall()
	db.commit()
	counter.close()
	return count[0]

def extra_data_store(ans, selec_set_ID):
	extra_inputer = db.cursor()
	query = "INSERT into selection_routines.mp_ancilliary_selection_data\
				(selection_set_ID,\
				selection_ID,\
				ancilliary_data,\
				ancilliary_data_type)\
			VALUES(\
				%s\
				@ID_counter\
				%s\
				%s\
			)"

	params = (selec_set_ID,  ans["extra"], ans["type"])

	extra_inputer.execute(query, params)

	extra_inputer.close()

	db.commit()

	return None


def add_to_selections_with_parents(ans,selec_set_ID,parent_selec_ID):
	answer = ans['full_code']
	ans_type = ans['type']
	answer_input = db.cursor()

	query = "select max(`lft`) into @lftmove from selection_routines.market_particulars_selections where market_particulars_selections.parent_set = %s and market_particulars_selections.unique_selection_ID=%s;"
	params = (f"{selec_set_ID}",f"{parent_selec_ID}")
	answer_input.execute(query,params)
	answer_input.execute("select @lftmove;")
	max_lft = answer_input.fetchone()
	if max_lft[0] == None or 0:
		add_to_selections_without_parents(answer,selec_set_ID)
		#query ='select max(`rgt`) into @lftmove from selection_routines.market_particulars_selections where market_particulars_selections.parent_set = %s;'
		#params = (selec_set_ID,)
		#answer_input.execute(query,params)
		#parent_selec_ID=None

	else:
		query = "update selection_routines.market_particulars_selections SET `rgt` := (`rgt`+2) where `rgt`>=@lftmove AND `parent_set`= %s;"
		params = (selec_set_ID,)
		answer_input.execute(query,params)

		query = "update selection_routines.market_particulars_selections SET `lft` := (`lft`+2) where `lft`>@lftmove and market_particulars_selections.parent_set = %s;"
		answer_input.execute(query,params)

#update the counter to keep track of entries in selection sets
	#counter(selec_set_ID)
		count = counter(selec_set_ID)

		query ="select @lftmove"
		answer_input.execute(query)
		lftmove=answer_input.fetchone()
		if not lftmove[0]==None:

			query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter, %s,%s,@lftmove + 1,@lftmove + 2,curdate())"
			params = (selec_set_ID,parent_selec_ID,answer)
			answer_input.execute(query,params)

# end add_to_selections_with_parents procedure
			db.commit()
			answer_input.close()

		else:
			query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter, %s,%s,1,2,curdate())"
			params = (selec_set_ID,parent_selec_ID,answer)
			answer_input.execute(query,params)

#add extra data if extra type answer
	if ans["type"] == "extra":
		extra_data_store( ans,selec_set_ID)

# end add_to_selections_with_parents procedure
	db.commit()
	answer_input.close()
	return None

def add_to_selections_without_parents(ans, selec_set_ID):
	answer = ans.full_code
	ans_type = ans.auxilliary_data

	answer_input = db.cursor()

	query ='select max(`rgt`) into @lftmove from selection_routines.market_particulars_selections where market_particulars_selections.parent_set = %s;'
	params =(selec_set_ID,)
	answer_input.execute(query,params)

	answer_input.execute("select @lftmove;")
	
	max_lft = answer_input.fetchone()
	if max_lft[0] == None or 0:
		query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter,%s,1,2,curdate());"
	else:
		query = "insert into selection_routines.market_particulars_selections(parent_set, unique_selection_ID, selection_ans,lft,rgt,selection) values (%s,@ID_counter,%s,@lftmove+1,@lftmove+2,curdate());"

	count = counter(selec_set_ID)

	params = (selec_set_ID,f"{answer}")

	answer_input.execute(query,params)
	if ans["type"] == "extra":
		extra_data_store( ans,selec_set_ID)
	db.commit()
	answer_input.close()
	return None	


def find_propagations(answer,selec_set_ID):
	findprops=db.cursor()

#find propagations from database
	query =("select sub_Q_props from questions_answers.answer_propagations where full_code = %s;")
	params = (answer,)
	findprops.execute(query,params)
	props=findprops.fetchall()

#find the parent_selec_ID as the last selection input into the selection set
	parent_selec_ID =last_input_to_select_set(selec_set_ID)
	query = "select max(prop_order) from selection_routines.mp_selection_set_queue where mp_selection_set_ID = %s;"
	params = (selec_set_ID,)
	findprops.execute(query,params)
	order=findprops.fetchone()
	prop_order = order[0]
	query="insert into selection_routines.mp_selection_set_queue(mp_selection_set_ID,Q_ID,prop_order,propagating_unique_selec_ID) Values(%s,%s,%s,%s)" 
	for row in props:
		if not prop_order == None or 0:
			prop_order = prop_order+1
		else:
			prop_order=1
		params = (selec_set_ID,row[0],prop_order,parent_selec_ID[0])
		findprops.execute(query,params)
	db.commit()
	findprops.close()




def last_input_to_select_set(selec_set_ID):
	selecid = db.cursor()
	query = ("select max(unique_selection_ID) from selection_routines.market_particulars_selections where parent_set = %s;")
	params = (selec_set_ID,)
	selecid.execute(query,params)
	parent_selec_ID=selecid.fetchone()
	selecid.close()
	return parent_selec_ID

#def delete_last_from_queue(selec_set_ID):
#	delete_from_queue = db.cursor()
#	query ='select max(`prop_order`) into @PO \
#			from selection_routines.mp_selection_set_queue \
#			where mp_selection_set_ID = %s'
#	params = (selec_set_ID,)
#
#	delete_from_queue.execute(query,params)
#
#	query = "delete from selection_routines.mp_selection_set_queue where mp_selection_set_ID = %s\
#			 and prop_order = @PO;"
#
#	delete_from_queue.execute(query,params)
#	db.commit()
#	delete_from_queue.close()
#	return None

def delete_last_from_queue(selec_set_ID):
	delete_from_queue = db.cursor()
	query =f'select max(`prop_order`)\
			from selection_routines.mp_selection_set_queue \
			where mp_selection_set_ID = {selec_set_ID}'

	delete_from_queue.execute(query)

	PO = delete_from_queue.fetchone()

	params = (PO[0],)

	query = f"DELETE from selection_routines.mp_selection_set_queue\
			 where mp_selection_set_ID = {selec_set_ID}\
			 and prop_order = %s;"

	delete_from_queue.execute(query,params)
	db.commit()
	delete_from_queue.close()
	return None

def sort_answers_and_add(answer,selec_set_ID,parent_selec_ID):
	if answer[0] == "no_extra":
		answer = answer[1]
		add_to_selections_with_parents(answer,selec_set_ID,parent_selec_ID)
		find_propagations(answer,selec_set_ID)
		db.commit()
			
	elif answer[0] == "extra":
		ans_extra = answer[1]
		answer = ans_extra[0]
		data = ans_extra[1]
		add_to_selections_with_parents(answer,selec_set_ID,parent_selec_ID)
				
		add_ancilliary_data = db.cursor()

		query= "insert into selection_routines.mp_ancilliary_selection_data(selection_set_ID,selection_ID,ancilliary_data)Values(%s,@ID_counter,%s);"
		params =(selec_set_ID,data)
		add_ancilliary_data.execute(query,params)

		find_propagations(answer,selec_set_ID)
		db.commit()
		add_ancilliary_data.close()
	elif answer[0] == "entries":
		ans_extra = answer[1]
		answer = ans_extra[0]
		new_entries = ans_extra[2]


	
def get_selection_keys(sesh_var,answers,a_type,particular_id,selec_set_ID,form_answer):
	for ans in sesh_var:
		skipformat = f"{ans}skip"
		skip =  skipformat in request.form
		if skip == True:
			text_ans = f"{ans}.4"
			key = ("no_extra",text_ans)
			answers.append(key)
		else:
			extra_data = request.form.get(f"{ans}")
			if extra_data== None or len(extra_data) <1:
				return 1

			ans = (ans,extra_data)
			key =(a_type,ans)
			answers.append(key)
	return answers


def check_selection_set(particular_id,current_user):
	query = "select `market_particulars_selection_set`.`market_particulars_selections_set_ID`,`market_particulars_selection_set`.`selections_owner`,selection_ID_counter from selection_routines.market_particulars_selection_set where market_particulars_selection_set.market_particulars_selections_set_ID = (select max(`market_particulars_selection_set`.`market_particulars_selections_set_ID`) from selection_routines.market_particulars_selection_set where `market_particulars_selection_set`.`market_particulars_ID` = %s);"
	params = (particular_id,)
	setfind = db.cursor()
	setfind.execute(query,params)
	selecset = setfind.fetchone()
	if selecset == None:
		query = "insert into selection_routines.market_particulars_selection_set(market_particulars_ID,selections_owner,creation_moment) Values (%s,%s,curdate());"
		params =(particular_id,current_user)
		setfind.execute(query,params)
		setfind.execute("select last_insert_id()")
		selecset=setfind.fetchone()
		selec_set_ID = selecset[0]
		db.commit()
		setfind.close()

	elif f"{selecset[1]}" == current_user:
		selec_set_ID=selecset[0]

	else:
		selec_set_ID_old = selecset[0]
		query = "insert into selection_routines.market_particulars_selection_set(market_particulars_ID,selections_owner,creation_moment,selection_ID_counter) Values (%s,%s,curdate(),%s);"
		params =(particular_id,current_user,selecset[2])
		setfind.execute(query,params)
		setfind.execute("select last_insert_id()")
		selecset=setfind.fetchone()
		selec_set_ID = selecset[0]
		copy_selection_set_queues(selec_set_ID_old,selec_set_ID)
		replicate_selections(selec_set_ID_old,selec_set_ID)
		db.commit()
		setfind.close()

	return selec_set_ID

def delete_last_from_object_queue(selec_set_ID,object_selection_set,object_unique_ID,object_ID):
	delete_from_queue = db.cursor()
	delete_from_queue
	query = f"delete from selection_routines.{object_selection_set} where mp_selection_set_ID = {selec_set_ID} and {object_unique_ID} = {object_ID} and prop_order = @PO;"
	delete_from_queue.execute(f'select max(`prop_order`) into @PO from selection_routines.{object_selection_set} where mp_selection_set_ID = {selec_set_ID}')
	delete_from_queue.execute(query)
	db.commit()
	delete_from_queue.close()

def add_to_selections_with_parents_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_ID_type,holding_ID):
	answer_input = db.cursor()

	query = f"select max(`lft`) into @lftmove from `selection_routines`.`{object_selection_set}` where parent_set = {selec_set_ID} and parent_unique_selection_ID ={parent_selec_ID};"
	#params = (object_selection_set,selec_set_ID,parent_selec_ID)
	answer_input.execute(query)
	answer_input.execute("select @lftmove;")
	max_lft = answer_input.fetchone()
	if max_lft[0] == None or 0:
		add_to_selections_without_parents_objects(answer,selec_set_ID,object_selection_set,holding_ID)

	else:
		query = "`update selection_routines`.`{object_selection_set}` SET `rgt` := (`rgt`+2) where `rgt`>=@lftmove AND `parent_set`= {selec_set_ID};"
		#params = (object_selection_set,selec_set_ID,)
		answer_input.execute(query)

		query = "`update selection_routines`.`{object_selection_set}` SET `lft` := (`lft`+2) where `lft`>@lftmove and `parent_set` = {selec_set_ID};"
		answer_input.execute(query)

#update the counter to keep track of entries in selection sets
	#counter(selec_set_ID)
		count = counter(selec_set_ID)

		query ="select @lftmove"
		answer_input.execute(query)
		lftmove=answer_input.fetchone()
		if not lftmove[0]==None:

			query = "`insert into selection_routines`.`{object_selection_set}`(parent_set,holding_ID, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values ({selec_set_ID},{holding_ID},@ID_counter, {parent_selec_ID},'{answer}',@lftmove + 1,@lftmove + 2,curdate()),holding_ID"
			#params = (object_selection_set,selec_set_ID,parent_selec_ID,answer)
			answer_input.execute(query)

# end add_to_selections_with_parents procedure
			db.commit()
			answer_input.close()

		else:
			query = "`insert into selection_routines`.`{object_selection_set}`(parent_set,holding_ID, unique_selection_ID, parent_unique_selection_ID, selection_ans,lft,rgt,selection) values ({selec_set_ID},{holding_ID},@ID_counter, {parent_selec_ID},'{answer}',1,2,curdate())"
			#params = (object_selection_set,selec_set_ID,parent_selec_ID,answer)
			answer_input.execute(query)

# end add_to_selections_with_parents procedure
	db.commit()
	answer_input.close()
	return None


def add_to_selections_without_parents_objects(answer,selec_set_ID,object_selection_set,holding_ID):
	
	answer_input = db.cursor()

	query =f'select max(`rgt`) into @lftmove from selection_routines.{object_selection_set} where parent_set = {selec_set_ID};'
	#params =(object_selection_set,selec_set_ID)
	answer_input.execute(query)

	answer_input.execute("select @lftmove;")
	
	max_lft = answer_input.fetchone()
	if max_lft[0] == None or 0:
		query = f"insert into `selection_routines`.`{object_selection_set}`(parent_set,holding_ID, unique_selection_ID, selection_ans,lft,rgt,selection) values ({selec_set_ID},{holding_ID},@ID_counter,'{answer}',1,2,curdate());"
	else:
		query = f"insert into `selection_routines`.`{object_selection_set}`(parent_set,holding_ID, unique_selection_ID, selection_ans,lft,rgt,selection) values ({selec_set_ID},{holding_ID},@ID_counter,'{answer}',@lftmove+1,@lftmove+2,curdate());"

	count = counter(selec_set_ID)

	#params = (object_selection_set,selec_set_ID,holding_ID,answer)

	answer_input.execute(query)

	db.commit()
	answer_input.close()
	return None


def sort_answers_and_add_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_selection_set_queue, object_ID_type ,holding_ID):
	if answer[0] == "no_extra":
		answer = answer[1]
		debug = add_to_selections_with_parents_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_ID_type,holding_ID)
		find_propagations(answer,selec_set_ID)
		db.commit()
			
	elif answer[0] == "extra":
		ans_extra = answer[1]
		answer = ans_extra[0]
		data = ans_extra[1]
		add_to_selections_with_parents_objects(answer,selec_set_ID,parent_selec_ID,object_selection_set,object_ID_type,holding_ID)
				
		add_ancilliary_data = db.cursor()

		query= "insert into selection_routines.mp_ancilliary_selection_data(selection_set_ID,selection_ID,ancilliary_data)Values(%s,@ID_counter,%s);"
		params =(selec_set_ID,data)
		add_ancilliary_data.execute(query,params)

		find_propagations(answer,selec_set_ID)
		db.commit()
		add_ancilliary_data.close()
	elif answer[0] == "entries":
		ans_extra = answer[1]
		answer = ans_extra[0]
		new_entries = ans_extra[2]

def collect_object_selections(table_name,holding_ID,parent_set):
	object_collect=db.cursor()

	query = f"SELECT * from {table_name} where holding_ID =%s and parent_set = %s"
	params =(holding_ID,parent_set)

	object_collect.execute (query,params)
	object_selections=object_collect.fetchall()

	object_collect.close()
	return object_selections


def update_last_data_entry_mp (particular_id,user_id):
	update=db.cursor()
	params = (user_id,particular_id)
	query = "UPDATE `selection_routines`.`market_particulars_selection_set` set last_data_change = curtime(),last_user_data_change = %s where market_particulars_ID=%s;"
	update.execute(query,params)
	db.commit()
	update.close()
	return None

def copy_selection_set_queues(selec_set_ID_old,selec_set_ID):
	copy_queue =db.cursor()
	query="UPDATE selection_routines.mp_selection_set_queue set mp_selection_set_ID = %s where mp_selection_set_ID = %s;"
	params=(selec_set_ID,selec_set_ID_old)
	copy_queue.execute(query,params)
	db.commit()
	copy_queue.close()
	return None

def replicate_selections(selec_set_ID_old,selec_set_ID):
	rs=db.cursor()
	query= "CALL selection_routines.duplicate_mp_selections(%s,%s)"
	params=(selec_set_ID_old,selec_set_ID)
	rs.execute(query,params)
	db.commit()
	rs.close()
	return None


def fetch_market_particular_components(particular_id):

# standard function to query tables for mp_objects	
	class mp_objects:
		def __init__(self,columns,table,particular_id):
			mp_dash_data = db.cursor(buffered=True)
			mp_data = f"select {columns} from {table} where market_particulars = {particular_id}"
			mp_dash_data.execute(mp_data)
			if not mp_dash_data.rowcount:
				self.objects=None
				mp_dash_data.close()
			else:
				self.objects= mp_dash_data.fetchall()
				mp_dash_data.close()

# all companies and shares linked to market particulars

	table = "selection_routines.cns_within_market_partics"
	columns =("`reference_name`, `registered_at_companies_house`")
	Cns = mp_objects(columns,table,particular_id)
	cns=Cns.objects

	if not cns ==None:
		no_of_cns = len(cns)
	else:
		no_of_cns=0
	cns_obj_list =(no_of_cns,cns)

# all Freehold shares linked to market particulars

	table = "selection_routines.unassigned_freehold_share"
	columns ="`provisioned_ID`, `reference_name`"
	Fhs =mp_objects(columns,table,particular_id)
	freehold_shares =Fhs.objects

	if not freehold_shares ==None:
		no_of_fhs = len(freehold_shares)
	else:
		no_of_fhs=0
	fhs_obj_list=(no_of_fhs,freehold_shares)

# all Leaseholds  linked to market particulars
	table = "selection_routines.unassigned_leasehold"
	columns ="reference_name, freehold_type, freehold_ID, holding_ID, X_location_point, Y_location_point"
	Lh = mp_objects(columns,table,particular_id)
	leaseholds =Lh.objects

	if not leaseholds ==None:
		no_of_lh = len(leaseholds)
	else:
		no_of_lh=0
	lh_obj_list=(no_of_lh,leaseholds)

# all commonholds  linked to market particulars

	table = "selection_routines.commonhold_within_market_partics"
	columns ="reference_name"
	commonholds = mp_objects(columns,table,particular_id)


# all Freeholds  linked to market particulars
	table = "selection_routines.unassigned_freehold"
	columns ="reference_name , provisioned_ID, date_first_specified,holding_ID, x_location_point, y_location_point"
	Freeholds = mp_objects(columns,table,particular_id)
	freeholds = Freeholds.objects

	if not freeholds ==None:
		no_of_fh = len(freeholds)
	else:
		no_of_fh=0
	fh_obj_list=(no_of_fh,freeholds)

	total_objects = no_of_cns+no_of_fhs+no_of_lh+no_of_fh

	object_list=[cns_obj_list,fhs_obj_list,lh_obj_list,fh_obj_list]

	return [total_objects,object_list]



