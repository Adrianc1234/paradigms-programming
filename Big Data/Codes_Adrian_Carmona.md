![mongo.png](https://miro.medium.com/max/1400/1*JvxScywQ5-PcFbr6s9gn2Q.png)
<center><h1>Codes for Mongodb</h1></center>
<h2>What is mongodb and how does it work?</h2>

**Mongodb** storages a lot of data inside of documents that are so light for example .json, by that reason the shields can changes between files and the data structure can be change over time.<br>
**Mongodb** is a distributed database in its core, so high availability, horizontal scalability and geographical distribution are integrated and easy to use.

<h3>How is it organized? or How does it storage?</h3>

![mongodb](https://lvemil.files.wordpress.com/2017/06/conceptos1.png?w=1000)

The first part is register one server in mongodb. We must understand that mongodb save only in documents, in that server we can create a lot of databases and inside of these we can create collections. Collection are like a stock that can save many documents. Like an advice i can say that the collections are the principal point to be completly organized because every collection should save documents for an especific topic. 

<h3><center>Commands</center></h3>
<h3>Create a data base</h3>
The most normal is that we thought that to create a database in Mongodb there would be a method of the `createDB` style or `createDataBase` or something like that. Mongodb does not allow to create a database by commands, but creates it at the very moment in which we insert an element into a collection.
````bash
use nombredb
(example: use test)
````
**Note:** after that we have a db we can made collections where we will save documents.

<h3>Insert a collection</h3>

In this part we can insert things into a collection using `.insert()` or using `.save()` like : `db.comunidades.save({comunidad:'Madrid'})`, but you must remember that the collections are the most important thing because here is where you define the organization of your database. <br>
Also we can use this command `db.createCollection('name')` if you want to go step by step because this command only mades an empty collection, but in this case i insert collections with documents.
	
````bash
db.friends.insert(
    {
        name:"Mario",
        hobbies:["Programming","playing videogames","studying"],
        friends:
        [
            {name:"Alan", ocuppation:"student", edad: 20},
            {name:"Oswaldo", ocuppation:"student", edad: 20},
            {name:"Pablito", occupation: "student", edad: 20}
        ],
        novia: "Fatima"
    }
)
//this is the output
>>WriteResult({ "nInserted" : 1 })
````
**Note:** I did many insertions with the same syntax.

<h3>How can we see all the collections and documents?</h3>

We can see the collections and the documents or files inside of a database, but if you are so noob in this topic you only need to write `db.name.find()` and it will show you a list of things but is a so bad format for our eyes, so we can write `db.name.find().pretty()` and it will see better. 
	
````bash
db.friends.find().pretty()
>>{
        "_id" : ObjectId("5ebc79c3a26f424895ace487"),
        "name" : "Isaac",
        "hobbies" : [
                "traveling",
                "programming",
                "reading"
        ],
        "friends" : [
                {
                        "name" : "Adrian",
                        "ocuppation" : "student",
                        "edad" : 20
                },
                {
                        "name" : "Hector",
                        "ocuppation" : "student",
                        "edad" : 20
                },
                {
                        "name" : "Auria",
                        "occupation" : "student",
                        "edad" : 20
                }
        ]
}
````
**Note:** that was only an example of how it would see.

<h3>How can we sort our output when we have many documents?</h3>

This is a simple funtion, but you must know that you need to define the most important variable or value that you want to choose like an index to make the sorting. the syntax is `db.nameofcollection.find().pretty().sort({"value": +1 or -1})` + or -1 is ascendig or descending.

	
````bash
db.friends.find().pretty().sort({name:-1});
>>{
	"_id" : ObjectId("5ebd776e058dac3630a0e8c1"),
	"name" : "Mario",
	"hobbies" : [
		"Programming",
		"playing videogames",
		"studying"
	],
	"friends" : [
		{
			"name" : "Alan",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Oswaldo",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Pablito",
			"occupation" : "student",
			"edad" : 20
		}
	],
	"novia" : "Fatima"
}
{
	"_id" : ObjectId("5ebc79c3a26f424895ace487"),
	"name" : "Isaac",
	"hobbies" : [
		"traveling",
		"programming",
		"reading"
	],
	"friends" : [
		{
			"name" : "Adrian",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Hector",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Auria",
			"occupation" : "student",
			"edad" : 20
		}
	]
}
{
	"_id" : ObjectId("5ebd7681058dac3630a0e8bf"),
	"name" : "Hector",
	"hobbies" : [
		"Programming",
		"playing videogames",
		"studying"
	],
	"friends" : [
		{
			"name" : "Liss",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Isaac",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Auria",
			"occupation" : "student",
			"edad" : 20
		}
	]
}
{
	"_id" : ObjectId("5ebd7713058dac3630a0e8c0"),
	"name" : "Caro",
	"hobbies" : [
		"Programming",
		"playing videogames",
		"studying"
	],
	"friends" : [
		{
			"name" : "Alan",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Oswaldo",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Mario",
			"occupation" : "student",
			"edad" : 20
		}
	]
}
{
	"_id" : ObjectId("5ebd762e058dac3630a0e8be"),
	"name" : "Adrian",
	"hobbies" : [
		"playing guitar",
		"playing videogames",
		"reading"
	],
	"friends" : [
		{
			"name" : "Liss",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Hector",
			"ocuppation" : "student",
			"edad" : 20
		},
		{
			"name" : "Auria",
			"occupation" : "student",
			"edad" : 20
		}
	]
}
````

<h3>How can we make opperations with the data?</h3>

Aggregations operations process data records and return computed results. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result. In SQL count(*) and with group by is an equivalent of MongoDB aggregation.<br>
We will made other collection with documents that have integers to make opperations. in this case we will make a sum of groups that have documents with the same id, we use `$group:{value to make groups}` and `$sum:{"values to sum"}`. 

	
````bash
db.friends.insert({ _id: 1, cust_id: "4321", ord_date: ISODate("2012-11-02T17:04:11.102Z"), status: "a", amount: 50 },
{ _id: 2, cust_id: "1234", ord_date: ISODate("2013-10-01T17:04:11.102Z"), status: "a", amount: 480 },
{ _id: 3, cust_id: "1234", ord_date: ISODate("2013-10-12T17:04:11.102Z"), status: "b", amount: 120 },
{ _id: 4, cust_id: "4321", ord_date: ISODate("2013-10-11T17:04:11.102Z"), status: "b", amount: 350 },
{ _id: 5, cust_id: "4321", ord_date: ISODate("2013-11-12T17:04:11.102Z"), status: "a", amount: 30 })

//command to make a sum of things but we use group to make groups with the id, then it will sum the things that have the same id.
db.friends.aggregate([
                     { $match: { status: "b" } },
                     { $group: { _id: "$cust_id",
                    "total sum": { $sum: "$amount" } } },
                     { $sort: { total: -1 } }
                   ])
//this is the output
{ "_id" : "4321", "total sum" : 350 }
{ "_id" : "1234", "total sum" : 120 }
````
<h3>Delete a collection</h3>
This is the code to delete something that is not so necesary in the collections.
	
````bash
db.empleados.remove({"cedula" : "123456"}); // this  is to delete one document.
db.empleados.drop(); // this is to delete a collection
````

<h2><center> Mongo db in python</center></h2>

Now we are going to change the enviroment cuz you must know that in python we can use mongodb too, but it has a complex systaxis.<br>
in this part we will star what things does it work with? It can work with `.json` or with `array`, but in the json the order is not important, on the other hand when you work with arrays, the order is important. 

````Python
// this is a dictionary 
{
'id': 12345,
'name': 'Donny Winston',
'instructor': true
}

// this is an array
Array = ['id','name','instructor']
```` 
<h3>Making a local server</h3>

In this part we need to start a local host using MongoClient and with this code where clientaaeeeas

````Python
import request
from pymongo import MongoClient
# Client connects to "localhost" by default
client = MongoClient()
# Create local "nobel" database on the fly
db = client["nobel"]
````










