# meeting-room
 ____________
/INSTRUCTIONS\
||||||||||||||

I. Installation:

1. new folder >> run:
git clone https://github.com/grizzlydevil/meeting-room.git

2. cd into the folder >> run:
docker-compose build

3. docker-compose up

4. open in browser: http://127.0.0.1:8000/

II. structure of API
admin/
you can login with supersuser: 
email: meska@mail.com
pass: somepass
this password is the same for all created users

auth/ for all authentication purposes
this would be the path to create a user:
auth/registration/
auth/login/
auth/logout/
auth/token/refresh/ - if your token has expired

after the user is created he will not have authorization
to create rooms or reservations. First we need to create an
employee for the user in this API endpoint:
employee/

now we can enter the rooms endpoints
rooms/create/ - to create a new meeting room
rooms/reservations/create/ - to create a new reservations
rooms/reservations/cancel/<int:pk>/ cancel a reservation
rooms/reservations/<int:room>/ to get all the reservations for the specified room primary key
rooms/reservations/<int:room>/<int:employee>/ to get all the reservations for the specified room and filtered by employee

a couple of users already created:
newacc@some.com
oneMore@time.com
again@again.com

all passwords match: somepass
