# Git and Software Development Quiz Study Guide

## Question 1: Git Trees and Functions
**Match the proper Git Tree with its function:**

- **Working Directory** → Modified
- **Staging Area** → Tracked  
- **Repository** → Committed

---

## Question 2: Docker Commands
**Statement:** Running the command `docker run -p 8080:80 --name my-dev python-image` will build a Docker Image called python-image

**Answer:** False

*Note: The `docker run` command runs a container from an existing image, it does not build an image. To build an image, you would use `docker build`.*

---

## Question 3: gRPC Client Compatibility
**A gRPC client App written in Python can exchange information with:**

**Correct Answer:** Any other server App that also uses gRPC, regardless of the programming language.

*Key Point: gRPC is language-agnostic - clients and servers can be written in different programming languages as long as they both use gRPC protocol.*

---

## Question 4: HATEOAS Definition
**HATEOAS stands for:**

**Answer:** Hypermedia As The Engine of Application State

*Definition: A key principle of RESTful architecture where clients learn how to interact with a REST API by following hypermedia links provided by the server, rather than relying on hardcoded URLs or prior knowledge.*

---

## Question 5: SOAP API Message Format
**Valid message format for SOAP APIs:**

**Answer:** XML

*Note: SOAP (Simple Object Access Protocol) exclusively uses XML for message formatting.*

---

## Question 6: HTTP Methods
**Valid HTTP Methods include:**

- ✅ GET
- ✅ POST  
- ✅ PUT
- ❌ DESTROY (not a standard HTTP method)
- ❌ PATCHED (should be PATCH)

---

## Question 7: Reliable Packet Transfer Protocol
**Best protocol for reliability in packet transfer:**

**Answer:** TCP (Transmission Control Protocol)

*TCP provides reliable, ordered delivery of data with error checking and retransmission, unlike UDP which is faster but unreliable.*

---

## Question 8: Software Development Methodologies
**Valid software development methodologies:**

- ✅ Waterfall
- ✅ Agile
- ✅ DevOps
- ❌ Reddit Application Development (not a methodology)
- ❌ OpEd (not a methodology)

---

## Question 9: API Documentation
**Statement:** Good API documentation should clearly state how to exchange information

**Answer:** True

*Good API documentation must clearly explain how to interact with the API, including request/response formats, endpoints, and data exchange methods.*

---

## Question 10: Data Format Size Comparison
**Information serialized and sent over network, ordered from least to greatest bytes:**

1. **Protobuf** (smallest)
2. **JSON** (medium)
3. **XML** (largest)

*Protobuf (Protocol Buffers) is Google's binary serialization format designed for efficiency and small size. JSON is text-based and more compact than XML. XML is the most verbose due to its tag-based structure.*

---

## Study Tips

- Focus on understanding the practical differences between protocols and formats
- Remember that gRPC is language-independent
- Know the basic HTTP methods and their purposes
- Understand Git's three-tree architecture (Working Directory, Staging Area, Repository)
- Practice distinguishing between Docker build vs run commands