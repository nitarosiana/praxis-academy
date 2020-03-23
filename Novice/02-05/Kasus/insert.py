import hubung

cursor = hubung.db.cursor()

sql = "INSERT INTO members (name, address, salutation_id) VALUES (%s, %s, %s)"
values = [
  ("Janet Jones", "First Street Plot 4", "2"),
  ("Robert Phill", "3 Street 34", "1"),
  ("Robert Phill", "5 Avenue", "1")
]

for val in values:
  cursor.execute(sql, val)
  hubung.db.commit()

print("{} data ditambahkan".format(len(values)))


sql = "INSERT INTO rent_mv (member_id, movie_rent) VALUES (%s, %s)"
values = [
  ("1", "Pirates of the Carribbean"),
  ("1", "Clash of the Titans"),
  ("2", "Forgetting Sarah Marshal"),
  ("2", "Daddy's Little Girls"),
  ("3", "Clash of the Titans"),
]

for val in values:
  cursor.execute(sql, val)
  hubung.db.commit()

print("{} data ditambahkan".format(len(values)))