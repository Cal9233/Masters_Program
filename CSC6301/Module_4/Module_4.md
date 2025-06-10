### Software Reuse Kinds

Opportunistic: The motivation is the realization of existing components.
Planned: When designing components are strategically planned to be reused in the future.
Interal: when a team/developer reuse own components.
External: when a team/developer reuse components from others.
Referenced: when the reused code is dully referenced in the new code.
Forked: when a copy of the reused code is incorporated into the new code.

Internal, Planned, and Referenced reuse is a common and healthy practice
in several environments;
External, Opportunistic, and Referenced reuse is even more common and
acceptable practice, but it requires extra attention:
Sources must be reliable, well documented, and you need to make sure
they are what is needed;
Forked reuse is discouraged because the reused/copied code will not
benefit from patches/enhancements;
Referenced reuse is usually a good option, but it often requires version
control.

## Composition

In Java (and other languages) classes
might have instance-level relations that
are either composition or aggregation:
○ composition - when an object of
Class A is composed by an object of
another Class B that is create within
Class A:
■ if the compound object (from
Class A) ceases to exist, the part-
of object ceases to exist.

## Aggregation

In Java (and other languages) classes might
have instance-level relations that are either
composition or aggregation:
○ aggregation - when an object of a Class
A is associated to an object of another
Class B that is created outside Class A:
■ when the object of A ceases to
exist, the object of B continues to
exist.

## Java Collections

● Part of java.util package;
● Full reference to be consulted,
frequently;
● An list of interfaces and basic
data structure classes ;
○ List - extensible lists;
○ Queue - ordered groups
of elements with an
access discipline;
○ Set - groups of elements
without implicit order;
○ Map - structures with
more sophisticated
access.

LinkedList Class
● A double linked list
● Common methods:
○ Constructor: LinkedList<int> list = new
LinkedList<>();
○ Add at the end: list.addLast(56);
list.add(56);
○ Add at the beginning: list.addFirst(10);
○ Remove from end: list.removeLast();
○ Remove from beginning: list.removeFirst();
list.remove();
○ Deliver the end: list.getLast();
○ Deliver the beginning: list.getFirst();
○ Deliver the i-th element: list.get(i);
○ Iterator: ListIterator<int> iter = list.listIterator();

Queue Class - A First In, First Out Queue
● Common methods:
○ Constructor: Queue<String> q = new
LinkedList<>();
○ Add at the tail: q.add("Adams");
○ Remove from the head: q.remove();
○ Deliver the head: q.peek();

Stack Class - A Last In, First Out Queue
● Common methods:
○ Constructor: Stack<String> s = new Stack<>();
○ Add at the top: s.push("Adams");
○ Remove from the top: s.pop();
○ Deliver the top: s.peek();

# Spring Framework

● Created in 2002 and maintained by VMware (open source);
● A comprehensive programming and configuration model for modern
Java-based enterprise applications;
● It offers a development environment, including a project initializer and
several templates;
● It is a full environment that is virtually impossible to grasp all features:
○ Training options provided by VMware;
○ Certifications provided by third parties.

# Hibernate Framework

● Created in 2001 and maintained by Red Hat (free software);
● Hibernate is an Object Relational Mapping framework specialized in data
persisting and retrieving from a database;
● ORM - Object Relational Mapping:
○ It provides relational database access in an object-oriented
environment;
● Hibernate is integrated into the Spring framework.
