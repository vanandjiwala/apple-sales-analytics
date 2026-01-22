## Apple Sales Analytics

Stack:

- dbt
- python
- duckdb

## Profile.yml

### Local

```
apple_retail_analytics:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: "../data/apple-retail.db"
```

### Motherduck

Note: [Follow documentation for setting up motherduck token and env variable](https://motherduck.com/docs/key-tasks/authenticating-and-connecting-to-motherduck/authenticating-to-motherduck/)

```
apple_retail_analytics:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: "md:apple-retail?motherduck_token={{env_var('MOTHERDUCK_TOKEN')}}"
```
