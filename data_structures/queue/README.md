# Lab 10: Queues
Implementing the Queue class

 ## Features
Create a Queue class with enqueue, dequeue methods

 ## Testing
- [x] Write a test which validates that a valid val is added to the queue when .enqueue is called
- [x] Write a test which validates that an exception is thrown if an invalid or None-type value is passed as an argument to .enqueue
- [x] Write a test which validates that the len attribute of your class increments when a new Node is added to the queue
 

 ## Changelog

 2018-08-26
 ======
- [x] Create a new branch called stack_queue
- [x] Create a queue directory
- [x] Create a README.md file
- [x] Create a node class file
- [x] Create a queue class file
- [x] Create a Class for a Queue which creates an empty Queue when instantiated
- [x] This class should be aware of a default None value assigned to front when the instance is created
- [x] This class should be aware of a default None value assigned to back when the instance is created
- [x] This class should be aware of the len of the queue, which represents the count of Nodes in the queue at any time
- [x] This class should have the ability to accept an iterable as an argument when instantiated, such as [1,2, 3, 4] , 
and creates a new Node in the queue for each value in the iterable
- [x] Define any further magic methods such as len and str to support user functionality and informative responses
- [x] Define a method called enqueue which takes any value as an argument and adds that value to the back of the queue with an O(1) time performance
- [x] Define a method called dequeue which takes no arguments and removes / returns the Node at the front of the queue
- [x] At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and 
return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.

