# Coffee Shop Full Stack

## Full Stack Nano - Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

# Tasks 
### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication. [View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. [View the README.md within ./frontend for more details.](./frontend/README.md)

## Postman Collection Auth details

### Auth0 account
```
AUTH0_DOMAIN = 'dev-498g0f6n.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffee'

```

> :warning: I DID updated the POSTman collection with both `barista` and `manager` accounts, the thing is that the token does expire, so I've created two dummy accounts on my Auth0 profile, both of them are verified and functional.

#### Manager account
```
User: Manager@yahoo.com
password: Manager@123
submitted token (which can be expired at the time of review - "2021-05-05"): 
```
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkR0OWdIMk5wQ3RLM1hWd19JQlJrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi00OThnMGY2bi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAyNjkwNTJiNDVlYzQwMDcwMjMxZDg5IiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjIwMzM4MTMwLCJleHAiOjE2MjAzNDUzMzAsImF6cCI6IndqbWVUUUxyRjB2QUdXTFQ5UWtMVUdRUElRS1hJU0pXIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rc1x0IiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.gexqYKZzTwEgxSRrhj5IuseOVNz2cayJN38weHkvcovV8cSu5KYfLnAje73FB0wSP278_ysCCVwdLR30j48nFqWGutrX5bf-wXOP5lrEbZwVofB2wdRMrtVIRZVhe1cjrtoa0qfXdUkJBQvqpzogRyHkTmW-vkpBVJdnkibp7Yzm2oRyAmNFTO7ti8q1ja6yjy_GDc9cxk2c9KdGoD5K_ZKIPRafbuiw6U0UYs01z-qq_YiGgSoXGyPFWz5ewSiy3rgzyEnqUXJ_hS5f9TVsnKzdT8J7LjqV9xHbo65GugJfZJt_kaenfJnQNVIWD_Tce5pPTihKmMrbF8FsJGT0tA`


#### Barista account
```
User: barista@yahoo.com
password: Barista@123
submitted token (which can be expired at the time of review - "2021-05-05"): 
```
`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkR0OWdIMk5wQ3RLM1hWd19JQlJrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi00OThnMGY2bi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAyNjliNjJjODg1MWMwMDY5MDE5ODcxIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjIwMzM4MDQ1LCJleHAiOjE2MjAzNDUyNDUsImF6cCI6IndqbWVUUUxyRjB2QUdXTFQ5UWtMVUdRUElRS1hJU0pXIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.t8CEYgrnFh_ka90NXzqcZ6ZyxJSujS81-66LgiQMiO0EDRWf_iYdkN_5ThY8FXb69FHgup43kHFL462t3Cpzp_nMC-B4UBJlI-7qPGixD99JTXjwmLDOUKDpxEKKrt9G-AZ-f4HwImJKWL63TEbE86zmA6ACq0YesH3DDle1cHiknClO1uzmgYQr0-CKP9LUSny8Pfe6qvZVEnC3V7rPlc80YUtAnV1RNNiMmfqSuT7OxmLiqMpbWU8Cg3HAIa4ZFpT1Ks7R75YR2WsCOpKziuhDuMosmdIFiXxPHZl27Xu27qUtBKsXiyrLl1W2paf1L_v93i2CmSPvQ_uTOjMO6Q`

### POSTman

* Exported collection with configured tokens can be found at: `/backend/udacity-fsnd-udaspicelatte.postman_collection_StudentToken.json`
* Test results containing 20 successful cases: `/backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json`
* Seed collection remains untouched 


## Resources
* https://github.com/udacity/FSND/tree/master/BasicFlaskAuth
* https://github.com/auth0-samples/auth0-python-api-samples/tree/master/00-Starter-Seed
* https://github.com/jungleBadger/udacity_coffee_shop.git [refrence for Collection handling]