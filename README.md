# business_entity_lifecycle
A State Machine micro service implementation to provide business entity lifecycle, using event sourcing and CQRS techniques

## Motivation

This project where developed to address a real use case in a business system (an HR system, but it fits well in many other use cases).

In order to tame a highly complex set of rules, based on more than 36 different types of laws,

One of the first challenges where to extract knowledge from the business users, which knows more about laws and HR rather
than any analysis tools and techniques.

To cope with this challenge, we started using **entity life cycle** diagrams to represent the workflow of what the users 
where telling us, and if if very well with state machines.

At first BPM/BPEL tools were tought to represent the problem, but it was not appropriate given the simple workflow needed, and
also given the team previous experience with such tools, it would be just too cumbersome to integrate with little gains given 
the solution we already had in mind.

This project is a reference implementation of what was tought to solve those issuies and to aproximate the business models
and what actialy was implemented in the system.

Some of the benefits we foresee by using this tool:
- Interaction with the clients, creating a domain specific language to discuss in an unambiguous way how the system should operate
- Patters make discussions with business users easy, and we can reuse previous conversations more easely;
- The tool helped amalgamate current concepts (CQRS, Event Sourcing, noSQL and microservices) into a valuable asset;

## How to model


# Other use cases

This technique and the reference code presented here can be used in sitiations where the problem can be mapped using state machines
that need actions and validations.

Some examples (many more can arise, but those are the ones that are subject of ):
- Collect rulers;
- General workflows for trades in banks;
- Insurance policy life cycle;

In summary, any simple workflow that requires parameterization rather than coding, but a BPM/BPEL tool is just overkill.


