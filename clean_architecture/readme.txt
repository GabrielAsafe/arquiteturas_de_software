Clean Architecture is a software design philosophy and methodology introduced by Robert C. Martin (Uncle Bob). The goal of Clean Architecture is to create a system that is easy to maintain, test, and scale. The core principles revolve around keeping the business logic and application logic separate from other concerns, like databases or UI, and designing systems where dependencies always point inwards, toward the core business logic.

Key Principles of Clean Architecture
Separation of Concerns (SoC):

The architecture enforces boundaries between different parts of the system. The core business logic is isolated from external details like frameworks, databases, and user interfaces.
Dependency Rule:

The direction of dependency is crucial. The outer layers depend on the inner layers, but the inner layers should never depend on the outer layers. This ensures that changes in the external components (e.g., UI, database) don't affect the core business logic.
Independence of Frameworks:

The system should not depend on any particular framework. You should be able to change frameworks or tools without affecting the business rules of your application.
Testability:

By decoupling the core logic from external dependencies, you can write unit tests for the business logic without worrying about UI, databases, or external services.
UI, Database, and External Services as "Details":

The UI and databases are considered "details" because they can change over time, but the core business logic should remain unaffected by such changes.
Structure of Clean Architecture
Clean Architecture is typically represented as concentric circles (or layers), with the innermost circle containing the core business logic and the outer circles containing external dependencies like frameworks, databases, and user interfaces.

Here’s a typical structure:

Entities (Core Business Logic):

The innermost layer, which represents the core business rules. This contains the entities or domain objects of the system. Entities are the most general and reusable business rules that don’t depend on any specific framework or technology.
Use Cases (Application Logic):

The next layer consists of application-specific business rules. These use cases orchestrate the flow of data between entities and the outside world. They define the system's intended behaviors, such as how a user might interact with the system.
Interface Adapters (Gateways/Controllers):

This layer contains the code that adapts data from the outside world (e.g., UI, database) into a format that the inner layers can understand. This includes things like controllers, presenters, and gateways that interact with external components. It’s where data gets translated between the core business logic and the external world.
Frameworks and Drivers (External Systems):

The outermost layer includes things like frameworks, databases, and UI components. These components are specific to the application and can be changed or replaced without affecting the core business logic. For example, a database could be swapped without altering how the system functions at its core.
Diagram Representation
The typical structure looks like this:

pgsql
Copy
+---------------------------+
|     Frameworks/Drivers     |
|  (Databases, UI, External  |
|      APIs, etc.)           |
+---------------------------+
            |
+---------------------------+
|   Interface Adapters       |
|  (Controllers, Gateways,   |
|     Presenters, etc.)      |
+---------------------------+
            |
+---------------------------+
|   Use Cases (Application   |
|     Business Logic)        |
+---------------------------+
            |
+---------------------------+
|   Entities (Core Business |
|     Logic - Domain Models) |
+---------------------------+
Benefits of Clean Architecture
Maintainability: Since the core business logic is decoupled from external concerns, it's easier to maintain and update the system without affecting the core functionality.

Testability: The separation allows for easy unit testing of core logic without involving complex setups for databases, UI, or external services.

Flexibility and Extensibility: New technologies (databases, frameworks, etc.) can be introduced without affecting the core business logic, which makes the system more adaptable.

Reusability: Core business logic (entities and use cases) is designed to be independent of external technologies, which can lead to greater reuse across different applications or environments.

Clear Boundaries: It enforces a clean separation between different concerns in the system, leading to better modularization and lower coupling.

Example
Let's imagine a simple online store:

Entities: This could include classes like Product, Order, and Customer. These represent the core domain objects that contain business rules like calculating prices or processing orders.

Use Cases: These would define the actions the user can perform, like CreateOrder, AddProductToCart, and Checkout. The use cases interact with the entities to accomplish the business logic.

Interface Adapters: This could be the code that connects the application to a web framework like Django or Flask, and the database via an ORM like SQLAlchemy. It translates data between the core use cases and the outside world (like HTTP requests or database queries).

Frameworks/Drivers: These are the external libraries, tools, or services used by the system, such as a specific database (PostgreSQL, MySQL), a web server (like Flask), or an external payment service.