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
What is a stock market trading? | Stock market trading is a fountain of information, with millions of shares and billions of dollars changing hands on a daily basis.
Why unstructured data is rawer than normalized data? |We argue that it’s better to store the unstructured string, because your semantic normalization algorithm may improve over time. If you store the unstructured string, you can renormalize that data at a later time when you have improved your algorithms.
What is Semantic normalization?|Semantic normalization is the process of reshaping free form information into a structured form of data.
When store in an Unstructured data? | As a rule of thumb, if your algorithm for extracting the data is simple and accurate, like extracting an age from an HTML page, you should store the results of that algorithm. If the algorithm is subject to change, due to improvements or broadening the requirements, store the unstructured form of the data.
What are the three components in a core of graph schema? | Nodes are the entities in the system - Edges are relationships between nodes. - Properties are information about entities. **Note:** Edges are strictly between nodes.
What do you do in a fact-based model? | In the fact-based model, you deconstruct the data into fundamental units called (unsurprisingly) facts.
Why the facts are atomic? | Facts are atomic because they can not be divided further into meaningful components.
What are the two ways more secure to delete data?| Garbage collection and regulations.
What is the two principals advantages with immutable data? | Human-fault tolerance: is when you put a limit for people that work with your data and  then you can reduce the impact if he made a mistake. the second point is Simplicity: how you know it has and index, then the posibilities to modify and have access to the data are so simple, even you can make appends in an easy way. 
