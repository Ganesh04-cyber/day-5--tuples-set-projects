emails = ["ganesh@gmail.com", "riya@gmail.com", "aman@gmail.com", "ganesh@gmail.com", 
          "neha@gmail.com", "riya@gmail.com"]

unique_emails=set(emails)
print("unique emial:",unique_emails)

duplicate=[email for email in emails if emails.count(email)>1]
print("duplicates emial",set(duplicate))