## Conditions

```
prefect server start
```

```
 prefect agent start docker --no-pull -v
```

```
 prefect create project "test"
```

Create and run the flow:

```
make build
./register.py
prefect run flow --name ubuntu-custom --project test
```

## Outcome:

Flow hangs in Submitted state even though agent logs indicate that flow has completed:

```
[2020-09-09 16:31:36,612] DEBUG - agent | Completed flow run submission (id: 8eab6dda-dec9-4fa1-8ea3-5f05298fdda4)
```

