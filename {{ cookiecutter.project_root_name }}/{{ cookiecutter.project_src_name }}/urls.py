from esmerald.routing.router import Include

route_patterns = [
    Include(path="/api/v1", namespace="welcome.v1.urls"),
]
