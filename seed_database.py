'''Script to seed database.'''

import os
from datetime import datetime

import crud
import model
import server

os.system('dropdb cleaning')
os.system('createdb cleaning')

model.connect_to_db(server.app)
model.db.create_all()

def create_fake_users():
  crud.create_user_with_id(111,'Leda','Garbett','leda.garbett@gmail.com','password','customer')
  crud.create_user_with_id(112,'Mercedes','Alenikov','mercedes.alenikov@gmail.com','password','customer')
  crud.create_user_with_id(114,'Jenni','Abrahamson','jenni.abrahamson@gmail.com','password','customer')
  crud.create_user_with_id(115,'Clare','Fulep','clare.fulep@gmail.com','password','customer')
  crud.create_user_with_id(117,'Kim','Deeming','kim.deeming@gmail.com','password','customer')
  crud.create_user_with_id(1111,'Dedie','Cockland','dedie.cockland@gmail.com','password','customer')
  crud.create_user_with_id(1113,'Tonia','Varran','tonia.varran@gmail.com','password','customer')
  crud.create_user_with_id(1114,'Gaelan','Savin','gaelan.savin@gmail.com','password','customer')
  crud.create_user_with_id(1116,'Sylvan','Tully','sylvan.tully@gmail.com','password','customer')
  crud.create_user_with_id(1117,'Ardra','Corn','ardra.corn@gmail.com','password','customer')
  crud.create_user_with_id(1118,'Rosina','Mattingson','rosina.mattingson@gmail.com','password','customer')
  crud.create_user_with_id(1119,'Brock','Leethem','brock.leethem@gmail.com','password','customer')
  crud.create_user_with_id(1122,'Ashley','Lammerich','ashley.lammerich@gmail.com','password','customer')
  crud.create_user_with_id(1124,'Bald','Dunsmore','bald.dunsmore@gmail.com','password','customer')
  crud.create_user_with_id(1125,'Olivia','McCrackan','olivia.mccrackan@gmail.com','password','customer')
  crud.create_user_with_id(1126,'Charin','Cowerd','charin.cowerd@gmail.com','password','customer')
  crud.create_user_with_id(1127,'Martelle','Stitch','martelle.stitch@gmail.com','password','customer')
  crud.create_user_with_id(1128,'Pattie','Heinritz','pattie.heinritz@gmail.com','password','customer')
  crud.create_user_with_id(1130,'Carmela','Warratt','carmela.warratt@gmail.com','password','customer')
  crud.create_user_with_id(11203,'Davin','Goane','davin.goane@gmail.com','password','employee')
  crud.create_user_with_id(11209,'Corly','Macewan','corly.macewan@gmail.com','password','employee')
  crud.create_user_with_id(11215,'Manda','Dibbin','manda.dibbin@gmail.com','password','employee')
  crud.create_user_with_id(11221,'Rosabel','Cowl','rosabel.cowl@gmail.com','password','employee')
  crud.create_user_with_id(11223,'Micky','Jakeway','micky.jakeway@gmail.com','password','employee')



def create_fake_addresses():
  crud.create_address_with_id(111, 111, 'Primary Residence', '3544 NW Braid Dr', 'Bend', 'OR', 97703)
  crud.create_address_with_id(112, 111, 'Vacation Home', '17652 Tennis Village Ct,', 'Sunriver', 'OR', 97707)
  crud.create_address_with_id(113, 111, 'Vacation Home', '63168 Peale St', 'Bend', 'OR', 97701)

def create_employee_job():
  crud.create_employee_job(11203,11100)
  crud.create_employee_job(11203,11101)
  crud.create_employee_job(11203,11102)
  crud.create_employee_job(11203,11103)
  crud.create_employee_job(11203,11104)
  crud.create_employee_job(11203,11105)
  crud.create_employee_job(11203,11106)
  crud.create_employee_job(11203,11107)
  crud.create_employee_job(11203,11108)
  # crud.create_employee_job(11203,11109)
  # crud.create_employee_job(11203,11110)
  # crud.create_employee_job(11203,11111)
  crud.create_employee_job(11209,11112)
  crud.create_employee_job(11209,11113)
  crud.create_employee_job(11209,11114)
  crud.create_employee_job(11209,11115)
  crud.create_employee_job(11209,11116)
  crud.create_employee_job(11209,11117)
  crud.create_employee_job(11209,11118)
  crud.create_employee_job(11209,11119)
  crud.create_employee_job(11209,11120)
  # crud.create_employee_job(11209,11121)
  # crud.create_employee_job(11209,11122)
  # crud.create_employee_job(11209,11123)
  crud.create_employee_job(11221,11124)
  crud.create_employee_job(11221,11125)
  crud.create_employee_job(11221,11126)
  crud.create_employee_job(11221,11127)
  crud.create_employee_job(11221,11128)
  crud.create_employee_job(11221,11129)
  crud.create_employee_job(11221,11130)
  crud.create_employee_job(11215,11112)
  crud.create_employee_job(11215,11113)
  crud.create_employee_job(11215,11114)
  crud.create_employee_job(11215,11115)
  crud.create_employee_job(11215,11116)
  crud.create_employee_job(11215,11117)
  crud.create_employee_job(11215,11118)
  crud.create_employee_job(11215,11119)
  crud.create_employee_job(11215,11120)
  # crud.create_employee_job(11215,11121)
  # crud.create_employee_job(11215,11122)
  # crud.create_employee_job(11215,11123)

def create_job():
  crud.create_job_with_id(11100, 111, 111, '2021-05-04 11:00:00', '2021-05-04 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11101, 111, 111, '2021-05-18 11:00:00', '2021-05-18 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11102, 111, 111, '2021-06-01 11:00:00', '2021-06-01 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11103, 111, 111, '2021-06-15 11:00:00', '2021-06-15 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11104, 111, 111, '2021-06-29 11:00:00', '2021-06-29 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11105, 111, 111, '2021-07-13 11:00:00', '2021-07-13 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11106, 111, 111, '2021-07-27 11:00:00', '2021-07-27 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11107, 111, 111, '2021-08-10 11:00:00', '2021-08-10 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11108, 111, 111, '2021-08-24 11:00:00', '2021-08-24 14:00:00', 150, 'Confirmed')
  # crud.create_job_with_id(11109, 111, 111, '2021-09-07 11:00:00', '2021-09-07 14:00:00', 150, 'Confirmed')
  # crud.create_job_with_id(11110, 111, 111, '2021-09-21 11:00:00', '2021-09-21 14:00:00', 150, 'Confirmed')
  # crud.create_job_with_id(11111, 111, 111, '2021-10-05 11:00:00', '2021-10-05 14:00:00', 150, 'Confirmed')
  crud.create_job_with_id(11112, 111, 112, '2021-05-07 8:00:00', '2021-05-07 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11113, 111, 112, '2021-05-21 8:00:00', '2021-05-21 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11114, 111, 112, '2021-06-04 8:00:00', '2021-06-04 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11115, 111, 112, '2021-06-18 8:00:00', '2021-06-18 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11116, 111, 112, '2021-07-02 8:00:00', '2021-07-02 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11117, 111, 112, '2021-07-16 8:00:00', '2021-07-16 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11118, 111, 112, '2021-07-30 8:00:00', '2021-07-30 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11119, 111, 112, '2021-08-13 8:00:00', '2021-08-13 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11120, 111, 112, '2021-08-27 8:00:00', '2021-08-27 13:00:00', 225, 'Confirmed')
  # crud.create_job_with_id(11121, 111, 112, '2021-09-10 8:00:00', '2021-09-10 13:00:00', 225, 'Confirmed')
  # crud.create_job_with_id(11122, 111, 112, '2021-09-24 8:00:00', '2021-09-24 13:00:00', 225, 'Confirmed')
  # crud.create_job_with_id(11123, 111, 112, '2021-10-08 8:00:00', '2021-10-08 13:00:00', 225, 'Confirmed')
  crud.create_job_with_id(11124, 111, 113, '2021-05-06 9:00:00', '2021-05-06 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11125, 111, 113, '2021-05-20 9:00:00', '2021-05-20 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11126, 111, 113, '2021-06-03 9:00:00', '2021-06-03 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11127, 111, 113, '2021-06-17 9:00:00', '2021-06-17 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11128, 111, 113, '2021-07-01 9:00:00', '2021-07-01 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11129, 111, 113, '2021-07-15 9:00:00', '2021-07-15 12:00:00', 175, 'Confirmed')
  crud.create_job_with_id(11130, 111, 113, '2021-07-29 9:00:00', '2021-07-29 12:00:00', 175, 'Confirmed')


create_fake_users()
create_fake_addresses()
create_job()
create_employee_job()
crud.create_invoices()
