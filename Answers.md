#### Q1: How do you estimate the runtime behavior of your implementation in terms of CPU usage and memory consumption?
I have done this is several different ways depending on the projects and also on the technologies used.
1. For AWS services, I have done resource monitoring using CloudWatch and I have also set up CloudWatch alarms to detect high CPU usage, memory usage, etc.
2. In code, I have used generators for low memory consumption. I have also used batch processing and batch requests to reduce load on CPU or external API services.
3. For applications orchestrated through Kubernetes we can check resource utilization with a monitoring tool. I mostly use lens.
4. I have also used Prometheus but I have to admit this was not setup by me.

#### Q2: How do you approach designing and architecting large-scale Python applications, and what tools or techniques do you use to ensure scalability, maintainability, and performance?
There are several things that need to be considered when designing large-scale Python applications. These are:
1. Understanding the requirements and figuring out the different components of the application. In my experience, if components are separate enough
its better to create microservices out of them rather than using a monolith. This also helps with horizontal scalability.
2. For Maintainability I try to use well established frameworks like Flask or FastAPI, depending on the usecase.
3. For speeding things up, its better to implement caching, and manage tasks by using message queues.
4. When creating Microservices based backend systems, its also a good thing to have a separate database based on the usecase for each service. This could mean
an SQL based DB for something like accounts, where as elastic for logs.
5. I also try to use Docker for easy deployment, and consider Kubernetes to manage containers and services.
6. I automate testing and deployment with CI/CD tools, and make sure that the app is error-proof with good error handling and monitoring tools. 
7. Finally I try to write as many tests as possible, including unit, component, system and smoke tests so that everything runs smoothly in Dev and Prod. 

#### Q3: Can you describe your experience working with any Python web frameworks, such as Flask or Django, and how you have used third-party tools or libraries to enhance their functionality?
I have used Flask a lot in my past expereinces and I think its a really cool Python framework when it comes to building microservices or even larger applications.
When building larger applications using Flask, I prefer to use hexagonal architecture so that there can be a separation of business logic, database aceess, API definitions, etc.
Some of the third party tools and libraries I use with Flask are SQLAlchemy for db connection and integration, Flask-Restplus for building APIs, Pytest for testing,
Factory boy for creating test data, Pydantic for Typing and creating data schemas, Flask-Cache for caching, Flask blueprints for separating APIs, Celery for parallel
processing, etc.

#### Q4: Can you discuss your experience with authentication and authorization in API design, and how you have implemented these features in Python?
For Authentication, especially when it comes to APIs, my goto is Token-Based Authentication, especially JWT. I mostly used pyJWT for impolementing JWT based 
authentication. I also make use of decorators so that there is no need to write redundant and repeated code each time we need to authenticate an API.
For Authorization, I have worked with roles and have worked with permission restriction for each role.

#### Q5: What are the pros and cons of deploying applications as a container (e.g. Docker)?
I think deploying applications as containers is most of the time the right way to go. In my eyes, it makes deploying and running different applications 
much easier and faster. Some of the pros of containiers are:-
1. Scalability - using orchestration tools
2. Dependency management - No need to download libraries or other dependencies as they come as part of the container. If it runs locally it runs everywhere.
3. Consistency - container based applications can run on most hardware, regardless of the OS, host system's configuration, underlying hardware, etc
4. Interaction - using docker-compose, several services can be run in a same network providing a way to run all parts of a service based application
5. Other benefits like easy migration, orchestration, and version control make it a good way to deploy applications

Some cons are:-
1. Complexity: they are more complex to run and especially orchestrate
2. There is some overhead because it is a form of virtualization
3. If proper configuration is not done there can be security issues

#### Q6: Suppose you need to continuously roll out an application to several stations in multiple remote locations in different time zones and sometimes unstable/slow internet connections. Service continuity and stability are paramount. Each on-site location has a central server available. How would you make sure that you can roll out updated versions of the application in a timely fashion while interrupting the service as shortly as possible?
1. The primary way to achieve this is to have a CICD pipeline in place that makes release and testing quite streamlined and automated
2. There also needs to be a staging environment that mimics the production in this case so that it allows us to test new versions 
of the application before deploying them to remote locations.
3. If no downtime is acceptable then maintaining two identical production environments and switching traffic between them during updates is something that can be 
a possible solution.
4. Deployment times can be programmed to minimize disruption in each time zone.
5. Alert systems also need to be in place, like Sentry, to figure out if something in failing in production
6. Fallback options should be available to roll back to previous version if something goes wrong

#### Q7: How do you optimize queries in a relational database, such as PostgreSQL or MySQL? Can you discuss techniques such as indexing, query planning, or query optimization?
1. I think one of the main steps to optimize queries is to first figure out what query is slow. I have done this using Grafana.
2. Proper use of indexing is also an important step. Instead of over indexing, which can slow down insert statements its better to identify 
frequently accessed columns like name, timestamp, etc is key. Also indexing columns that heavily used in WHERE, SELECT clauses makes the queries faster.
3. In PostgreSQL I use EXPLAIN to analyze the execution plan for a query and optimize it accordingly.
4. Also, I make sure to only SELECT columns that are actually required instead of all the columns.
5. For query optimization, I follow several rules including, avoidance of cross join, use of temporary tables, avoidance of inner queries, use or LIMIT to get only
necessary rows, avoidance of type change inside a WHERE clause, etc