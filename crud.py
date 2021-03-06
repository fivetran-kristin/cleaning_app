"""CRUD operations."""

from model import db, User, Address, Job, Image, Invoice, Review, EmployeeJob, connect_to_db
from datetime import date, timedelta
import invoice_generator
import os

# User functions
def create_user(first_name, last_name, email, password, role):
  """Create and return a new user"""

  user = User(first_name=first_name, 
              last_name=last_name, 
              email=email, 
              password=password, 
              role=role
              )

  db.session.add(user)
  db.session.commit()

  return user


def get_user_by_email(email):
  """ Takes an email, and returns the user record.  If email doesn't exist, returns empty list. """

  return User.query.filter(User.email==email).first()
  
def get_user_by_id(user_id):
  """ Takes a user ID, returns the user record. """

  return User.query.get(user_id)

def is_correct_password(email, password):
  """ Takes an email and password. Returns true if password correct. Returns false if password is incorrect."""

  User = get_user_by_email(email)

  if User is None:
    return False
  
  return User.password == password
  
# Address functions
def create_address(customer_id, address_type, street, city, state, zip_code):
  """Create and return a new address"""

  address = Address(customer_id=customer_id, 
                    address_type=address_type, 
                    street=street, 
                    city=city, 
                    state=state, 
                    zip_code=zip_code
                    )

  db.session.add(address)
  db.session.commit()

  return address


def create_job(customer_id, address_id, start_time, end_time, amount, status):
  """Create and return a new job"""

  job = Job(customer_id=customer_id,
            address_id=address_id, 
            start_time=start_time, 
            end_time=end_time,
            amount=amount,
            status=status
            )

  db.session.add(job)
  db.session.commit()

  return job

def get_all_pending_jobs():
  """ Returns list of all Pending jobs """

  return Job.query.filter_by(status='Pending').all()

def update_job_status(job_id, status):
  """ Takes a job id and updates the status to confirmed """

  job = Job.query.get(job_id)

  job.status = status

  db.session.commit()
  
  return

def update_job_estimate(job_id, amount=150):
  """ Takes a job id and updates the status to confirmed """

  job = Job.query.get(job_id)

  job.amount = amount

  db.session.commit()
  
  return

def get_job_by_id(job_id):
  """ Takes a job ID, returns the job record. """

  return Job.query.get(job_id)


def create_employee_job(employee_id, job_id):
  """Create and return a new employee job relationship"""

  employee_job = EmployeeJob(employee_id=employee_id,
                              job_id=job_id
                              )

  db.session.add(employee_job)
  db.session.commit()

  return employee_job
  
def create_image(job_id, user_id, image_url, uploaded_at):
  """Create and return a new image"""

  image = Image(job_id=job_id, 
                user_id=user_id, 
                image_url=image_url,
                uploaded_at=uploaded_at
                )

  db.session.add(image)
  db.session.commit()

  return image

def create_invoices():
  """ Creates invoices for all jobs that do not have associated invoices """
  existing_invoices = Invoice.query.all()
  existing_jobs = Job.query.all()

  job_ids_with_invoices = []

  for invoice in existing_invoices:
    job_ids_with_invoices.append(invoice.job_id)

  for job in existing_jobs:
    if job.job_id not in job_ids_with_invoices:
      invoice = Invoice(job_id=job.job_id)
      db.session.add(invoice)
      db.session.commit()

def generate_invoices():
  existing_invoices = Invoice.query.all()

  for invoice in existing_invoices:
    customer_id = invoice.job.customer.user_id
    customer_first_name = invoice.job.customer.first_name
    invoice_number = invoice.invoice_id
    date = (invoice.job.start_time).date().isoformat()
    due_date = (invoice.job.start_time.date() + timedelta(days=30)).isoformat()
    item_name = invoice.job.address.address_type
    item_cost = invoice.job.amount
    
    if not os.path.exists(f'invoices/{customer_id}'):
      os.makedirs(f'invoices/{customer_id}')
    
    if not os.path.exists(f'invoices/{customer_id}/{invoice_number}.pdf'):
      invoice = invoice_generator.InvoiceGenerator(
                          to=customer_first_name, 
                          number=invoice_number, 
                          date=date,
                          due_date=due_date,
                          item_name=item_name,
                          item_quantity=1,
                          item_cost=item_cost)
  
      invoice.download(f'invoices/{customer_id}/{invoice_number}.pdf') 


def create_review(job_id, customer_id, star_rating, review_text):
  """Create and return a new review"""

  review = Review(job_id=job_id, 
                  customer_id=customer_id, 
                  star_rating=star_rating, 
                  review_text=review_text
                  )

  db.session.add(review)
  db.session.commit()

  return review







# FOR CRUD OPERATIONS
def create_user_with_id(user_id, first_name, last_name, email, password, role):
  """Create and return a new user"""

  user = User(user_id=user_id, 
              first_name=first_name, 
              last_name=last_name, 
              email=email, 
              password=password, 
              role=role
              )

  db.session.add(user)
  db.session.commit()

  return user

def create_address_with_id(address_id, customer_id, address_type, street, city, state, zip_code):
  """Create and return a new address"""

  address = Address(address_id=address_id, 
                    customer_id=customer_id, 
                    address_type=address_type, 
                    street=street, 
                    city=city, 
                    state=state, 
                    zip_code=zip_code
                    )

  db.session.add(address)
  db.session.commit()

  return address

def create_job_with_id(job_id, customer_id, address_id, start_time, end_time, amount, status):
  """Create and return a new job"""

  job = Job(job_id=job_id, 
            customer_id=customer_id,
            address_id=address_id, 
            start_time=start_time, 
            end_time=end_time,
            amount=amount,
            status=status
            )

  db.session.add(job)
  db.session.commit()

  return job
  
if __name__ == '__main__':
    from server import app
    connect_to_db(app)