# Section A — Architecture \& Trade-offs

## Architecture Overview:

The Agentic Travel Recommendations API is designed as a lightweight orchestration layer built in Python. It acts as the intermediary between the AI Agent (connecting via the MCP tool endpoint) and our internal data services. When an AI agent invokes get\_recommendations, the service executes parallel asynchronous calls to the (mocked) Member Data API and Partner Config API. It then processes the member's history through a functional rule engine that dynamically applies the partner's configuration constraints before returning a sanitized JSON payload back to the agent.

----------------------------------------------------------------------------------------------------------------



## Design Trade-offs:



In-Memory Mocks vs. Database Setup: For this proof-of-concept, upstream services are mocked using in-memory data structures rather than a database. Why: This prioritizes delivery speed and self-contained execution for the reviewer, though in production, these would be separate robust microservices with caching layers.



Functional Rule Engine vs. Complex Rules Engine Library: Partner constraints are enforced via sequential functional filters rather than integrating a heavy business rules engine (like Drools). Why: It keeps the system highly observable and debuggable. For a 2 AM on-call scenario, tracing a standard Python function is vastly faster than debugging a complex declarative rules graph.



## Handling Partner Configuration Changes:

Because the service queries the Partner Config API at runtime (or relies on a short-lived cache), changes like a new recommendation cap or a category exclusion take effect immediately on the next API call. If a new type of exclusion rule is added (e.g., "exclude flights over 5 hours"), a new filter function must be added to the core recommendation pipeline and deployed.



# Section B — Production Readiness \& Incident Response

## Incident Runbook Entry:

Cruise Recommendations Leak



## Alert:

AI Concierge showing cruise recommendations for a partner with strict cruise exclusions.



## Diagnose:

1\. Query the API logs using the correlation ID attached to the affected member's session.

2\. Inspect the raw payload returned by the Partner Config service for that specific partner\_id to confirm exclude\_cruises is actively set to true.

3\. Verify the exact tool invocation sent by the AI Agent to ensure it didn't hallucinate or bypass the API's returned constraints.



## Confirm:

If the Partner Config shows exclude\_cruises: true but our API response included a cruise, the failure is in our internal Rule Engine layer. If our API response correctly omitted the cruise, the failure is on the AI Agent/LLM prompt side.



## Resolve:

If it's a Rule Engine bug, initiate a rollback to the previous stable container image. Implement a hotfix in the filter logic, add a regression test for that specific partner configuration, and push through the CI/CD pipeline.



# Section C — AI Usage Log



## Interaction 1: 

Asked: "Help me design an architecture to handle partner-specific rules for an AI travel agent."



Received: A highly complex microservices architecture utilizing Kafka for event streaming and a separate caching layer.



Action: Rejected. Pushed back because the assignment requires a 4-week delivery scope for a single engineer. Re-prompted for a lean, monolithic FastAPI orchestrator that prioritizes observability.



## Interaction 2:



Asked: "Generate the README components for Section A and the Runbook, focusing on system reliability."



Received: Drafts covering trade-offs and an incident response plan.



Action: Kept and modified. Toned down the complexity of the runbook to reflect the actual mocked architecture I built.



## Interaction 3:



Asked: "Write a quick Python functional filter for excluding cruise data based on a config dictionary."



Received: A standard Python list comprehension snippet.



Action: Kept. Integrated it directly into the get\_recommendations endpoint to act as the primary rule enforcement mechanism.

