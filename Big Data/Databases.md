<h1>DATABASES</h1>

---

<h2>Graphical Databases</h2>

Graphical databases serve to establish relationships, which are run later when in use. The way these are organized is the gradi of value of the data, so the relationships are classified as first-class citizens in the databases, and the rest derive with more relationships with different values.  These databases use nodes to save information of each data and borders to store the relationships, which having this relationship has a start node and end node, It should also be mentioned that there is no limit to the number of relationships a node can have.<br>
<br>

**Note:** 
They have advantages over usage cases such as social media, recommendation engines and fraud detection, where you need to link data and quickly query it.

![Graph database](https://miro.medium.com/max/1000/1*3XqHO9_jmc_ENLXuLhWpgQ.png)
![Why is important the graph database?(Benny Ogidan,Oct 30, 2018)](https://medium.com/the-andela-way/graph-databases-why-are-they-important-c438e1a224ae)

<h3>Use cases</h3>

With quick graphics queries, you can detect if, for example, a prospective buyer is using the same email address and credit card as a known fraud case. Graphics databases can also help you easily detect relationship patterns like, for example, that several people have the same personal email address or that several people share the same IP address even if they live in different physical addresses.  Another use of this type of database is that of recommendations, in which basically the user nodes are seen and the higher values of the nodes that are linked to the main node are recommended, from there that for example spotify and facebook give you music recommendations or similar movies.
<br>

![Spotify](https://indiehoy.com/wp-content/uploads/2018/06/spotify.jpg)

![more information](https://aws.amazon.com/es/nosql/graph/)

Most popular data set:

Database |	Description
-- | --
Neo4j |	An ACID-compliant DBMS with native graph storage and processing. As of this writing, Neo4j is the most popular graph database in the world.
ArangoDB |	Not exclusively a graph database, ArangoDB is a multi-model database that unites the graph, document, and key-value data models in one DBMS. It features AQL (a native SQL-like query language), full-text search, and a ranking engine.
OrientDB |	Another multi-model database, OrientDB supports the graph, document, key-value, and object models. It supports SQL queries and ACID transactions.

![Reference of table(more information)](https://www.digitalocean.com/community/tutorials/a-comparison-of-nosql-database-management-systems-and-models#graph-databases)

---

<h2>Ledger Databases</h2>
  
General ledgers are commonly seen as a huge book of records within a database, where they can be saved for example by recording a complete history of an organization’s economic or financial activity. for example, monitoring credit and debit history in banking transactions, verifying the data flow of an insurance claim or tracking the movement of an item in a supply chain network.

A ledger database is immutable this means that you never change the data in the document or DB table, which is so important for the companies because with this way to organize access to the information, by that only their employments can edit. What we may think of as a change, updating a person’s address, for instance, becomes a new version of that record. So, no matter what changes happen you will never overwrite the existing data.

You can apply encryption methods to improve the security of your database, so that the data is safeguarded and hidden by means of encryption in which only a base key can show the data that is in it.

![More information](https://hackernoon.com/relational-nosql-ledger-databases-work-not-permissioned-blockchains-9ccaef7b3139)

![Ledger database](https://image.slidesharecdn.com/dat378-mir-mon-d-fri-1000-dat3-f4a3d376-f592-4089-b388-cf5aec113bed-281602960-181211171732/95/new-launch-how-do-i-know-i-need-a-ledger-database-an-introduction-to-amazon-qldb-dat378-aws-reinvent-2018-14-638.jpg?cb=1544548685)

![Slides with more information and the picture](https://www.slideshare.net/AmazonWebServices/new-launch-how-do-i-know-i-need-a-ledger-database-an-introduction-to-amazon-qldb-dat378-aws-reinvent-2018)
