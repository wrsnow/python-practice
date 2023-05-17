test = "(pymysql.err.IntegrityError) (1062, \"Duplicate entry 'lwallesr0@mayoclinic.com' for key 'user.email'\")\n[SQL: INSERT INTO user (name, email) VALUES (%(name)s, %(email)s)]\n[parameters: {'name': 'Lissi2', 'email': 'lwallesr0@mayoclinic.com'}]\n(Background on this error at: https://sqlalche.me/e/20/gkpj)"

print(test.find("Duplicate entry"))