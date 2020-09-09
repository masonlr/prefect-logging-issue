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
prefect run flow --name python-custom --project test
```

## Outcome:

Flow runs correctly.