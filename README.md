# Django Hexagonal Example

### Context approach
 - Catalog 
   -  Contains the products and the logics related to variants 
 - Purchase
   - Contains logic related to prices, offers and shopping cart 
 - Logistic
   - Contains the shipping, stock and destination warehouse logics.


### TODO
- [x] Change pk|id from integer autoincremental to uuid4
- [x] Create first django app | context
- [x] Create Shared context
- [x] Create basic Value Objects
- [x] Create a test ci github action
- [x] Create base Use Case
- [x] Create domain Repository
- [x] Create basic repository implementation in Django
- [x] Make a first use case
- [ ] Do a product search use case functional with criteria pattern 