def update_last_user_access(particular_id,user_id):
	params = (particular_id,user_id,user_id)
	query = "UPDATE particulars_and_objects.market_particulars set last_user_access = %s,last_user_access_timestamp=curtime() where particular_id = %s and last_user_access = %s;"
	user_access=db.cursor()
	user_access.execute(query,params)
	db.commit()
	user_access.close()
	return None