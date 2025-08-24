# CSC 6304 Week 7 - Hybrid Native Application Development

## Overview

**Course:** CSC 6304 - Advanced Programming Concepts  
**Professor:** Rob Sand  
**Topic:** Hybrid Native Application Development

## What is Hybrid Native Mobile Development?

An approach to building mobile applications that combines elements of both native and web development to create apps that can run across multiple platforms while sharing a significant portion of the codebase.

### Key Benefits

Instead of writing separate applications for iOS (Swift) and Android (Kotlin/Java), hybrid development allows developers to:

- **Write once, deploy everywhere**
- **Leverage web technologies**
- **Access native features**
- **Maintain platform feel**

### Key Characteristics

#### Shared Business Logic
- Data models, API calls, and business rules written once
- Core application functionality remains consistent across platforms

#### Platform Abstraction
- Framework handles platform-specific differences
- Developers work with unified APIs rather than platform-specific code

#### Native Integration
- Access to device features (camera, GPS, notifications)
- Platform-specific UI components when needed
- App store distribution like traditional native apps

## Why Choose a Hybrid Approach?

### The Problem with Traditional Development
Traditional mobile development requires separate teams, codebases, and expertise for each platform, leading to:
- Doubled development time and costs
- Inconsistent features and user experiences
- Maintenance overhead across multiple codebases

### The Hybrid Solution
Hybrid frameworks provide a middle ground that offers:
- Faster time to market
- Reduced development costs
- Consistent user experience
- Single team can target multiple platforms

## Common Misconceptions

❌ **FALSE Assumptions:**
- Hybrid apps are always slower
- Hybrid means web apps in a wrapper
- One size fits all
- No platform-specific code needed

## The Hybrid Spectrum

The hybrid development landscape can be visualized as a spectrum from pure native to web apps:

**Pure Native** → **Native Components** → **Custom Rendering** → **WebView** → **Progressive Web Apps**

### Technologies by Category

#### Native Components
- **React Native** - Uses native UI components
- **NativeScript** - Direct access to native APIs
- **Xamarin** - Microsoft's cross-platform solution
- **.NET MAUI** - Evolution of Xamarin

#### Custom Rendering
- **Flutter** - Custom rendering engine using Skia
- **Compose Multiplatform** - Jetpack Compose across platforms

#### WebView
- **Ionic** - Web technologies in native containers
- **Capacitor** - Modern successor to Cordova

## WebView Approach

WebView-based solutions run web applications inside native containers:
- **Examples:** Ionic, Capacitor
- **Pros:** Leverage existing web skills and codebases
- **Cons:** Performance limitations, platform inconsistencies

## Custom Rendering

### Flutter Architecture
Flutter uses a unique approach with four key components:

1. **Canvas Based Rendering**
   - Uses Skia graphics engine
   - Direct pixel control

2. **Direct Rendering Pipeline**
   - Bypasses platform UI systems
   - Consistent across platforms

3. **Platform Channels**
   - Communication with native features
   - Access to device capabilities

4. **"Embedder" Layer**
   - Platform-specific integration
   - Handles system events

### Flutter Development Resources
- **Setup:** Flutter Setup and Install
- **Language:** Dart programming language
- **Widgets:** Flutter widget system
- **Tools:** VS Code IDE integration
- **Preview:** Emulators and hot reload
- **Version Control:** GitHub integration

**Official Resources:** [Dart](https://dart.dev) and [Flutter](https://flutter.dev)

## Native Components Approach

### React Native Architecture

React Native uses a bridge-based architecture with four key aspects:

1. **Rendering Philosophy**
   - JavaScript logic, native UI components
   - Platform-specific rendering

2. **Bridge Mechanism**
   - Communication between JavaScript and native
   - Serialized data exchange

3. **JS Execution Environment**
   - Separate JavaScript thread
   - Multiple engine options

4. **Component Rendering Process**
   - Virtual DOM to native components
   - Platform-specific implementations

### JavaScript Engine Evolution

#### Original Engines
- **JavaScriptCore (iOS)** - WebKit's JS engine
- **V8 (Android)** - Google's JS engine

#### Hermes Engine
Modern React Native uses Hermes for improved performance:
- **Fast Startup Time** - Reduced app launch time
- **Ahead of Time Compilation (AOT)** - Pre-compiled bytecode
- **Garbage Collection (Hades)** - Efficient memory management

### React Native New Architecture

The latest React Native architecture introduces:

#### JavaScript Interface (JSI)
- Direct communication between JS and native
- Eliminates bridge bottlenecks

#### Fabric
- New rendering system
- Uses JSI for direct communication
- Synchronous layout calculations
- Improved animation performance

**Learn More:** [React Native New Architecture](https://reactnative.dev/docs/new-architecture-intro)

### React Native Development Resources
- **Setup:** React Native and Expo installation
- **Framework:** Expo for rapid development
- **Tools:** EAS (Expo Application Services)
- **IDE:** VS Code integration
- **Testing:** Emulators and device preview
- **Version Control:** GitHub integration

**Official Resources:** [React Native](https://reactnative.dev) and [Expo](https://expo.dev)

## Project Assignment

### Project #7 Requirements

Choose one cross-platform framework and create an interactive mobile app:

#### Option 1: Flutter
- **Language:** Dart
- **Resource:** [Your First Flutter App](https://flutter.dev/docs/get-started/codelab)
- **Focus:** Widget-based UI development

#### Option 2: React Native
- **Framework:** Expo
- **Resource:** [Tutorial: Using React Native and Expo](https://expo.dev/tutorial)
- **Focus:** Component-based development

**Submission:** See Canvas and GitLab issues for detailed requirements

## Course Reminders

### Week 7 Deliverables
- Complete Project #7 by Monday
- Complete Sprint Review by Monday

### Next Week
- **Final Exam** - Comprehensive course review

## Study Tips for Exam

1. **Understand the Spectrum** - Know where each technology fits
2. **Compare Approaches** - WebView vs Custom Rendering vs Native Components
3. **Architecture Details** - Flutter's Skia vs React Native's bridge
4. **Performance Trade-offs** - When to choose each approach
5. **Development Workflow** - Setup, tools, and deployment processes

## Key Takeaways

- Hybrid development offers a balance between development efficiency and native performance
- Different hybrid approaches serve different use cases and requirements
- Modern frameworks like Flutter and React Native provide near-native performance
- Tool ecosystem and developer experience are crucial factors in framework selection
- The choice depends on team expertise, project requirements, and long-term maintenance considerations