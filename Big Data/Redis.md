

![Redis](https://wikihosting.es/wp-content/uploads/2019/11/Redis-980x551.png)
<br>
***

<h2>How can we install it in ubuntu? </h2>

Install Redis-server

````Bash
$ sudo apt install redis-server
````
Open this file to make changes

````Bash
$ sudo nano /etc/redis/redis.conf
````
Now we must found the part where we see supervised inside of the file, this part, allow us declare a system, init to manage Redis
like a server, which give us a control over its functions. by default the value the supervised value is 'no', then as we are in ubuntu,
we will change this for systemd.

````txt
. . .

# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no      - no supervision interaction
#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
#   supervised auto    - detect upstart or systemd method based on
#                        UPSTART_JOB or NOTIFY_SOCKET environment variables
# Note: these supervision methods only signal "process is ready."
#       They do not enable continuous liveness pings back to your supervisor.
supervised systemd
. . .
````
lets go to restard the service and then chek if it works.

````Bash
#supervised systemd
$ sudo systemctl restart redis.service

#check the service
$ sudo systemctl status redis
````
This would be the output:

*Note:* we can see that it says running

````Bash
redis-server.service - Advanced key-value store
     Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor >
     Active: active (running) since Sun 2020-05-24 11:46:46 CDT; 8h ago
       Docs: http://redis.io/documentation,
             man:redis-server(1)
    Process: 967 ExecStart=/usr/bin/redis-server /etc/redis/redis.conf (code=ex>
   Main PID: 1028 (redis-server)
      Tasks: 4 (limit: 9230)
     Memory: 4.4M
     CGroup: /system.slice/redis-server.service
             └─1028 /usr/bin/redis-server 127.0.0.1:6379

may 24 11:46:42 adrian-HP-Laptop-15-da0xxx systemd[1]: Starting Advanced key-va>
may 24 11:46:45 adrian-HP-Laptop-15-da0xxx systemd[1]: redis-server.service: Ca>
may 24 11:46:46 adrian-HP-Laptop-15-da0xxx systemd[1]: Started Advanced key-val>
````
Then we can start using it.

<h2>Commands for Redis</h2>

````bash
#we write this code to execute the server.
redis-cli
# the otuput would be:
127.0.0.1:6379> 
````
<h3>Hello world</h3>

Lets make our first hello world, but like a set. we only need to write this comando:
We use `SET` and `GET` to declare that is a set of strings and after that we use `GET hkey` to get the set
and show our hello world.

````bash
127.0.0.1:6379> SET hkey "hello world"
OK
127.0.0.1:6379> Get hkey
"hello world"
127.0.0.1:6379> 
````
<h3>Choosing a database and cheking its size</h3>

````Bash
#to check the size of some database
127.0.0.1:6379> dbsize
(integer) 2

#to select one
127.0.0.1:6379> select 1
OK

#to see the size
127.0.0.1:6379[1]> dbsize
(integer) 20
````

<h2>Using python</h2>
As we know we can use Redis in python and the unique thing that we need to do is install it with `pip install hiredis`.
<br>
we can add a set of documents like a dictionary using this syntaxis.
for example:
````Python
import redis

r = redis.StrictRedis(host='myserver', port=6379, db=0)
r.hmset('my_key', {'field0': 'value0', 'field1':'value1', 'field2':'value2'}
````






