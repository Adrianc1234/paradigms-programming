<center><h1>Big Data</h1></center>
<center>Adrian Roberto Carmona Rodriguez</center>

![big-data-definition.jpeg](https://live.mrf.io/statics/i/ps/www.muylinux.com/wp-content/uploads/2019/06/bigdata.jpg?width=1200&enable=upscale)

<h2>Chapter 1 Paradigm for Big Data</h2>
<h3>Table of Questions</h3>

**Questions**| **Answers**
--------|-------------------
What does The Lambda Architecture provide? | provides a general-purpose approach to implementing an arbitrary function on an arbitrary dataset and having the function return its results with low latency.
What happen if you build immutability and recomputation into the core of a Big Data system?| the system will be innately resilient to human error by providing a clear and simple mechanism for recovery.
What is scalability? | Scalability is the ability to maintain performance in the face of increasing data or load by adding resources to the system.<br>  **Note:** The Lambda Architecture is horizontally scalable across all layers of the system stack: scaling is accomplished by adding more machines.
What is generalization? | That means that your General system can give supports for many applications without problems.
What do you need to check in a maintenance? | This process includes anticipating when to add machines to scale, keeping processes up and running, and debugging anything that goes wrong in production. An important part of this process is choosing components that have as little implementation complexity as possible.
What is debuggability? | This definition is so easy to understand, this means the easy access to data and also the easy manipulation and control of data in a server.
What is compaction? | Creates a new file to which the active information is written. Meanwhile, the existing database files stay in place and continue to be used for storing information and updating the index data.
What do you need to make a compaction correctly? | You have to schedule compactions on each node so that not too many nodes are affected at once.other thing that You have to make sure is check if you have enough disk capacity on your nodes to last them between compactions. the final thing an is one of the most important is that you have to make sure you have enough capacity on your cluster.
What is lambda architecture?| The lambda architecture combines the two best forms of data processing, so the combination of batch and stream is sought by providing better processing and access to data.
What is a batch layer? | The batch layer stores the master copy of the dataset and precomputes batch views on that master dataset.
What are the two thing that a batch layer would be able to do? | Store an immutable, constantly growing master dataset, and compute arbitrary functions on that dataset.




***
<h2>Chapter 2 Batch layer</h2>
<h3>Table of Questions</h3>

**Questions**| **Answers**
-------------------- | -------------------
Why could you reconstruct all your serving and where? even if you lose it.| This is because the batch views served by the serving layer are produced via functions on the master dataset, and since the speed layer is based only on recent data, it can construct itself within a few hours.
What is a stock market trading? | Stock market trading is a fountain of information, with millions of shares and billions of dollars that being exchanged.
Why unstructured data is rawer than normalized data? |We argue that it’s better to store the unstructured string, because your semantic normalization algorithm may improve over time. If you store the unstructured string, you can renormalize that data at a later time when you have improved your algorithms.
What is Semantic normalization?|Semantic normalization is the process of reshaping free form information into a structured form of data.
When store in an Unstructured data? | As a rule of thumb, if your algorithm for extracting the data is simple and accurate, like extracting an age from an HTML page, you should store the results of that algorithm. If the algorithm is subject to change, due to improvements or broadening the requirements, store the unstructured form of the data.
What are the three components in a core of graph schema? | Nodes are the entities in the system - Edges are relationships between nodes. - Properties are information about entities. **Note:** Edges are strictly between nodes.
What do you do in a fact-based model? | In the fact-based model, you deconstruct the data into fundamental units called (unsurprisingly) facts.
Why the facts are atomic? | Facts are atomic because they can not be divided further into meaningful components.
What are the two ways more secure to delete data?| Garbage collection and regulations.
What is the two principals advantages with immutable data? | Human-fault tolerance: is when you put a limit for people that work with your data and  then you can reduce the impact if he made a mistake. the second point is Simplicity: how you know it has and index, then the posibilities to modify and have access to the data are so simple, even you can make appends in an easy way. 

- - -

<h2>Chapter 3 Data model for big data: illustration</h2>
<h3>Table of Questions</h3>

**Questions**| **Answers**
--------|-------------------
What is a serialization framework? |is the process of translating data structures or objects to a state that can be stored for example in a file or buffer also can be transmitted for example, through a network connection link and reconstructing it later.
Say three serialization frameworks| Apache Thrift, Protocol Buffers and Avro.
In which type of structure the time stamp for the information is maintained and may also contain debugging information, besides mentioning that it corresponds to the final structure of the data.| Pedigree and The final Data struct corresponds to a fact from the fact-based model. 
Say the three most important rules to have a good evolving schema | Fields may be renamed, A field may be removed, but you must never reuse that field and Only optional fields can be added to existing structs. 
One example of a limit of serialization framework: | They can’t check more specific things or human errors like, ages should not be negative or time marks should not be towards the future.


- - -

<h2>Chapter 4 Data storage on the batch layer</h2>
<h3>Table of Questions</h3>

**Questions**| **Answers**
--------|-------------------
What does Hadoop Distributed File System (HDFS) do?| HDFS stores the files by splitting them into blocks, a type of divide and conquer, thus minimizing the cost of searches.
What type of architecture use HDFS?| HDFS uses a Master-Slave architecture where the master is the Namenode that manages the files and metadata. These metadata contain information about the file, blockages and their location in the Datanodes.
What is a vertical partitioning?| Vertical partition consists of creating thousands of tables with thousands of columns and creating tables to put the remaining columns.
What is the horizontal partition?|consists of putting different rows in different tables, being able to adapt each table to the needs and optimize the search, but consuming more space.


<h1>Designing Data Intensive Applications</h1>
<h2>Reliable, Scalable, and Maintainable Application</h2>
<h3>Table of Questions</h3>

**Questions**| **Answers**
--------|-------------------
Tell 5 things that the applications need: | Data bases, caches, search indexes, stream processing and batch processing.
What is reliability? | It means that the application should be ready to perform the function that the user expected, should also be able to tolerate that the user commits errors or uses the software unexpectedly and as a last point, its performance is sufficient for the required use, under the expected load and volume of data. The system must be secure.
what is scalability? |  is the ability of a database to handle changing demands by adding/removing resources. 
How many dimentions has a database scalability? | has three basic dimensions: amount of data, volume of requests and size of requests. The two ways to manage the database are : Vertical and Horizontal.
what is maintainability? | It is the way to organize a database adapted to the needs of the user. the three most common ways of organizing are: VACUMM where you use a table with rows, ANALIZE where if they are numeric data you can use statistic to organize it, but it is changing every time and can include VACUMM and the third is REINDEX rebuilds the indexes in case these have degenerated by unusual data patterns inserted. This can happen for example if you insert many rows with increasing index values, and delete low index values ![More information](https://www.pgadmin.org/docs/pgadmin3/1.22.2/maintenance.html).
