# Glossary

An incomplete listing of terms used in the algorithms, usually as variable names. This focuses on terms that are likely
new or have a more specific meaning in this codebase.

#### Adjacent

Nodes are adjacent if there's an edge between them.

#### Component

A subgraph where all nodes are connected to each other and not connected to any other nodes. Commonly called a connected
component.

#### Connected

Nodes are connected if there's a path between them. A graph is connected if all of its nodes are connected.

#### Degree

The degree of a node is the count of the edges going to and from that node. In-degree is the number of directed edges
going to that node.

#### Next Node

An adjacent node. Most likely it's getting added to a collection of nodes to visit.

#### Path

A sequence of edges that connect a sequence of nodes. In this codebase, it's usually expressed as the sequence of nodes
that are connected.

#### Ret

A variable name for the return value of a function when the output is obvious, and a better name isn't available.

#### Seen

Items that have been placed in a collection to be processed, or decided never to be added.

#### Visited

Items that have been removed from a collection for processing.
