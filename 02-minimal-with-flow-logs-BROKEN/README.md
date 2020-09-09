## Conditions

```
prefect server start
```

```
prefect agent start docker --no-pull -v --show-flow-logs
```

```
prefect create project "test"
```

Create and run the flow:

```
make build
./register.py
prefect run flow --name prefect-base-logs --project test
```

## Outcome:

Agent logs show:

```
[2020-09-09 16:23:22,840] ERROR - agent | Logging platform error for flow run 8c9f55d4-3b81-43c1-9983-5a38413465b9
[2020-09-09 16:23:22,887] ERROR - agent | Error while deploying flow: AttributeError("Can't pickle local object 'Agent.run_heartbeat_thread.<locals>.run'")
```
