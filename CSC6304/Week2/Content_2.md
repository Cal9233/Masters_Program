# CSC 6304 - Advanced Programming Concepts
## Week 2: Understanding Protocols and APIs

### Course Information
- **Professor:** Rob Sand
- **Institution:** Merrimack College
- **Course:** Advanced Programming Concepts
- **Contact:** sandro@merrimack.edu

---

## Network Protocols

### What is a Protocol?
A protocol is a set of rules and conventions for communication between systems that:
- Defines format, timing, sequencing, and error control
- Ensures interoperability in distributed systems
- Provides a common language for different systems to communicate

### The Protocol Stack
Network communication follows a layered architecture where each layer builds upon the previous:

```
Application Layer    - HTTP/FTP/SMTP/HTTPS
Security Layer      - SSL/TLS
Transport Layer     - TCP/UDP  
Internet/Network    - IP
Data Link Layer     - Ethernet/WiFi
Physical Layer      - Cables/Wireless
```

### Evolution of Protocol Architecture

**Timeline:**
- **1970:** ARPANET uses Network Control Protocol (NCP)
  - Single protocol handling everything
  - Limited to single network

- **1973-1974:** Original "Transmission Control Program" 
  - First internet protocol by Cerf and Kahn
  - Still monolithic but designed for multiple networks
  - Handled routing AND reliability in one protocol

- **1978:** The Great Split - Recognition of Separation of Concerns
  - Network functions (addressing/routing) vs. Transport functions (reliability)
  - TCP (reliability) + IP (routing) + later UDP (speed)

- **1981:** TCP/IP v4 stabilized
  - Foundation for modern internet
  - Layered architecture enables innovation

---

## Network Layer Protocols

### Internet Protocol (IP) - The Network Foundation

**Key Characteristics:**
- Born from the 1978 split of original TCP
- Network layer protocol
- Provides addressing and routing between networks
- Connectionless and best-effort delivery

**Key Features:**
- IP addresses identify devices uniquely
- Packet-based communication
- Routing across multiple networks
- No guarantees about delivery, order, or integrity

---

## Transport Layer Protocols

### TCP (Transmission Control Protocol) - The Reliability Layer

**Purpose:** 
- Also born from the 1978 split
- Transport layer protocol built on top of IP
- Connection-oriented and reliable
- Provides what IP deliberately omits

**TCP Features:**
- Three-way handshake for connection establishment
- Sequence numbers for ordering
- Automatic retransmission on packet loss
- Flow control and congestion control

### UDP (User Datagram Protocol) - The Speed Layer

**Purpose:**
- Developed after TCP/IP split to address different needs
- Transport layer protocol (alternative to TCP)
- Connectionless and unreliable
- Minimal overhead

**UDP Characteristics:**
- No connection establishment
- No ordering guarantees
- No error recovery
- Very small header overhead

**When to use UDP:**
- Real-time applications (gaming, video streaming)
- DNS queries (simple request-response)
- Applications that handle their own reliability

---

## Application Layer Protocols

### HTTP (Hypertext Transfer Protocol)

**Characteristics:**
- Built on top of the TCP/IP foundation (typically uses TCP)
- Application layer protocol
- Client-server request-response model
- Stateless protocol

**HTTP Methods:**
- **GET:** Retrieve data
- **POST:** Submit data
- **PUT:** Update/create resource
- **PATCH:** Partial update
- **DELETE:** Remove resource

### Security Layer - SSL/TLS

**SSL/TLS: Universal Security Solution**
- **SSL (Secure Sockets Layer):** Created by Netscape in 1994
- **TLS (Transport Layer Security):** IETF standardization of SSL (1999)
- **Purpose:** Provide security for any application protocol
- **Position:** Between application and transport layers

**HTTPS: HTTP over TLS**
- Implementation: HTTP running over TLS/SSL
- Port 443: Standard HTTPS port (vs HTTP port 80)
- Ubiquitous adoption: Now standard for all web traffic
- Browser integration: Visual security indicators, warnings for HTTP

### SSH (Secure Shell) - Security-First Design

**Alternative Security Approach:**
- 1995: Created by Tatu Ylönen after password-sniffing attack
- Philosophy: Security designed in from the ground up
- Replacement strategy: New protocol replaces insecure ones
- Port 22: Chosen between Telnet (23) and FTP (21)

### DNS (Domain Name System)

**Purpose and Characteristics:**
- Translates domain names to IP addresses
- Hierarchical distributed database
- Uses UDP for queries (usually)
- Security evolution: DNS over HTTPS (DoH), DNS over TLS (DoT)

### Legacy Protocols and Their Secure Successors

| Insecure Original | Secure Replacement | Method |
|------------------|-------------------|---------|
| HTTP | HTTPS | HTTP over TLS |
| FTP | FTPS / SFTP | FTP over TLS / SSH File Transfer |
| Telnet | SSH | Complete redesign |
| SMTP | SMTPS | SMTP over TLS |
| POP3/IMAP | POP3S/IMAPS | Email protocols over TLS |

---

## Application Programming Interfaces (APIs)

### Introduction to APIs

**Definition:** Application Programming Interface
- Contract between software components
- Define how applications communicate
- Abstract implementation details
- Enable system integration and reusability

---

## API Protocols and Architectures

### REST (Representational State Transfer)

**REST: Architectural Style for Web APIs**
- Uses standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Resource-based URLs
- Stateless communication
- Multiple representation formats (JSON, XML, HTML)

**HATEOAS: Hypermedia as the Engine of Application State**

Instead of a client knowing beforehand what endpoints are available, the server provides this information dynamically:

```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "_links": {
    "self": { "href": "/users/123" },
    "orders": { "href": "/users/123/orders" },
    "delete": { "href": "/users/123", "method": "DELETE" },
    "update": { "href": "/users/123", "method": "PUT" }
  }
}
```

**HATEOAS Benefits:**
- Loose Coupling
- Self-Discovery
- State-Driven Navigation

### SOAP (Simple Object Access Protocol)

**SOAP: XML-Based Protocol**
- Standardized protocol with strict specifications
- XML messaging format
- Built-in error handling
- Transport protocol agnostic (HTTP, SMTP, etc.)

**SOAP Features:**
- WSDL (Web Services Description Language)
- Strong typing and contracts
- Built-in security standards
- Enterprise-focused

**SOAP Structure:**
```xml
<soap:Envelope>
  <soap:Header>
    <!-- Optional header information -->
  </soap:Header>
  <soap:Body>
    <!-- Actual message content -->
  </soap:Body>
</soap:Envelope>
```

### RPC (Remote Procedure Call)

**RPC: Making Remote Calls Look Local**
- Makes remote function calls appear local
- Various implementations (JSON-RPC, gRPC, XML-RPC)
- Strong typing (in modern variants)
- Efficient binary protocols (gRPC)

**gRPC Example Features:**
- Uses Protocol Buffers for serialization
- HTTP/2 for transport
- Streaming support
- Cross-language compatibility

**RPC vs. REST:**
- **RPC:** Action-oriented (getUserDetails())
- **REST:** Resource-oriented (GET /users/123)

### GraphQL

**GraphQL: Query Language for APIs**
- Single endpoint for all operations
- Client specifies exactly what data to fetch
- Strong type system
- Real-time subscriptions

**GraphQL Benefits:**
- Reduces over-fetching and under-fetching
- Strongly typed schema
- Excellent developer tools
- Evolutionary API design

**GraphQL Query Example:**
```graphql
query {
  user(id: "123") {
    name
    email
    posts {
      title
      publishedAt
    }
  }
}
```

---

## API Protocol Selection Guide

### When to Use Each Protocol:

**REST**
- Simple CRUD operations
- Resource-based thinking fits naturally
- Caching is important
- Wide client compatibility needed
- **Use Cases:** Web APIs, Public APIs

**SOAP**
- Enterprise environments
- Formal contracts required
- Complex transactions
- Existing SOAP infrastructure
- **Use Cases:** Enterprise Systems

**RPC/gRPC**
- High performance required
- Strong typing desired
- Microservices communication
- Real-time applications
- **Use Cases:** Microservices

**GraphQL**
- Complex data relationships
- Mobile applications (bandwidth concerns)
- Rapid frontend development
- Multiple client types
- **Use Cases:** Modern Apps

### Quick Decision Guide:
- Need high performance & strong typing? → **gRPC**
- Complex data needs & flexible queries? → **GraphQL**
- Enterprise with formal contracts? → **SOAP**
- Simple web API with wide support? → **REST**

**Key Insight:** These aren't mutually exclusive! Large organizations often use different protocols for different use cases: REST for public APIs, gRPC for microservices, GraphQL for mobile apps.

---

## Serialization

### What is Serialization?
Serialization is the process of converting data structures or objects into a format that can be transmitted over a network or stored.

**Process:**
- **Serialization:** Converting in-memory data → transmittable format
- **Deserialization:** Converting received data → in-memory data structures

### Why Do We Need Serialization?

**The Problem:**
- Your application works with objects, arrays, numbers, strings
- Networks only transmit bytes (1s and 0s)
- Different programming languages represent data differently
- Need a common format for communication

### Common Serialization Formats

**Size Comparison:**
- **JSON:** `{"id":123,"name":"Alice","email":"alice@example.com","active":true}` - **67 bytes**
- **XML:** `<user><id>123</id><name>Alice</name>...</user>` - **~120 bytes**
- **Protobuf:** `[binary data]` - **~25 bytes**

**What Actually Gets Transmitted:**
```
Application layer: "Hello World"
         ↓
Encoding (UTF-8): [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
         ↓
Network transmission: 01001000 01100101 01101100... (raw bytes)
         ↓
Receiving end: [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
         ↓
Decoding (UTF-8): "Hello World"
```

---

## API Documentation and Tools

### Creating Server APIs

**A good API documentation must state clearly:**

**Protocol definition:**
- Host and port, or full URL
- Packages to import

**Message format:**
- XML, JSON, strings, etc.
- How to pack and unpack the message payload

### Reading Server APIs

**Well-Documented APIs:**
- Most existing server APIs are documented sufficiently to guide developers in building client applications
- However, the quality and depth of documentation can vary significantly

**Reverse Engineering in Client Development:**
- Despite having documentation, client development often involves a degree of reverse engineering

### API Development Tools

**Tools to speed up API development:**
- **Postman:** Popular GUI-based API testing tool
- **Insomnia:** Alternative API client
- **cURL (cli):** Command-line tool for API requests
- **httpie.io:** Modern command-line HTTP client

---

## Summary and Key Takeaways

### Protocol Hierarchy
- Lower layers (IP, TCP/UDP) provide foundation
- Higher layers (HTTP, APIs) provide application services
- Each layer builds on the previous one

### Practical Implications
- Choose protocols based on requirements
- Understand trade-offs and limitations
- Design for scalability and maintainability

---

## Week 2 Tasks

### Assignments
- [ ] Complete Project #2
- [ ] Sprint Review #2
- [ ] Complete Quiz #1
- [ ] Due Monday 11:59 PM

### Study Tips for Exam
1. Understand the protocol stack layers and their purposes
2. Know the differences between TCP and UDP and when to use each
3. Understand the evolution from monolithic to layered protocol design
4. Compare REST, SOAP, RPC/gRPC, and GraphQL - know when to use each
5. Understand serialization and why it's necessary
6. Know the security evolution from insecure to secure protocols
7. Understand HATEOAS and its benefits in REST APIs
8. Know the key features of HTTP, HTTPS, SSH, and DNS

### Next Week Preview
- Proper documentation of API modules

---

## Additional Resources
- **Communication:** sandro@merrimack.edu
- **Zoom Sessions:** Available in Main Menu
- **Repository Submissions:** GitLab platform
- **Documentation:** Course materials and slides